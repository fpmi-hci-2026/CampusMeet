# Модель требований API и реестр вариантов использования — ЛР4

Модель: **Действующее лицо → User Story → Use Case → HTTP-операция / MCP Tool**. Исходные US-01..12 и UC-01..05 сохранены из ЛР3; новые истории устраняют пробелы API. Семь персонажей ЛР1 представлены шестью ролями: Артём и Влад — слушатели.

![Модель требований](../docs/diagrams/lab4/requirements.svg)

## 1. Действующие лица и истории

| Действующее лицо | User Stories |
|:--|:--|
| Слушатель · Артём / Влад | US-01, US-02, US-08, US-10, US-13, US-14, US-15, US-17 |
| Волонтер · Дарья | US-03, US-04, US-13 |
| Организатор · Максим | US-05, US-06, US-09, US-11, US-12, US-16 |
| Капитан · Кирилл | US-07, US-13 |
| Спикер · Виктор | US-16, US-13 |
| Администратор · Сергей | US-05, US-12, US-13 |

## 2. Каталог историй и трассировка

| История | Цель | Use Cases |
|:--|:--|:--|
| US-01 | Регистрация в один клик | UC-01 |
| US-02 | Билет и Offline-First доступ | UC-07 |
| US-03 | Быстрый оптический чекин | UC-02 |
| US-04 | Проверка и синхронизация офлайн-проходов | UC-02 |
| US-05 | Событие, площадка и внешняя проверка даты | UC-03,UC-13 |
| US-06 | Квота и очередь ожидания | UC-01,UC-08 |
| US-07 | Набор команды хакатона | UC-05 |
| US-08 | Каталог и сквозной поиск | UC-06 |
| US-09 | Экстренное оповещение | UC-10 |
| US-10 | Экспорт билета в Wallet | UC-11 |
| US-11 | Редактирование программы | UC-09 |
| US-12 | Выгрузка явки XLSX | UC-12 |
| US-13 | [Новая] Вход и профиль текущего пользователя | UC-14 |
| US-14 | [Новая] Отмена своего неиспользованного билета | UC-08 |
| US-15 | [Новая] Персональная программа докладов | UC-09 |
| US-16 | [Новая] Подача и модерация CFP | UC-04 |
| US-17 | [Новая] Работа с каталогом и своим билетом через ассистента | UC-15 |

Новые формулировки:

- **US-13:** как пользователь, я хочу получать профиль своей учетной записи, чтобы выполнять только доступные мне действия.
- **US-14:** как слушатель, я хочу отменить неиспользованный билет, чтобы освободить место следующему в очереди.
- **US-15:** как слушатель, я хочу сохранять выбранные доклады, чтобы видеть личную программу.
- **US-16:** как спикер, я хочу подать тезисы, а как организатор — принять решение, чтобы сформировать программу. Конкретизирует UC-04 ЛР3, не переименовывает US-10..12.
- **US-17:** как слушатель, я хочу находить мероприятия и управлять своим билетом через ассистента, сохраняя ограничения доступа.

## 3. Реестр Use Cases

| ID | Сценарий | Актор | Предусловие | Постусловие | Альтернативы / границы |
|:--|:--|:--|:--|:--|:--|
| UC-01 | Зарегистрироваться и получить билет / очередь | Слушатель | Регистрация открыта; пользователь определен | Билет registered либо waitlisted; квота не превышена | 409: квота исчерпана или повтор; 422: схема запроса |
| UC-02 | Проверить билет и передать журнал проходов | Назначенный волонтер | Волонтер назначен на событие | Один GRANTED на билет; повтор обнаружен | 403: нет назначения; 409: использован / конфликт scan_id |
| UC-03 | Создать, изменить или удалить черновик события | Организатор | Есть площадка; вместимость известна | Событие сохраняется с версией; черновик может быть удален | 409: ограничение БД; 412: версия устарела; 428: нет If-Match |
| UC-04 | Подать заявку CFP и принять решение | Спикер / организатор | Пользователь определен; права на модерацию | Контракт submitted → accepted/rejected | 422: тело; 403: нет прав; MVP возвращает примеры |
| UC-05 | Создать команду и пригласить участника | Капитан / участник | Регистрация на хакатон; права капитана | Контракт команды и приглашения | 409: целевая квота; MVP возвращает примеры |
| UC-06 | Найти и просмотреть мероприятие | Любой посетитель | Есть опубликованные события | Каталог/поиск с пагинацией; черновики не раскрываются | 404: карточка отсутствует; 422: пагинация |
| UC-07 | Прочитать собственный билет | Слушатель | Владелец билета определен | Получены данные для клиента; SecureStore — ответственность Mobile | 403: чужой билет; 404: отсутствует |
| UC-08 | Отменить регистрацию и передать место очереди | Владелец билета | Статус registered либо waitlisted | Логическая отмена; первый в очереди получает место | 409: checked_in/no_show; повтор отмены → 204 |
| UC-09 | Составить программу и выбрать доклады | Организатор / слушатель | Есть программа события | Контракт полной замены программы / личного списка | Целевой 409 при наложении; MVP возвращает примеры |
| UC-10 | Поставить уведомление в очередь | Организатор | Организатор владеет событием | 202 + job_id; прием задачи не равен доставке | 403: нет прав; MVP не отправляет push |
| UC-11 | Получить пропуск Wallet | Владелец билета | Есть билет и настроенный провайдер | Целевой подписанный пропуск; MVP → 501 | 501: ключи провайдеров отсутствуют |
| UC-12 | Заказать выгрузку явки | Организатор / администратор | Разрешен доступ к данным явки | 202 + job_id для XLSX | MVP не создает файл; download_url=null |
| UC-13 | Выбрать площадку, проверить адрес и дату | Организатор / администратор | Настроены внешние шлюзы | Контракт геокодинга и календаря; черновик не блокируется | В MVP фиксированные ответы без внешних вызовов |
| UC-14 | Определить текущего пользователя | Пользователь | Учетная запись активна | Demo Bearer и профиль; health публичен | 401: неизвестный токен; 404: fixture user отсутствует |
| UC-15 | Работать через MCP-ассистента | Слушатель через LLM-клиент | Локальный stdio-процесс закреплен за пользователем | Tools/Resources/Prompts; изменения проходят общую бизнес-валидацию | -32602: схема; isError=true: предметный отказ |

## 4. Варианты использования → конечные точки

| Use Case | HTTP и маршрут | operationId | Режим MVP |
|:--|:--|:--|:--|
| UC-14 | `GET /api/v1/health` | `health` | stateful |
| UC-14 | `POST /api/v1/auth/token` | `demoLogin` | stateful |
| UC-14 | `GET /api/v1/me` | `getProfile` | stateful |
| UC-06 | `GET /api/v1/events` | `listEvents` | stateful |
| UC-03 | `POST /api/v1/events` | `createEvent` | stateful |
| UC-06 | `GET /api/v1/events/{event_id}` | `getEvent` | stateful |
| UC-03 | `PUT /api/v1/events/{event_id}` | `replaceEvent` | stateful |
| UC-03 | `DELETE /api/v1/events/{event_id}` | `deleteDraft` | stateful |
| UC-01 | `POST /api/v1/events/{event_id}/registrations` | `registerAttendee` | stateful |
| UC-07 | `GET /api/v1/me/tickets` | `listMyTickets` | stateful |
| UC-07 | `GET /api/v1/tickets/{ticket_id}` | `getTicket` | stateful |
| UC-08 | `DELETE /api/v1/tickets/{ticket_id}` | `cancelTicket` | stateful |
| UC-02 | `GET /api/v1/events/{event_id}/check-ins` | `listCheckIns` | stateful |
| UC-02 | `POST /api/v1/events/{event_id}/check-ins` | `checkIn` | stateful |
| UC-02 | `POST /api/v1/events/{event_id}/check-in-batches` | `syncCheckIns` | example |
| UC-09 | `GET /api/v1/events/{event_id}/schedule` | `getSchedule` | example |
| UC-09 | `PUT /api/v1/events/{event_id}/schedule` | `replaceSchedule` | example |
| UC-09 | `PUT /api/v1/me/schedule` | `replacePersonalSchedule` | example |
| UC-04 | `GET /api/v1/events/{event_id}/proposals` | `listProposals` | example |
| UC-04 | `POST /api/v1/events/{event_id}/proposals` | `submitProposal` | example |
| UC-04 | `PATCH /api/v1/proposals/{proposal_id}` | `reviewProposal` | example |
| UC-05 | `GET /api/v1/events/{event_id}/teams` | `listTeams` | example |
| UC-05 | `POST /api/v1/events/{event_id}/teams` | `createTeam` | example |
| UC-05 | `POST /api/v1/teams/{team_id}/invitations` | `inviteMember` | example |
| UC-05 | `PATCH /api/v1/team-invitations/{invitation_id}` | `answerInvitation` | example |
| UC-06 | `GET /api/v1/search` | `search` | stateful |
| UC-10 | `POST /api/v1/events/{event_id}/announcements` | `broadcast` | example |
| UC-10 | `GET /api/v1/jobs/{job_id}` | `getJob` | example |
| UC-11 | `GET /api/v1/tickets/{ticket_id}/wallet-pass` | `getWalletPass` | stateful |
| UC-12 | `POST /api/v1/events/{event_id}/attendance-exports` | `exportAttendance` | example |
| UC-13 | `GET /api/v1/venues` | `listVenues` | stateful |
| UC-13 | `GET /api/v1/integrations/geocoding` | `geocode` | example |
| UC-13 | `GET /api/v1/integrations/holidays` | `holidays` | example |
| UC-15 | MCP: list_events, check_event_capacity, get_ticket, register_for_event, cancel_ticket | Через общий Store | stateful |

## 5. Критерии сценариев

| Требование | Given → When → Then |
|:--|:--|
| Квота | Два места → пять одновременных регистраций → два registered и три waitlisted |
| Идемпотентность | Один ключ и тело → повтор → тот же билет; другое тело → 409 |
| Очередь | Есть waitlisted → владелец отменяет registered → первый получает место |
| Контроль доступа | Чужой ticket_id → чтение/отмена → 403 |
| Проход | Есть успешный чекин → новый scan_id → 409, аудит сохранен |
| MCP | Использованный билет → cancel_ticket → isError=true и запись аудита |
| Профиль процесса | Tool содержит user_id → валидация → -32602 до действия |

## 6. Источники и связанные документы

- [ЛР3: исходные User Stories и Use Cases](../docs/reports/Lab3_report.md).
- [Полный контракт и реестр маршрутов](../docs/api/route-matrix.md).
- [Исполняемый API / MCP в CampusMeet-Server](https://github.com/fpmi-hci-2026/CampusMeet-Server).
- [Методический пример проектирования API](https://babok-school.ru/blog/how-to-design-rest-api-i-shop-example/): использована последовательность актор → история → сценарий → ресурс → метод.
