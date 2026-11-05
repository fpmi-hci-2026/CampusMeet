/**
 * CampusMeet / EventHub — Search Registry & Page Titles
 */

window.CampusMeetData = window.CampusMeetData || {};

window.CampusMeetData.searchRegistry = [
    // Lab 5
    { id: 'lab5-overview', url: 'pages/lab5.html#lab5-overview', title: 'Лаб. №5: Проектирование прототипа и визуальный язык', category: 'Лабораторная 5', keywords: 'прототип визуальный язык стиль сетки figma адаптивность дифференциал' },
    { id: 'lab5-visual', url: 'pages/lab5.html#lab5-visual', title: 'Лаб. №5: Исследование визуального языка (N=10, 3 палитры)', category: 'Лабораторная 5', keywords: 'семантический дифференциал осгуд палитры цвета тестирование n=10 диаграмма профиль' },
    { id: 'lab5-grids', url: 'pages/lab5.html#lab5-grids', title: 'Лаб. №5: Модульные сетки (6 разрешений) и 5 устройств', category: 'Лабораторная 5', keywords: 'модульная сетка 12 колонок 1140 1440 responsive breakpoint iphone galaxy pixel ipad' },
    { id: 'lab5-prototype', url: 'pages/lab5.html#lab5-prototype', title: 'Лаб. №5: Интерактивный кликабельный прототип экосистемы', category: 'Лабораторная 5', keywords: 'прототип интерактивный qr билет чекин сканер волонтер figma каталог' },
    { id: 'lab5-styleguide', url: 'pages/lab5.html#lab5-styleguide', title: 'Лаб. №5: Руководство по стилям (UI Style Guide, WCAG AAA)', category: 'Лабораторная 5', keywords: 'style guide дизайн система типографика кнопки формы контраст wcag токены' },
    { id: 'report-lab5', url: 'pages/lab5.html#report-lab5', title: 'Отчет: Лабораторная работа №5', category: 'Отчеты', keywords: 'lab5_report отчет лаб 5 прототип сетки стиль' },

    { id: 'lab4-overview', url: 'pages/lab4.html#lab4-overview', title: 'Лаб. №4: Стили интеграции и проектирование API', category: 'Лабораторная 4', keywords: 'api openapi swagger rest mcp docker требования интеграция' },
    { id: 'lab4-requirements', url: 'pages/lab4.html#lab4-requirements', title: 'Лаб. №4: Акторы → User Stories → Use Cases', category: 'Лабораторная 4', keywords: 'требования реестр трассировка uc us' },
    { id: 'lab4-database', url: 'pages/lab4.html#lab4-database', title: 'Лаб. №4: Логическая и физическая БД, 17 таблиц', category: 'Лабораторная 4', keywords: 'postgresql sqlite er sql ddl база данных' },
    { id: 'lab4-api', url: 'pages/lab4.html#lab4-api', title: 'Лаб. №4: OpenAPI и mock-сервер', category: 'Лабораторная 4', keywords: 'маршруты rest bruno postman swagger mock http' },
    { id: 'lab4-mcp', url: 'pages/lab4.html#lab4-mcp', title: 'Лаб. №4: MCP Tools, Resources и Prompts', category: 'Лабораторная 4', keywords: 'mcp stdio json rpc tools resources prompts inspector ассистент' },
    { id: 'lab4-infrastructure', url: 'pages/lab4.html#lab4-infrastructure', title: 'Лаб. №4: Docker и CI/CD', category: 'Лабораторная 4', keywords: 'docker compose github actions sonarqube render инфраструктура' },
    { id: 'report-lab4', url: 'pages/lab4.html#report-lab4', title: 'Отчет: Лабораторная работа №4', category: 'Отчеты', keywords: 'lab4_report отчет лаб 4 api mcp' },
    // Portal / Overview
    { id: 'portal-overview', url: 'index.html#portal-overview', title: 'Главная: Проектный портал CampusMeet (ФПМИ БГУ)', category: 'Портал', keywords: 'портал главная обзор паспорт цели kpi дорожная карта репозитории бгу фпми' },

    // Lab 1
    { id: 'lab1-overview', url: 'pages/lab1.html#lab1-overview', title: 'Лаб. №1: Исследование пользователей и предметной области', category: 'Лабораторная 1', keywords: 'опрос исследование предметная область kano hcd контекст' },
    { id: 'survey-data', url: 'pages/lab1.html#survey-data', title: 'Эмпирическое исследование опроса (N=68)', category: 'Лабораторная 1', keywords: 'опрос n=68 анкета статистика кано pain points ios android' },
    { id: 'personas-gallery', url: 'pages/lab1.html#personas-gallery', title: 'Галерея 7 синтезированных персонажей', category: 'Лабораторная 1', keywords: 'персонажи артем ковалев дарья максим кирилл виктор сергей влад' },
    { id: 'as-is-processes', url: 'pages/lab1.html#as-is-processes', title: 'Диаграммы бизнес-процессов As-Is', category: 'Лабораторная 1', keywords: 'as-is процессы bpmn чекин регистрация спикеры узкие места' },
    
    // Lab 2
    { id: 'lab2-overview', url: 'pages/lab2.html#lab2-overview', title: 'Лаб. №2: Обзор информационной архитектуры', category: 'Лабораторная 2', keywords: 'информационная архитектура купер монопольный интерфейс optimalsort' },
    { id: 'lab2-ia', url: 'pages/lab2.html#lab2-ia', title: 'Информационная архитектура и Sitemap (>3 уровней)', category: 'Лабораторная 2', keywords: 'sitemap карта сайта таксономия аудит контента' },
    { id: 'lab2-nav-search', url: 'pages/lab2.html#lab2-nav-search', title: 'Системы навигации и поиска (Omnibox ⌘K)', category: 'Лабораторная 2', keywords: 'навигация карточная сортировка меню поиск omnibox fuzzy search' },
    { id: 'lab2-cjm-impact', url: 'pages/lab2.html#lab2-cjm-impact', title: 'Impact Map и Карты путей клиентов (CJM 7 персонажей)', category: 'Лабораторная 2', keywords: 'cjm impact map путь клиента артем дарья максим' },
    { id: 'lab2-storyboards', url: 'pages/lab2.html#lab2-storyboards', title: 'Интерактивные раскадровки (Storyboards) и Edge Cases', category: 'Лабораторная 2', keywords: 'раскадровки storyboards edge cases vs-01 vs-07 сбои форс-мажор' },
    { id: 'lab2-mockups', url: 'pages/lab2.html#lab2-mockups', title: 'Галерея векторных Wireframes и UI Макетов (12 экранов)', category: 'Лабораторная 2', keywords: 'вайрфреймы макеты mockups svg desktop mobile сканер билет' },
    
    // Lab 3
    { id: 'lab3-overview', url: 'pages/lab3.html#lab3-overview', title: 'Лаб. №3: Обзор и User Stories (Mike Cohn & BDD)', category: 'Лабораторная 3', keywords: 'user stories пользовательские истории bdd given when then moscow' },
    { id: 'lab3-uml', url: 'pages/lab3.html#lab3-uml', title: 'Спецификация UML (PlantUML: 29 схем)', category: 'Лабораторная 3', keywords: 'plantuml use case activity class sequence components erd' },
    { id: 'lab3-events', url: 'pages/lab3.html#lab3-events', title: 'EventStorming и Event Modeling (Adam Dymitruk)', category: 'Лабораторная 3', keywords: 'eventstorming event modeling срезы command view automation ddd' },
    { id: 'lab3-c4-srs', url: 'pages/lab3.html#lab3-c4-srs', title: 'C4 Model (C1-C4) и ТЗ (SRS по Карлу Вигерсу / IEEE 830)', category: 'Лабораторная 3', keywords: 'c4 model саймон браун srs тз вигерс ieee 830 трассируемость' },
    
    // Wiki
    { id: 'wiki-func', url: 'pages/wiki.html#wiki-func', title: 'Wiki: Функциональные требования и Use Case', category: 'База знаний', keywords: 'функциональные требования use case прецеденты' },
    { id: 'wiki-arch', url: 'pages/wiki.html#wiki-arch', title: 'Wiki: Архитектура экосистемы (4 репозитория)', category: 'База знаний', keywords: 'архитектура сервер веб мобайл fast api next js react native' },
    { id: 'wiki-db', url: 'pages/wiki.html#wiki-db', title: 'Wiki: Реляционная схема базы данных (10 таблиц)', category: 'База знаний', keywords: 'база данных sql erd postgresql sqlite schema' },
    { id: 'wiki-api', url: 'pages/wiki.html#wiki-api', title: 'Wiki: REST API, Nominatim OSM и Nager.Date', category: 'База знаний', keywords: 'rest api геокодирование openstreetmap nager date праздники' },
    { id: 'wiki-security', url: 'pages/wiki.html#wiki-security', title: 'Wiki: Безопасность и токен билета HMAC-SHA256', category: 'База знаний', keywords: 'безопасность hmac sha256 криптография токен оффлайн' },
    { id: 'wiki-presentation', url: 'pages/wiki.html#wiki-presentation', title: 'Wiki: Концептуальная презентация и матрица RACI', category: 'База знаний', keywords: 'презентация raci регламент команда git-flow' },

    // Academic Reports (Markdown Previews)
    { id: 'report-lab1', url: 'pages/lab1.html#report-lab1', title: 'Отчет: Лабораторная работа №1 (Lab1_report.md)', category: 'Отчеты', keywords: 'отчет лаб 1 markdown lab1_report md исследование hcd опрос персоны' },
    { id: 'report-lab2', url: 'pages/lab2.html#report-lab2', title: 'Отчет: Лабораторная работа №2 (Lab2_report.md)', category: 'Отчеты', keywords: 'отчет лаб 2 markdown lab2_report md инфо-архитектура cjm раскадровки макеты' },
    { id: 'report-lab3', url: 'pages/lab3.html#report-lab3', title: 'Отчет: Лабораторная работа №3 (Lab3_report.md)', category: 'Отчеты', keywords: 'отчет лаб 3 markdown lab3_report md user stories uml c4 srs тз' }
];

window.CampusMeetData.titleMap = {
    'portal-overview': 'CampusMeet / EventHub — Проектный портал ПЧМИ',
    'lab1-overview': 'Лаб. №1: Исследование пользователей — CampusMeet',
    'survey-data': 'Опрос N=68 и статистика — CampusMeet',
    'personas-gallery': 'Галерея 7 персонажей — CampusMeet',
    'as-is-processes': 'Процессы As-Is — CampusMeet',
    'lab2-overview': 'Лаб. №2: Обзор инфо-архитектуры — CampusMeet',
    'lab2-ia': 'Инфо-архитектура и Sitemap — CampusMeet',
    'lab2-nav-search': 'Системы навигации и поиска — CampusMeet',
    'lab2-cjm-impact': 'Impact Map и CJM пути — CampusMeet',
    'lab2-storyboards': 'Раскадровки и Edge Cases — CampusMeet',
    'lab2-mockups': 'Вайрфреймы и UI Макеты — CampusMeet',
    'lab3-overview': 'Лаб. №3: Обзор и User Stories — CampusMeet',
    'lab3-uml': 'Диаграммы UML (PlantUML) — CampusMeet',
    'lab3-events': 'EventStorming & Event Modeling — CampusMeet',
    'lab3-c4-srs': 'C4 Model & ТЗ (SRS) — CampusMeet',
    'lab4-overview': 'Лаб. №4: Стили интеграции и API — CampusMeet',
    'lab4-database': 'Лаб. №4: База данных (17 таблиц) — CampusMeet',
    'lab4-api': 'Лаб. №4: REST API и Mock-сервер — CampusMeet',
    'lab4-mcp': 'Лаб. №4: MCP-сервер и AI-инструменты — CampusMeet',
    'lab4-infrastructure': 'Лаб. №4: Docker и CI/CD — CampusMeet',
    'lab5-overview': 'Лаб. №5: Проектирование прототипа — CampusMeet',
    'lab5-visual': 'Лаб. №5: Исследование визуального языка — CampusMeet',
    'lab5-grids': 'Лаб. №5: Модульные сетки и адаптивность — CampusMeet',
    'lab5-prototype': 'Лаб. №5: Интерактивный прототип — CampusMeet',
    'lab5-styleguide': 'Лаб. №5: Руководство по стилям — CampusMeet',
    'wiki-func': 'Wiki: Функциональные требования — CampusMeet',
    'wiki-arch': 'Wiki: Архитектура Web/Mobile — CampusMeet',
    'wiki-db': 'Wiki: Схема базы данных — CampusMeet',
    'wiki-api': 'Wiki: REST API и внешние сервисы — CampusMeet',
    'wiki-security': 'Wiki: HMAC-SHA256 безопасность — CampusMeet',
    'wiki-presentation': 'Wiki: Презентация и RACI регламент — CampusMeet'
};
