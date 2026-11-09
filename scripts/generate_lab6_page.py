# -*- coding: utf-8 -*-
"""Generate rich interactive HTML page for Lab 6 adhering 100% to CampusMeet design system."""
from pathlib import Path

OUT_FILE = Path("/Users/victoriaivanova/university/7_sem/pchmi/project/CampusMeet/docs/pages/lab6.html")

content = """<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CampusMeet / EventHub — Лабораторная работа №6: Тестирование и оценка качества интерфейса</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700&family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;1,6..72,400&display=swap" rel="stylesheet">
    <link rel="icon" type="image/svg+xml" href="../assets/favicon.svg">
    <link rel="stylesheet" href="../css/style.css">
    <script>
        (function() {
            var t = null;
            try { t = localStorage.getItem('cm_theme'); } catch(e) {}
            if (!t) {
                t = window.matchMedia && window.matchMedia('(prefers-color-scheme: light)').matches ? 'light' : 'dark';
            }
            document.documentElement.setAttribute('data-theme', t);
        })();
    </script>
    <style>
        /* Custom Lab 6 Interactive Styles (harmonized with style.css) */
        .interactive-widget {
            background: var(--surface-primary);
            border: 1px solid var(--border-subtle);
            border-radius: var(--radius-md);
            padding: 24px;
            margin: 20px 0;
            box-shadow: 0 4px 20px rgba(0,0,0,0.03);
        }
        .goms-selector-bar {
            display: flex;
            gap: 12px;
            flex-wrap: wrap;
            margin-bottom: 20px;
            background: var(--surface-secondary);
            padding: 16px;
            border-radius: var(--radius-md);
            border: 1px solid var(--border-subtle);
        }
        .goms-select-group {
            display: flex;
            flex-direction: column;
            gap: 6px;
            flex: 1;
            min-width: 200px;
        }
        .goms-select-group label {
            font-size: 0.75rem;
            font-weight: 700;
            color: var(--text-secondary);
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }
        .goms-select-group select {
            padding: 8px 12px;
            border-radius: var(--radius-sm);
            border: 1px solid var(--border-default);
            background: var(--surface-primary);
            color: var(--text-primary);
            font-size: 0.85rem;
            font-family: inherit;
            cursor: pointer;
        }
        .metric-pill-row {
            display: flex;
            gap: 12px;
            margin-bottom: 20px;
            flex-wrap: wrap;
        }
        .metric-pill {
            padding: 12px 18px;
            border-radius: var(--radius-md);
            background: var(--surface-secondary);
            border: 1px solid var(--border-subtle);
            display: flex;
            flex-direction: column;
            min-width: 120px;
        }
        .metric-pill-val {
            font-size: 1.45rem;
            font-weight: 700;
            font-family: var(--font-mono);
            color: var(--text-primary);
        }
        .metric-pill-lbl {
            font-size: 0.72rem;
            color: var(--text-secondary);
            text-transform: uppercase;
            font-weight: 600;
            letter-spacing: 0.04em;
        }
        .goms-step-table {
            width: 100%;
            border-collapse: collapse;
            font-size: 0.85rem;
            margin-top: 12px;
        }
        .goms-step-table th, .goms-step-table td {
            padding: 10px 14px;
            border-bottom: 1px solid var(--border-subtle);
            text-align: left;
        }
        .goms-step-table th {
            background: var(--surface-secondary);
            color: var(--text-secondary);
            font-weight: 700;
        }
        .op-badge {
            display: inline-block;
            padding: 2px 7px;
            border-radius: var(--radius-xs);
            font-family: var(--font-mono);
            font-size: 0.75rem;
            font-weight: 700;
            margin-right: 4px;
        }
        .op-K { background: #e0f2fe; color: #0369a1; }
        .op-P { background: #fef3c7; color: #b45309; }
        .op-H { background: #f3e8ff; color: #7e22ce; }
        .op-M { background: #fee2e2; color: #b91c1c; }
        .op-T { background: #dcfce7; color: #15803d; }
        .op-R { background: #e2e8f0; color: #334155; }
        .op-D { background: #ffedd5; color: #c2410c; }
        .op-F { background: #ccfbf1; color: #0f766e; }

        /* SUS Calculator Styles */
        .sus-question-card {
            background: var(--surface-secondary);
            border: 1px solid var(--border-subtle);
            border-radius: var(--radius-md);
            padding: 14px 18px;
            margin-bottom: 12px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 16px;
            flex-wrap: wrap;
        }
        .sus-q-text {
            flex: 1;
            font-size: 0.9rem;
            color: var(--text-primary);
            font-weight: 500;
            min-width: 260px;
        }
        .sus-scale-group {
            display: flex;
            gap: 8px;
            align-items: center;
        }
        .sus-scale-btn {
            width: 32px;
            height: 32px;
            border-radius: var(--radius-full);
            border: 1px solid var(--border-default);
            background: var(--surface-primary);
            color: var(--text-secondary);
            font-weight: 700;
            font-size: 0.85rem;
            cursor: pointer;
            transition: all var(--duration-hover) var(--ease-snappy);
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .sus-scale-btn:hover {
            border-color: var(--action-primary-bg);
            color: var(--action-primary-bg);
        }
        .sus-scale-btn.active {
            background: var(--action-primary-bg);
            color: #ffffff;
            border-color: var(--action-primary-bg);
        }

        /* Checklists Table Styles */
        .checklist-item-row {
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 14px 18px;
            border-bottom: 1px solid var(--border-subtle);
            gap: 16px;
        }
        .checklist-item-row:hover {
            background: var(--surface-hover);
        }
        .status-badge {
            display: inline-flex;
            align-items: center;
            gap: 4px;
            padding: 3px 10px;
            border-radius: var(--radius-full);
            font-size: 0.75rem;
            font-weight: 700;
            font-family: var(--font-mono);
        }
        .status-pass { background: #dcfce7; color: #166534; }
        .status-warn { background: #fef3c7; color: #92400e; }

        .preview-frame-container {
            width: 100%;
            overflow-x: auto;
            border: 1px solid var(--border-subtle);
            border-radius: var(--radius-md);
            background: var(--surface-canvas);
            padding: 16px;
            text-align: center;
        }
        .preview-frame-container img {
            max-width: 100%;
            height: auto;
            border-radius: var(--radius-sm);
        }
        .interactive-tab-btn {
            background: var(--surface-secondary);
            border: 1px solid var(--border-subtle);
            color: var(--text-secondary);
            padding: 8px 16px;
            border-radius: var(--radius-md);
            font-size: 0.85rem;
            font-weight: 600;
            cursor: pointer;
            transition: all var(--duration-hover) var(--ease-snappy);
        }
        .interactive-tab-btn:hover {
            background: var(--surface-hover);
            color: var(--text-primary);
        }
        .interactive-tab-btn.active {
            background: var(--action-primary-bg);
            color: #ffffff;
            border-color: var(--action-primary-bg);
        }
    </style>
</head>
<body data-page="lab6">

    <!-- Mobile Topbar -->
    <header class="mobile-topbar">
        <a href="../index.html" class="mobile-brand">
            <img src="../assets/favicon.svg" alt="CampusMeet Logo">
            <span>CampusMeet</span>
        </a>
        <div style="display: flex; align-items: center; gap: 8px;">
            <button class="theme-toggle-btn" type="button" aria-label="Переключить тему оформления" title="Светлая / Темная тема">
                <svg class="icon-sun" viewBox="0 0 24 24"><circle cx="12" cy="12" r="5"></circle><line x1="12" y1="1" x2="12" y2="3"></line><line x1="12" y1="21" x2="12" y2="23"></line><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line><line x1="1" y1="12" x2="3" y2="12"></line><line x1="21" y1="12" x2="23" y2="12"></line><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line></svg>
                <svg class="icon-moon" viewBox="0 0 24 24"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path></svg>
            </button>
            <button id="mobile-hamburger" class="hamburger-btn" type="button" aria-label="Открыть навигацию">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <line x1="3" y1="12" x2="21" y2="12"></line>
                    <line x1="3" y1="6" x2="21" y2="6"></line>
                    <line x1="3" y1="18" x2="21" y2="18"></line>
                </svg>
            </button>
        </div>
    </header>

    <div id="sidebar-backdrop" class="sidebar-backdrop"></div>

    <!-- Sidebar Navigation (Strictly adhering to layout.css) -->
    <aside id="sidebar">
        <div class="sidebar-header">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
                <span class="brand-badge" style="margin-bottom: 0;">ПЧМИ • ФПМИ БГУ</span>
                <button class="theme-toggle-btn" type="button" aria-label="Переключить тему оформления" title="Светлая / Темная тема">
                    <svg class="icon-sun" viewBox="0 0 24 24"><circle cx="12" cy="12" r="5"></circle><line x1="12" y1="1" x2="12" y2="3"></line><line x1="12" y1="21" x2="12" y2="23"></line><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line><line x1="1" y1="12" x2="3" y2="12"></line><line x1="21" y1="12" x2="23" y2="12"></line><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line></svg>
                    <svg class="icon-moon" viewBox="0 0 24 24"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path></svg>
                </button>
            </div>
            <h1>CampusMeet</h1>
            <p>Платформа студенческих митапов, хакатонов и офлайн-чекина</p>
            <button class="omnibox-trigger-btn" type="button" aria-label="Быстрый поиск">
                <span class="omnibox-trigger-label">
                    <svg class="icon" viewBox="0 0 24 24"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
                    Поиск по порталу...
                </span>
                <span class="kbd-shortcut">⌘K</span>
            </button>
        </div>

        <div class="nav-section-title">Разделы портала</div>
        <ul class="nav-menu">
            <li class="nav-item">
                <a href="../index.html" class="nav-link">
                    <svg class="icon icon-nav" viewBox="0 0 24 24"><path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path><polyline points="9 22 9 12 15 12 15 22"></polyline></svg>
                    <span>Главный портал</span>
                    <span class="nav-badge">Hub</span>
                </a>
            </li>
            <li class="nav-item">
                <a href="lab1.html" class="nav-link">
                    <svg class="icon icon-nav" viewBox="0 0 24 24"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg>
                    <span>Лабораторная №1</span>
                    <span class="nav-badge">L1</span>
                </a>
            </li>
            <li class="nav-item">
                <a href="lab2.html" class="nav-link">
                    <svg class="icon icon-nav" viewBox="0 0 24 24"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><line x1="3" y1="9" x2="21" y2="9"></line><line x1="9" y1="21" x2="9" y2="9"></line></svg>
                    <span>Лабораторная №2</span>
                    <span class="nav-badge">L2</span>
                </a>
            </li>
            <li class="nav-item">
                <a href="lab3.html" class="nav-link">
                    <svg class="icon icon-nav" viewBox="0 0 24 24"><polygon points="12 2 2 7 12 12 22 7 12 2"></polygon><polyline points="2 17 12 22 22 17"></polyline><polyline points="2 12 12 17 22 12"></polyline></svg>
                    <span>Лабораторная №3</span>
                    <span class="nav-badge">L3</span>
                </a>
            </li>
            <li class="nav-item">
                <a href="lab4.html" class="nav-link">
                    <svg class="icon icon-nav" viewBox="0 0 24 24"><polyline points="16 18 22 12 16 6"></polyline><polyline points="8 6 2 12 8 18"></polyline></svg>
                    <span>Лабораторная №4</span>
                    <span class="nav-badge">L4</span>
                </a>
            </li>
            <li class="nav-item">
                <a href="lab5.html" class="nav-link">
                    <svg class="icon icon-nav" viewBox="0 0 24 24"><rect x="5" y="2" width="14" height="20" rx="2" ry="2"></rect><line x1="12" y1="18" x2="12.01" y2="18"></line></svg>
                    <span>Лабораторная №5</span>
                    <span class="nav-badge">L5</span>
                </a>
            </li>
            <li class="nav-item">
                <a href="lab6.html" class="nav-link active current-page">
                    <svg class="icon icon-nav" viewBox="0 0 24 24"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>
                    <span>Лабораторная №6</span>
                    <span class="nav-badge" style="background: var(--action-primary-bg); color: #fff;">L6</span>
                </a>
            </li>
            <li class="nav-item">
                <a href="wiki.html" class="nav-link">
                    <svg class="icon icon-nav" viewBox="0 0 24 24"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path></svg>
                    <span>База знаний (Wiki)</span>
                    <span class="nav-badge">Docs</span>
                </a>
            </li>
        </ul>

        <div class="nav-section-title">Содержание работы</div>
        <ul class="nav-menu">
            <li class="nav-item">
                <a href="#lab6-overview" class="nav-link active" onclick="switchTab('lab6-overview', this)">
                    <span class="nav-num">01</span>
                    <span>Паспорт и цели</span>
                </a>
            </li>
            <li class="nav-item">
                <a href="#lab6-performance" class="nav-link" onclick="switchTab('lab6-performance', this)">
                    <span class="nav-num">02</span>
                    <span>Метрики и Scorecard</span>
                </a>
            </li>
            <li class="nav-item">
                <a href="#lab6-treejack" class="nav-link" onclick="switchTab('lab6-treejack', this)">
                    <span class="nav-num">03</span>
                    <span>Treejack &amp; Карточки</span>
                </a>
            </li>
            <li class="nav-item">
                <a href="#lab6-expectations" class="nav-link" onclick="switchTab('lab6-expectations', this)">
                    <span class="nav-num">04</span>
                    <span>Ожидания &amp; Чек-листы</span>
                </a>
            </li>
            <li class="nav-item">
                <a href="#lab6-goms-tlm" class="nav-link" onclick="switchTab('lab6-goms-tlm', this)">
                    <span class="nav-num">05</span>
                    <span>GOMS &amp; TLM модели</span>
                </a>
            </li>
            <li class="nav-item">
                <a href="#lab6-sus" class="nav-link" onclick="switchTab('lab6-sus', this)">
                    <span class="nav-num">06</span>
                    <span>Анкетирование SUS</span>
                </a>
            </li>
            <li class="nav-item">
                <a href="#lab6-report-view" class="nav-link" onclick="switchTab('lab6-report-view', this)">
                    <span class="nav-num">07</span>
                    <span>Академический отчет (MD)</span>
                </a>
            </li>
        </ul>
    </aside>

    <!-- Main Content Area (#content matches layout.css) -->
    <main id="content">
        <div class="content-container">

            <!-- Breadcrumbs Navigation -->
            <nav class="content-breadcrumbs" aria-label="Хлебные крошки">
                <ol class="breadcrumbs-list">
                    <li class="breadcrumb-item"><a href="../index.html">Главная</a></li>
                    <li class="breadcrumb-separator">/</li>
                    <li class="breadcrumb-item"><a href="lab6.html">Лабораторная работа №6</a></li>
                    <li class="breadcrumb-separator">/</li>
                    <li class="breadcrumb-item breadcrumb-active" id="active-breadcrumb-tab">Паспорт и цели</li>
                </ol>
            </nav>

            <!-- TAB 1: Overview -->
            <section id="lab6-overview" class="tab-pane active">
                <div class="section-header">
                    <h2>Лабораторная работа №6: Тестирование и оценка качества интерфейса</h2>
                    <p>Эмпирическое юзабилити-тестирование (N=10), расчет 12 моделей GOMS для веб-форм, 3 сенсорные модели TLM, верификация структуры меню в Treejack, тестирование ожиданий и стандартизированное анкетирование SUS</p>
                </div>

                <!-- Stats KPI Grid (Strictly .stats-grid & .stat-card) -->
                <div class="stats-grid">
                    <div class="stat-card">
                        <div class="stat-value" style="color: #10b981;">97.5%</div>
                        <div class="stat-label">Task Success Rate (39 из 40 тестов)</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-value" style="color: #2563eb;">85.75</div>
                        <div class="stat-label">System Usability Scale (SUS, Grade A+)</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-value" style="color: #8b5cf6;">90.7%</div>
                        <div class="stat-label">Интегральный SUM индекс Сауро</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-value" style="color: #06b6d4;">14.10 с</div>
                        <div class="stat-label">Оптимум GOMS (Ускорение в 2.3..7.8 раза)</div>
                    </div>
                </div>

                <div class="profile-card" style="margin-top: 24px;">
                    <h3>Паспорт Лабораторной работы №6</h3>
                    <p style="color: var(--text-muted); font-size: 0.9rem; margin-bottom: 16px;">
                        Лабораторная работа №6 завершает цикл концептуального проектирования экосистемы CampusMeet. В рамках работы проведена всесторонняя оценка качества интерфейсов методами быстрой оценки концепций (обратная карточная сортировка, Treejack, тестирование ожиданий, чек-листы) и формальными моторно-когнитивными моделями <strong>GOMS (12 расчетов)</strong> и <strong>TLM (3 экрана)</strong>. На выборке $N=10$ респондентов подтверждены высочайшие показатели результативности (97.5%) и удовлетворенности (SUS 85.8 баллов, 96-й перцентиль).
                    </p>
                    <div style="display: flex; gap: 12px; flex-wrap: wrap;">
                        <button class="btn btn-primary" onclick="switchTab('lab6-report-view')">
                            <svg class="icon" viewBox="0 0 24 24"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line></svg>
                            Читать академический отчет Lab6_report.md
                        </button>
                        <button class="btn btn-secondary" onclick="switchTab('lab6-goms-tlm')">
                            <svg class="icon" viewBox="0 0 24 24"><rect x="2" y="3" width="20" height="14" rx="2" ry="2"></rect><line x1="8" y1="21" x2="16" y2="21"></line><line x1="12" y1="17" x2="12" y2="21"></line></svg>
                            Калькулятор GOMS &amp; TLM
                        </button>
                        <button class="btn btn-secondary" onclick="switchTab('lab6-sus')">
                            <svg class="icon" viewBox="0 0 24 24"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>
                            Интерактивная анкета SUS
                        </button>
                        <button class="btn btn-secondary" onclick="switchTab('lab6-expectations')">
                            <svg class="icon" viewBox="0 0 24 24"><polyline points="9 11 12 14 22 4"></polyline><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"></path></svg>
                            Экспертные чек-листы
                        </button>
                    </div>
                </div>

                <div class="card" style="margin-top: 24px;">
                    <div class="card-header">
                        <h4>Ключевые результаты и этапы тестирования</h4>
                    </div>
                    <div class="card-body">
                        <ul style="line-height: 1.8; color: var(--text-secondary); font-size: 0.9rem;">
                            <li><strong>Этап 1 (Пользовательские сессии):</strong> 4 сквозных сценария на выборке $N=10$, расчет 95% интервалов Вильсона, замер Time-on-Task против эталона, Single Usability Metric (SUM = 90.7%).</li>
                            <li><strong>Этап 2 (Инфо-архитектура):</strong> Оффлайн карточная сортировка (91.4% попаданий) и онлайн-тест Sitemap в Treejack (95.0% успешность, 88.8% Directness).</li>
                            <li><strong>Этап 3 (Тестирование ожиданий):</strong> Опрос ожиданий до клика, устранение обманутых ожиданий в терминах CFP и пиктограмме HMAC-щита.</li>
                            <li><strong>Этап 4 (Чек-листы):</strong> Экспертная проверка Web (98.0%, 10 пунктов WCAG 2.1 AA / Nielsen) и Mobile (97.5%, 8 пунктов Apple HIG / Material).</li>
                            <li><strong>Этап 5 (GOMS &amp; TLM):</strong> Расчет 12 моделей GOMS для 3 веб-форм (доказано сокращение времени в 2.3–7.8 раза при Tab-навигации) и 3 моделей TLM для мобильного приложения (3.85–6.10 с).</li>
                            <li><strong>Этап 6 (Анкетирование SUS):</strong> 10 стандартизированных вопросов, средний балл 85.75, высшая категория Grade A+ (Best Imaginable).</li>
                        </ul>
                    </div>
                </div>
            </section>

            <!-- TAB 2: Performance Metrics & Usability Scorecard -->
            <section id="lab6-performance" class="tab-pane">
                <div class="section-header">
                    <h2>Метрики производительности и Usability Scorecard</h2>
                    <p>Эмпирические замеры результативности (Task Success Rate, 95% ДИ Вильсона), эффективности (Time-on-Task vs эталон) и интегрального индекса SUM ($N=10$)</p>
                </div>

                <div class="table-responsive" style="margin-bottom: 24px;">
                    <table class="data-table">
                        <thead>
                            <tr>
                                <th>ID</th>
                                <th>Сценарий и контекст роли</th>
                                <th>Успех (%)</th>
                                <th>95% ДИ Вильсона</th>
                                <th>Время ($M \pm SD$)</th>
                                <th>Эталон</th>
                                <th>SUM</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td><strong>S1</strong></td>
                                <td>Регистрация студента и получение крипто-билета (Артём)</td>
                                <td><span class="status-badge status-pass">100.0%</span></td>
                                <td><code>[72.2% .. 100%]</code></td>
                                <td>$26.8 \pm 3.7$ с</td>
                                <td>20.0 с</td>
                                <td><strong>92.4%</strong></td>
                            </tr>
                            <tr>
                                <td><strong>S2</strong></td>
                                <td>Создание митапа и настройка CFP организатором (Дарья)</td>
                                <td><span class="status-badge status-pass">90.0%</span></td>
                                <td><code>[59.6% .. 98.2%]</code></td>
                                <td>$54.7 \pm 7.4$ с</td>
                                <td>40.0 с</td>
                                <td><strong>84.1%</strong></td>
                            </tr>
                            <tr>
                                <td><strong>S3</strong></td>
                                <td>Поиск в каталоге через Omnibox ⌘K и фильтрация (Максим)</td>
                                <td><span class="status-badge status-pass">100.0%</span></td>
                                <td><code>[72.2% .. 100%]</code></td>
                                <td>$15.9 \pm 2.8$ с</td>
                                <td>11.0 с</td>
                                <td><strong>94.8%</strong></td>
                            </tr>
                            <tr>
                                <td><strong>S4</strong></td>
                                <td>Офлайн-контроль и сканирование билетов на входе (Виктор)</td>
                                <td><span class="status-badge status-pass">100.0%</span></td>
                                <td><code>[72.2% .. 100%]</code></td>
                                <td>$17.7 \pm 3.1$ с</td>
                                <td>12.0 с</td>
                                <td><strong>91.6%</strong></td>
                            </tr>
                        </tbody>
                    </table>
                </div>

                <div class="interactive-widget">
                    <h3 style="margin-bottom: 8px;">Сводная лепестковая диаграмма качества (Usability Scorecard)</h3>
                    <p style="color: var(--text-muted); font-size: 0.85rem; margin-bottom: 16px;">
                        Сопоставление фактически измеренных показателей прототипа CampusMeet с нормативными требованиями и отраслевыми эталонами:
                    </p>
                    <div class="preview-frame-container">
                        <img src="../assets/lab6/usability_scorecard_radar.svg" alt="Лепестковая диаграмма юзабилити">
                    </div>
                </div>
            </section>

            <!-- TAB 3: Treejack & Card Sorting -->
            <section id="lab6-treejack" class="tab-pane">
                <div class="section-header">
                    <h2>Обратная карточная сортировка и Treejack IA</h2>
                    <p>Тестирование трехуровневой структуры информационной архитектуры (Sitemap из ЛР2): процент попаданий, показатель прямолинейности Directness и навигационные пути</p>
                </div>

                <div class="interactive-widget">
                    <h3 style="margin-bottom: 8px;">Навигационные пути и коэффициент прямолинейности (Treejack Paths)</h3>
                    <p style="color: var(--text-muted); font-size: 0.85rem; margin-bottom: 16px;">
                        Средний показатель успешности поиска ключевых разделов составил <strong>95.0%</strong>, а коэффициент прямолинейности путей (Directness) — <strong>88.8%</strong> (респонденты достигали цели напрямую без блуждания):
                    </p>
                    <div class="preview-frame-container">
                        <img src="../assets/lab6/treejack_paths_ia.svg" alt="Treejack IA Paths">
                    </div>
                </div>
            </section>

            <!-- TAB 4: Expectations & Checklists -->
            <section id="lab6-expectations" class="tab-pane">
                <div class="section-header">
                    <h2>Тестирование ожиданий и экспертные чек-листы</h2>
                    <p>Психологический тест ожиданий пользователей до взаимодействия и инспекция интерфейсов по стандартам WCAG 2.1 AA, Nielsen Heuristics, Apple HIG и Google Material Design</p>
                </div>

                <div class="interactive-widget">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px; flex-wrap: wrap; gap: 10px;">
                        <div>
                            <h3 style="margin: 0;">Интерактивный инспектор чек-листов</h3>
                            <span style="font-size: 0.8rem; color: var(--text-muted);">Переключайте между платформами для просмотра подробных оценок и замечаний:</span>
                        </div>
                        <div style="display: flex; gap: 8px;">
                            <button id="cl-btn-web" class="interactive-tab-btn active" onclick="switchChecklist('web')">Web (10 критериев — 98.0%)</button>
                            <button id="cl-btn-mob" class="interactive-tab-btn" onclick="switchChecklist('mobile')">Mobile (8 критериев — 97.5%)</button>
                        </div>
                    </div>

                    <div id="checklist-items-container">
                        <!-- Populated by JS -->
                    </div>
                </div>
            </section>

            <!-- TAB 5: GOMS & TLM Modeling -->
            <section id="lab6-goms-tlm" class="tab-pane">
                <div class="section-header">
                    <h2>Количественный хронометраж по моделям GOMS (12 расчетов) и TLM</h2>
                    <p>Моделирование взаимодействия по константам Карда–Морана–Ньюэлла (K=0.2с, P=1.1с, H=0.4с, M=1.35с) с правилами 0–4 расстановки ментальных пауз и сенсорная модель TLM</p>
                </div>

                <div class="interactive-widget">
                    <h3 style="margin-bottom: 8px;">Интерактивный симулятор-калькулятор GOMS</h3>
                    <p style="color: var(--text-muted); font-size: 0.85rem; margin-bottom: 16px;">
                        Выберите форму, вариант компоновки и метод ввода данных для просмотра точной пошаговой цепочки операторов и выигрыша во времени:
                    </p>

                    <div class="goms-selector-bar">
                        <div class="goms-select-group">
                            <label for="goms-form-select">Экранная форма</label>
                            <select id="goms-form-select" onchange="updateGomsView()">
                                <option value="form1">Форма 1: Создание митапа / CFP</option>
                                <option value="form2" selected>Форма 2: Регистрация участника</option>
                                <option value="form3">Форма 3: Поиск и фильтрация каталога</option>
                            </select>
                        </div>
                        <div class="goms-select-group">
                            <label for="goms-variant-select">Вариант компоновки</label>
                            <select id="goms-variant-select" onchange="updateGomsView()">
                                <option value="A">Вариант А: Традиционная форма</option>
                                <option value="B" selected>Вариант Б: Оптимизированная форма</option>
                            </select>
                        </div>
                        <div class="goms-select-group">
                            <label for="goms-method-select">Метод ввода данных</label>
                            <select id="goms-method-select" onchange="updateGomsView()">
                                <option value="mouse">Только мышь (наведение и клики)</option>
                                <option value="keyboard_tab" selected>Клавиатура (Tab-навигация / Хоткеи)</option>
                            </select>
                        </div>
                    </div>

                    <div class="metric-pill-row">
                        <div class="metric-pill">
                            <div id="goms-total-time" class="metric-pill-val" style="color: #10b981;">4.85 с</div>
                            <div class="metric-pill-lbl">Расчетное время</div>
                        </div>
                        <div class="metric-pill">
                            <div id="goms-k-count" class="metric-pill-val">4</div>
                            <div class="metric-pill-lbl">Клавиши (K = 0.2с)</div>
                        </div>
                        <div class="metric-pill">
                            <div id="goms-p-count" class="metric-pill-val">0</div>
                            <div class="metric-pill-lbl">Мышь (P = 1.1с)</div>
                        </div>
                        <div class="metric-pill">
                            <div id="goms-h-count" class="metric-pill-val">0</div>
                            <div class="metric-pill-lbl">Homing (H = 0.4с)</div>
                        </div>
                        <div class="metric-pill">
                            <div id="goms-m-count" class="metric-pill-val">3</div>
                            <div class="metric-pill-lbl">Ментальные (M = 1.35с)</div>
                        </div>
                    </div>

                    <div class="table-responsive">
                        <table class="goms-step-table">
                            <thead>
                                <tr>
                                    <th style="width: 40px;">#</th>
                                    <th>Действие пользователя</th>
                                    <th style="width: 140px;">Операторы</th>
                                    <th>Обоснование правила элиминации M</th>
                                </tr>
                            </thead>
                            <tbody id="goms-steps-body">
                                <!-- Populated dynamically -->
                            </tbody>
                        </table>
                    </div>
                </div>

                <div class="interactive-widget">
                    <h3 style="margin-bottom: 8px;">Сравнение хронометража: 12 моделей GOMS и 3 модели TLM</h3>
                    <p style="color: var(--text-muted); font-size: 0.85rem; margin-bottom: 16px;">
                        Наглядное сопоставление времени выполнения операций при переходе от классических вертикальных форм к оптимизированным чип-интерфейсам с BSU SSO:
                    </p>
                    <div class="preview-frame-container">
                        <img src="../assets/lab6/goms_tlm_comparison.svg" alt="GOMS vs TLM Bar Chart">
                    </div>
                </div>
            </section>

            <!-- TAB 6: SUS Survey -->
            <section id="lab6-sus" class="tab-pane">
                <div class="section-header">
                    <h2>Оценка удовлетворенности (System Usability Scale)</h2>
                    <p>Стандартизированная методика Джона Брука (10 вопросов, шкала Ликерта 1..5, нормализация 0..100) и классификация по Бангу–Кортуму</p>
                </div>

                <div class="interactive-widget">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px; flex-wrap: wrap; gap: 12px;">
                        <div>
                            <h3 style="margin: 0;">Интерактивный опросник и калькулятор SUS</h3>
                            <span style="font-size: 0.8rem; color: var(--text-muted);">Кликайте по шкале ответов (1..5) для мгновенного пересчета интегрального балла и грейда:</span>
                        </div>
                        <div style="display: flex; align-items: center; gap: 12px; background: var(--surface-secondary); padding: 8px 16px; border-radius: var(--radius-md); border: 1px solid var(--border-subtle);">
                            <span style="font-size: 0.85rem; font-weight: 600;">Итоговый балл:</span>
                            <span id="live-sus-score" style="font-size: 1.6rem; font-weight: 800; font-family: var(--font-mono); color: #10b981;">85.0</span>
                            <span id="live-sus-grade" class="status-badge status-pass" style="font-size: 0.8rem;">Grade A+ (Excellent)</span>
                        </div>
                    </div>

                    <div id="sus-questions-list">
                        <!-- Populated by JS -->
                    </div>
                </div>

                <div class="interactive-widget">
                    <h3 style="margin-bottom: 8px;">Распределение оценок респондентов по шкале Банга–Кортума</h3>
                    <p style="color: var(--text-muted); font-size: 0.85rem; margin-bottom: 16px;">
                        Все 10 оценок респондентов ($M = 85.75$) превышают средний мировой отраслевой бенчмарк ($68.0$), входя в 4% лучших систем мира:
                    </p>
                    <div class="preview-frame-container">
                        <img src="../assets/lab6/sus_distribution_chart.svg" alt="SUS Distribution Chart">
                    </div>
                </div>
            </section>

            <!-- TAB 7: Full Academic Report View -->
            <section id="lab6-report-view" class="tab-pane">
                <div class="section-header">
                    <h2>Академический отчёт по лабораторной работе №6</h2>
                    <p>Полный текст технического отчёта со всеми расчётами, таблицами доверительных интервалов и списком литературы</p>
                </div>

                <div id="markdown-report-container" class="markdown-body" style="background: var(--surface-primary); border: 1px solid var(--border-subtle); border-radius: var(--radius-md); padding: 32px;">
                    <div style="text-align: center; color: var(--text-muted); padding: 40px;">
                        Загрузка академического отчета...
                    </div>
                </div>
            </section>

        </div>
    </main>

    <!-- Scripts (Strictly following modular portal architecture) -->
    <script src="../js/vendor/marked.min.js"></script>
    <script src="../js/data/navigation.js"></script>
    <script src="../js/data/search.js"></script>
    <script src="../js/data/reports.js"></script>
    <script src="../js/data/lab6.js"></script>
    <script src="../js/modules/renderers.js"></script>
    <script src="../js/modules/router.js"></script>
    <script src="../js/data/diagram-pages.js"></script>
    <script src="../js/modules/diagram-gestures.js"></script>
    <script src="../js/modules/lightbox.js"></script>
    <script src="../js/modules/omnibox.js"></script>
    <script src="../js/modules/report-viewer.js"></script>
    <script src="../js/modules/ui.js"></script>
    <script src="../js/main.js"></script>

    <!-- Interactive Logic for Lab 6 -->
    <script>
        let gomsData = [];
        let checklistData = {};
        let susQuestions = [];
        let susResponses = [5, 2, 5, 1, 4, 1, 5, 2, 5, 1]; // Default realistic responses

        // Load JSON Data
        function loadLab6Data() {
            if (window.CampusMeetLab6Data) {
                gomsData = window.CampusMeetLab6Data.gomsData || [];
                checklistData = window.CampusMeetLab6Data.checklistData || {};
                susQuestions = (window.CampusMeetLab6Data.usabilityMetrics && window.CampusMeetLab6Data.usabilityMetrics.susQuestions) || [];
                initChecklists();
                initSusSurvey();
                updateGomsView();
                return;
            }
        }

        // Checklists Renderer
        function switchChecklist(type) {
            document.getElementById('cl-btn-web').classList.toggle('active', type === 'web');
            document.getElementById('cl-btn-mob').classList.toggle('active', type === 'mobile');
            
            const container = document.getElementById('checklist-items-container');
            const items = checklistData[type] || [];
            
            container.innerHTML = items.map(item => `
                <div class="checklist-item-row">
                    <div style="flex: 1;">
                        <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 4px;">
                            <span style="font-family: var(--font-mono); font-size: 0.75rem; font-weight: 700; color: #2563eb;">${item.id}</span>
                            <span style="font-size: 0.72rem; text-transform: uppercase; color: var(--text-tertiary); font-weight: 600;">${item.category}</span>
                        </div>
                        <div style="font-size: 0.9rem; font-weight: 600; color: var(--text-primary); margin-bottom: 2px;">${item.item}</div>
                        <div style="font-size: 0.8rem; color: var(--text-secondary);">${item.notes}</div>
                    </div>
                    <div style="display: flex; align-items: center; gap: 12px;">
                        <span class="status-badge status-pass">Pass (${item.score}/${item.max})</span>
                    </div>
                </div>
            `).join('');
        }

        function initChecklists() {
            switchChecklist('web');
        }

        // GOMS Calculator & Inspector
        function updateGomsView() {
            if (!gomsData || gomsData.length === 0) return;
            const formId = document.getElementById('goms-form-select').value;
            const variant = document.getElementById('goms-variant-select').value;
            const method = document.getElementById('goms-method-select').value;

            const targetId = `${formId}_var${variant}_${method === 'keyboard_tab' ? 'tab' : 'mouse'}`;
            const model = gomsData.find(m => m.id === targetId) || gomsData[0];

            document.getElementById('goms-total-time').textContent = `${model.totalSeconds.toFixed(2)} с`;
            document.getElementById('goms-k-count').textContent = model.counts.K || 0;
            document.getElementById('goms-p-count').textContent = model.counts.P || 0;
            document.getElementById('goms-h-count').textContent = model.counts.H || 0;
            document.getElementById('goms-m-count').textContent = model.counts.M || 0;

            const tbody = document.getElementById('goms-steps-body');
            tbody.innerHTML = model.steps.map((s, idx) => `
                <tr>
                    <td style="color: var(--text-tertiary); font-family: var(--font-mono);">${idx + 1}</td>
                    <td style="font-weight: 500; color: var(--text-primary);">${s.action}</td>
                    <td>${s.ops.map(op => `<span class="op-badge op-${op}">${op}</span>`).join('')}</td>
                    <td style="color: var(--text-secondary); font-size: 0.8rem;">${s.desc}</td>
                </tr>
            `).join('');
        }

        // SUS Calculator Logic
        function initSusSurvey() {
            const container = document.getElementById('sus-questions-list');
            if (!susQuestions || susQuestions.length === 0) return;

            container.innerHTML = susQuestions.map((q, qIdx) => `
                <div class="sus-question-card">
                    <div class="sus-q-text">
                        <strong>Q${q.num}.</strong> ${q.text}
                    </div>
                    <div class="sus-scale-group">
                        <span style="font-size: 0.75rem; color: var(--text-tertiary); margin-right: 4px;">Не согласен</span>
                        ${[1, 2, 3, 4, 5].map(val => `
                            <button class="sus-scale-btn ${susResponses[qIdx] === val ? 'active' : ''}" 
                                onclick="setSusResponse(${qIdx}, ${val})">${val}</button>
                        `).join('')}
                        <span style="font-size: 0.75rem; color: var(--text-tertiary); margin-left: 4px;">Согласен</span>
                    </div>
                </div>
            `).join('');

            recalcSus();
        }

        function setSusResponse(qIdx, val) {
            susResponses[qIdx] = val;
            initSusSurvey();
        }

        function recalcSus() {
            let total = 0;
            for (let i = 0; i < 10; i++) {
                const resp = susResponses[i];
                if ((i + 1) % 2 === 1) {
                    total += (resp - 1);
                } else {
                    total += (5 - resp);
                }
            }
            const score = total * 2.5;
            document.getElementById('live-sus-score').textContent = score.toFixed(1);

            let grade = 'Grade F (Fail)';
            let badgeClass = 'status-warn';
            if (score >= 80.3) {
                grade = 'Grade A+ (Best Imaginable)';
                badgeClass = 'status-pass';
            } else if (score >= 68.0) {
                grade = 'Grade B / Good';
                badgeClass = 'status-pass';
            } else if (score >= 50.0) {
                grade = 'Grade D / Marginal';
            }
            
            const badge = document.getElementById('live-sus-grade');
            badge.textContent = grade;
            badge.className = `status-badge ${badgeClass}`;
        }

        // Load Academic Markdown Report
        function loadMarkdownReport() {
            const container = document.getElementById('markdown-report-container');
            if (!container) return;

            let reportMd = '';
            if (window.CampusMeetReports && window.CampusMeetReports['Lab6_report.md']) {
                reportMd = window.CampusMeetReports['Lab6_report.md'];
            }

            if (reportMd && typeof marked !== 'undefined') {
                container.innerHTML = marked.parse(reportMd);
            } else if (reportMd) {
                container.innerHTML = '<pre style="white-space: pre-wrap; font-family: monospace;">' + reportMd.replace(/</g, '&lt;') + '</pre>';
            }
        }

        document.addEventListener('DOMContentLoaded', function() {
            loadLab6Data();
            loadMarkdownReport();
            
            // Check hash for initial tab
            const hash = window.location.hash.replace('#', '');
            if (hash && typeof window.switchTab === 'function') {
                window.switchTab(hash);
            }
        });
    </script>
</body>
</html>
"""

OUT_FILE.write_text(content, encoding="utf-8")
print(f"Successfully generated Lab 6 page matching design system: {OUT_FILE} ({len(content)} chars)")
