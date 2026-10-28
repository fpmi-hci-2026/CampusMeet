/**
 * CampusMeet / EventHub — Diagram Viewer & Lightbox Engine
 * Provides interactive pan-zoom frames, expand/collapse toggles,
 * and high-resolution modal inspection for PlantUML SVGs, Wireframes, and Mermaid diagrams.
 * Strictly adheres to docs/DESIGN_SYSTEM.md monochrome guidelines.
 */

(function () {
    'use strict';

    // Global Lightbox State
    let lbZoom = 1;
    let lbPanX = 0;
    let lbPanY = 0;

    function getActiveLightboxElement() {
        const img = document.getElementById('lightbox-img');
        const svg = document.getElementById('lightbox-svg');
        if (img && img.style.display !== 'none') return img;
        if (svg) return svg;
        return null;
    }

    function updateLightboxTransform() {
        const target = getActiveLightboxElement();
        if (!target) return;
        target.style.transform = `translate(${lbPanX}px, ${lbPanY}px) scale(${lbZoom})`;
        const badge = document.getElementById('lightbox-zoom-badge');
        if (badge) badge.textContent = `${Math.round(lbZoom * 100)}%`;
    }

    /**
     * Pan-Zoom Engine for viewports
     * Pinch / Ctrl+wheel zoom with native scrolling and no canvas dragging
     */
    function makePanZoomable(viewport, canvas, zoomBadge, options) {
        options = options || {};
        const minZoom = options.minZoom || 0.5;
        const maxZoom = options.maxZoom || 3.5;
        let zoom = 1;
        let panX = 0;
        let panY = 0;

        function applyTransform() {
            canvas.style.transform = `translate(${panX}px, ${panY}px) scale(${zoom})`;
            if (zoomBadge) zoomBadge.textContent = `${Math.round(zoom * 100)}%`;
        }

        function setZoom(newZoom) {
            zoom = Math.min(Math.max(newZoom, minZoom), maxZoom);
            applyTransform();
        }

        function reset() {
            zoom = 1;
            panX = 0;
            panY = 0;
            viewport.scrollTop = viewport.scrollLeft = 0;
            applyTransform();
        }

        const gestures = window.CampusMeetDiagramGestures.bind(viewport, {
            getZoom: function () { return zoom; },
            setZoom: setZoom
        });

        return {
            setZoom: setZoom,
            reset: reset,
            getZoom: function () { return zoom; },
            hasMoved: gestures.hasMoved
        };
    }

    /**
     * Extracts readable title from diagram element context
     */
    function extractTitle(el) {
        if (el.dataset && el.dataset.title) return el.dataset.title;

        // Check previous headings
        let prev = el.previousElementSibling;
        while (prev) {
            if (/^H[2-5]$/i.test(prev.tagName)) {
                return prev.textContent.trim().replace(/^[\d.]+\s*/, '');
            }
            prev = prev.previousElementSibling;
        }

        // Check parent's preceding headings
        const parent = el.parentElement;
        if (parent && parent !== document.body) {
            let pPrev = parent.previousElementSibling;
            while (pPrev) {
                if (/^H[2-5]$/i.test(pPrev.tagName)) {
                    return pPrev.textContent.trim().replace(/^[\d.]+\s*/, '');
                }
                pPrev = pPrev.previousElementSibling;
            }
            const childHeading = parent.querySelector('h2, h3, h4');
            if (childHeading && childHeading !== el) {
                return childHeading.textContent.trim().replace(/^[\d.]+\s*/, '');
            }
        }

        if (el.tagName === 'IMG' && el.alt && !/^диаграмма|схема$/i.test(el.alt)) {
            return el.alt;
        }

        return 'Архитектурная схема';
    }

    /**
     * Extracts badge format string
     */
    function extractBadge(el) {
        if (el.tagName === 'IMG') {
            const src = el.src || '';
            if (src.includes('wireframe')) return 'Wireframe • SVG';
            if (src.includes('mockup')) return 'Mockup • SVG';
            if (src.includes('c4')) return 'C4 Model • SVG';
            if (src.includes('puml') || src.includes('diagrams')) return 'PlantUML • SVG';
            return 'Векторная схема';
        } else {
            const text = (el.textContent || '').trim();
            if (text.includes('sequenceDiagram')) return 'Mermaid • Sequence';
            if (text.includes('graph TD') || text.includes('flowchart TD')) return 'Mermaid • Flowchart';
            if (text.includes('graph LR') || text.includes('flowchart LR')) return 'Mermaid • Flowchart';
            return 'Mermaid • Схема';
        }
    }

    /**
     * Global Lightbox Modal Controller
     */
    window.openLightbox = function (target, title, badge, type) {
        const dialog = document.getElementById('lightbox-dialog');
        const img = document.getElementById('lightbox-img');
        const titleEl = document.getElementById('lightbox-title');
        const badgeEl = document.getElementById('lightbox-badge');
        const openTabLink = document.getElementById('lightbox-open-link');
        const body = document.querySelector('.lightbox-body');
        if (!dialog || !body) return;

        // Reset transforms
        lbZoom = 1;
        lbPanX = 0;
        lbPanY = 0;
        body.scrollTop = body.scrollLeft = 0;

        // Set Title & Badge
        if (titleEl) titleEl.textContent = title || 'Просмотр схемы';
        if (badgeEl) badgeEl.textContent = badge || 'SVG';

        // Clear previous cloned SVGs and wrappers
        const oldWrap = document.getElementById('lightbox-svg-wrap');
        if (oldWrap) oldWrap.remove();
        const oldSvg = document.getElementById('lightbox-svg');
        if (oldSvg) oldSvg.remove();

        if (type === 'mermaid' || (target && target.tagName === 'svg')) {
            const svgSource = target.tagName === 'svg' ? target : (target.querySelector('svg') || target);
            if (svgSource && svgSource.tagName === 'svg') {
                const originalId = svgSource.id;
                const cloned = svgSource.cloneNode(true);
                cloned.id = 'lightbox-svg';
                cloned.classList.add('lightbox-svg-content');
                if (originalId) {
                    cloned.querySelectorAll('style').forEach(st => {
                        st.textContent = st.textContent.replaceAll(originalId, 'lightbox-svg');
                    });
                }
                cloned.style.maxWidth = '95%';
                cloned.style.maxHeight = '95%';
                cloned.style.transform = `translate(0px, 0px) scale(1)`;
                if (img) img.style.display = 'none';

                const wrap = document.createElement('div');
                wrap.id = 'lightbox-svg-wrap';
                wrap.className = 'mermaid-lightbox-wrap mermaid';
                wrap.style.cssText = 'display:flex;align-items:center;justify-content:center;width:100%;height:100%;pointer-events:none;background:transparent;';
                wrap.appendChild(cloned);
                body.appendChild(wrap);

                if (openTabLink) openTabLink.style.display = 'none';
            }
        } else {
            const src = typeof target === 'string' ? target : (target ? target.src : '');
            if (img && src) {
                img.style.display = 'block';
                img.src = src;
                img.alt = title || 'Диаграмма';
                img.style.transform = `translate(0px, 0px) scale(1)`;
                if (src.includes('mockup') || src.includes('wireframe')) {
                    img.classList.add('dark-render');
                } else {
                    img.classList.remove('dark-render');
                }
                if (openTabLink) {
                    openTabLink.href = src;
                    openTabLink.style.display = 'inline-flex';
                }
            }
        }

        updateLightboxTransform();
        if (typeof dialog.showModal === 'function') {
            dialog.showModal();
        }
    };

    /**
     * Diagram Auto-Enhancer
     * Wraps raw diagram images and Mermaid blocks in interactive frames
     */
    window.enhanceDiagrams = function (root) {
        const container = root || document;

        // 1. Target Images (PlantUML, Wireframes, Mockups)
        const images = container.querySelectorAll('img');
        images.forEach(function (img) {
            // Filter only technical diagrams and mockups
            const src = img.getAttribute('src') || '';
            const isDiagram = src.includes('diagrams/') ||
                              src.includes('wireframes/') ||
                              src.includes('mockups/') ||
                              img.classList.contains('diagram-img');
            const isAvatar = img.classList.contains('persona-avatar') || img.classList.contains('brand-logo');

            if (!isDiagram || isAvatar || img.closest('.diagram-card')) return;

            const title = extractTitle(img);
            const badge = extractBadge(img);

            // Create Diagram Card Structure
            const card = document.createElement('div');
            card.className = 'diagram-card';
            card.setAttribute('data-diagram-title', title);

            // Header Bar
            const header = document.createElement('div');
            header.className = 'diagram-card-header';
            header.innerHTML = `
                <div class="diagram-card-meta">
                    <svg class="diagram-card-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12 2 2 7 12 12 22 7 12 2"></polygon><polyline points="2 17 12 22 22 17"></polyline><polyline points="2 12 12 17 22 12"></polyline></svg>
                    <span class="diagram-card-title" title="${title}">${title}</span>
                    <span class="diagram-card-badge">${badge}</span>
                </div>
                <div class="diagram-card-toolbar">
                    <button type="button" class="diagram-btn" data-action="zoom-out" title="Уменьшить (−)">−</button>
                    <span class="diagram-zoom-badge">100%</span>
                    <button type="button" class="diagram-btn" data-action="zoom-in" title="Увеличить (+)">+</button>
                    <button type="button" class="diagram-btn" data-action="zoom-reset" title="Сбросить (1:1)">1:1</button>
                    <button type="button" class="diagram-btn" data-action="toggle-collapse" title="Свернуть диаграмму"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="4 14 10 14 10 20"></polyline><polyline points="20 10 14 10 14 4"></polyline><line x1="14" y1="10" x2="21" y2="3"></line><line x1="3" y1="21" x2="10" y2="14"></line></svg></button>
                    <button type="button" class="diagram-btn" data-action="fullscreen" title="Во весь экран"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M8 3H5a2 2 0 0 0-2 2v3m18 0V5a2 2 0 0 0-2-2h-3m0 18h3a2 2 0 0 0 2-2v-3M3 16v3a2 2 0 0 0 2 2h3"></path></svg></button>
                    <a href="${src}" target="_blank" rel="noopener noreferrer" class="diagram-btn" title="В новой вкладке"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path><polyline points="15 3 21 3 21 9"></polyline><line x1="10" y1="14" x2="21" y2="3"></line></svg></a>
                </div>
            `;

            // Viewport & Canvas
            const viewport = document.createElement('div');
            viewport.className = 'diagram-viewport';
            viewport.tabIndex = 0;
            viewport.setAttribute('aria-label', 'Диаграмма: ' + title);

            const canvas = document.createElement('div');
            canvas.className = 'diagram-canvas';

            // Collapsed Banner
            const banner = document.createElement('div');
            banner.className = 'diagram-collapsed-banner';
            banner.innerHTML = `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="15 3 21 3 21 9"></polyline><polyline points="9 21 3 21 3 15"></polyline><line x1="21" y1="3" x2="14" y2="10"></line><line x1="3" y1="21" x2="10" y2="14"></line></svg><span>Схема свёрнута • Нажмите, чтобы развернуть</span>`;

            // Floating Hint
            const hint = document.createElement('div');
            hint.className = 'diagram-hint-overlay';
            hint.textContent = 'Перетаскивание мышью: панорамирование • + / − или Ctrl + колесо: масштаб • Клик: во весь экран';

            // Insert Card into DOM
            img.parentNode.insertBefore(card, img);
            card.appendChild(header);
            card.appendChild(viewport);
            viewport.appendChild(canvas);
            viewport.appendChild(banner);
            viewport.appendChild(hint);
            canvas.appendChild(img);
            img.style.maxWidth = 'none';
            img.style.width = 'auto';

            // Hook Pan-Zoom Engine
            const zoomBadge = header.querySelector('.diagram-zoom-badge');
            const pz = makePanZoomable(viewport, canvas, zoomBadge, { minZoom: 0.5, maxZoom: 3.0 });

            // Hook Toolbar Actions safely
            function bindBtn(sel, handler) {
                const btn = header.querySelector(sel);
                if (btn) btn.addEventListener('click', handler);
            }
            bindBtn('[data-action="zoom-in"]', () => pz.setZoom(pz.getZoom() * 1.25));
            bindBtn('[data-action="zoom-out"]', () => pz.setZoom(pz.getZoom() / 1.25));
            bindBtn('[data-action="zoom-reset"]', () => pz.reset());
            bindBtn('[data-action="fullscreen"]', () => window.openLightbox(img, title, badge, 'image'));

            const key = src.split('diagrams/')[1]?.split(/[?#]/)[0];
            const pages = key && window.CampusMeetDiagramPages?.[key];
            if (pages && pages.length > 1) {
                const originalUrl = img.src;
                const pager = document.createElement('nav');
                pager.className = 'diagram-pages';
                pager.setAttribute('aria-label', 'Фрагменты диаграммы');
                const previous = document.createElement('button');
                const next = document.createElement('button');
                const select = document.createElement('select');
                previous.type = next.type = 'button';
                previous.textContent = '←';
                next.textContent = '→';
                previous.setAttribute('aria-label', 'Предыдущий фрагмент');
                next.setAttribute('aria-label', 'Следующий фрагмент');
                select.setAttribute('aria-label', 'Выбрать фрагмент');
                pages.forEach((page, index) => select.add(new Option(page.label, String(index))));
                const hint = document.createElement('span');
                hint.textContent = 'Масштаб 1:1 · прокрутка внутри схемы';
                let active = 0;
                function showPage(index) {
                    active = Math.max(0, Math.min(index, pages.length - 1));
                    img.src = new URL(pages[active].file, originalUrl).href;
                    select.value = String(active);
                    previous.disabled = active === 0;
                    next.disabled = active === pages.length - 1;
                    viewport.scrollTop = viewport.scrollLeft = 0;
                    pz.reset();
                }
                previous.addEventListener('click', () => showPage(active - 1));
                next.addEventListener('click', () => showPage(active + 1));
                select.addEventListener('change', () => showPage(Number(select.value)));
                pager.append(previous, select, next, hint);
                card.insertBefore(pager, viewport);
                showPage(0);
            }

            // Hook Collapse Toggle
            const btnCollapse = header.querySelector('[data-action="toggle-collapse"]');
            function toggleCardCollapse() {
                card.classList.toggle('is-collapsed');
                const isCol = card.classList.contains('is-collapsed');
                if (btnCollapse) {
                    btnCollapse.setAttribute('title', isCol ? 'Развернуть диаграмму' : 'Свернуть диаграмму');
                    btnCollapse.classList.toggle('active', isCol);
                }
            }

            if (btnCollapse) btnCollapse.addEventListener('click', toggleCardCollapse);
            banner.addEventListener('click', toggleCardCollapse);

            // Viewport Click Opens Lightbox (only if not dragged and not collapsed)
            viewport.addEventListener('click', function (e) {
                if (card.classList.contains('is-collapsed')) return;
                if (e.target.closest('.diagram-card-toolbar') || e.target.closest('.diagram-btn')) return;
                if (!pz.hasMoved()) {
                    window.openLightbox(img, title, badge, 'image');
                }
            });
        });

        // 2. Target Mermaid Diagram Blocks
        const mermaids = container.querySelectorAll('.mermaid');
        mermaids.forEach(function (m) {
            const renderedSvg = m.querySelector('svg');
            if (renderedSvg && renderedSvg.viewBox && renderedSvg.viewBox.baseVal.width) {
                const bounds = renderedSvg.viewBox.baseVal;
                renderedSvg.style.maxWidth = 'none';
                renderedSvg.style.width = bounds.width + 'px';
                renderedSvg.style.height = bounds.height + 'px';
            }
            if (m.closest('.diagram-card')) return;

            const title = extractTitle(m);
            const badge = extractBadge(m);

            const card = document.createElement('div');
            card.className = 'diagram-card';
            card.setAttribute('data-diagram-title', title);

            const header = document.createElement('div');
            header.className = 'diagram-card-header';
            header.innerHTML = `
                <div class="diagram-card-meta">
                    <svg class="diagram-card-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12 2 2 7 12 12 22 7 12 2"></polygon><polyline points="2 17 12 22 22 17"></polyline><polyline points="2 12 12 17 22 12"></polyline></svg>
                    <span class="diagram-card-title" title="${title}">${title}</span>
                    <span class="diagram-card-badge">${badge}</span>
                </div>
                <div class="diagram-card-toolbar">
                    <button type="button" class="diagram-btn" data-action="zoom-out" title="Уменьшить (−)">−</button>
                    <span class="diagram-zoom-badge">100%</span>
                    <button type="button" class="diagram-btn" data-action="zoom-in" title="Увеличить (+)">+</button>
                    <button type="button" class="diagram-btn" data-action="zoom-reset" title="Сбросить (1:1)">1:1</button>
                    <button type="button" class="diagram-btn" data-action="toggle-collapse" title="Свернуть диаграмму"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="4 14 10 14 10 20"></polyline><polyline points="20 10 14 10 14 4"></polyline><line x1="14" y1="10" x2="21" y2="3"></line><line x1="3" y1="21" x2="10" y2="14"></line></svg></button>
                    <button type="button" class="diagram-btn" data-action="fullscreen" title="Во весь экран"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M8 3H5a2 2 0 0 0-2 2v3m18 0V5a2 2 0 0 0-2-2h-3m0 18h3a2 2 0 0 0 2-2v-3M3 16v3a2 2 0 0 0 2 2h3"></path></svg></button>
                </div>
            `;

            const viewport = document.createElement('div');
            viewport.className = 'diagram-viewport';

            const canvas = document.createElement('div');
            canvas.className = 'diagram-canvas';

            const banner = document.createElement('div');
            banner.className = 'diagram-collapsed-banner';
            banner.innerHTML = `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="15 3 21 3 21 9"></polyline><polyline points="9 21 3 21 3 15"></polyline><line x1="21" y1="3" x2="14" y2="10"></line><line x1="3" y1="21" x2="10" y2="14"></line></svg><span>Схема свёрнута • Нажмите, чтобы развернуть</span>`;

            const hint = document.createElement('div');
            hint.className = 'diagram-hint-overlay';
            hint.textContent = 'Перетаскивание мышью: панорамирование • + / − или Ctrl + колесо: масштаб • Клик: во весь экран';

            m.parentNode.insertBefore(card, m);
            card.appendChild(header);
            card.appendChild(viewport);
            viewport.appendChild(canvas);
            viewport.appendChild(banner);
            viewport.appendChild(hint);
            canvas.appendChild(m);

            const zoomBadge = header.querySelector('.diagram-zoom-badge');
            const pz = makePanZoomable(viewport, canvas, zoomBadge, { minZoom: 0.5, maxZoom: 3.0 });

            function bindMermaidBtn(sel, handler) {
                const btn = header.querySelector(sel);
                if (btn) btn.addEventListener('click', handler);
            }
            bindMermaidBtn('[data-action="zoom-in"]', () => pz.setZoom(pz.getZoom() * 1.25));
            bindMermaidBtn('[data-action="zoom-out"]', () => pz.setZoom(pz.getZoom() / 1.25));
            bindMermaidBtn('[data-action="zoom-reset"]', () => pz.reset());
            bindMermaidBtn('[data-action="fullscreen"]', () => window.openLightbox(m, title, badge, 'mermaid'));

            viewport.addEventListener('click', function (e) {
                if (card.classList.contains('is-collapsed')) return;
                if (e.target.closest('.diagram-card-toolbar') || e.target.closest('.diagram-btn')) return;
                if (!pz.hasMoved()) {
                    window.openLightbox(m, title, badge, 'mermaid');
                }
            });
        });
    };

    /**
     * Initializes global lightbox listeners & enhances diagrams
     */
    window.initLightbox = function () {
        const dialog = document.getElementById('lightbox-dialog');
        const body = document.querySelector('.lightbox-body');
        if (!dialog || !body) return;

        // Zoom Controls
        const zoomInBtn = document.getElementById('lightbox-zoom-in');
        const zoomOutBtn = document.getElementById('lightbox-zoom-out');
        const zoomResetBtn = document.getElementById('lightbox-zoom-reset');
        const fitBtn = document.getElementById('lightbox-fit-btn');
        const closeBtn = document.getElementById('lightbox-close');

        if (zoomInBtn) {
            zoomInBtn.addEventListener('click', () => {
                lbZoom = Math.min(lbZoom * 1.25, 4.5);
                updateLightboxTransform();
            });
        }

        if (zoomOutBtn) {
            zoomOutBtn.addEventListener('click', () => {
                lbZoom = Math.max(lbZoom / 1.25, 0.3);
                updateLightboxTransform();
            });
        }

        if (zoomResetBtn) {
            zoomResetBtn.addEventListener('click', () => {
                lbZoom = 1;
                lbPanX = 0;
                lbPanY = 0;
                body.scrollTop = body.scrollLeft = 0;
                updateLightboxTransform();
            });
        }

        if (fitBtn) {
            fitBtn.addEventListener('click', () => {
                const target = getActiveLightboxElement();
                lbZoom = target ? Math.min(1, (body.clientWidth-48)/target.clientWidth, (body.clientHeight-48)/target.clientHeight) : 1;
                lbPanX = 0;
                lbPanY = 0;
                body.scrollTop = body.scrollLeft = 0;
                updateLightboxTransform();
            });
        }

        if (closeBtn) {
            closeBtn.addEventListener('click', () => dialog.close());
        }

        // Close on backdrop click
        dialog.addEventListener('click', function (e) {
            if (e.target === dialog) dialog.close();
        });

        window.CampusMeetDiagramGestures.bind(body, {
            getZoom: function () { return lbZoom; },
            setZoom: function (value) {
                lbZoom = Math.min(Math.max(value, 0.3), 4.5);
                updateLightboxTransform();
            }
        });

        // Keyboard Shortcuts
        document.addEventListener('keydown', function (e) {
            if (!dialog.open) return;
            if (e.key === 'Escape') {
                dialog.close();
            } else if (e.key === '0') {
                lbZoom = 1;
                lbPanX = 0;
                lbPanY = 0;
                updateLightboxTransform();
            }
        });

        // Run diagram enhancement across the document
        window.enhanceDiagrams(document);
    };
})();
