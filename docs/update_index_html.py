#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Update docs/index.html to include comprehensive interactive sections for Laboratory Work No. 2
"""

with open("docs/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update sidebar
lab2_nav = '''
        <div class="nav-section-title">Лабораторная работа №2</div>
        <ul class="nav-menu">
            <li class="nav-item">
                <a href="#lab2-overview" class="nav-link" onclick="switchTab('lab2-overview', this)">
                    Лаб. №2: Обзор и концепция
                </a>
            </li>
            <li class="nav-item">
                <a href="#lab2-ia" class="nav-link" onclick="switchTab('lab2-ia', this)">
                    Инфо-архитектура и Sitemap
                </a>
            </li>
            <li class="nav-item">
                <a href="#lab2-nav-search" class="nav-link" onclick="switchTab('lab2-nav-search', this)">
                    Системы навигации и поиска
                </a>
            </li>
            <li class="nav-item">
                <a href="#lab2-cjm-impact" class="nav-link" onclick="switchTab('lab2-cjm-impact', this)">
                    Impact Map и CJM пути
                </a>
            </li>
            <li class="nav-item">
                <a href="#lab2-storyboards" class="nav-link" onclick="switchTab('lab2-storyboards', this)">
                    Раскадровки и Edge Cases
                </a>
            </li>
            <li class="nav-item">
                <a href="#lab2-mockups" class="nav-link" onclick="switchTab('lab2-mockups', this)">
                    Вайрфреймы и UI Макеты
                </a>
            </li>
        </ul>
'''

# Find insertion point in sidebar: right after the first <ul class="nav-menu">...</ul> of Lab 1
target_sidebar_str = '            <li class="nav-item">\n                <a href="#as-is-processes" class="nav-link" onclick="switchTab(\'as-is-processes\', this)">\n                    Процессы As-Is\n                </a>\n            </li>\n        </ul>'
if target_sidebar_str in html:
    html = html.replace(target_sidebar_str, target_sidebar_str + lab2_nav)
else:
    print("Warning: target_sidebar_str not found!")

# Update external links in sidebar to include Lab 2 report
ext_target = '<a href="./reports/Lab1_report.md" class="nav-link" target="_blank">\n                    Открыть сырой Markdown\n                </a>'
new_ext = '<a href="./reports/Lab2_report.md" class="nav-link" target="_blank" style="color: #38bdf8; font-weight: bold;">\n                    📄 Отчет Лаб. №2 (Markdown)\n                </a>\n            </li>\n            <li class="nav-item">\n                <a href="./reports/Lab1_report.md" class="nav-link" target="_blank">\n                    📄 Отчет Лаб. №1 (Markdown)\n                </a>'
if ext_target in html:
    html = html.replace(ext_target, new_ext)

# 2. Add Tab panes before </main>
lab2_sections = '''
            <!-- TAB: Lab 2 Overview -->
            <section id="lab2-overview" class="tab-pane">
                <div class="hero-card" style="border-left: 4px solid var(--accent);">
                    <span class="brand-badge">Лабораторная работа №2</span>
                    <h1>Проектирование информационной архитектуры и взаимодействия с пользователем</h1>
                    <p>Концептуальное проектирование кроссплатформенной экосистемы CampusMeet / EventHub: дуальная модель Web & Mobile, структуры систем организации, именования, навигации и поиска, эмпирическая карточная сортировка OptimalSort, карты путей клиентов (CJM) и Impact Mapping.</p>
                    <div style="display: flex; gap: 12px; margin-top: 20px; flex-wrap: wrap;">
                        <a href="./reports/Lab2_report.md" class="btn btn-primary" target="_blank">📄 Открыть полный отчет Lab2_report.md (1375 строк)</a>
                        <button class="btn btn-secondary" onclick="switchTab('lab2-mockups', document.querySelector('a[href=\\'#lab2-mockups\\']'))">🎨 Перейти к дизайн-макетам</button>
                    </div>
                </div>

                <div class="stats-grid" style="grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); margin-top: 24px;">
                    <div class="stat-card">
                        <div class="stat-value" style="color: var(--accent);">4 уровня</div>
                        <div class="stat-label">Глубина карты сайта (Sitemap)</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-value" style="color: var(--success);">N = 15</div>
                        <div class="stat-label">Респондентов OptimalSort</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-value" style="color: var(--warning);">7 персонажей</div>
                        <div class="stat-label">Навигационные модели & Storyboards</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-value" style="color: #818cf8;">11 экранов</div>
                        <div class="stat-label">Векторных Wireframes & UI Mockups</div>
                    </div>
                </div>

                <h2>Ключевые концептуальные решения Лабораторной работы №2</h2>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; margin-top: 16px;">
                    <div class="profile-card">
                        <h3>1. Разделение типов интерфейса (Купер)</h3>
                        <p style="color: var(--text-muted); font-size: 0.9rem;">
                            <strong>Монопольный интерфейс:</strong> Десктопный Web-кабинет организатора для длительных рабочих сессий (30–90 мин), высокой информационной плотности и верстки таймлайна.<br/><br/>
                            <strong>Временный интерфейс:</strong> Мобильный экран электронного билета и сканер волонтера (внимание на 5–15 секунд, эргономика Thumb Zone).
                        </p>
                    </div>
                    <div class="profile-card">
                        <h3>2. Отказоустойчивость Zero-Latency Offline</h3>
                        <p style="color: var(--text-muted); font-size: 0.9rem;">
                            Локальное шифрованное хранение билета (SecureStore / Keystore), криптографическая подпись HMAC-SHA256 с ротацией токена каждые 60с для защиты от скриншотов, авто-яркость 100% при открытии билета.
                        </p>
                    </div>
                    <div class="profile-card">
                        <h3>3. Управление квотами и лист ожидания</h3>
                        <p style="color: var(--text-muted); font-size: 0.9rem;">
                            Жесткий лимит вместимости (Hard Cap), обязательное подтверждение явки за 24 часа и автоматическая передача освободившихся мест кандидатам из листа ожидания (Waitlist auto-promotion).
                        </p>
                    </div>
                </div>

                <h2>Сводная диаграмма путей экосистемы CampusMeet</h2>
                <div class="mermaid">
flowchart LR
    Start([Точка входа: Web / Mobile]) --> Landing[Афиша событий]
    Landing --> Details[Детальная страница митапа]
    Details --> CapCheck{Места есть?}
    CapCheck -->|Да| TicketVault[(Локальный SecureStore)]
    CapCheck -->|Лимит исчерпан| Waitlist[Лист ожидания]
    TicketVault --> OfflinePass[Офлайн QR-билет]
    OfflinePass --> ScanCheckin[Оптический сканер волонтера: &lt;500мс]
    ScanCheckin --> SuccessAdmission[Вход: Зеленый HUD]
    SuccessAdmission --> TrackStream[Интерактивная программа]
    ScanCheckin --> LiveAudit[(Live-лента чекина организатора)]
                </div>
            </section>

            <!-- TAB: Lab 2 IA & Sitemap -->
            <section id="lab2-ia" class="tab-pane">
                <h1>Информационная архитектура и Карта сайта (Sitemap)</h1>
                <p>Разработка структуры данных, классификации контента и иерархического чертежа сайта с глубиной вложенности более 3 уровней.</p>

                <h2>Иерархическая карта сайта (Sitemap)</h2>
                <div class="mermaid">
graph TD
    Root["Главная страница (CampusMeet Portal)"]
    Root --> Events["1.0. Каталог событий (Афиша)"]
    Root --> Hackathons["2.0. Хакатоны и контесты"]
    Root --> Teams["3.0. Биржа команд (Team Match)"]
    Root --> MyTickets["4.0. Личный кабинет участника"]
    Root --> Organizer["5.0. Кабинет организатора"]

    Events --> EventPage["1.1. Страница события (:slug)"]
    EventPage --> EventReg["1.1.1. Регистрация в 1 клик"]
    EventPage --> EventSchedule["1.1.2. Программа докладов"]
    EventPage --> EventSpeakers["1.1.3. Список спикеров"]
    EventPage --> EventVenue["1.1.4. Схема проезда (OSM)"]

    EventSchedule --> TrackSlot["1.1.2.1. Детали доклада и тезисы"]
    EventVenue --> FloorMap["1.1.4.1. План этажа аудитории 512"]

    Teams --> TeamCard["3.1. Карточка команды (:team_id)"]
    TeamCard --> ApplyRole["3.1.1. Отклик на вакансию"]

    MyTickets --> TicketPass["4.1. Электронный билет (:ticket_id)"]
    TicketPass --> AppleWallet["4.1.1. Apple Wallet (.pkpass)"]

    Organizer --> OrgEvent["5.1. Управление митапом (:id)"]
    OrgEvent --> OrgBuilder["5.1.1. Конструктор таймлайна D&D"]
    OrgEvent --> OrgCheckin["5.1.2. Live-мониторинг чекина"]
    OrgEvent --> OrgBroadcast["5.1.3. Экстренный Push"]
                </div>

                <h2>Инвентаризация и аудит контента</h2>
                <table>
                    <thead>
                        <tr>
                            <th>ID</th>
                            <th>Единица контента</th>
                            <th>Тип данных</th>
                            <th>Объем</th>
                            <th>Владелец</th>
                            <th>Частота обновления</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr><td><strong>CNT-01</strong></td><td>Карточка анонса митапа</td><td>Текст + Баннер 16:9 + Теги</td><td>500–1000 Б</td><td>Организатор</td><td>1–3 раза в неделю</td></tr>
                        <tr><td><strong>CNT-02</strong></td><td>Программа докладов (Таймлайн)</td><td>Иерархический список слотов</td><td>2–5 КБ</td><td>Модератор</td><td>До начала события</td></tr>
                        <tr><td><strong>CNT-03</strong></td><td>Электронный билет</td><td>QR-код + HMAC-SHA256 токен</td><td>256 Б</td><td>Ядро системы</td><td>Ротация каждые 60с</td></tr>
                        <tr><td><strong>CNT-06</strong></td><td>Профиль команды хакатона</td><td>Стек + Список вакансий ролей</td><td>1–2 КБ</td><td>Капитан</td><td>По мере комплектования</td></tr>
                        <tr><td><strong>CNT-07</strong></td><td>Интерактивная карта проезда</td><td>Векторные тайлы OSM + Геомаркер</td><td>50–200 КБ</td><td>Nominatim API</td><td>Привязана к залу</td></tr>
                        <tr><td><strong>CNT-08</strong></td><td>Лог входа (Check-in feed)</td><td>Транзакционная запись</td><td>128 Б</td><td>Сканер волонтера</td><td>Real-time потоковое</td></tr>
                        <tr><td><strong>CNT-09</strong></td><td>Экстренное оповещение</td><td>Высокоприоритетный Push-алерт</td><td>100–300 Б</td><td>Организатор</td><td>По факту форс-мажора</td></tr>
                    </tbody>
                </table>
            </section>

            <!-- TAB: Lab 2 Navigation & Search -->
            <section id="lab2-nav-search" class="tab-pane">
                <h1>Системы навигации и поиска</h1>
                <p>Эмпирическая открытая карточная сортировка OptimalSort ($N=15$), трехуровневая навигация, граф состояний главного меню и фасетный полнотекстовый поиск.</p>

                <h2>Результаты открытой карточной сортировки OptimalSort (35 карточек, N=15)</h2>
                <div class="mermaid">
flowchart LR
    subgraph Clusters["Сформированные кластеры навигации"]
        C1["Кластер 1 (Сходство 88%): Афиша и каталог<br/>- Каталог митапов<br/>- Фасетные фильтры<br/>- Поиск событий ⌘K<br/>- Календарь"]
        C2["Кластер 2 (Сходство 93%): Мой билет<br/>- QR-пропуск офлайн<br/>- Apple Wallet<br/>- Схема прохода в ауд. 512"]
        C3["Кластер 3 (Сходство 80%): Биржа команд<br/>- Команды хакатона<br/>- Поиск по стеку технологий<br/>- Отклик на вакансию"]
        C4["Кластер 4 (Сходство 91%): Кабинет организатора<br/>- Конструктор расписания D&D<br/>- Live-чекин поток<br/>- Экстренный Push-алерт<br/>- Экспорт CSV для деканата"]
    end
                </div>

                <h2>Граф состояний главного меню (Menu State Graph)</h2>
                <p style="color: var(--text-muted); font-size: 0.9rem;">Отображает изменение доступности разделов и команд меню в зависимости от роли и контекста экранной формы:</p>
                <div class="mermaid">
stateDiagram-v2
    [*] --> GuestState: Вход на сайт
    GuestState --> AttendeeState: Авторизация студента
    AttendeeState --> VolunteerState: Ввод PIN-кода волонтера
    AttendeeState --> OrganizerState: Открытие созданного митапа
    GuestState --> DeanState: Вход BSU SSO (@bsu.by)
    VolunteerState --> AttendeeState: Закрытие смены
    OrganizerState --> AttendeeState: Возврат в профиль
    DeanState --> GuestState: Выход
                </div>

                <h2>Архитектура поисковой системы и фасетов</h2>
                <div class="profile-card" style="margin-top: 16px;">
                    <h3>Полнотекстовый и нечеткий поиск (Fuzzy Search)</h3>
                    <p style="color: var(--text-muted); font-size: 0.9rem;">
                        Поддержка горячих клавиш <code>⌘K</code> / <code>Ctrl+K</code>, автодополнение подсказок с классификацией (События, Спикеры, Теги), обработка опечаток с расстоянием Левенштейна $D \le 2$. Взвешенная формула релевантности:<br/>
                        <code>Score = 10·Title + 8·Tags + 6·Speakers + 5·Venue + 3·Description</code>.
                    </p>
                </div>
            </section>

            <!-- TAB: Lab 2 CJM & Impact Map -->
            <section id="lab2-cjm-impact" class="tab-pane">
                <h1>Карта влияния (Impact Map) и Пути клиентов (CJM)</h1>
                <p>Декомпозиция целей платформы и подробные карты клиентского пути (Customer Journey Maps) для ключевых персонажей проекта.</p>

                <h2>Карта влияния (Impact Map)</h2>
                <div class="mermaid">
flowchart LR
    Goal["ЦЕЛЬ:<br/>Чекин &lt;1.5 сек,<br/>No-Show &lt;15%,<br/>100% без сети"]
    Goal --> A1["Слушатели"]
    Goal --> A2["Волонтеры"]
    Goal --> A3["Организаторы"]

    A1 --> I1["Регистрация в 1 тап"]
    A1 --> I2["Показ билета без интернета"]
    A2 --> I3["Сканирование камерой &lt;500 мс"]
    A2 --> I4["Отсечение повторных скриншотов"]
    A3 --> I5["Контроль Hard Cap квот"]
    A3 --> I6["1-Click экстренное вещание"]

    I1 --> D1["1-Click Auth через Telegram/SSO"]
    I2 --> D2["Offline SecureStore + HMAC-SHA256"]
    I3 --> D3["Камера-сканер с виброоткликом"]
    I4 --> D4["Детектор дубликатов в real-time"]
    I5 --> D5["Авто-перевод из Waitlist при отмене"]
    I6 --> D6["Шлюз широковещательного Push"]
                </div>

                <h2>Сводная матрица этапов CJM ключевых персонажей</h2>
                <table>
                    <thead>
                        <tr>
                            <th>Персонаж</th>
                            <th>1. Поиск / Подготовка</th>
                            <th>2. Регистрация</th>
                            <th>3. Вход на площадку</th>
                            <th>4. Участие / Деятельность</th>
                            <th>5. Финал / Отчет</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td><strong>Артём Ковалёв</strong><br/>(Слушатель)</td>
                            <td>Находит анонс митапа по тегам GenAI в перерыве между парами</td>
                            <td>Регистрируется в 1 тап; подтверждает бронь за 24ч через Push</td>
                            <td>Открывает офлайн-билет в подвале; проходит контроль за 1 секунду</td>
                            <td>Смотрит персональный таймлайн докладов во 2 ряду</td>
                            <td>Оценивает доклады на 5 звезд; скачивает слайды презентации</td>
                        </tr>
                        <tr>
                            <td><strong>Дарья Мельникова</strong><br/>(Волонтер)</td>
                            <td>Получает PIN смены; открывает режим сканера камеры</td>
                            <td>Тестирует прицел видоискателя и тактильный виброотклик</td>
                            <td>Сканирует 100 гостей со скоростью 1 чел в 1.1 сек</td>
                            <td>Пресекает вход по пересланному скриншоту билета</td>
                            <td>Счетчик 94/100; закрывает смену без утомления и очередей</td>
                        </tr>
                        <tr>
                            <td><strong>Максим Романов</strong><br/>(Организатор)</td>
                            <td>Создает карточку митапа; валидирует праздники через Nager.Date</td>
                            <td>Верстает таймлайн в Drag-and-Drop конструкторе; модерирует CFP</td>
                            <td>Следит за дашбордом входов; Waitlist закрывает неявки</td>
                            <td>При ремонте проводки жмет «Экстренный Push»: перенос в ауд. 519</td>
                            <td>Экспортирует официальную ведомость с явкой 88% для зам. декана</td>
                        </tr>
                    </tbody>
                </table>
            </section>

            <!-- TAB: Lab 2 Storyboards & Edge Cases -->
            <section id="lab2-storyboards" class="tab-pane">
                <h1>Интерактивные раскадровки и Проверочные сценарии</h1>
                <p>Моделирование нестандартных и форс-мажорных ситуаций (Verification Scenarios / Edge Cases) для гарантии отказоустойчивости решений.</p>

                <h2>Матрица проверочных сценариев отказоустойчивости (Edge Cases)</h2>
                <table>
                    <thead>
                        <tr>
                            <th>Код</th>
                            <th>Стресс-сценарий</th>
                            <th>Входные условия</th>
                            <th>Поведение системы и алгоритм защиты</th>
                            <th>Результат верификации</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td><strong>VS-01</strong></td>
                            <td><strong>Полный офлайн у гостя</strong></td>
                            <td>0% сигнала LTE в цокольном этаже</td>
                            <td>Рендеринг QR из локального защищенного SecureStore</td>
                            <td>Билет открыт за &lt;200 мс</td>
                        </tr>
                        <tr>
                            <td><strong>VS-02</strong></td>
                            <td><strong>Повторный проход (Фрод)</strong></td>
                            <td>Пересылка скриншота троим друзьям</td>
                            <td>Сканер фиксирует повторный хэш: двойная вибрация, красный экран с временем первого чекина</td>
                            <td>100% блокировка дубликата</td>
                        </tr>
                        <tr>
                            <td><strong>VS-03</strong></td>
                            <td><strong>Разбитый экран смартфона</strong></td>
                            <td>Треснувшее защитное стекло гостя</td>
                            <td>Волонтер переключается в «Ручной поиск» по фамилии в 1 тап</td>
                            <td>Гость верифицирован за &lt;5 сек</td>
                        </tr>
                        <tr>
                            <td><strong>VS-04</strong></td>
                            <td><strong>Овербукинг и лист ожидания</strong></td>
                            <td>Заняты все 100 мест в зале</td>
                            <td>101-й ставится в Waitlist; при отказе брони за 24ч место мгновенно передается кандидату</td>
                            <td>100% заполняемость без давки</td>
                        </tr>
                        <tr>
                            <td><strong>VS-05</strong></td>
                            <td><strong>Срочный перенос зала</strong></td>
                            <td>Аудитория 512 закрыта комендантом</td>
                            <td>Организатор жмет «Экстренный Push» в 1 клик: звуковой алерт 100 участникам с новой картой</td>
                            <td>Доставка за 1.8 секунды</td>
                        </tr>
                    </tbody>
                </table>

                <h2>Совокупная диаграмма взаимодействия (State Machine)</h2>
                <div class="mermaid">
stateDiagram-v2
    [*] --> Idle: Открытие приложения
    Idle --> Booking: Выбор митапа и регистрация
    Booking --> IssueTicket: Hard Cap доступен
    Booking --> WaitlistQueue: Лимит исчерпан
    WaitlistQueue --> IssueTicket: Авто-промоушн
    IssueTicket --> LocalSecureVault: Шифрование HMAC-SHA256
    LocalSecureVault --> PresentationMode: Вызов билета офлайн (100% яркость)
    PresentationMode --> ScannerReading: Оптическое сканирование
    ScannerReading --> ValidEntry: Код уникален и валиден
    ScannerReading --> DuplicateAlert: Повторный код (Фрод)
    ValidEntry --> HallAdmission: Зеленый вибро-отклик
    DuplicateAlert --> Rejection: Красный звуковой алерт
    HallAdmission --> EmergencyHandling: Возникновение форс-мажора
    EmergencyHandling --> HallAdmission: Обновление зала по Push
    HallAdmission --> FeedbackRating: Оценка и закрытие
    FeedbackRating --> [*]
                </div>
            </section>

            <!-- TAB: Lab 2 Mockups & Wireframes Gallery -->
            <section id="lab2-mockups" class="tab-pane">
                <h1>Векторные каркасы (Wireframes) и Дизайн-макеты (Mockups)</h1>
                <p>Полная галерея проектных макетов экосистемы CampusMeet: 12-колоночная сетка десктопа (1440px) и 8-точечная сетка мобильных устройств (375x812px).</p>

                <h2>1. Цветные дизайн-макеты высокого уровня детализации (UI Mockups)</h2>
                
                <div class="profile-card" style="margin-bottom: 24px;">
                    <h3>Десктоп: Каталог событий и митапов (1440 × 960 px)</h3>
                    <p style="color: var(--text-muted); font-size: 0.85rem; margin-bottom: 12px;">Полноэкранный темный интерфейс с фасетной фильтрацией, поиском Omnibox ⌘K, карточками событий и индикаторами квот.</p>
                    <img src="./assets/mockups/mockup_desktop_catalog.svg" alt="Mockup Desktop Catalog" style="width: 100%; border-radius: 8px; border: 1px solid var(--border-color); background: #0b1120;"/>
                </div>

                <div class="profile-card" style="margin-bottom: 24px;">
                    <h3>Десктоп: Страница события с интерактивным таймлайном и картой OSM (1440 × 1100 px)</h3>
                    <p style="color: var(--text-muted); font-size: 0.85rem; margin-bottom: 12px;">Двухколоночная верстка: сетка докладов спикеров, Sticky-виджет регистрации со статусом Hard Cap и векторная схема проезда.</p>
                    <img src="./assets/mockups/mockup_desktop_event_details.svg" alt="Mockup Desktop Event Details" style="width: 100%; border-radius: 8px; border: 1px solid var(--border-color); background: #0b1120;"/>
                </div>

                <div class="profile-card" style="margin-bottom: 24px;">
                    <h3>Десктоп: Кабинет организатора и Live Check-in мониторинг (1440 × 960 px)</h3>
                    <p style="color: var(--text-muted); font-size: 0.85rem; margin-bottom: 12px;">4 аналитические карточки KPI, журнал потоковой верификации с выявлением попытки прохода по дубликату и кнопка экстренного пуша.</p>
                    <img src="./assets/mockups/mockup_desktop_dashboard.svg" alt="Mockup Desktop Dashboard" style="width: 100%; border-radius: 8px; border: 1px solid var(--border-color); background: #0b1120;"/>
                </div>

                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 24px; margin-bottom: 32px;">
                    <div class="profile-card">
                        <h3>Мобайл: Афиша событий (375 × 812 px)</h3>
                        <p style="color: var(--text-muted); font-size: 0.85rem; margin-bottom: 12px;">Карусель категорий, карточки с регистрацией в 1 тап и эргономичный таб-бар.</p>
                        <div style="text-align: center;">
                            <img src="./assets/mockups/mockup_mobile_catalog.svg" alt="Mockup Mobile Catalog" style="width: 100%; max-width: 320px; border-radius: 20px; border: 1px solid var(--border-color);"/>
                        </div>
                    </div>

                    <div class="profile-card">
                        <h3>Мобайл: Офлайн-билет с QR (375 × 812 px)</h3>
                        <p style="color: var(--text-muted); font-size: 0.85rem; margin-bottom: 12px;">Высококонтрастный матричный QR-код, таймер HMAC, 100% авто-яркость и Apple Wallet.</p>
                        <div style="text-align: center;">
                            <img src="./assets/mockups/mockup_mobile_ticket.svg" alt="Mockup Mobile Ticket" style="width: 100%; max-width: 320px; border-radius: 20px; border: 1px solid var(--border-color);"/>
                        </div>
                    </div>

                    <div class="profile-card">
                        <h3>Мобайл: Сканер волонтера (375 × 812 px)</h3>
                        <p style="color: var(--text-muted); font-size: 0.85rem; margin-bottom: 12px;">Видоискатель камеры с прицелом, зеленый HUD верификации, счетчик смены и ручной поиск.</p>
                        <div style="text-align: center;">
                            <img src="./assets/mockups/mockup_mobile_scanner.svg" alt="Mockup Mobile Scanner" style="width: 100%; max-width: 320px; border-radius: 20px; border: 1px solid var(--border-color);"/>
                        </div>
                    </div>
                </div>

                <h2>2. Структурные схемы низкой точности (Wireframes)</h2>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(400px, 1fr)); gap: 20px;">
                    <div class="profile-card">
                        <h3>Wireframe: Десктопный каталог</h3>
                        <img src="./assets/wireframes/wireframe_desktop_catalog.svg" alt="Wireframe Catalog" style="width: 100%; border-radius: 6px; border: 1px solid var(--border-color);"/>
                    </div>
                    <div class="profile-card">
                        <h3>Wireframe: Детали события и регистрация</h3>
                        <img src="./assets/wireframes/wireframe_desktop_event_details.svg" alt="Wireframe Details" style="width: 100%; border-radius: 6px; border: 1px solid var(--border-color);"/>
                    </div>
                    <div class="profile-card">
                        <h3>Wireframe: Панель организатора</h3>
                        <img src="./assets/wireframes/wireframe_desktop_dashboard.svg" alt="Wireframe Dashboard" style="width: 100%; border-radius: 6px; border: 1px solid var(--border-color);"/>
                    </div>
                    <div class="profile-card">
                        <h3>Wireframe: Мобильный билет и Сканер</h3>
                        <div style="display: flex; gap: 12px; justify-content: center;">
                            <img src="./assets/wireframes/wireframe_mobile_ticket.svg" alt="Wireframe Ticket" style="width: 48%; border-radius: 12px; border: 1px solid var(--border-color);"/>
                            <img src="./assets/wireframes/wireframe_mobile_scanner.svg" alt="Wireframe Scanner" style="width: 48%; border-radius: 12px; border: 1px solid var(--border-color);"/>
                        </div>
                    </div>
                </div>
            </section>
'''

# Insert lab2_sections right before </main>
main_close = '        </div>\n    </main>'
if main_close in html:
    html = html.replace(main_close, lab2_sections + '\n        </div>\n    </main>')
else:
    print("Warning: main_close not found!")

with open("docs/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print(f"Updated docs/index.html successfully! Total length: {len(html)} chars")
