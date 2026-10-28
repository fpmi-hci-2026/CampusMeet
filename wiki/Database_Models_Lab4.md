# Логическая и физическая модели базы данных — ЛР4

В рамках Лабораторной работы №4 реляционная модель базы данных CampusMeet расширена с 10 таблиц (ЛР1) до **17 нормализованных отношений**, обеспечивающих транзакционную надежность, поддержку очереди ожидания, журнал оптических чекинов, фиксацию ключей идемпотентности и аудит AI-ассистента.

---

## 1. Логическая схема базы данных (Рисунок 2)

В соответствии с методическими требованиями (Задание 2, Рисунок 2 методички) структура отношений представлена в виде детализированной спецификации полей:

| Сущность | Таблица БД | Поле | Смысл поля | Тип данных |
| :--- | :--- | :--- | :--- | :--- |
| **Пользователь** | `users` | `id` | Первичный суррогатный ключ пользователя | VARCHAR(36) / UUID |
| | | `email` | Адрес электронной почты (уникальный логин) | VARCHAR(255) |
| | | `password_hash` | Криптографический хеш пароля | TEXT |
| | | `full_name` | Фамилия, имя и отчество пользователя | VARCHAR(150) |
| | | `role` | Роль (attendee, volunteer, organizer, admin) | VARCHAR(24) |
| | | `is_active` | Флаг активности учетной записи | BOOLEAN |
| | | `created_at` | Метка времени регистрации | TIMESTAMPTZ |
| **Площадка** | `venues` | `id` | Первичный ключ университетской аудитории | VARCHAR(36) / UUID |
| | | `name` | Наименование зала (например, «Ауд. 518 ФПМИ») | VARCHAR(200) |
| | | `address` | Физический адрес учебного корпуса | TEXT |
| | | `latitude` | Географическая широта для навигации | NUMERIC(10,7) |
| | | `longitude` | Географическая долгота для навигации | NUMERIC(10,7) |
| | | `total_capacity` | Предельная вместимость зала (пожнадзор) | INTEGER |
| **Мероприятие** | `events` | `id` | Первичный ключ митапа или хакатона | VARCHAR(36) / UUID |
| | | `slug` | Человеко-понятный уникальный слаг URL | VARCHAR(120) |
| | | `title` | Название мероприятия | VARCHAR(200) |
| | | `event_type` | Тип (meetup, hackathon, workshop) | VARCHAR(20) |
| | | `status` | Жизненный цикл (draft, published, completed) | VARCHAR(24) |
| | | `venue_id` | Внешний ключ площадки проведения | VARCHAR(36) / UUID |
| | | `organizer_user_id`| Внешний ключ ответственного организатора | VARCHAR(36) / UUID |
| | | `start_time` | Метка времени начала мероприятия | TIMESTAMPTZ |
| | | `end_time` | Метка времени окончания мероприятия | TIMESTAMPTZ |
| | | `capacity_limit` | Квота регистрационных мест | INTEGER |
| | | `waitlist_enabled` | Флаг включения листа ожидания при аншлаге | BOOLEAN |
| | | `version` | Номер версии для контроля параллелизма (ETag) | INTEGER |
| **Билет** | `tickets` | `id` | Первичный ключ электронного билета | VARCHAR(36) / UUID |
| | | `ticket_code` | Публичный номер билета (DEMO-ARTEM-01) | VARCHAR(32) |
| | | `event_id` | Мероприятие, к которому привязан билет | VARCHAR(36) / UUID |
| | | `user_id` | Пользователь-держатель билета | VARCHAR(36) / UUID |
| | | `status` | Статус (registered, waitlisted, checked_in) | VARCHAR(20) |
| | | `qr_token_hash` | SHA-256 хеш полезной нагрузки QR-кода | VARCHAR(64) |
| | | `signature_key_id` | Идентификатор ключа HMAC-SHA256 подписи | VARCHAR(80) |
| | | `created_at` | Метка времени оформления билета | TIMESTAMPTZ |
| **Очередь** | `waitlist_entries`| `ticket_id` | Внешний ключ билета в статусе waitlisted | VARCHAR(36) / UUID |
| | | `queued_at` | Метка времени постановки в очередь | TIMESTAMPTZ |
| | | `promoted_at` | Метка времени автоматического повышения | TIMESTAMPTZ |
| | | `offer_expires_at`| Окно подтверждения согласия на визит | TIMESTAMPTZ |
| **Чекин-лог** | `check_in_logs` | `id` | Первичный ключ факта сканирования билета | VARCHAR(36) / UUID |
| | | `event_id` | Мероприятие прохода | VARCHAR(36) / UUID |
| | | `ticket_id` | Проверяемый билет | VARCHAR(36) / UUID |
| | | `scanned_by_volunteer_id`| Волонтер-контролер на входе | VARCHAR(36) / UUID |
| | | `client_scan_id` | Клиентский UUID сканирования (дедупликация) | VARCHAR(64) |
| | | `verdict` | Вердикт (granted, denied_duplicate) | VARCHAR(20) |
| | | `verification_mode`| Режим фиксации (online, offline_sync) | VARCHAR(20) |
| | | `scanned_at` | Точное время сканирования камерой | TIMESTAMPTZ |
| **Персонал** | `event_staff` | `event_id` | Мероприятие назначения | VARCHAR(36) / UUID |
| | | `user_id` | Назначенный волонтер | VARCHAR(36) / UUID |
| | | `assignment` | Роль (scanner, checkin_lead, room_mod) | VARCHAR(20) |
| **Заявка CFP**| `speaker_proposals`| `id` | Идентификатор заявки на доклад | VARCHAR(36) / UUID |
| | | `event_id` | Мероприятие | VARCHAR(36) / UUID |
| | | `speaker_user_id` | Спикер-докладчик | VARCHAR(36) / UUID |
| | | `topic` | Тема доклада | VARCHAR(200) |
| | | `abstract_text` | Аннотация и план выступления | TEXT |
| | | `status` | Статус (submitted, accepted, rejected) | VARCHAR(20) |
| **Расписание** | `schedule_items` | `id` | Идентификатор пункта программы | VARCHAR(36) / UUID |
| | | `event_id` | Мероприятие | VARCHAR(36) / UUID |
| | | `speaker_user_id` | Докладчик | VARCHAR(36) / UUID |
| | | `title` | Название выступления / воркшопа | VARCHAR(200) |
| | | `room` | Аудитория / зал | VARCHAR(60) |
| | | `start_time` | Время начала | TIMESTAMPTZ |
| | | `end_time` | Время окончания | TIMESTAMPTZ |
| **Личная программа**| `personal_schedule`| `user_id` | Слушатель | VARCHAR(36) / UUID |
| | | `schedule_item_id`| Выбранный доклад | VARCHAR(36) / UUID |
| **Команда** | `team_matches` | `id` | Первичный ключ команды хакатона | VARCHAR(36) / UUID |
| | | `event_id` | Хакатон проведения | VARCHAR(36) / UUID |
| | | `captain_user_id` | Капитан команды | VARCHAR(36) / UUID |
| | | `team_name` | Название команды | VARCHAR(120) |
| | | `looking_for_roles`| Искомые компетенции (ML, Frontend) | TEXT |
| | | `max_members` | Предельный размер команды | INTEGER |
| | | `status` | Статус (forming, ready, locked) | VARCHAR(20) |
| **Член команды**| `team_members` | `team_id` | Идентификатор команды | VARCHAR(36) / UUID |
| | | `event_id` | Мероприятие хакатона | VARCHAR(36) / UUID |
| | | `user_id` | Участник команды | VARCHAR(36) / UUID |
| | | `role_in_team` | Роль в проекте | VARCHAR(60) |
| **Инвайт** | `team_invitations`| `id` | Приглашение в команду | VARCHAR(36) / UUID |
| | | `team_id` | Команда | VARCHAR(36) / UUID |
| | | `user_id` | Приглашенный пользователь | VARCHAR(36) / UUID |
| | | `status` | Статус (pending, accepted, declined) | VARCHAR(20) |
| **Оповещение** | `emergency_announcements`| `id`| Идентификатор оповещения | VARCHAR(36) / UUID |
| | | `event_id` | Мероприятие | VARCHAR(36) / UUID |
| | | `author_user_id` | Автор сообщения | VARCHAR(36) / UUID |
| | | `title` | Заголовок оповещения | VARCHAR(200) |
| | | `body_text` | Текст сообщения | TEXT |
| | | `created_at` | Метка времени отправки | TIMESTAMPTZ |
| **Доставка** | `notification_deliveries`| `id` | Идентификатор доставки | VARCHAR(36) / UUID |
| | | `announcement_id` | Оповещение | VARCHAR(36) / UUID |
| | | `user_id` | Адресат сообщения | VARCHAR(36) / UUID |
| | | `channel` | Канал (push, email, telegram) | VARCHAR(20) |
| | | `status` | Статус доставки (sent, delivered, failed) | VARCHAR(20) |
| **Аудит агента**| `agent_audit_log`| `id` | Первичный ключ записи аудита | VARCHAR(36) / UUID |
| | | `actor_user_id` | Пользователь, вызвавший агента | VARCHAR(36) / UUID |
| | | `action` | Вызванный Tool или прочитанный Resource | VARCHAR(60) |
| | | `target_id` | ID затронутой сущности | VARCHAR(64) |
| | | `outcome` | Результат (success, forbidden, rejected) | VARCHAR(20) |
| | | `created_at` | Точное время выполнения операции | TIMESTAMPTZ |
| **Идемпотентность**| `idempotency_keys`| `actor_user_id`| Владелец ключа повторного запроса | VARCHAR(36) / UUID |
| | | `operation` | Наименование эндпоинта / метода | VARCHAR(64) |
| | | `idempotency_key` | Токен идемпотентности из заголовка | VARCHAR(128) |
| | | `request_hash` | SHA-256 хеш исходного тела запроса | VARCHAR(64) |
| | | `response_status` | Код сохраненного HTTP-ответа | INTEGER |
| | | `response_body` | Тело сохраненного HTTP-ответа | TEXT |
| | | `created_at` | Время фиксации ключа | TIMESTAMPTZ |

---

## 2. Логическая ER-диаграмма данных

Логическая модель иллюстрирует сущности предметной области, их семантические атрибуты и ключевые связи:

![Логическая ER-модель базы данных](../docs/diagrams/lab4/logical_erd.svg)

---

## 3. Физическая ER-модель PostgreSQL 16 (Рисунок 3)

Физическая модель базы данных разработана с учетом спецификации СУБД PostgreSQL 16:

![Физическая ER-модель PostgreSQL 16](../docs/diagrams/lab4/physical_erd.svg)

---

## 4. Ограничения целостности, индексы и транзакции

1. **Гарантия однократной регистрации:** `UNIQUE(event_id, user_id)` в таблице `tickets` предотвращает выпуск нескольких активных билетов на одно лицо;
2. **Атомарная защита от повторного чекина:** Частичный уникальный индекс `CREATE UNIQUE INDEX idx_single_granted ON check_in_logs (ticket_id) WHERE verdict = 'GRANTED'` аппаратно отсекает повторный допуск;
3. **Ограничение вместимости зала:** Триггер на уровне ядра СУБД проверяет инвариант `events.capacity_limit <= venues.total_capacity`;
4. **Оптимистический параллелизм:** Поле `events.version` проверяется в заголовке `If-Match` и предотвращает перезапись изменений при одновременной правке несколькими организаторами;
5. **Безопасность удалений:** Для системных журналов используется `ON DELETE RESTRICT`. Удаление билета выполняется логически (`status = 'cancelled'`).

---

## 5. Исходные файлы схем DDL

* [PostgreSQL 16 DDL (Целевая схема)](https://github.com/fpmi-hci-2026/CampusMeet-Server/blob/main/database/schema.postgresql.sql);
* [SQLite DDL (Легковесная схема Mock)](https://github.com/fpmi-hci-2026/CampusMeet-Server/blob/main/database/schema.sqlite.sql);
* [Генератор SQLite DDL из PostgreSQL](https://github.com/fpmi-hci-2026/CampusMeet-Server/blob/main/scripts/build_sqlite_schema.py).
