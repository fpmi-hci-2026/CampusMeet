/**
 * CampusMeet / EventHub — App Shell Bootstrapper
 * Single-line script inclusion for rapid lab page authoring:
 * <script src="../js/app-shell.js" defer></script>
 */

(function () {
    'use strict';

    // Determine base path to docs/js/
    function getJsBasePath() {
        const currentScript = document.currentScript;
        if (currentScript && currentScript.src) {
            const src = currentScript.src;
            return src.substring(0, src.lastIndexOf('/') + 1);
        }
        const pathname = window.location.pathname || '';
        if (pathname.includes('/pages/')) {
            return '../js/';
        }
        return 'js/';
    }

    const basePath = getJsBasePath();

    const MODULES = [
        'vendor/marked.min.js',
        'data/navigation.js',
        'data/search.js',
        'data/reports.js',
        'modules/components.js',
        'modules/layout.js',
        'modules/renderers.js',
        'modules/router.js',
        'modules/lightbox.js',
        'modules/omnibox.js',
        'modules/report-viewer.js',
        'modules/ui.js',
        'main.js'
    ];

    /**
     * Sequentially loads modules to preserve strict dependency order
     */
    function loadNextModule(index) {
        if (index >= MODULES.length) {
            return;
        }

        const scriptSrc = basePath + MODULES[index];
        // Check if already present in DOM
        const existing = Array.from(document.querySelectorAll('script')).find(s => s.src && s.src.includes(MODULES[index]));
        if (existing) {
            loadNextModule(index + 1);
            return;
        }

        const script = document.createElement('script');
        script.src = scriptSrc;
        script.async = false;
        script.onload = function () {
            loadNextModule(index + 1);
        };
        script.onerror = function () {
            console.warn(`[AppShell] Notice: Failed to load ${scriptSrc}`);
            loadNextModule(index + 1);
        };
        document.head.appendChild(script);
    }

    loadNextModule(0);
})();
