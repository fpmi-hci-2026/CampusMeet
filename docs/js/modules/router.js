/**
 * CampusMeet / EventHub — SPA Tab Router & Lazy Mermaid Engine
 */

(function () {
    'use strict';

    function getTitleMap() {
        return (window.CampusMeetData && window.CampusMeetData.titleMap) ? window.CampusMeetData.titleMap : {};
    }

    /**
     * Lazy Mermaid Rendering Engine
     * Prevents 0x0 size and layout distortion by rendering only when the container is visible
     */
    window.renderTabMermaid = function (pane) {
        if (typeof mermaid === 'undefined' || !pane) return;
        const unrendered = pane.querySelectorAll('.mermaid:not([data-processed="true"])');
        if (unrendered.length > 0) {
            try {
                const res = mermaid.run({ nodes: Array.from(unrendered) });
                if (res && typeof res.then === 'function') {
                    res.then(function () {
                        if (typeof window.enhanceDiagrams === 'function') {
                            window.enhanceDiagrams(pane);
                        }
                    }).catch(function () {
                        if (typeof window.enhanceDiagrams === 'function') {
                            window.enhanceDiagrams(pane);
                        }
                    });
                } else {
                    if (typeof window.enhanceDiagrams === 'function') {
                        window.enhanceDiagrams(pane);
                    }
                }
            } catch (err) {
                console.warn('Mermaid rendering notice:', err);
            }
        } else {
            if (typeof window.enhanceDiagrams === 'function') {
                window.enhanceDiagrams(pane);
            }
        }
    };

    /**
     * Core SPA Tab Router & Deep Linking Engine
     */
    window.switchTab = function (tabId, element) {
        let targetElem = document.getElementById(tabId);
        if (!targetElem) return;

        let targetPane = targetElem;
        let scrollToSubElement = false;

        if (!targetPane.classList.contains('tab-pane')) {
            const parentPane = targetPane.closest('.tab-pane');
            if (parentPane) {
                targetPane = parentPane;
                scrollToSubElement = true;
            } else {
                // Declarative pages use ordinary document sections, not SPA tabs.
                targetElem.scrollIntoView({ behavior: 'smooth', block: 'start' });
                if (typeof window.closeMobileSidebar === 'function') window.closeMobileSidebar();
                return;
            }
        }

        // Hide all tabs
        const panes = document.querySelectorAll('.tab-pane');
        panes.forEach(p => p.classList.remove('active'));

        // Show active tab
        targetPane.classList.add('active');

        // Update active in-page tab link in sidebar
        const tabLinks = document.querySelectorAll('.nav-menu a[href^="#"]');
        tabLinks.forEach(l => l.classList.remove('active'));

        const activeLink = document.querySelector(`.nav-menu a[href="#${tabId}"]`) ||
                           document.querySelector(`.nav-menu a[href="#${targetPane.id}"]`) ||
                           (element && element.classList.contains('nav-link') ? element : null);
        if (activeLink) {
            activeLink.classList.add('active');
        }

        // Update URL hash without breaking history
        if (window.location.hash !== `#${tabId}`) {
            history.pushState(null, '', `#${tabId}`);
        }

        // Update document title
        const titles = getTitleMap();
        if (titles[tabId]) {
            document.title = titles[tabId];
        } else if (titles[targetPane.id]) {
            document.title = titles[targetPane.id];
        }

        // Update dynamic breadcrumb leaf item
        const breadcrumbTab = document.getElementById('active-breadcrumb-tab');
        if (breadcrumbTab) {
            if (activeLink) {
                const clone = activeLink.cloneNode(true);
                const num = clone.querySelector('.nav-num');
                if (num) num.remove();
                const badge = clone.querySelector('.nav-badge');
                if (badge) badge.remove();
                const icon = clone.querySelector('.icon');
                if (icon) icon.remove();
                breadcrumbTab.textContent = clone.textContent.trim();
            } else if (titles[tabId] || titles[targetPane.id]) {
                const titleStr = titles[tabId] || titles[targetPane.id];
                const clean = titleStr.split('—')[0].replace(/^(Лаб\.\s*№\d+:|Wiki:)\s*/, '').trim();
                breadcrumbTab.textContent = clean;
            }
        }

        // Scroll to element or top
        if (scrollToSubElement && targetElem) {
            setTimeout(() => {
                targetElem.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }, 60);
        } else {
            const content = document.getElementById('content');
            if (window.innerWidth > 900 && content) {
                content.scrollTop = 0;
            } else {
                window.scrollTo({ top: 0, behavior: 'smooth' });
            }
        }

        // Close mobile drawer if open
        if (typeof window.closeMobileSidebar === 'function') {
            window.closeMobileSidebar();
        }

        // Render Mermaid on-demand for this pane
        window.renderTabMermaid(targetPane);

        // Enhance diagram viewers inside active pane
        if (typeof window.enhanceDiagrams === 'function') {
            window.enhanceDiagrams(targetPane);
        }
    };

    /**
     * URL Hash Router & Lifecycle Initialization
     */
    window.initRouter = function () {
        function handleHash() {
            const hash = window.location.hash.substring(1);
            if (hash && document.getElementById(hash)) {
                window.switchTab(hash);
            } else {
                const firstPane = document.querySelector('section.tab-pane');
                if (firstPane) {
                    window.switchTab(firstPane.id);
                }
            }
        }

        window.addEventListener('hashchange', handleHash);
        handleHash();
    };
})();
