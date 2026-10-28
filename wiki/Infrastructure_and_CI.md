# Инфраструктура и CI/CD — ЛР4, дополнительное задание 6

![Инфраструктура](../docs/diagrams/lab4/infrastructure.svg)

## 1. Структура четырех репозиториев

| Репозиторий | Что добавлено в ЛР4 |
|:--|:--|
| CampusMeet | Отчет, Wiki, 6 SVG-схем с исходниками, портал ЛР4, Swagger UI и офлайн-каталог |
| CampusMeet-Server | 33 операции OpenAPI, 17 таблиц PostgreSQL/SQLite, HTTP mock, MCP, тесты, Compose, CI, Sonar и Render-конфигурация |
| CampusMeet-Web | Отдельная demo-афиша Node.js 22 без зависимостей, API-прокси, Dockerfile и 3 теста |
| CampusMeet-Mobile | Минимальный Expo-экран App.js, конфигурация адреса API, 3 теста клиента и CI |

Web demo представляет минимальную афишу для демонстрации интеграции с API. Мобильный клиент использует каркас Expo и общий контракт каталога.

## 2. Локальный запуск контейнеров

Все репозитории находятся рядом. Из CampusMeet-Server:

```bash
docker compose config --quiet
docker compose up --build -d
docker compose ps
curl http://127.0.0.1:8000/api/v1/health
curl http://127.0.0.1:3000/health
python3 scripts/smoke_http.py --output evidence/http-session.json
```

Smoke-сценарий требует свежую отдельную mock-базу: регистрация Артёма, повтор по одному ключу, запрет чужого билета, первый и повторный проход, запрет отмены после прохода. Он изменяет учебные данные. Если уже были другие прогоны, запустите локальный API с новым `--db` или используйте отдельное имя Compose-проекта с новыми volumes. `docker compose down` сохраняет данные; удаление volumes намеренно не включено в обычную остановку.

Для автоматического отдельного прогона: `bash scripts/verify-docker.sh` из Server. Нужны свободные порты 8000 и 3000. Скрипт создает свой Compose-проект, проверяет API/Web/PostgreSQL, сохраняет evidence/docker-verification.txt и evidence/http-session.json, затем удаляет только созданные им временные контейнеры/volumes.

```bash
# Отдельная PostgreSQL для проверки DDL:
docker compose --profile database up -d postgres
docker compose exec postgres psql -U campusmeet -d campusmeet -c '\\dt'
# Локальный SonarQube (анализ запускается отдельно):
docker compose --profile quality up -d sonarqube
```

API использует SQLite volume. PostgreSQL профиль применяет физический DDL только при создании пустого PostgreSQL volume; изменение файла не обновляет существующую базу автоматически. Пароль по умолчанию — демонстрационный, PostgreSQL-порт не публикуется наружу. SonarQube доступен только на loopback:9000; для проекта нужны токен и запуск SonarScanner. Аналогичный `sonar-project.properties` есть в Web.

## 3. CI и публикация

Серверный workflow: checkout → Python → установка dev-валидаторов → lint → экспорт контрактов → проверка git diff → тесты → MCP transcript → PostgreSQL DDL → Docker build → HTTP smoke. Сборка зависит от тестового job. Web CI выполняет тесты до Docker build; Mobile CI проверяет синтаксис и API-клиент.

Ручной workflow `quality-deploy.yml` выполняет тесты и quality gate SonarCloud с ожиданием результата. Требуются секрет `SONAR_TOKEN` и переменная `SONAR_ORGANIZATION`. Деплой допускается только после этого job, при явно включенном `deploy`, настроенном environment `production` и `RENDER_DEPLOY_HOOK`. Проверки не объявляются успешными при отсутствии ключей.

Для Render подготовлен blueprint `render.yaml` с отключенным автодеплоем. Это mock с временным SQLite: данные могут сбрасываться при пересоздании контейнера. Облачный аккаунт, проект Sonar, deploy hook и GitHub environment еще не настроены; опубликованного URL нет. Статус бесплатного тарифа и доступность платформы проверяются при реальном развертывании.

## 4. Ветки, проект и план работ

Регламент проекта предусматривает main для production, develop для интеграции, feature/* для реализации и docs/lab4 для документации.

[План задач](../docs/data/lab4/project-plan.csv) объединяет разработку моделей данных, API, MCP, документации и клиентских окружений. Процесс работы с задачами: To do → In progress → To check → Done.

## 5. Документация инструментов

[Docker Compose: startup order](https://docs.docker.com/compose/how-tos/startup-order/) · [PostgreSQL: ограничения](https://www.postgresql.org/docs/16/ddl-constraints.html) · [GitHub Actions](https://docs.github.com/en/actions) · [SonarQube](https://docs.sonarsource.com/sonarqube-server/) · [Render Docker](https://render.com/docs/docker).

Проверка документации в GitHub сопоставляет OpenAPI с соседним репозиторием Server. Для приватного Server нужен секрет CAMPUSMEET_READ_TOKEN с правом чтения этого репозитория; стандартного github.token может быть недостаточно. Сначала отправляется серверный контракт, затем соответствующий snapshot документации. Само наличие workflow не означает, что доступ уже настроен.
