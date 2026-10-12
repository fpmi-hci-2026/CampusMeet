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
                mermaid.run({ nodes: Array.from(unrendered) });
            } catch (err) {
                console.warn('Mermaid rendering notice:', err);
            }
        }
    };

    /**
     * Core SPA Tab Router
     */
    window.switchTab = function (tabId, element) {
        const targetPane = document.getElementById(tabId);
        if (!targetPane) return;

        // Hide all tabs
        const panes = document.querySelectorAll('.tab-pane');
        panes.forEach(p => p.classList.remove('active'));

        // Show active tab
        targetPane.classList.add('active');

        // Update active navigation link in sidebar
        const links = document.querySelectorAll('.nav-link');
        links.forEach(l => l.classList.remove('active'));

        const activeLink = document.querySelector(`.nav-link[href="#${tabId}"]`) || (element && element.classList.contains('nav-link') ? element : null);
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
        }

        // Scroll to top
        const content = document.getElementById('content');
        if (window.innerWidth > 900 && content) {
            content.scrollTop = 0;
        } else {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        }

        // Close mobile drawer if open
        if (typeof window.closeMobileSidebar === 'function') {
            window.closeMobileSidebar();
        }

        // Render Mermaid on-demand for this pane
        window.renderTabMermaid(targetPane);
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
                const firstPane = document.querySelector('.tab-pane');
                if (firstPane) {
                    window.switchTab(firstPane.id);
                }
            }
        }

        window.addEventListener('hashchange', handleHash);
        handleHash();
    };
})();
