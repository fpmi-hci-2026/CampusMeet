# Схема базы данных проекта CampusMeet (GitHub Wiki)

Настоящая страница содержит спецификацию реляционной модели данных программного комплекса **CampusMeet / EventHub**, концептуальную диаграмму сущностей (ER-диаграмму), описание полей, внешних ключей и индексов, а также ссылку на исходный исполняемый DDL-скрипт.

---

## 1. Концептуальная диаграмма связей сущностей (ER-Diagram)

```mermaid
erDiagram
    USERS ||--o{ EVENTS : "организует"
    USERS ||--o{ TICKETS : "владеет"
    USERS ||--o{ SPEAKER_PROPOSALS : "подает"
    USERS ||--o{ TEAM_MATCHES : "капитан"
    USERS ||--o{ TEAM_MEMBERS : "состоит"
    USERS ||--o{ CHECK_IN_LOGS : "сканирует (волонтер)"
    USERS ||--o{ EMERGENCY_ANNOUNCEMENTS : "рассылает"

    VENUES ||--o{ EVENTS : "предоставляет площадку"

    EVENTS ||--o{ SCHEDULE_ITEMS : "содержит программу"
    EVENTS ||--o{ TICKETS : "выпускает"
    EVENTS ||--o{ SPEAKER_PROPOSALS : "принимает заявки"
    EVENTS ||--o{ TEAM_MATCHES : "проводит хакатон"
    EVENTS ||--o{ EMERGENCY_ANNOUNCEMENTS : "оповещения"

    TICKETS ||--o{ CHECK_IN_LOGS : "аудит прохода"

    TEAM_MATCHES ||--o{ TEAM_MEMBERS : "включает участников"

    USERS {
        string id PK
        string email UK
        string password_hash
        string full_name
        string role
        string telegram_username
        string phone
        datetime created_at
    }

    VENUES {
        string id PK
        string name
        string address
        numeric latitude
        numeric longitude
        string room
        int total_capacity
    }

    EVENTS {
        string id PK
        string slug UK
        string title
        string event_type
        string status
        string venue_id FK
        datetime start_time
        datetime end_time
        int capacity_limit
        boolean waitlist_enabled
        int registered_count
        int checked_in_count
    }

    SCHEDULE_ITEMS {
        string id PK
        string event_id FK
        string track_name
        string title
        string speaker_user_id FK
        datetime start_time
        datetime end_time
        string room_override
    }

    TICKETS {
        string id PK
        string ticket_code UK
        string event_id FK
        string user_id FK
        string ticket_type
        string qr_token_hash
        string status
        int waitlist_position
    }

    CHECK_IN_LOGS {
        string id PK
        string ticket_id FK
        string event_id FK
        string scanned_by_volunteer_id FK
        datetime scanned_at
        string verification_mode
        int scan_duration_ms
    }

    SPEAKER_PROPOSALS {
        string id PK
        string event_id FK
        string speaker_user_id FK
        string topic
        text abstract_text
        string status
    }

    TEAM_MATCHES {
        string id PK
        string event_id FK
        string captain_user_id FK
        string team_name
        string looking_for_roles
        string status
    }

    TEAM_MEMBERS {
        string id PK
        string team_id FK
        string user_id FK
        string role_in_team
        datetime joined_at
    }

    EMERGENCY_ANNOUNCEMENTS {
        string id PK
        string event_id FK
        string author_user_id FK
        string title
        text body_text
        string urgency_level
        datetime created_at
    }
```

---

## 2. Описание таблиц реляционной модели

### 1. Таблица `users` (Учетные записи пользователей)
* `id` (VARCHAR(36), PK): Уникальный UUID v4 пользователя.
* `email` (VARCHAR(255), UNIQUE): Основной почтовый адрес.
* `role` (VARCHAR(30)): Роль в системе (`guest`, `attendee`, `team_lead`, `speaker`, `volunteer`, `organizer`, `admin`).
* `telegram_username` (VARCHAR(100)): Имя в мессенджере для дублирования Push-уведомлений.
* `skills_tags` (TEXT): Набор навыков для хакатонов (Frontend, ML, UI/UX).

### 2. Таблица `venues` (Геолокация и площадки)
* Содержит координаты `latitude` и `longitude`, полученные через Nominatim OpenStreetMap API, поэтажные инструкции и схему прохода.

### 3. Таблица `events` (Мероприятия)
* Обеспечивает сквозное управление жизненным циклом события (`draft`, `registration_open`, `ongoing`, `completed`).
* Содержит атрибуты `capacity_limit` (жесткая квота) и `waitlist_enabled` (лист ожидания).

### 4. Таблица `tickets` (Билеты и офлайн-токены)
* `ticket_code`: Публичный человекочитаемый номер билета (например, `CMP-2026-X89K`).
* `qr_token_hash`: Криптографическая HMAC-SHA256 сигнатура для офлайн-валидации сканером.
* `status`: Текущее состояние билета (`registered`, `waitlisted`, `checked_in`, `cancelled`, `no_show`).

### 5. Таблица `check_in_logs` (Журнал аудита проходов)
* Фиксирует факт прохода участника, идентификатор волонтера, метод верификации (`online` / `offline_hmac`), модель смартфона и длительность считывания `scan_duration_ms` для контроля соблюдения UX-норматива (<500 мс).

---

## 3. Исходный SQL DDL файл

В соответствии с архитектурным разделением ответственности между репозиториями, исполняемый скрипт создания таблиц, внешних ключей, проверочных ограничений (`CHECK`), B-Tree индексов и тестовых демонстрационных данных размещен в серверном репозитории бэкенда:

**[database/schema.sql в репозитории CampusMeet-Server](https://github.com/fpmi-hci-2026/CampusMeet-Server/blob/main/database/schema.sql)**
