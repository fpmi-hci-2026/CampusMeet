/**
 * CampusMeet / EventHub — Client-side Core Bootstrapper
 * Orchestrates modules on DOMContentLoaded
 */

(function () {
    'use strict';

    document.addEventListener('DOMContentLoaded', function () {
        // Safe mermaid initialization with dark theme
        if (typeof mermaid !== 'undefined') {
            mermaid.initialize({
                startOnLoad: false,
                theme: 'dark',
                themeVariables: {
                    darkMode: true,
                    background: '#131c31',
                    primaryColor: '#1e293b',
                    primaryTextColor: '#f8fafc',
                    primaryBorderColor: '#38bdf8',
                    lineColor: '#94a3b8',
                    secondaryColor: '#182238',
                    tertiaryColor: '#0b1120'
                }
            });
        }

        // Initialize modules in lifecycle order
        if (typeof window.initDynamicComponents === 'function') {
            window.initDynamicComponents();
        }
        if (typeof window.initLightbox === 'function') {
            window.initLightbox();
        }
        if (typeof window.initOmnibox === 'function') {
            window.initOmnibox();
        }
        if (typeof window.initCodeCopy === 'function') {
            window.initCodeCopy();
        }
        if (typeof window.initRouter === 'function') {
            window.initRouter();
        }

        // Mobile drawer toggles
        const hamburgerBtn = document.getElementById('mobile-hamburger');
        const backdrop = document.getElementById('sidebar-backdrop');
        if (hamburgerBtn && typeof window.openMobileSidebar === 'function') {
            hamburgerBtn.addEventListener('click', window.openMobileSidebar);
        }
        if (backdrop && typeof window.closeMobileSidebar === 'function') {
            backdrop.addEventListener('click', window.closeMobileSidebar);
        }
    });
})();
