/**
 * CampusMeet / EventHub — Laboratory 3 Datasets (User Stories & Traceability Matrix)
 */

window.CampusMeetData = window.CampusMeetData || {};

// Key User Stories (US-01..US-12)
window.CampusMeetData.userStories = [
    {
        code: 'US-01',
        role: 'Слушатель',
        story: 'Как слушатель, я хочу зарегистрироваться в 1 клик, чтобы забронировать место без повторного ввода анкеты.',
        priority: 'Must (High)',
        priorityClass: 'tag-anti',
        platform: 'Mobile / Web'
    },
    {
        code: 'US-02',
        role: 'Слушатель',
        story: 'Как участник, я хочу открывать свой QR-билет офлайн, чтобы пройти в аудиторию без сотовой связи.',
        priority: 'Must (High)',
        priorityClass: 'tag-anti',
        platform: 'Mobile (SecureStore)'
    },
    {
        code: 'US-03',
        role: 'Волонтер',
        story: 'Как волонтер, я хочу сканировать QR-коды камерой <500 мс, чтобы ликвидировать очереди на стойке входа.',
        priority: 'Must (High)',
        priorityClass: 'tag-anti',
        platform: 'Mobile Scanner'
    },
    {
        code: 'US-04',
        role: 'Волонтер',
        story: 'Как волонтер, я хочу валидировать подписи HMAC и блокировать дубликаты офлайн, чтобы исключить фрод.',
        priority: 'Must (High)',
        priorityClass: 'tag-anti',
        platform: 'Mobile (Offline Cache)'
    },
    {
        code: 'US-05',
        role: 'Организатор',
        story: 'Как организатор, я хочу валидировать адрес через OSM и календарь через Nager.Date, чтобы исключить накладки.',
        priority: 'Should (Med)',
        priorityClass: 'tag-lead',
        platform: 'Web Dashboard'
    },
    {
        code: 'US-06',
        role: 'Организатор',
        story: 'Как организатор, я хочу задавать Hard Cap и включать Waitlist, чтобы соблюдать пожарные лимиты зала.',
        priority: 'Must (High)',
        priorityClass: 'tag-anti',
        platform: 'Web Dashboard'
    },
    {
        code: 'US-07',
        role: 'Капитан хакатона',
        story: 'Как капитан, я хочу публиковать вакансии по стеку (ML, UI/UX), чтобы быстро добрать команду.',
        priority: 'Should (Med)',
        priorityClass: 'tag-lead',
        platform: 'Mobile / Web'
    },
    {
        code: 'US-08',
        role: 'Организатор',
        story: 'Как администратор, я хочу вызывать сквозной Omnibox по ⌘K, чтобы мгновенно находить события и спикеров.',
        priority: 'Could (Med)',
        priorityClass: 'tag-supp',
        platform: 'Web (⌘K Omnibox)'
    },
    {
        code: 'US-09',
        role: 'Организатор',
        story: 'Как организатор, я хочу отправлять экстренный Push в 1 клик, чтобы уведомить аудиторию о смене зала за <3 с.',
        priority: 'Must (High)',
        priorityClass: 'tag-anti',
        platform: 'Web / Mobile Push'
    },
    {
        code: 'US-10',
        role: 'Слушатель',
        story: 'Как владелец iPhone, я хочу экспортировать билет в Apple Wallet (.pkpass) с геофенсингом на экране блокировки.',
        priority: 'Should (Med)',
        priorityClass: 'tag-lead',
        platform: 'Mobile (iOS / Android)'
    },
    {
        code: 'US-11',
        role: 'Организатор',
        story: 'Как организатор, я хочу верстать программу Drag-and-Drop в сетке таймлайна, чтобы визуально балансировать треки.',
        priority: 'Should (Med)',
        priorityClass: 'tag-lead',
        platform: 'Web Dashboard'
    },
    {
        code: 'US-12',
        role: 'Деканат (Куратор)',
        story: 'Как куратор, я хочу выгружать сводную ведомость чекинов в Excel для контроля учебной посещаемости.',
        priority: 'Could (Low)',
        priorityClass: 'tag-supp',
        platform: 'Web Dashboard'
    }
];

// Traceability Matrix (SRS <-> Stories <-> Use Cases <-> Code)
window.CampusMeetData.traceabilityMatrix = [
    {
        srsId: 'FR-CAT-01',
        us: 'US-01',
        uc: 'UC-01',
        component: 'EventManagementController',
        test: 'Фильтрация каталога и подсчет свободных мест'
    },
    {
        srsId: 'FR-TCK-02',
        us: 'US-02',
        uc: 'UC-02',
        component: 'TicketCryptoEngine',
        test: 'Модульный тест криптографической HMAC-подписи'
    },
    {
        srsId: 'FR-TCK-03',
        us: 'US-02',
        uc: 'UC-02',
        component: 'Mobile Secure Vault',
        test: 'Тест открытия билета в «Авиарежиме» без сети'
    },
    {
        srsId: 'FR-SCN-01',
        us: 'US-03',
        uc: 'UC-02',
        component: 'OpticalScannerEngine',
        test: 'Бенчмарк времени захвата QR-кадра (<500 мс)'
    },
    {
        srsId: 'FR-SCN-03',
        us: 'US-04',
        uc: 'UC-02',
        component: 'AttendanceCheckinService',
        test: 'Стресс-тест блокировки повторного прохода (дубликата)'
    },
    {
        srsId: 'FR-EXT-01',
        us: 'US-05',
        uc: 'UC-03',
        component: 'GeoCalendarAdapter',
        test: 'Интеграционный тест к OpenStreetMap Nominatim'
    },
    {
        srsId: 'FR-NTF-01',
        us: 'US-09',
        uc: 'UC-15',
        component: 'NotificationDispatcher',
        test: 'Тест скорости multicast push-рассылки (<3 с)'
    }
];
