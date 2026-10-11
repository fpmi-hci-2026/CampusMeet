#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Update docs/index.html to include:
1. 12 screens counter and all 7 personas indicators
2. Dedicated search wireframe in navigation/search tab & mockups tab
3. Complete 7 personas in Impact Map & CJM table & CJM detailed cards
4. Complete 7 personas in Storyboards & VS-01..07 Edge Cases
5. Resilient offline JS (typeof mermaid !== 'undefined') & hash-based routing
"""

with open("docs/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update stats in #lab2-overview
html = html.replace(
    '<div class="stat-value" style="color: #818cf8;">11 экранов</div>\n                        <div class="stat-label">Векторных Wireframes & UI Mockups</div>',
    '<div class="stat-value" style="color: #818cf8;">12 экранов</div>\n                        <div class="stat-label">Векторных Wireframes & UI Mockups (6 + 6)</div>'
)
html = html.replace(
    '<div class="stat-value" style="color: var(--warning);">7 персонажей</div>\n                        <div class="stat-label">Навигационные модели & Storyboards</div>',
    '<div class="stat-value" style="color: var(--warning);">7 персонажей</div>\n                        <div class="stat-label">Навигационные модели, CJM & Storyboards</div>'
)
html = html.replace(
    'Lab2_report.md (1375 строк)',
    'Lab2_report.md (1466 строк)'
)

# 2. Update #lab2-nav-search with Search Modal Wireframe
search_wireframe_html = '''
                <div class="profile-card" style="margin-top: 24px;">
                    <h3>Вайрфрейм модального окна сквозного поиска Omnibox (⌘K / Ctrl+K)</h3>
                    <p style="color: var(--text-muted); font-size: 0.85rem; margin-bottom: 12px;">
                        Векторный каркас интерфейса быстрого поиска и фасетной фильтрации: поисковая строка с автодополнением и нечетким поиском ($D \\le 2$), чипы активных фильтров, мгновенная выдача с категоризацией (События, Спикеры, Теги), подсказки навигации по стрелкам клавиатуры.
                    </p>
                    <img src="./assets/wireframes/wireframe_desktop_search_modal.svg" alt="Wireframe Desktop Search Modal" style="width: 100%; border-radius: 8px; border: 1px solid var(--border-color); background: #0b1120; margin-top: 8px;"/>
                </div>
'''

if '<h3>Полнотекстовый и нечеткий поиск (Fuzzy Search)</h3>' in html and 'wireframe_desktop_search_modal.svg' not in html:
    html = html.replace(
        '            </section>\n\n            <!-- TAB: Lab 2 CJM & Impact Map -->',
        search_wireframe_html + '            </section>\n\n            <!-- TAB: Lab 2 CJM & Impact Map -->'
    )

# 3. Update #lab2-cjm-impact with all 7 actors and all 7 personas CJM
new_impact_mermaid = '''flowchart TD
    Goal["ЦЕЛЬ ПЛАТФОРМЫ:<br/>Чекин &lt;1.5 сек, No-Show &lt;15%, 100% Offline-Safe"]
    Goal --> A1["1. Слушатели (Артём)"]
    Goal --> A2["2. Волонтеры (Дарья)"]
    Goal --> A3["3. Организаторы (Максим)"]
    Goal --> A4["4. Капитаны хакатонов (Кирилл)"]
    Goal --> A5["5. Спикеры (Виктор)"]
    Goal --> A6["6. Заказчик деканат (Сергей Николаевич)"]
    Goal --> A7["7. Анти-персонаж (Влад)"]

    A1 --> I1["Регистрация в 1 тап и офлайн-билет"]
    A2 --> I2["Потоковое сканирование &lt;500 мс"]
    A3 --> I3["Контроль квот и экстренный Push"]
    A4 --> I4["Мгновенный добор людей по стеку"]
    A5 --> I5["Подача CFP и контроль сценического тайминга"]
    A6 --> I6["Аудит пожарной безопасности и CSV-отчет"]
    A7 --> I7["Пресечение фрода и захвата мест"]

    I1 --> D1["Крипто-билет HMAC-SHA256 + Apple Wallet"]
    I2 --> D2["Оптический сканер с тактильным HUD"]
    I3 --> D3["D&D конструктор сетки + Broadcast шлюз"]
    I4 --> D4["Биржа команд с фильтром компетенций"]
    I5 --> D5["Личный кабинет докладчика + Live-таймер"]
    I6 --> D6["Модуль экспорта ведомостей посещаемости"]
    I7 --> D7["Hard Cap квота + Блокировка дубликатов токена"]'''

old_impact_block = '''flowchart LR
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
    I6 --> D6["Шлюз широковещательного Push"]'''

html = html.replace(old_impact_block, new_impact_mermaid)

all_7_cjm_rows = '''                        <tr>
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
                        <tr>
                            <td><strong>Кирилл Савицкий</strong><br/>(Капитан хакатона)</td>
                            <td>Изучает регламент хакатона; видит нехватку ML-инженера</td>
                            <td>Создает профиль команды на бирже; выставляет вакансию роли</td>
                            <td>Принимает отклик за 3 часа до дедлайна; команда укомплектована</td>
                            <td>Команда кодит; капитан получает синхронные алерты чекпоинтов</td>
                            <td>Загружает ссылку на репозиторий проекта в 1 клик на финальном питче</td>
                        </tr>
                        <tr>
                            <td><strong>Виктор Громов</strong><br/>(Приглашенный спикер)</td>
                            <td>Получает инвайт от Максима через Telegram; согласовывает тему</td>
                            <td>Загружает тезисы и слайды в кабинет спикера; проверяет тайминг 30 мин</td>
                            <td>Приезжает в корпус; персональный бейдж спикера готов без очереди</td>
                            <td>Выступает с докладом; видит мягкий желтый таймер обратного отсчета</td>
                            <td>Получает мгновенный фидбек зала (4.9/5.0) и контакты сильных студентов</td>
                        </tr>
                        <tr>
                            <td><strong>Сергей Николаевич Котов</strong><br/>(Зам. декана / Заказчик)</td>
                            <td>Получает запрос на согласование аудитории 512 на 100 мест</td>
                            <td>Проверяет лимит вместимости Hard Cap в деканском интерфейсе; ставит визу</td>
                            <td>Приходит на площадку во время чекина; очередей в коридоре нет</td>
                            <td>Наблюдает за ходом мероприятия с гостевого планшета</td>
                            <td>Выгружает верифицированный реестр присутствовавших студентов в 1 клик</td>
                        </tr>
                        <tr>
                            <td><strong>Влад Костылев</strong><br/>(Анти-герой / Мерч-хантер)</td>
                            <td>Видит анонс бесплатной пиццы; жмет регистрацию на все ивенты подряд</td>
                            <td>Сталкивается с барьером подтверждения брони за 24 часа</td>
                            <td>Не подтверждает явку; система отзывает билет и передает кандидату из Waitlist</td>
                            <td>Пытается пройти по старому скриншоту билета друга; сканер выдает отказ «Фрод»</td>
                            <td>Остается вне площадки; добросовестные студенты занимают свободные места</td>
                        </tr>'''

old_3_cjm_rows = '''                        <tr>
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
                        </tr>'''

html = html.replace(old_3_cjm_rows, all_7_cjm_rows)

# Add detailed CJM cards below the table in #lab2-cjm-impact
detailed_cjm_cards = '''
                <h2>Детальный анализ путей взаимодействия (CJM Breakdown)</h2>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 16px; margin-top: 16px;">
                    <div class="profile-card">
                        <h3>1. Артём Ковалёв (Слушатель)</h3>
                        <p style="color: var(--text-muted); font-size: 0.85rem;">
                            <strong>Ключевая цель:</strong> Попасть на полезный доклад и пройти в аудиторию мгновенно.<br/>
                            <strong>Эмоциональный трек:</strong> Интерес (+1) → Уверенность (+2) → Облегчение (+2) → Вовлечение (+2) → Удовлетворение (+2).<br/>
                            <strong>Интерфейсное решение:</strong> 1-Tap RSVP, локальный токен билета HMAC-SHA256, авто-яркость 100%, экспорт в Apple Wallet.
                        </p>
                    </div>
                    <div class="profile-card">
                        <h3>2. Дарья Мельникова (Волонтер)</h3>
                        <p style="color: var(--text-muted); font-size: 0.85rem;">
                            <strong>Ключевая цель:</strong> Проверить поток гостей со скоростью &lt;1.5 сек/чел без очередей.<br/>
                            <strong>Эмоциональный трек:</strong> Тревога (-1) → Спокойствие (+1) → Драйв (+2) → Победа (+2) → Гордость (+2).<br/>
                            <strong>Интерфейсное решение:</strong> Видоискатель с тактильным HUD, звуковой/виброотклик, мгновенный детектор дубликатов.
                        </p>
                    </div>
                    <div class="profile-card">
                        <h3>3. Максим Романов (Организатор)</h3>
                        <p style="color: var(--text-muted); font-size: 0.85rem;">
                            <strong>Ключевая цель:</strong> Собрать полный зал, удержать тайминг и не допустить давки.<br/>
                            <strong>Эмоциональный трек:</strong> Напряжение (0) → Контроль (+1) → Стресс (-1) → Облегчение (+2) → Триумф (+2).<br/>
                            <strong>Интерфейсное решение:</strong> Монопольный веб-кабинет, D&D сетка программы, 1-Click экстренный пуш-шлюз.
                        </p>
                    </div>
                    <div class="profile-card">
                        <h3>4. Кирилл Савицкий (Капитан хакатона)</h3>
                        <p style="color: var(--text-muted); font-size: 0.85rem;">
                            <strong>Ключевая цель:</strong> Быстро закрыть дефицит стека в команде и сдать проект вовремя.<br/>
                            <strong>Эмоциональный трек:</strong> Беспокойство (-1) → Надежда (+1) → Воодушевление (+2) → Фокус (+2) → Успех (+2).<br/>
                            <strong>Интерфейсное решение:</strong> Биржа команд с фильтрами по технологиям, командный таймлайн чекпоинтов.
                        </p>
                    </div>
                    <div class="profile-card">
                        <h3>5. Виктор Громов (Приглашенный спикер)</h3>
                        <p style="color: var(--text-muted); font-size: 0.85rem;">
                            <strong>Ключевая цель:</strong> Выступить перед мотивированной аудиторией и уложиться в 30 минут.<br/>
                            <strong>Эмоциональный трек:</strong> Скепсис (0) → Удобство (+1) → Уверенность (+2) → Энергия (+2) → Удовлетворение (+2).<br/>
                            <strong>Интерфейсное решение:</strong> Кабинет докладчика, статус готовности слайдов, таймер сцены с предупреждением о 5 минутах.
                        </p>
                    </div>
                    <div class="profile-card">
                        <h3>6. Сергей Николаевич Котов (Заказчик / Зам. декана)</h3>
                        <p style="color: var(--text-muted); font-size: 0.85rem;">
                            <strong>Ключевая цель:</strong> Соблюдение регламентов пожарной безопасности и отчетность по посещаемости.<br/>
                            <strong>Эмоциональный трек:</strong> Настороженность (0) → Одобрение (+1) → Спокойствие (+2) → Уважение (+2) → Удовлетворение (+2).<br/>
                            <strong>Интерфейсное решение:</strong> Деканский дашборд аудиторного фонда с Hard Cap лимитами и экспорт CSV ведомостей.
                        </p>
                    </div>
                    <div class="profile-card" style="border-left: 3px solid var(--danger);">
                        <h3>7. Влад Костылев (Анти-персонаж / Мерч-хантер)</h3>
                        <p style="color: var(--text-muted); font-size: 0.85rem;">
                            <strong>Паттерн:</strong> Захват бесплатных мест, No-Show 70%, попытки пройти по чужому скриншоту.<br/>
                            <strong>Эмоциональный трек:</strong> Азарт (+1) → Раздражение (-1) → Досада (-2) → Стыд (-2) → Уход (0).<br/>
                            <strong>Барьеры системы:</strong> Обязательное подтверждение брони за 24ч, динамический QR с ротацией каждые 60с, детектор дубликатов.
                        </p>
                    </div>
                </div>
'''

if 'Детальный анализ путей взаимодействия (CJM Breakdown)' not in html:
    html = html.replace(
        '            </section>\n\n            <!-- TAB: Lab 2 Storyboards & Edge Cases -->',
        detailed_cjm_cards + '            </section>\n\n            <!-- TAB: Lab 2 Storyboards & Edge Cases -->'
    )

# 4. Update #lab2-storyboards with all 7 personas Storyboards and VS-01..07
storyboards_cards_html = '''
                <h2>Интерактивные раскадровки (Storyboards) для каждого из 7 персонажей</h2>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 16px; margin-bottom: 24px;">
                    <div class="profile-card">
                        <h4>1. Артём Ковалёв (Слушатель)</h4>
                        <ol style="font-size: 0.85rem; padding-left: 18px; color: var(--text-muted);">
                            <li><strong>Кадр 1:</strong> Листает ленту в перерыве между парами, видит анонс «Deep Learning в продакшене».</li>
                            <li><strong>Кадр 2:</strong> Нажимает «Иду в 1 тап»; билет загружается в локальный защищенный кэш приложения.</li>
                            <li><strong>Кадр 3:</strong> Спускается в подвал без связи, открывает экран билета; экран автоматически включает 100% яркость.</li>
                            <li><strong>Кадр 4:</strong> Волонтер подносит сканер — зеленый сигнал за 0.8 сек, турникет открыт, Артём проходит в зал.</li>
                        </ol>
                    </div>
                    <div class="profile-card">
                        <h4>2. Дарья Мельникова (Волонтер)</h4>
                        <ol style="font-size: 0.85rem; padding-left: 18px; color: var(--text-muted);">
                            <li><strong>Кадр 1:</strong> Вводит 4-значный PIN смены организатора, активируется камера мобильного сканера.</li>
                            <li><strong>Кадр 2:</strong> Направляет прицел видоискателя на QR-код первого подошедшего студента — мягкая тактильная вибрация.</li>
                            <li><strong>Кадр 3:</strong> Второй гость предъявляет скриншот чужого билета — экран вспыхивает красным HUD «ДУБЛИКАТ».</li>
                            <li><strong>Кадр 4:</strong> Дарья спокойно отводит нарушителя, счетчик смены показывает 94/100, очередь движется без пауз.</li>
                        </ol>
                    </div>
                    <div class="profile-card">
                        <h4>3. Максим Романов (Организатор)</h4>
                        <ol style="font-size: 0.85rem; padding-left: 18px; color: var(--text-muted);">
                            <li><strong>Кадр 1:</strong> В веб-панели задает лимит зала (100 мест) и перетаскивает мышью тайм-слоты спикеров в Drag-and-Drop сетке.</li>
                            <li><strong>Кадр 2:</strong> За 30 минут до старта комендант сообщает о закрытии аудитории 512 из-за проводки.</li>
                            <li><strong>Кадр 3:</strong> Максим нажимает «🚨 Экстренный Push в 1 клик», выбирает «Перенос в ауд. 519» и отправляет оповещение.</li>
                            <li><strong>Кадр 4:</strong> Все 100 участников мгновенно получают Push со схемой этажа; митап начинается минута в минуту.</li>
                        </ol>
                    </div>
                    <div class="profile-card">
                        <h4>4. Кирилл Савицкий (Капитан хакатона)</h4>
                        <ol style="font-size: 0.85rem; padding-left: 18px; color: var(--text-muted);">
                            <li><strong>Кадр 1:</strong> Заходит в раздел «Биржа команд», видит статус состава: «3/4 участников, нужен Computer Vision разработчик».</li>
                            <li><strong>Кадр 2:</strong> Размещает карточку вакансии роли с фильтрами по стеку PyTorch / OpenCV.</li>
                            <li><strong>Кадр 3:</strong> Получает пуш с откликом студента с профилем GitHub, принимает заявку за 2 клика.</li>
                            <li><strong>Кадр 4:</strong> Команда в полном составе получает доступ к чекпоинтам и загружает итоговое решение на питч.</li>
                        </ol>
                    </div>
                    <div class="profile-card">
                        <h4>5. Виктор Громов (Приглашенный спикер)</h4>
                        <ol style="font-size: 0.85rem; padding-left: 18px; color: var(--text-muted);">
                            <li><strong>Кадр 1:</strong> Открывает личный кабинет спикера по инвайт-ссылке из Telegram, загружает тезисы доклада.</li>
                            <li><strong>Кадр 2:</strong> Видит статус модерации «Одобрено» и тайм-слот: 18:30–19:00, ауд. 512.</li>
                            <li><strong>Кадр 3:</strong> Выходит к трибуне, интерфейс докладчика показывает таймер с обратным отсчетом (желтый цвет за 5 минут).</li>
                            <li><strong>Кадр 4:</strong> Завершает доклад вовремя, видит в дашборде среднюю оценку зала 4.9/5.0 и контакты 5 лучших студентов.</li>
                        </ol>
                    </div>
                    <div class="profile-card">
                        <h4>6. Сергей Николаевич Котов (Заказчик / Зам. декана)</h4>
                        <ol style="font-size: 0.85rem; padding-left: 18px; color: var(--text-muted);">
                            <li><strong>Кадр 1:</strong> Открывает модуль согласования мероприятий БГУ, видит заявку на митап с ограничением 100 мест.</li>
                            <li><strong>Кадр 2:</strong> Проверяет соблюдение лимитов пожарной безопасности (Hard Cap не превышает емкость зала 512).</li>
                            <li><strong>Кадр 3:</strong> В день события инспектирует коридор — столпотворения и заторов нет благодаря быстрому чекину.</li>
                            <li><strong>Кадр 4:</strong> По окончании мероприятия в 1 клик скачивает официальную ведомость посещаемости в формате `.xlsx`.</li>
                        </ol>
                    </div>
                    <div class="profile-card" style="border-left: 3px solid var(--danger);">
                        <h4>7. Влад Костылев (Анти-персонаж / Мерч-хантер)</h4>
                        <ol style="font-size: 0.85rem; padding-left: 18px; color: var(--text-muted);">
                            <li><strong>Кадр 1:</strong> Видит анонс бесплатной пиццы и автоматически кликает бронь, занимая последнее 100-е место.</li>
                            <li><strong>Кадр 2:</strong> За 24 часа получает push-запрос на подтверждение брони; игнорирует его, предпочитая компьютерную игру.</li>
                            <li><strong>Кадр 3:</strong> Система аннулирует неподтвержденный билет и автоматически передает его первому человеку из листа ожидания.</li>
                            <li><strong>Кадр 4:</strong> Пытается войти на площадку по скриншоту билета друга, сканер Дарьи блокирует проход «Ошибка: код уже использован».</li>
                        </ol>
                    </div>
                </div>
'''

if 'Интерактивные раскадровки (Storyboards) для каждого из 7 персонажей' not in html:
    html = html.replace(
        '                <h2>Матрица проверочных сценариев отказоустойчивости (Edge Cases)</h2>',
        storyboards_cards_html + '                <h2>Матрица проверочных сценариев отказоустойчивости (Edge Cases)</h2>'
    )

# Expand Edge cases table with VS-06 and VS-07
old_vs_rows = '''                        <tr>
                            <td><strong>VS-05</strong></td>
                            <td><strong>Срочный перенос зала</strong></td>
                            <td>Аудитория 512 закрыта комендантом</td>
                            <td>Организатор жмет «Экстренный Push» в 1 клик: звуковой алерт 100 участникам с новой картой</td>
                            <td>Доставка за 1.8 секунды</td>
                        </tr>
                    </tbody>'''

new_vs_rows = '''                        <tr>
                            <td><strong>VS-05</strong></td>
                            <td><strong>Срочный перенос зала</strong></td>
                            <td>Аудитория 512 закрыта комендантом на внеплановый ремонт</td>
                            <td>Организатор жмет «🚨 Экстренный Push в 1 клик»: шлюз рассылает 100 участникам приоритетный Push с обновленной картой этажа</td>
                            <td>Доставка Push 100% активных участников за &lt;2 сек</td>
                        </tr>
                        <tr>
                            <td><strong>VS-06</strong></td>
                            <td><strong>Опоздание ключевого спикера</strong></td>
                            <td>Спикер застрял в дорожной пробке; слот доклада необходимо сдвинуть на 40 минут</td>
                            <td>Организатор в веб-кабинете перетаскивает слоты в Drag-and-Drop конструкторе; мобильные клиенты обновляют таймлайн на лету</td>
                            <td>Сетка докладов синхронизирована без перезагрузки страницы</td>
                        </tr>
                        <tr>
                            <td><strong>VS-07</strong></td>
                            <td><strong>Некомплект команды за 2ч до старта</strong></td>
                            <td>В команде хакатона заболел фронтендер; риск дисквалификации</td>
                            <td>Капитан выставляет статус «🔥 Срочно ищем разработчика»; свободные участники получают push с биржи команд</td>
                            <td>Вакансия закрыта за 40 минут до жеребьевки</td>
                        </tr>
                    </tbody>'''

html = html.replace(old_vs_rows, new_vs_rows)

# 5. Add search modal wireframe in #lab2-mockups
old_wireframes_grid = '''                <h2>2. Структурные схемы низкой точности (Wireframes)</h2>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(400px, 1fr)); gap: 20px;">
                    <div class="profile-card">
                        <h3>Wireframe: Десктопный каталог</h3>
                        <img src="./assets/wireframes/wireframe_desktop_catalog.svg" alt="Wireframe Catalog" style="width: 100%; border-radius: 6px; border: 1px solid var(--border-color);"/>
                    </div>'''

new_wireframes_grid = '''                <h2>2. Структурные схемы низкой точности (Wireframes)</h2>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(400px, 1fr)); gap: 20px;">
                    <div class="profile-card">
                        <h3>Wireframe: Модальное окно поиска Omnibox ⌘K</h3>
                        <p style="color: var(--text-muted); font-size: 0.8rem; margin-bottom: 8px;">Быстрый поиск, фасетные чипы, категоризированные результаты и горячие клавиши.</p>
                        <img src="./assets/wireframes/wireframe_desktop_search_modal.svg" alt="Wireframe Search Modal" style="width: 100%; border-radius: 6px; border: 1px solid var(--border-color);"/>
                    </div>
                    <div class="profile-card">
                        <h3>Wireframe: Десктопный каталог</h3>
                        <img src="./assets/wireframes/wireframe_desktop_catalog.svg" alt="Wireframe Catalog" style="width: 100%; border-radius: 6px; border: 1px solid var(--border-color);"/>
                    </div>'''

html = html.replace(old_wireframes_grid, new_wireframes_grid)

# 6. Update script at bottom: safe mermaid and hash routing
old_script = '''    <script>
        mermaid.initialize({ startOnLoad: true, theme: 'dark' });

        function switchTab(tabId, element) {
            // Hide all tabs
            const panes = document.querySelectorAll('.tab-pane');
            panes.forEach(pane => pane.classList.remove('active'));

            // Show selected tab
            const targetPane = document.getElementById(tabId);
            if (targetPane) {
                targetPane.classList.add('active');
            }

            // Update active nav link
            if (element) {
                const links = document.querySelectorAll('.nav-link');
                links.forEach(link => link.classList.remove('active'));
                element.classList.add('active');
            }

            // Scroll content to top
            document.getElementById('content').scrollTop = 0;
        }
    </script>'''

new_script = '''    <script>
        // Safe mermaid initialization (offline-resilient)
        if (typeof mermaid !== 'undefined') {
            mermaid.initialize({ startOnLoad: true, theme: 'dark' });
        }

        function switchTab(tabId, element) {
            // Hide all tabs
            const panes = document.querySelectorAll('.tab-pane');
            panes.forEach(pane => pane.classList.remove('active'));

            // Show selected tab
            const targetPane = document.getElementById(tabId);
            if (targetPane) {
                targetPane.classList.add('active');
            }

            // Update active nav link
            if (element) {
                const links = document.querySelectorAll('.nav-link');
                links.forEach(link => link.classList.remove('active'));
                element.classList.add('active');
            }

            // Scroll content to top
            const content = document.getElementById('content');
            if (content) content.scrollTop = 0;
        }

        // URL hash routing support
        function handleHash() {
            const hash = window.location.hash.substring(1);
            if (hash) {
                const link = document.querySelector(`.nav-link[href="#${hash}"]`);
                switchTab(hash, link);
            }
        }
        window.addEventListener('DOMContentLoaded', handleHash);
        window.addEventListener('hashchange', handleHash);
    </script>'''

html = html.replace(old_script, new_script)

with open("docs/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Successfully updated docs/index.html! Length:", len(html))
