/**
 * CampusMeet / EventHub — Layout Shell & Dynamic Navigation Engine
 * Automatically generates Sidebar, Breadcrumbs, Right-Side TOC with Scrollspy,
 * Bottom Pager, and Dialogs for Declarative Lab Pages.
 * Matches existing docs/DESIGN_SYSTEM.md architecture.
 */

(function () {
    'use strict';

    function getNav() {
        return window.CampusMeetNavigation || null;
    }

    function resolve(path) {
        const nav = getNav();
        return (nav && typeof nav.resolvePath === 'function') ? nav.resolvePath(path) : path;
    }

    /**
     * SVG Icons Dictionary
     */
    const ICONS = {
        home: '<svg class="icon icon-nav" viewBox="0 0 24 24"><path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path><polyline points="9 22 9 12 15 12 15 22"></polyline></svg>',
        lab: '<svg class="icon icon-nav" viewBox="0 0 24 24"><polygon points="12 2 2 7 12 12 22 7 12 2"></polygon><polyline points="2 17 12 22 22 17"></polyline><polyline points="2 12 12 17 22 12"></polyline></svg>',
        users: '<svg class="icon icon-nav" viewBox="0 0 24 24"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg>',
        layout: '<svg class="icon icon-nav" viewBox="0 0 24 24"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><line x1="3" y1="9" x2="21" y2="9"></line><line x1="9" y1="21" x2="9" y2="9"></line></svg>',
        fileText: '<svg class="icon icon-nav" viewBox="0 0 24 24"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line></svg>',
        book: '<svg class="icon icon-nav" viewBox="0 0 24 24"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path></svg>',
        github: '<svg class="icon icon-nav" viewBox="0 0 24 24"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"></path></svg>',
        search: '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>',
        menu: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg>',
        sun: '<svg class="icon-sun" viewBox="0 0 24 24"><circle cx="12" cy="12" r="5"></circle><line x1="12" y1="1" x2="12" y2="3"></line><line x1="12" y1="21" x2="12" y2="23"></line><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line><line x1="1" y1="12" x2="3" y2="12"></line><line x1="21" y1="12" x2="23" y2="12"></line><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line></svg>',
        moon: '<svg class="icon-moon" viewBox="0 0 24 24"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path></svg>'
    };

    /**
     * Builds the complete Sidebar HTML
     */
    function renderSidebarHtml(currentPageId, sections) {
        const nav = getNav();
        if (!nav) return '';

        const homeActive = currentPageId === 'portal' ? 'active current-page' : '';
        const wikiActive = currentPageId === 'wiki' ? 'active current-page' : '';

        // Build Labs list
        const labsHtml = nav.labs.map(lab => {
            const isActive = lab.id === currentPageId ? 'active current-page' : '';
            const statusClass = lab.status === 'done' ? 'tag-key' : 'tag-supp';
            const iconSvg = ICONS[lab.icon] || ICONS.lab;
            return `
                <li class="nav-item">
                    <a href="${resolve(lab.path)}" class="nav-link ${isActive}" title="${lab.title}: ${lab.desc}">
                        ${iconSvg}
                        <span>${lab.shortTitle}</span>
                        <span class="nav-badge ${statusClass}" style="font-size: 0.65rem;">${lab.badge}</span>
                    </a>
                </li>
            `;
        }).join('');

        // Build On-page section links
        let onPageHtml = '';
        if (sections && sections.length > 0) {
            const listItems = sections.map((sec, idx) => {
                const numStr = (idx + 1).toString().padStart(2, '0');
                return `
                    <li class="nav-item">
                        <a href="#${sec.id}" class="nav-link" data-toc-target="${sec.id}">
                            <span class="nav-num">${numStr}</span>
                            <span>${sec.title}</span>
                        </a>
                    </li>
                `;
            }).join('');

            onPageHtml = `
                <div class="nav-section-title">Содержание страницы</div>
                <ul class="nav-menu">
                    ${listItems}
                </ul>
            `;
        }

        // Build Reports list
        const reportsHtml = nav.labs
            .filter(lab => lab.status === 'done')
            .map(lab => `
                <li class="nav-item">
                    <a href="${resolve(lab.report)}" class="nav-link" id="report-${lab.id}" target="_blank" rel="noopener noreferrer">
                        ${ICONS.fileText}
                        <span>Отчет ${lab.shortTitle} (MD)</span>
                    </a>
                </li>
            `).join('');

        // Build External Repos list
        const reposHtml = nav.repos.map(r => `
            <li class="nav-item">
                <a href="${r.url}" class="nav-link" target="_blank" rel="noopener noreferrer">
                    ${ICONS.github}
                    <span>${r.name}</span>
                </a>
            </li>
        `).join('');

        return `
            <div class="sidebar-header">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
                    <span class="brand-badge" style="margin-bottom: 0;">ПЧМИ • БГУ ФПМИ</span>
                    <button class="theme-toggle-btn" type="button" aria-label="Переключить тему оформления" title="Светлая / Темная тема">
                        ${ICONS.sun}
                        ${ICONS.moon}
                    </button>
                </div>
                <h1>
                    <span>CampusMeet</span>
                    <span class="version-badge">${nav.site.version}</span>
                </h1>
                <p>${nav.site.subtitle}</p>
                <button type="button" class="omnibox-trigger-btn" id="sidebar-search-btn" onclick="if(window.openOmnibox)window.openOmnibox();">
                    <span style="display: flex; align-items: center; gap: 8px;">
                        ${ICONS.search}
                        <span>Быстрый поиск...</span>
                    </span>
                    <kbd class="kbd-shortcut">⌘K</kbd>
                </button>
            </div>

            <div class="nav-section-title">Разделы курса</div>
            <ul class="nav-menu">
                <li class="nav-item">
                    <a href="${resolve(nav.portal.path)}" class="nav-link ${homeActive}">
                        ${ICONS.home}
                        <span>Главный портал</span>
                        <span class="nav-badge">Hub</span>
                    </a>
                </li>
                ${labsHtml}
                <li class="nav-item">
                    <a href="${resolve(nav.wiki.path)}" class="nav-link ${wikiActive}">
                        ${ICONS.book}
                        <span>База знаний (Wiki)</span>
                        <span class="nav-badge">Docs</span>
                    </a>
                </li>
            </ul>

            ${onPageHtml}

            <div class="nav-section-title">Материалы и отчеты</div>
            <ul class="nav-menu">
                ${reportsHtml}
            </ul>

            <div class="nav-section-title">Репозитории экосистемы</div>
            <ul class="nav-menu">
                ${reposHtml}
            </ul>
        `;
    }

    /**
     * Builds Breadcrumbs Navigation
     */
    function renderBreadcrumbsHtml(currentPageId) {
        const nav = getNav();
        const curLab = nav.labs.find(l => l.id === currentPageId);

        let breadcrumbLabel = 'Обзор портала';
        if (curLab) {
            breadcrumbLabel = `${curLab.title}: ${curLab.subtitle}`;
        } else if (currentPageId === 'wiki') {
            breadcrumbLabel = 'База знаний (Wiki)';
        }

        return `
            <nav class="content-breadcrumbs" aria-label="Хлебные крошки">
                <ol class="breadcrumbs-list">
                    <li class="breadcrumb-item"><a href="${resolve(nav.portal.path)}">Главная</a></li>
                    <li class="breadcrumb-separator">/</li>
                    ${curLab ? `<li class="breadcrumb-item"><a href="${resolve(curLab.path)}">${curLab.shortTitle}</a></li><li class="breadcrumb-separator">/</li>` : ''}
                    <li class="breadcrumb-item breadcrumb-active" id="active-breadcrumb-tab">${breadcrumbLabel}</li>
                </ol>
            </nav>
        `;
    }

    /**
     * Builds Bottom Pager Navigation
     */
    function renderPagerHtml(currentPageId) {
        const nav = getNav();
        const { prev, next } = nav.getPrevNextLabs(currentPageId);
        if (!prev && !next) return '';

        return `
            <nav class="page-nav-pager" aria-label="Навигация по лабораторным работам">
                ${prev ? `
                <a href="${resolve(prev.path)}" class="pager-card pager-prev">
                    <span class="pager-direction">← Предыдущая работа</span>
                    <span class="pager-title">${prev.shortTitle}: ${prev.subtitle}</span>
                </a>` : '<div></div>'}
                ${next ? `
                <a href="${resolve(next.path)}" class="pager-card pager-next">
                    <span class="pager-direction">Следующая работа →</span>
                    <span class="pager-title">${next.shortTitle}: ${next.subtitle}</span>
                </a>` : '<div></div>'}
            </nav>
        `;
    }

    /**
     * Injects Common Dialogs if Missing
     */
    function ensureDialogs() {
        if (!document.getElementById('lightbox-dialog')) {
            const dlg = document.createElement('dialog');
            dlg.id = 'lightbox-dialog';
            dlg.setAttribute('aria-labelledby', 'lightbox-title');
            dlg.innerHTML = `
                <div class="lightbox-header">
                    <div class="lightbox-meta">
                        <div class="lightbox-title" id="lightbox-title">Просмотр схемы</div>
                        <span class="lightbox-badge" id="lightbox-badge">SVG</span>
                    </div>
                    <div class="lightbox-controls">
                        <button class="lightbox-btn" id="lightbox-zoom-out" type="button" title="Уменьшить (−)">−</button>
                        <span class="lightbox-zoom-badge" id="lightbox-zoom-badge">100%</span>
                        <button class="lightbox-btn" id="lightbox-zoom-in" type="button" title="Увеличить (+)">+</button>
                        <button class="lightbox-btn" id="lightbox-zoom-reset" type="button" title="Сбросить (1:1)">1:1</button>
                        <button class="lightbox-btn" id="lightbox-fit-btn" type="button" title="Вписать в экран">Вписать</button>
                        <a class="lightbox-btn" id="lightbox-open-link" href="#" target="_blank" rel="noopener noreferrer" title="В новой вкладке">↗</a>
                        <button class="lightbox-btn" id="lightbox-close" type="button" title="Закрыть (Esc)"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg></button>
                    </div>
                </div>
                <div class="lightbox-body">
                    <img id="lightbox-img" src="" alt="Схема">
                    <div class="lightbox-footer-hints">
                        <span>Колесо: Zoom</span> • <span>Перетаскивание: Pan</span> • <span>Двойной клик: 100%/200%</span> • <span>Esc: Закрыть</span>
                    </div>
                </div>
            `;
            document.body.appendChild(dlg);
        }

        if (!document.getElementById('omnibox-dialog')) {
            const dlg = document.createElement('dialog');
            dlg.id = 'omnibox-dialog';
            dlg.setAttribute('aria-label', 'Быстрый поиск');
            dlg.innerHTML = `
                <div class="omnibox-header">
                    <span class="omnibox-icon">${ICONS.search}</span>
                    <input type="text" id="omnibox-input" class="omnibox-input" placeholder="Поиск по разделам, диаграммам, User Stories...">
                    <button type="button" class="omnibox-close-btn" onclick="document.getElementById('omnibox-dialog').close()" aria-label="Закрыть"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg></button>
                </div>
                <ul id="omnibox-results" class="omnibox-results"></ul>
            `;
            document.body.appendChild(dlg);
        }
    }

    /**
     * Initializes Scrollspy for Sidebar Section Links
     */
    function initScrollspy(sectionIds) {
        if (!('IntersectionObserver' in window) || !sectionIds || sectionIds.length === 0) return;

        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const id = entry.target.id;
                    document.querySelectorAll('[data-toc-target]').forEach(link => {
                        const target = link.dataset.tocTarget;
                        if (target === id) {
                            link.classList.add('active');
                        } else {
                            link.classList.remove('active');
                        }
                    });
                }
            });
        }, {
            rootMargin: '-10% 0px -70% 0px',
            threshold: 0
        });

        sectionIds.forEach(id => {
            const el = document.getElementById(id);
            if (el) observer.observe(el);
        });
    }

    /**
     * Layout Engine Initializer
     */
    function initLayout() {
        const nav = getNav();
        if (!nav) return;

        const currentPageId = nav.getCurrentPageId();
        const existingSidebar = document.getElementById('sidebar');

        // Extract sections from page content
        const sectionNodes = document.querySelectorAll('doc-section, section.doc-section, section[id]');
        const sections = Array.from(sectionNodes).map(node => {
            const id = node.id;
            const h2 = node.querySelector('h2, .section-title');
            const title = node.getAttribute('title') || (h2 ? h2.textContent.trim() : id);
            return { id, title };
        }).filter(s => !!s.id);

        if (!existingSidebar) {
            // Transform declarative page into full standard layout
            const contentNodes = Array.from(document.body.childNodes);
            document.body.innerHTML = '';

            // 1. Mobile topbar
            const mobileTopbar = document.createElement('header');
            mobileTopbar.className = 'mobile-topbar';
            mobileTopbar.innerHTML = `
                <a href="${resolve(nav.portal.path)}" class="mobile-brand">
                    <img src="${resolve('assets/favicon.svg')}" alt="CampusMeet Logo">
                    <span>CampusMeet</span>
                </a>
                <div style="display: flex; align-items: center; gap: 8px;">
                    <button class="theme-toggle-btn" type="button" aria-label="Переключить тему оформления">
                        ${ICONS.sun}
                        ${ICONS.moon}
                    </button>
                    <button id="mobile-hamburger" class="hamburger-btn" type="button" aria-label="Открыть навигацию">
                        ${ICONS.menu}
                    </button>
                </div>
            `;

            // 2. Sidebar backdrop
            const backdrop = document.createElement('div');
            backdrop.id = 'sidebar-backdrop';
            backdrop.className = 'sidebar-backdrop';

            // 3. Sidebar
            const sidebar = document.createElement('aside');
            sidebar.id = 'sidebar';
            sidebar.innerHTML = renderSidebarHtml(currentPageId, sections);

            // 4. Main content container
            const mainContent = document.createElement('main');
            mainContent.id = 'content';

            const contentContainer = document.createElement('div');
            contentContainer.className = 'content-container';

            // Insert breadcrumbs
            const breadcrumbs = document.createElement('div');
            breadcrumbs.innerHTML = renderBreadcrumbsHtml(currentPageId);
            contentContainer.appendChild(breadcrumbs.firstElementChild);

            // Insert unique page content
            contentNodes.forEach(node => contentContainer.appendChild(node));

            // Insert pager
            const pager = document.createElement('div');
            pager.innerHTML = renderPagerHtml(currentPageId);
            if (pager.firstElementChild) {
                contentContainer.appendChild(pager.firstElementChild);
            }

            // Footer notes
            const footerNote = document.createElement('div');
            footerNote.style.cssText = 'margin-top: 48px; padding-top: 24px; border-top: 1px solid var(--border-subtle); display: flex; justify-content: space-between; align-items: center; font-size: 0.8rem; color: var(--text-tertiary); flex-wrap: wrap; gap: 12px;';
            footerNote.innerHTML = `
                <div>© 2025–2026 CampusMeet / EventHub • БГУ ФПМИ, Кафедра технологий программирования</div>
                <div>Команда: Минчук С., Иванова В., Шварцман Д.</div>
            `;
            contentContainer.appendChild(footerNote);

            mainContent.appendChild(contentContainer);

            // Mount directly onto body
            document.body.appendChild(mobileTopbar);
            document.body.appendChild(backdrop);
            document.body.appendChild(sidebar);
            document.body.appendChild(mainContent);
        }

        // Ensure dialogs and hooks
        ensureDialogs();

        // Initialize Scrollspy
        if (sections.length > 0) {
            initScrollspy(sections.map(s => s.id));
        }

        // Initialize theme toggles
        if (typeof window.initThemeToggle === 'function') {
            window.initThemeToggle();
        }

        // Hook mobile drawer
        const hamburgerBtn = document.getElementById('mobile-hamburger');
        const backdrop = document.getElementById('sidebar-backdrop');
        if (hamburgerBtn && typeof window.openMobileSidebar === 'function') {
            hamburgerBtn.addEventListener('click', window.openMobileSidebar);
        }
        if (backdrop && typeof window.closeMobileSidebar === 'function') {
            backdrop.addEventListener('click', window.closeMobileSidebar);
        }
    }

    window.initCampusMeetLayout = initLayout;

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initLayout);
    } else {
        initLayout();
    }
})();
