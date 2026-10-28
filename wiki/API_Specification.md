# Черновик спецификации REST API и внешних интеграций (GitHub Wiki)

> Актуальный контракт ЛР4: [OpenAPI 3.0.3](../docs/api/index.html), [трассировка API](API_Requirements_and_Use_Cases.md), [MCP MVP](MCP_Server.md). Ниже сохранен предварительный контракт ЛР1; старые register/validate-qr/broadcast заменены ресурсами в ЛР4.

> **Статус документа:** Предварительная спецификация программных интерфейсов для последующей реализации серверной части в рамках Лабораторных работ №5–6. На этапе Лабораторной работы №1 документ фиксирует архитектурный контракт обмена данными между компонентами (Web, Mobile, Server) и специфицирует интеграцию с внешними открытыми сервисами.

Настоящая спецификация описывает архитектуру проектируемых программных интерфейсов (RESTful API) комплекса **CampusMeet / EventHub**, форматы сериализации JSON, коды ответов HTTP, а также интеграционные шлюзы с внешними открытыми API (Nominatim OpenStreetMap и Nager.Date Public Holidays).

---

## 1. Базовые принципы и авторизация

* **Базовый URL шлюза API (локальная среда разработки):** `http://localhost:8000/api/v1`
* **Формат обмена данными:** `application/json; charset=utf-8`
* **Аутентификация:** Bearer JWT токен в HTTP-заголовке:  
  `Authorization: Bearer <access_token>`

---

## 2. Основные эндпоинты внутренней системы

### 2.1. Мероприятия (Events API)

#### `GET /events` — Получение каталога мероприятий
* **Параметры запроса (Query):**
  * `type` (optional, string): `meetup | hackathon | workshop`
  * `status` (optional, string): `registration_open | all`
  * `page` (optional, int, default=1), `limit` (optional, int, default=20)
* **Пример успешного ответа (HTTP 200 OK):**
```json
{
  "total": 1,
  "page": 1,
  "items": [
    {
      "id": "ev-campusmeet-2026",
      "slug": "bsu-campus-meet-autumn-2026",
      "title": "CampusMeet Minsk: AI & Web Tech Autumn 2026",
      "event_type": "meetup",
      "status": "registration_open",
      "start_time": "2026-10-15T16:00:00+03:00",
      "end_time": "2026-10-15T20:30:00+03:00",
      "venue": {
        "name": "Главный лекторий ФПМИ БГУ",
        "address": "г. Минск, пр-т Независимости, 4, ауд. 512",
        "latitude": 53.8930090,
        "longitude": 27.5468790
      },
      "capacity_limit": 100,
      "registered_count": 82,
      "is_spots_available": true
    }
  ]
}
```

#### `POST /events` — Создание нового события (Web Organizer)
* **Авторизация:** Требуются права `organizer` или `admin`.
* **Тело запроса:**
```json
{
  "title": "Митап по мобильной разработке и UI/UX",
  "short_summary": "Секреты создания доступных интерфейсов и офлайн-приложений",
  "description": "Практический воркшоп с разбором реальных кейсов...",
  "event_type": "workshop",
  "venue_id": "ven-bsu-fpmi-01",
  "start_time": "2026-11-05T17:00:00+03:00",
  "end_time": "2026-11-05T20:00:00+03:00",
  "registration_deadline": "2026-11-04T23:59:00+03:00",
  "capacity_limit": 60,
  "waitlist_enabled": true
}
```

---

### 2.2. Регистрация и Билеты (Tickets & Check-in API)

#### `POST /events/{event_id}/register` — Регистрация на событие (1 клик)
* **Авторизация:** Bearer JWT участника.
* **Пример ответа (HTTP 201 Created):**
```json
{
  "ticket_id": "tkt-8829-uuid",
  "ticket_code": "CMP-2026-X89K",
  "status": "registered",
  "qr_offline_token": "eyJhbGciOiJIUzI1NiJ9.eyJ0aWQiOiJDTVAteDg5ayIsImVpZCI6ImV2LTAxIn0.SIGNATURE_TOKEN",
  "created_at": "2026-09-21T15:40:00Z"
}
```

#### `POST /tickets/validate-qr` — Оптическая валидация QR-билета (Сканер волонтера)
* **Авторизация:** Bearer JWT волонтера с назначенными правами доступа.
* **Тело запроса:**
```json
{
  "event_id": "ev-campusmeet-2026",
  "scanned_payload": "eyJhbGciOiJIUzI1NiJ9.eyJ0aWQiOiJDTVAteDg5ayIsImVpZCI6ImV2LTAxIn0.SIGNATURE_TOKEN",
  "verification_mode": "online"
}
```
* **Пример ответа (HTTP 200 OK — Доступ разрешен):**
```json
{
  "verdict": "GRANTED",
  "ticket_code": "CMP-2026-X89K",
  "attendee_name": "Артём Ковалёв",
  "ticket_type": "standard",
  "first_scanned_at": "2026-10-15T15:45:12+03:00",
  "is_duplicate": false
}
```
* **Пример ответа при повторной попытке прохода (HTTP 409 Conflict):**
```json
{
  "verdict": "DENIED_ALREADY_USED",
  "ticket_code": "CMP-2026-X89K",
  "attendee_name": "Артём Ковалёв",
  "first_scanned_at": "2026-10-15T15:45:12+03:00",
  "first_scanned_by": "Дарья Мельникова (Волонтер №2)"
}
```

---

### 2.3. Экстренное вещание (Emergency API)

#### `POST /events/{event_id}/announcements/broadcast` — Срочный Push-алерт
* **Авторизация:** `organizer`.
* **Тело запроса:**
```json
{
  "title": "Срочно: перенос в аудиторию 519",
  "body_text": "В аудитории 512 технические неполадки. Открытие митапа и все доклады перенесены в ауд. 519!",
  "urgency_level": "urgent_hall_shift",
  "channels": ["push", "telegram"]
}
```

---

## 3. Спецификация интеграции с внешними REST API

### 3.1. API 1: Nominatim OpenStreetMap API
* **Официальная документация:** [https://nominatim.org/release-docs/latest/api/Overview/](https://nominatim.org/release-docs/latest/api/Overview/)
* **Назначение в CampusMeet:** Прямое и обратное геокодирование адресов площадок, вычисление координат для карты навигации в мобильном приложении.
* **Авторизация:** Открытый API (No Auth). Обязательно наличие заголовка `User-Agent: CampusMeetApp/1.0 (info@campusmeet.by)`.
* **Базовый эндпоинт поиска:** `GET https://nominatim.openstreetmap.org/search`
* **Параметры вызова:**
  * `q`: Текстовый адрес площадки (например, `Минск, пр-т Независимости 4`).
  * `format`: `jsonv2`.
  * `limit`: `1`.
  * `countrycodes`: `by`.
* **Пример ответа Nominatim API:**
```json
[
  {
    "place_id": 102938475,
    "licence": "Data © OpenStreetMap contributors, ODbL 1.0",
    "osm_type": "way",
    "osm_id": 34829103,
    "lat": "53.8930090",
    "lon": "27.5468790",
    "category": "amenity",
    "type": "university",
    "display_name": "Белорусский государственный университет, 4, проспект Независимости, Московский район, Минск, 220030, Беларусь"
  }
]
```

---

### 3.2. API 2: Nager.Date Public Holidays API
* **Официальная документация:** [https://date.nager.at/Api](https://date.nager.at/Api)
* **Назначение в CampusMeet:** Валидация календаря организатора при планировании дат событий для предотвращения конфликтов с государственными праздниками Республики Беларусь.
* **Авторизация:** Открытый REST API (No Auth).
* **Базовый эндпоинт:** `GET https://date.nager.at/api/v3/PublicHolidays/{year}/{countryCode}`
* **Пример вызова для Беларуси:** `GET https://date.nager.at/api/v3/PublicHolidays/2026/BY`
* **Пример ответа Nager.Date API:**
```json
[
  {
    "date": "2026-01-01",
    "localName": "Новы год",
    "name": "New Year's Day",
    "countryCode": "BY",
    "fixed": true,
    "global": true
  },
  {
    "date": "2026-01-07",
    "localName": "Каляды праваслаўныя",
    "name": "Orthodox Christmas Day",
    "countryCode": "BY",
    "fixed": true,
    "global": true
  },
  {
    "date": "2026-05-09",
    "localName": "Дзень Перамогі",
    "name": "Victory Day",
    "countryCode": "BY",
    "fixed": true,
    "global": true
  }
]
```
* **Логика в UI:** Если выбранная организатором дата совпадает с элементом массива `date`, в интерфейсе выводится предупреждающий баннер:  
  *«Внимание: выбранная дата совпадает с государственным праздником (Victory Day). Студенты могут разъехаться на длинные выходные, ожидаемая явка может снизиться на 40%»*.
