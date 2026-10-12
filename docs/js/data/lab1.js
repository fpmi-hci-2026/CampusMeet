/**
 * CampusMeet / EventHub — Laboratory 1 Datasets (Pain Points & Personas)
 */

window.CampusMeetData = window.CampusMeetData || {};

// Empirical Survey Pain Points (N=68)
window.CampusMeetData.painPoints = [
    {
        issue: 'Сбои мобильного интернета / Wi-Fi в аудиториях',
        n: 24,
        pct: '35.3%',
        severity: 'Критический',
        severityColor: 'var(--danger)'
    },
    {
        issue: 'Очереди на входе из-за ручной сверки фамилий в Excel',
        n: 23,
        pct: '33.8%',
        severity: 'Критический',
        severityColor: 'var(--danger)'
    },
    {
        issue: 'Овербукинг: пришел, а мест в зале не хватило',
        n: 21,
        pct: '30.9%',
        severity: 'Критический',
        severityColor: 'var(--danger)'
    },
    {
        issue: 'Забыл о событии из-за отсутствия пушей',
        n: 20,
        pct: '29.4%',
        severity: 'Высокий',
        severityColor: 'var(--warning)'
    },
    {
        issue: 'Потерял схему прохода в дебрях чатов',
        n: 11,
        pct: '16.2%',
        severity: 'Средний',
        severityColor: 'var(--text-muted)'
    }
];

// Synthesized Personas Gallery (7 Profiles)
window.CampusMeetData.personas = [
    {
        id: 'artem',
        name: 'Артём Ковалёв, 20 лет',
        role: 'Студент 3 курса ФПМИ БГУ • Слушатель митапов',
        tag: 'Ключевой персонаж №1',
        tagClass: 'tag-key',
        avatar: 'assets/personas/artem.jpg',
        desc: 'Активный посетитель лекций и митапов по React и AI. Ценит скорость прохода на входе и возможность заранее собрать персональную программу. Пользуется iPhone 14.'
    },
    {
        id: 'daria',
        name: 'Дарья Мельникова, 19 лет',
        role: 'Студентка 2 курса • Волонтер стойки регистрации',
        tag: 'Ключевой персонаж №2',
        tagClass: 'tag-key',
        avatar: 'assets/personas/daria.jpg',
        desc: 'Встречает гостей на входе. Испытывает огромный стресс от очередей и ручного поиска фамилий в списках. Требует высокоскоростной сканер камерой с откликом < 500 мс.'
    },
    {
        id: 'maxim',
        name: 'Максим Романов, 22 года',
        role: 'Студент 4 курса • Лидер IT-клуба, Организатор',
        tag: 'Ключевой персонаж №3',
        tagClass: 'tag-key',
        avatar: 'assets/personas/maxim.jpg',
        desc: 'Организует хакатоны и митапы на 100+ человек. Устал от хаоса Google Forms, потери заявок спикеров и отсутствия инструмента для экстренного оповещения участников.'
    },
    {
        id: 'kirill',
        name: 'Кирилл Савицкий, 21 год',
        role: 'Fullstack разработчик • Капитан команды хакатона',
        tag: 'Дополнительный персонаж',
        tagClass: 'tag-lead',
        avatar: 'assets/personas/kirill.jpg',
        desc: 'Ищет толковых ML-инженеров и дизайнеров в команду. Нуждается в бирже нетворкинга с фильтрацией по стеку и синхронных напоминаниях о питчах проектов.'
    },
    {
        id: 'viktor',
        name: 'Виктор Громов, 27 лет',
        role: 'Senior Backend Architect • Приглашенный спикер',
        tag: 'Вспомогательный персонаж',
        tagClass: 'tag-supp',
        avatar: 'assets/personas/viktor.jpg',
        desc: 'Выступает с докладами по распределенным системам. Требует прозрачного CFP, четкого регламента времени и оперативного пуша при сдвиге тайминга доклада.'
    },
    {
        id: 'sergey',
        name: 'Сергей Николаевич Котов, 45 лет',
        role: 'Зам. декана по воспитательной работе ФПМИ БГУ',
        tag: 'Заказчик системы',
        tagClass: 'tag-supp',
        avatar: 'assets/personas/sergey.jpg',
        desc: 'Заинтересован в цивилизованном учете посещаемости мероприятий, защите аудиторий от переполнения и формировании официальных отчетов для руководства вуза.'
    },
    {
        id: 'vlad',
        name: 'Влад Костылев, 21 год',
        role: '«Мерч-хантер и халявщик» • No-show фактор',
        tag: 'Отрицательный персонаж (Анти)',
        tagClass: 'tag-anti',
        avatar: 'assets/personas/vlad.jpg',
        desc: 'Регистрируется на все митапы подряд ради бесплатной пиццы и наклеек, блокируя места реальным участникам, и часто не приходит. Система защищается подтверждением явки за 24 ч.'
    }
];
