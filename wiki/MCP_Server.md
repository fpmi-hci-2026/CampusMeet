# MCP-сервер CampusMeet — архитектура и MVP

Лабораторная №4, задание 5. Ассистент получает доступ к каталогу и билетам через ограниченные инструменты; не выполняет произвольный SQL или HTTP по переданному пользователем адресу.

![Архитектура MCP](../docs/diagrams/lab4/mcp_architecture.svg)

## 1. Сущности и границы

Основные сущности — User, Event, Ticket, WaitlistEntry, AgentAuditLog. MCP и HTTP используют общий Store и SQLite mock-базу на 17 таблиц. Профиль пользователя закреплен за процессом через параметр запуска; пользовательский текст не меняет роль и владельца.

| Примитив | Схема / URI | Связь с требованием |
|:--|:--|:--|
| Tool `list_events` | query?: string | UC-06 / US-08 |
| Tool `check_event_capacity` | event_id: string | UC-01 / US-06 |
| Tool `get_ticket` | ticket_id: string | UC-07 / US-02 |
| Tool `register_for_event` | event_id: string, join_waitlist: boolean, idempotency_key: string | UC-01 / US-01,06 |
| Tool `cancel_ticket` | ticket_id: string | UC-08 / US-14 |
| Resource | events://upcoming | Опубликованный каталог |
| Resource | tickets://mine | Собственные билеты |
| Resource | policy://ticket-cancellation | Правила отмены и очереди |
| Resource template | events://{event_id} | Карточка конкретного события |
| Prompt | plan_visit(interest) | Каталог → проверка мест → выбор |
| Prompt | cancel_registration(ticket_id) | Правила → собственный билет → отмена |

[JSON Schema всех Tools](https://github.com/fpmi-hci-2026/CampusMeet-Server/blob/main/mcp/tools.json) экспортирована из реального `tools/list`, `additionalProperties=false`, обязательные ID не подменяются именами.

## 2. Жизненный цикл и обработка ошибок

Зафиксирована совместимая версия MCP **2025-11-25**: initialize → capabilities → notifications/initialized → discovery → вызовы. Транспорт — JSON-RPC 2.0 поверх newline-delimited stdio. Реализация стандартной библиотеки намеренно ограничена MVP: нет Streamable HTTP, OAuth, sampling, subscriptions или protocol 2026-07-28. 

- Некорректный JSON: -32700; структура сообщения: -32600; неизвестный метод: -32601; неверные аргументы: -32602.
- Чужой билет, исчерпанная квота и использованный билет: Tool result с `isError=true` и предметным кодом.
- `cancel_ticket` не отменяет checked_in/no_show. Повторная отмена идемпотентна.
- Регистрация использует ту же транзакцию и Idempotency-Key, что REST; ограничения промпта не заменяют код доступа.
- В аудит входят actor/action/target/outcome/time, без токенов и QR-payload. Выполненные Tools и успешные Resources журналируются; невалидная схема отклоняется до предметного действия.
- Подсказки Prompts направляют ассистента читать ресурс перед действием. Запросы содержат точные ID из ресурсов, а не угаданные идентификаторы.

## 3. Запуск и демонстрация

Из репозитория Server:

```bash
python3 -m campusmeet.mcp_server --token demo-artem
python3 scripts/mcp_client.py --output evidence/mcp-session.json
python3 -m unittest discover -s tests -v
```

Для подключения через официальный MCP Inspector используйте:

```bash
npx @modelcontextprotocol/inspector python3 -m campusmeet.mcp_server --token demo-artem
```

[Полный README сервера с конфигурацией клиента](https://github.com/fpmi-hci-2026/CampusMeet-Server/blob/main/mcp/README.md).

Примеры фраз: «Найди митап по AI», «Проверь свободные места», «Покажи мои билеты», «Отмени мой билет, если я еще не проходил». Нет инструмента массового удаления, рассылки или произвольного администрирования от лица ассистента.

## 4. Нормативные источники

- [MCP lifecycle 2025-11-25](https://modelcontextprotocol.io/specification/2025-11-25/basic/lifecycle).
- [MCP Tools](https://modelcontextprotocol.io/specification/2025-11-25/server/tools).
- [Официальный Python SDK](https://github.com/modelcontextprotocol/python-sdk) — источник для последующего SDK-адаптера; текущий MVP реализован без него.
