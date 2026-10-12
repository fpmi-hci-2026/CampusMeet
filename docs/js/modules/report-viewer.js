/**
 * CampusMeet / EventHub — Academic Markdown Report Viewer Module
 * Implements interactive full-fidelity preview for academic reports,
 * with table-of-contents navigation, raw/rendered toggling, code copying,
 * and 100% offline compatibility via embedded reports data.
 * Strictly adheres to docs/DESIGN_SYSTEM.md monochrome guidelines.
 */

(function () {
    'use strict';

    let currentReportKey = null;
    let currentMarkdownText = '';
    let isRawMode = false;

    const REPORT_TITLES = {
        'Lab1_report.md': 'Лабораторная работа №1: Исследование пользователей и предметной области',
        'Lab2_report.md': 'Лабораторная работа №2: Проектирование информационной архитектуры и взаимодействия',
        'Lab3_report.md': 'Лабораторная работа №3: Разработка требований к программной системе'
    };

    function normalizeReportKey(raw) {
        if (!raw) return 'Lab1_report.md';
        const lower = raw.toLowerCase();
        if (lower.includes('lab1')) return 'Lab1_report.md';
        if (lower.includes('lab2')) return 'Lab2_report.md';
        if (lower.includes('lab3')) return 'Lab3_report.md';
        return raw;
    }

    /**
     * Ensures Dialog Markup is present in the document
     */
    function ensureDialogDOM() {
        let dialog = document.getElementById('report-dialog');
        if (dialog) return dialog;

        dialog = document.createElement('dialog');
        dialog.id = 'report-dialog';
        dialog.setAttribute('aria-labelledby', 'report-dialog-title');
        dialog.innerHTML = `
            <div class="report-header">
                <div class="report-meta">
                    <svg class="report-meta-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
                    <div class="report-title" id="report-dialog-title">Предпросмотр отчета</div>
                    <span class="report-badge" id="report-dialog-badge">MARKDOWN</span>
                    <span class="report-stats" id="report-dialog-stats">0 строк</span>
                </div>
                <div class="report-controls">
                    <button type="button" class="report-btn" id="report-toc-toggle-btn" title="Скрыть/показать оглавление">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg>
                        <span>Оглавление</span>
                    </button>
                    <button type="button" class="report-btn" id="report-raw-toggle-btn" title="Переключить форматирование / сырой Markdown">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="16 18 22 12 16 6"></polyline><polyline points="8 6 2 12 8 18"></polyline></svg>
                        <span id="report-raw-label">Исходник</span>
                    </button>
                    <button type="button" class="report-btn" id="report-copy-btn" title="Скопировать Markdown в буфер">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect width="14" height="14" x="8" y="8" rx="2" ry="2"></rect><path d="M4 16c-1.1 0-2-.9-2-2V4c0-1.1.9-2 2-2h10c1.1 0 2 .9 2 2"></path></svg>
                        <span>Копировать</span>
                    </button>
                    <a href="#" class="report-btn" id="report-download-btn" download title="Скачать файл .md">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
                        <span>Скачать .md</span>
                    </a>
                    <button type="button" class="report-btn" id="report-close-btn" title="Закрыть (Esc)">
                        <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
                    </button>
                </div>
            </div>
            <div class="report-workspace">
                <aside class="report-toc-sidebar" id="report-toc-sidebar">
                    <div class="report-toc-header">
                        <span>Навигация по разделам</span>
                        <span id="report-toc-count" style="font-family: var(--font-mono); font-size: 0.68rem; color: var(--text-tertiary);">0 тем</span>
                    </div>
                    <div class="report-toc-search">
                        <input type="text" id="report-toc-input" placeholder="Поиск по оглавлению..." autocomplete="off">
                    </div>
                    <ul class="report-toc-nav" id="report-toc-nav"></ul>
                </aside>
                <div class="report-content-pane" id="report-content-pane">
                    <article class="report-document" id="report-document"></article>
                    <div class="report-raw-view" id="report-raw-view">
                        <pre><code id="report-raw-code"></code></pre>
                    </div>
                    <button type="button" class="report-scroll-top-btn" id="report-scroll-top-btn" title="Наверх">
                        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="18 15 12 9 6 15"></polyline></svg>
                    </button>
                </div>
            </div>
        `;
        document.body.appendChild(dialog);

        bindDialogEvents(dialog);
        return dialog;
    }

    /**
     * Binds permanent listeners on Dialog
     */
    function bindDialogEvents(dialog) {
        const closeBtn = dialog.querySelector('#report-close-btn');
        if (closeBtn) closeBtn.addEventListener('click', () => dialog.close());

        // Close on backdrop click
        dialog.addEventListener('click', function (e) {
            const rect = dialog.getBoundingClientRect();
            const isInDialog = (
                rect.top <= e.clientY && e.clientY <= rect.top + rect.height &&
                rect.left <= e.clientX && e.clientX <= rect.left + rect.width
            );
            if (!isInDialog) dialog.close();
        });

        // Close on Esc
        dialog.addEventListener('cancel', () => dialog.close());

        // TOC Toggle
        const tocBtn = dialog.querySelector('#report-toc-toggle-btn');
        const tocSidebar = dialog.querySelector('#report-toc-sidebar');
        if (tocBtn && tocSidebar) {
            tocBtn.addEventListener('click', function () {
                tocSidebar.classList.toggle('collapsed');
                tocBtn.classList.toggle('active', !tocSidebar.classList.contains('collapsed'));
            });
        }

        // Raw / Formatted Toggle
        const rawBtn = dialog.querySelector('#report-raw-toggle-btn');
        const docEl = dialog.querySelector('#report-document');
        const rawEl = dialog.querySelector('#report-raw-view');
        const rawLabel = dialog.querySelector('#report-raw-label');
        if (rawBtn) {
            rawBtn.addEventListener('click', function () {
                isRawMode = !isRawMode;
                if (isRawMode) {
                    docEl.style.display = 'none';
                    rawEl.style.display = 'block';
                    rawBtn.classList.add('active');
                    if (rawLabel) rawLabel.textContent = 'Текст';
                } else {
                    docEl.style.display = 'block';
                    rawEl.style.display = 'none';
                    rawBtn.classList.remove('active');
                    if (rawLabel) rawLabel.textContent = 'Исходник';
                }
            });
        }

        // Copy Markdown
        const copyBtn = dialog.querySelector('#report-copy-btn');
        if (copyBtn) {
            copyBtn.addEventListener('click', async function () {
                if (!currentMarkdownText) return;
                try {
                    await navigator.clipboard.writeText(currentMarkdownText);
                    const span = copyBtn.querySelector('span');
                    if (span) {
                        const prev = span.textContent;
                        span.textContent = 'Скопировано!';
                        setTimeout(() => { span.textContent = prev; }, 2000);
                    }
                } catch (err) {
                    console.error('Clipboard copy error:', err);
                }
            });
        }

        // TOC Search Filter
        const tocInput = dialog.querySelector('#report-toc-input');
        if (tocInput) {
            tocInput.addEventListener('input', function () {
                const q = this.value.toLowerCase().trim();
                const items = dialog.querySelectorAll('#report-toc-nav .report-toc-item');
                items.forEach(it => {
                    const txt = it.textContent.toLowerCase();
                    it.style.display = txt.includes(q) ? 'block' : 'none';
                });
            });
        }

        // Scroll to Top Button
        const scrollPane = dialog.querySelector('#report-content-pane');
        const topBtn = dialog.querySelector('#report-scroll-top-btn');
        if (scrollPane && topBtn) {
            scrollPane.addEventListener('scroll', function () {
                if (scrollPane.scrollTop > 400) {
                    topBtn.classList.add('visible');
                } else {
                    topBtn.classList.remove('visible');
                }
            });

            topBtn.addEventListener('click', function () {
                scrollPane.scrollTo({ top: 0, behavior: 'smooth' });
            });
        }
    }

    /**
     * Resolves Markdown text from cache or network
     */
    async function loadMarkdownContent(key) {
        // 1. Direct memory access from reports.js
        if (window.CampusMeetReports && window.CampusMeetReports[key]) {
            return window.CampusMeetReports[key];
        }

        // 2. Network / HTTP fetch fallback
        const candidatePaths = [
            `../reports/${key}`,
            `./reports/${key}`,
            `reports/${key}`
        ];

        for (const p of candidatePaths) {
            try {
                const resp = await fetch(p);
                if (resp.ok) {
                    const text = await resp.text();
                    if (text && !text.includes('<!DOCTYPE html>')) {
                        return text;
                    }
                }
            } catch (e) {
                // Ignore and try next path
            }
        }

        throw new Error(`Не удалось загрузить отчет: ${key}`);
    }

    /**
     * Opens Report Viewer Modal for the given report ID
     */
    window.openReportViewer = async function (rawKey) {
        const dialog = ensureDialogDOM();
        const key = normalizeReportKey(rawKey);
        currentReportKey = key;

        const titleEl = dialog.querySelector('#report-dialog-title');
        const statsEl = dialog.querySelector('#report-dialog-stats');
        const docEl = dialog.querySelector('#report-document');
        const rawCodeEl = dialog.querySelector('#report-raw-code');
        const downloadBtn = dialog.querySelector('#report-download-btn');
        const tocNav = dialog.querySelector('#report-toc-nav');
        const tocCount = dialog.querySelector('#report-toc-count');
        const scrollPane = dialog.querySelector('#report-content-pane');

        const displayTitle = REPORT_TITLES[key] || key;
        if (titleEl) titleEl.textContent = displayTitle;

        // Reset state
        isRawMode = false;
        docEl.style.display = 'block';
        dialog.querySelector('#report-raw-view').style.display = 'none';
        const rawBtn = dialog.querySelector('#report-raw-toggle-btn');
        if (rawBtn) rawBtn.classList.remove('active');
        const rawLabel = dialog.querySelector('#report-raw-label');
        if (rawLabel) rawLabel.textContent = 'Исходник';

        // Set download link
        if (downloadBtn) {
            downloadBtn.download = key;
            const inPages = window.location.pathname.includes('/pages/');
            downloadBtn.href = inPages ? `../reports/${key}` : `./reports/${key}`;
        }

        // Loading indicator
        docEl.innerHTML = '<div style="padding: 40px; text-align: center; color: var(--text-tertiary); font-family: var(--font-sans);">Загрузка и рендеринг отчета...</div>';
        tocNav.innerHTML = '';
        if (typeof dialog.showModal === 'function') {
            dialog.showModal();
        }

        try {
            const md = await loadMarkdownContent(key);
            currentMarkdownText = md;

            // Stats
            const lineCount = md.split('\n').length;
            const wordCount = md.split(/\s+/).filter(Boolean).length;
            const readMinutes = Math.max(1, Math.round(wordCount / 180));
            if (statsEl) {
                statsEl.textContent = `${lineCount} строк • ~${readMinutes} мин чтения`;
            }

            // Raw view code
            if (rawCodeEl) rawCodeEl.textContent = md;

            // Render Markdown
            let renderedHtml = '';
            if (typeof marked !== 'undefined' && typeof marked.parse === 'function') {
                marked.setOptions({
                    gfm: true,
                    breaks: false
                });
                renderedHtml = marked.parse(md);
            } else {
                // Basic fallback if marked is not yet loaded
                renderedHtml = '<pre style="white-space: pre-wrap;">' + md.replace(/</g, '&lt;').replace(/>/g, '&gt;') + '</pre>';
            }

            docEl.innerHTML = renderedHtml;

            // Post-process Document DOM
            postProcessReport(docEl, tocNav, tocCount, scrollPane);

            // Scroll to top
            if (scrollPane) scrollPane.scrollTop = 0;

        } catch (err) {
            console.error('Report viewer render error:', err);
            docEl.innerHTML = `
                <div style="padding: 40px; text-align: center; color: var(--text-primary); font-family: var(--font-sans);">
                    <h3 style="margin-bottom: 8px;">Ошибка загрузки отчета</h3>
                    <p style="color: var(--text-tertiary); font-size: 0.9rem;">${err.message || 'Файл отчета недоступен'}</p>
                </div>
            `;
        }
    };

    /**
     * Post-processes rendered markdown document:
     * - Generates Table of Contents with Scrollspy
     * - Fixes image URLs
     * - Wraps tables in responsive containers
     * - Adds copy buttons to code blocks
     */
    function postProcessReport(docEl, tocNav, tocCount, scrollPane) {
        // 1. Headers & TOC
        const headers = docEl.querySelectorAll('h1, h2, h3');
        tocNav.innerHTML = '';
        let headerIndex = 0;
        const tocItems = [];

        headers.forEach(h => {
            headerIndex++;
            const text = h.textContent.trim();
            if (!text) return;

            // Generate clean anchor ID
            const anchorId = 'sec-' + headerIndex + '-' + text.toLowerCase().replace(/[^a-zа-я0-9]+/gi, '-').slice(0, 40);
            h.id = anchorId;

            const level = h.tagName.toLowerCase() === 'h1' ? 1 : (h.tagName.toLowerCase() === 'h2' ? 2 : 3);

            const li = document.createElement('li');
            li.className = 'report-toc-item';
            const a = document.createElement('a');
            a.className = `report-toc-link level-${level}`;
            a.href = '#' + anchorId;
            a.textContent = text;
            a.title = text;

            a.addEventListener('click', function (e) {
                e.preventDefault();
                const target = docEl.querySelector('#' + anchorId);
                if (target && scrollPane) {
                    const targetTop = target.offsetTop - 20;
                    scrollPane.scrollTo({ top: targetTop, behavior: 'smooth' });
                }
            });

            li.appendChild(a);
            tocNav.appendChild(li);
            tocItems.push({ header: h, link: a });
        });

        if (tocCount) tocCount.textContent = `${tocItems.length} тем`;

        // 2. Scrollspy for Active TOC item
        if (scrollPane && tocItems.length > 0) {
            let ticking = false;
            scrollPane.addEventListener('scroll', function () {
                if (ticking) return;
                window.requestAnimationFrame(() => {
                    const scrollPos = scrollPane.scrollTop + 60;
                    let current = null;

                    for (let i = 0; i < tocItems.length; i++) {
                        if (tocItems[i].header.offsetTop <= scrollPos) {
                            current = tocItems[i];
                        } else {
                            break;
                        }
                    }

                    tocItems.forEach(item => {
                        if (current && item === current) {
                            item.link.classList.add('active');
                        } else {
                            item.link.classList.remove('active');
                        }
                    });
                    ticking = false;
                });
                ticking = true;
            });
        }

        // 3. Fix Image paths in report
        const inPages = window.location.pathname.includes('/pages/');
        docEl.querySelectorAll('img').forEach(img => {
            const src = img.getAttribute('src') || '';
            if (src.startsWith('../') && !inPages) {
                img.setAttribute('src', src.replace(/^\.\.\//, './'));
            } else if (src.startsWith('./') && inPages) {
                img.setAttribute('src', src.replace(/^\.\//, '../'));
            }
        });

        // 4. Wrap Tables in .table-responsive
        docEl.querySelectorAll('table').forEach(tbl => {
            if (tbl.closest('.table-responsive')) return;
            const wrap = document.createElement('div');
            wrap.className = 'table-responsive';
            tbl.parentNode.insertBefore(wrap, tbl);
            wrap.appendChild(tbl);
        });

        // 5. Code Copy Buttons inside Report
        if (typeof window.initCodeCopy === 'function') {
            window.initCodeCopy();
        }
    }

    /**
     * Initializes Global Link Interceptors for Reports
     */
    window.initReportLinks = function () {
        // Intercept any link matching report files
        document.addEventListener('click', function (e) {
            const link = e.target.closest('a');
            if (!link) return;

            const href = link.getAttribute('href') || '';
            const isReportLink = (
                href.includes('Lab1_report.md') ||
                href.includes('Lab2_report.md') ||
                href.includes('Lab3_report.md') ||
                link.hasAttribute('data-report-id')
            );

            if (isReportLink) {
                e.preventDefault();
                const reportId = link.getAttribute('data-report-id') || href.split('/').pop().split('?')[0].split('#')[0];
                window.openReportViewer(reportId);
            }
        });

        // Hash Navigation Hook (#report-lab1, #report-lab2, #report-lab3)
        function checkReportHash() {
            const hash = window.location.hash.toLowerCase();
            if (hash.startsWith('#report-') || hash.startsWith('#doc-')) {
                const id = hash.replace(/^#(report|doc)-/, '');
                window.openReportViewer(id);
            }
        }

        window.addEventListener('hashchange', checkReportHash);
        checkReportHash();
    };

    // Auto-initialize when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', window.initReportLinks);
    } else {
        window.initReportLinks();
    }

})();
