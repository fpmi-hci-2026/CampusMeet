# -*- coding: utf-8 -*-
"""Generate rich interactive HTML page for Lab 6."""
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
        /* Custom Lab 6 Interactive Styles */
        .interactive-widget {
            background: var(--surface-primary);
            border: 1px solid var(--border-default);
            border-radius: var(--radius-lg);
            padding: 24px;
            margin: 20px 0;
            box-shadow: 0 4px 20px rgba(0,0,0,0.04);
        }
        .goms-selector-bar {
            display: flex;
            gap: 12px;
            flex-wrap: wrap;
            margin-bottom: 20px;
            background: var(--surface-secondary);
            padding: 12px;
            border-radius: var(--radius-md);
            border: 1px solid var(--border-subtle);
        }
        .goms-select-group {
            display: flex;
            flex-direction: column;
            gap: 4px;
            flex: 1;
            min-width: 180px;
        }
        .goms-select-group label {
            font-size: 0.75rem;
            font-weight: 700;
            color: var(--text-secondary);
            text-transform: uppercase;
            letter-spacing: 0.5px;
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
            margin-bottom: 16px;
            flex-wrap: wrap;
        }
        .metric-pill {
            padding: 10px 16px;
            border-radius: var(--radius-md);
            background: var(--surface-secondary);
            border: 1px solid var(--border-subtle);
            display: flex;
            flex-direction: column;
            min-width: 110px;
        }
        .metric-pill-val {
            font-size: 1.4rem;
            font-weight: 800;
            font-family: 'JetBrains Mono', monospace;
            color: var(--text-primary);
        }
        .metric-pill-lbl {
            font-size: 0.7rem;
            color: var(--text-secondary);
            text-transform: uppercase;
            font-weight: 600;
        }
        .goms-step-table {
            width: 100%;
            border-collapse: collapse;
            font-size: 0.85rem;
            margin-top: 12px;
        }
        .goms-step-table th, .goms-step-table td {
            padding: 8px 12px;
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
            padding: 2px 6px;
            border-radius: 4px;
            font-family: 'JetBrains Mono', monospace;
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
        }
        .sus-scale-group {
            display: flex;
            gap: 8px;
            align-items: center;
        }
        .sus-scale-btn {
            width: 32px;
            height: 32px;
            border-radius: 50%;
            border: 1px solid var(--border-default);
            background: var(--surface-primary);
            color: var(--text-secondary);
            font-weight: 700;
            font-size: 0.85rem;
            cursor: pointer;
            transition: all 0.15s ease;
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
            padding: 12px 16px;
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
            padding: 3px 8px;
            border-radius: 12px;
            font-size: 0.75rem;
            font-weight: 700;
        }
        .status-pass { background: #dcfce7; color: #166534; }
        .status-warn { background: #fef3c7; color: #92400e; }
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

    <!-- Sidebar Navigation -->
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
                    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
                    Поиск по проекту...
                </span>
                <span class="kbd-badge">⌘K</span>
            </button>
        </div>

        <nav class="sidebar-nav">
            <div class="nav-section-title">Лабораторные работы</div>
            <a href="lab1.html" class="nav-item">
                <span class="nav-item-badge">L1</span>
                <span>Исследование аудитории</span>
            </a>
            <a href="lab2.html" class="nav-item">
                <span class="nav-item-badge">L2</span>
                <span>Инфо-архитектура & CJM</span>
            </a>
            <a href="lab3.html" class="nav-item">
                <span class="nav-item-badge">L3</span>
                <span>UML, C4 & ТЗ (SRS)</span>
            </a>
            <a href="lab4.html" class="nav-item">
                <span class="nav-item-badge">L4</span>
                <span>OpenAPI, Mock & MCP</span>
            </a>
            <a href="lab5.html" class="nav-item">
                <span class="nav-item-badge">L5</span>
                <span>Прототип & Дизайн-система</span>
            </a>
            <a href="lab6.html" class="nav-item active">
                <span class="nav-item-badge" style="background: var(--action-primary-bg); color: #fff;">L6</span>
                <span>Тестирование & Оценка</span>
            </a>
            <a href="wiki.html" class="nav-item">
                <span class="nav-item-badge">Docs</span>
                <span>База знаний (Wiki)</span>
            </a>
        </nav>

        <div class="sidebar-footer">
            <a href="https://github.com/fpmi-hci-2026/CampusMeet" target="_blank" rel="noopener" class="repo-link">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z"/></svg>
                <span>fpmi-hci-2026 / CampusMeet</span>
            </a>
        </div>
    </aside>

    <!-- Main Content Area -->
    <main id="main-content">
        <div class="content-container">

            <!-- Breadcrumbs -->
            <nav class="breadcrumbs" aria-label="Хлебные крошки">
                <a href="../index.html">Портал</a>
                <span class="breadcrumb-separator">/</span>
                <span class="breadcrumb-current">Лабораторная работа №6</span>
            </nav>

            <!-- Hero Section -->
            <header class="lab-header">
                <div class="lab-meta-badges">
                    <span class="badge badge-accent">Лаб. №6</span>
                    <span class="badge" style="background: #dcfce7; color: #166534; font-weight: 700;">Grade A+ (SUS 85.8)</span>
                    <span class="badge">N = 10 респондентов</span>
                    <span class="badge">95% ДИ Вильсона</span>
                    <span class="badge">12 моделей GOMS</span>
                </div>
                <h1 class="lab-title">Тестирование и количественная оценка качества прототипа CampusMeet</h1>
                <p class="lab-description">
                    Комплексное тестирование юзабилити интерактивного прототипа экосистемы: эмпирические пользовательские сессии ($N=10$), моторно-когнитивный хронометраж GOMS/TLM, проверка информационной архитектуры в Treejack, тестирование ожиданий и стандартизированное анкетирование SUS.
                </p>
                <div class="lab-action-buttons" style="display: flex; gap: 10px; margin-top: 16px;">
                    <a href="#report-lab6" class="btn btn-primary" style="font-size: 0.85rem;">
                        Читать полный академический отчет
                    </a>
                    <a href="#lab6-goms-tlm" class="btn btn-secondary" style="font-size: 0.85rem;">
                        Интерактивный калькулятор GOMS
                    </a>
                </div>
            </header>

            <!-- KPI Metric Grid -->
            <div class="metrics-grid">
                <div class="metric-card">
                    <div class="metric-value" style="color: #10b981;">97.5%</div>
                    <div class="metric-label">Task Success Rate</div>
                    <div class="metric-hint">39 из 40 сценариев (95% ДИ: 87.1%..99.6%)</div>
                </div>
                <div class="metric-card">
                    <div class="metric-value" style="color: #2563eb;">85.75</div>
                    <div class="metric-label">System Usability Scale (SUS)</div>
                    <div class="metric-hint">96-й перцентиль (Grade A+ / Best Imaginable)</div>
                </div>
                <div class="metric-card">
                    <div class="metric-value" style="color: #8b5cf6;">90.7%</div>
                    <div class="metric-label">Интегральный индекс SUM</div>
                    <div class="metric-hint">Комбинированный z-показатель Сауро</div>
                </div>
                <div class="metric-card">
                    <div class="metric-value" style="color: #06b6d4;">14.10 с</div>
                    <div class="metric-label">Оптимум GOMS (Web)</div>
                    <div class="metric-hint">Ускорение ввода данных в 2.3..7.8 раза</div>
                </div>
            </div>

            <!-- SECTION 1: Performance Metrics & Usability Scorecard -->
            <section id="lab6-performance" class="doc-section">
                <div class="section-header">
                    <div class="section-badge">Метрики</div>
                    <h2>1. Показатели производительности и Usability Scorecard</h2>
                </div>
                <p>
                    Тестирование проводилось на репрезентативной выборке $N=10$ пользователей по 4 сквозным сценариям. Точность оценки бинарного успеха подтверждена расчетом интервалов Вильсона при уровне доверия 95%.
                </p>

                <!-- Scenarios Table -->
                <div class="table-container" style="margin-bottom: 24px;">
                    <table>
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

                <!-- Radar Chart Visualizer -->
                <div class="interactive-widget">
                    <h3 style="margin-top: 0; font-size: 1.1rem;">Сводная лепестковая диаграмма качества (Usability Scorecard)</h3>
                    <p style="font-size: 0.85rem; color: var(--text-secondary); margin-bottom: 16px;">
                        Сопоставление фактически измеренных показателей прототипа CampusMeet с нормативными требованиями и отраслевыми бенчмарками.
                    </p>
                    <div style="text-align: center; background: var(--surface-secondary); padding: 16px; border-radius: var(--radius-md); border: 1px solid var(--border-subtle);">
                        <img src="../assets/lab6/usability_scorecard_radar.svg" alt="Лепестковая диаграмма юзабилити" style="max-width: 100%; height: auto; border-radius: 8px;">
                    </div>
                </div>
            </section>

            <!-- SECTION 2: Information Architecture & Treejack -->
            <section id="lab6-treejack" class="doc-section">
                <div class="section-header">
                    <div class="section-badge">Инфо-архитектура</div>
                    <h2>2. Обратная карточная сортировка и Treejack-исследование</h2>
                </div>
                <p>
                    Верификация структуры меню и навигации проводилась изолированно от визуального оформления: оффлайн-сортировкой карточек на карте сайта и онлайн-тестированием дерева в инструменте <strong>Treejack</strong> (Optimal Workshop).
                </p>

                <div class="interactive-widget">
                    <h3 style="margin-top: 0; font-size: 1.1rem;">Пути навигации и прямолинейность (Treejack Paths)</h3>
                    <p style="font-size: 0.85rem; color: var(--text-secondary); margin-bottom: 16px;">
                        Средний показатель успешности поиска разделов составил <strong>95.0%</strong>, а коэффициент прямолинейности (Directness) — <strong>88.8%</strong>.
                    </p>
                    <div style="text-align: center; background: var(--surface-secondary); padding: 16px; border-radius: var(--radius-md); border: 1px solid var(--border-subtle);">
                        <img src="../assets/lab6/treejack_paths_ia.svg" alt="Treejack IA Paths" style="max-width: 100%; height: auto; border-radius: 8px;">
                    </div>
                </div>
            </section>

            <!-- SECTION 3: Expectation Testing & Checklists -->
            <section id="lab6-expectations" class="doc-section">
                <div class="section-header">
                    <div class="section-badge">Эвристики & Чек-листы</div>
                    <h2>3. Тестирование ожиданий и экспертные чек-листы (Web & Mobile)</h2>
                </div>
                <p>
                    Исследование позволило выявить ментальные модели пользователей и сопоставить их с программной логикой, исключив «обманутые ожидания».
                </p>

                <!-- Interactive Checklists -->
                <div class="interactive-widget">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px; flex-wrap: wrap; gap: 10px;">
                        <div>
                            <h3 style="margin: 0; font-size: 1.1rem;">Интерактивный инспектор чек-листов</h3>
                            <span style="font-size: 0.8rem; color: var(--text-secondary);">Стандарты WCAG 2.1, Nielsen Heuristics, Apple HIG & Material Design</span>
                        </div>
                        <div style="display: flex; gap: 8px;">
                            <button id="cl-btn-web" class="interactive-tab-btn active" onclick="switchChecklist('web')">Web (10 критериев)</button>
                            <button id="cl-btn-mob" class="interactive-tab-btn" onclick="switchChecklist('mobile')">Mobile (8 критериев)</button>
                        </div>
                    </div>

                    <div id="checklist-items-container">
                        <!-- Populated by JS -->
                    </div>
                </div>
            </section>

            <!-- SECTION 4: GOMS & TLM Quantitative Modeling -->
            <section id="lab6-goms-tlm" class="doc-section">
                <div class="section-header">
                    <div class="section-badge">GOMS & TLM</div>
                    <h2>4. Количественный хронометраж по моделям GOMS (12 расчетов) и TLM</h2>
                </div>
                <p>
                    Аналитическое моделирование уровня нажатия клавиш (KLM/GOMS) и касаний (TLM) позволяет точно спрогнозировать время работы квалифицированного пользователя без запуска секундомера на основе фундаментальных психофизиологических констант взаимодействия.
                </p>

                <!-- Interactive GOMS Calculator -->
                <div class="interactive-widget">
                    <h3 style="margin-top: 0; font-size: 1.1rem;">Интерактивный симулятор-калькулятор GOMS</h3>
                    <p style="font-size: 0.85rem; color: var(--text-secondary);">
                        Выберите форму, вариант проектирования и метод ввода, чтобы изучить детальную цепочку моторных операторов ($K, P, H, M$) с учетом правил элиминации.
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
                                <option value="mouse">Только мышь (клики и наведение)</option>
                                <option value="keyboard_tab" selected>Клавиатура (Tab-навигация / Хоткеи)</option>
                            </select>
                        </div>
                    </div>

                    <!-- Metrics Badges for Selected Model -->
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

                    <div style="overflow-x: auto;">
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

                <!-- GOMS & TLM Comparison Bar Chart -->
                <div class="interactive-widget">
                    <h3 style="margin-top: 0; font-size: 1.1rem;">Сравнение хронометража: 12 моделей GOMS и 3 модели TLM</h3>
                    <div style="text-align: center; background: var(--surface-secondary); padding: 16px; border-radius: var(--radius-md); border: 1px solid var(--border-subtle);">
                        <img src="../assets/lab6/goms_tlm_comparison.svg" alt="GOMS vs TLM Bar Chart" style="max-width: 100%; height: auto; border-radius: 8px;">
                    </div>
                </div>
            </section>

            <!-- SECTION 5: SUS Survey & Live Calculator -->
            <section id="lab6-sus" class="doc-section">
                <div class="section-header">
                    <div class="section-badge">Шкала SUS</div>
                    <h2>5. Оценка субъективной удовлетворенности (System Usability Scale)</h2>
                </div>
                <p>
                    Стандартизированная анкета SUS позволяет сопоставить субъективное восприятие системы со среднемировыми показателями. Средний балл CampusMeet составил <strong>85.75</strong>, что соответствует категории <strong>Grade A+ (Best Imaginable)</strong>.
                </p>

                <!-- Live SUS Questionnaire Simulator -->
                <div class="interactive-widget">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px; flex-wrap: wrap; gap: 12px;">
                        <div>
                            <h3 style="margin: 0; font-size: 1.1rem;">Интерактивный опросник и калькулятор SUS</h3>
                            <span style="font-size: 0.8rem; color: var(--text-secondary);">Попробуйте изменить ответы, чтобы увидеть пересчет итогового балла и грейда</span>
                        </div>
                        <div style="display: flex; align-items: center; gap: 12px; background: var(--surface-secondary); padding: 8px 16px; border-radius: var(--radius-md); border: 1px solid var(--border-subtle);">
                            <span style="font-size: 0.85rem; font-weight: 600;">Итоговый балл:</span>
                            <span id="live-sus-score" style="font-size: 1.6rem; font-weight: 800; font-family: 'JetBrains Mono', monospace; color: #10b981;">85.0</span>
                            <span id="live-sus-grade" class="status-badge status-pass" style="font-size: 0.8rem;">Grade A+ (Excellent)</span>
                        </div>
                    </div>

                    <div id="sus-questions-list">
                        <!-- Populated by JS -->
                    </div>
                </div>

                <div class="interactive-widget">
                    <h3 style="margin-top: 0; font-size: 1.1rem;">Распределение оценок респондентов по шкале Банга–Кортума</h3>
                    <div style="text-align: center; background: var(--surface-secondary); padding: 16px; border-radius: var(--radius-md); border: 1px solid var(--border-subtle);">
                        <img src="../assets/lab6/sus_distribution_chart.svg" alt="SUS Distribution Chart" style="max-width: 100%; height: auto; border-radius: 8px;">
                    </div>
                </div>
            </section>

            <!-- SECTION 6: Embedded Full Academic Report -->
            <section id="report-lab6" class="doc-section">
                <div class="section-header">
                    <div class="section-badge">Академический отчет</div>
                    <h2>6. Полный технический отчёт по лабораторной работе №6</h2>
                </div>
                <p>
                    Ниже приведён встроенный академический отчёт с детальными расчётами, математическими выкладками, таблицами доверительных интервалов и списком литературы по курсу ПЧМИ:
                </p>

                <!-- Markdown Container -->
                <div id="markdown-report-container" class="markdown-body" style="background: var(--surface-primary); border: 1px solid var(--border-default); border-radius: var(--radius-lg); padding: 32px;">
                    <div style="text-align: center; color: var(--text-muted); padding: 40px;">
                        Загрузка академического отчета...
                    </div>
                </div>
            </section>

        </div>
    </main>

    <!-- Embedded Scripts and Data -->
    <script src="../js/vendor/marked.min.js"></script>
    <script src="../js/data/navigation.js"></script>
    <script src="../js/data/search.js"></script>
    <script src="../js/data/reports.js"></script>
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
        async function loadLab6Data() {
            try {
                const [rGoms, rCl, rMetrics] = await Promise.all([
                    fetch('../data/lab6/goms-models.json').then(r => r.json()),
                    fetch('../data/lab6/checklists.json').then(r => r.json()),
                    fetch('../data/lab6/usability-metrics.json').then(r => r.json())
                ]);
                gomsData = rGoms;
                checklistData = rCl;
                susQuestions = rMetrics.susQuestions;
                
                initChecklists();
                initSusSurvey();
                updateGomsView();
            } catch (e) {
                console.error("Data load fallback", e);
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
                            <span style="font-family: 'JetBrains Mono', monospace; font-size: 0.75rem; font-weight: 700; color: #2563eb;">${item.id}</span>
                            <span style="font-size: 0.75rem; text-transform: uppercase; color: var(--text-tertiary); font-weight: 600;">${item.category}</span>
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
                    <td style="color: var(--text-tertiary); font-family: 'JetBrains Mono', monospace;">${idx + 1}</td>
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
        });
    </script>
</body>
</html>
"""

OUT_FILE.write_text(content, encoding="utf-8")
print(f"Generated Lab 6 web page: {OUT_FILE} ({len(content)} chars)")
