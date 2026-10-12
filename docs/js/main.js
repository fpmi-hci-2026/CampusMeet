/**
 * CampusMeet / EventHub — Client-side Core Bootstrapper
 * Orchestrates modules on DOMContentLoaded with Monochrome Config
 */

(function () {
    'use strict';

    document.addEventListener('DOMContentLoaded', function () {
        // Safe mermaid initialization with strict monochrome theme
        // Safe mermaid initialization with strict monochrome theme
        if (typeof mermaid !== 'undefined') {
            const isLight = document.documentElement.getAttribute('data-theme') === 'light';
            mermaid.initialize({
                startOnLoad: false,
                theme: 'base',
                themeVariables: isLight ? {
                    darkMode: false,
                    background: '#ffffff',
                    mainBkg: '#ffffff',
                    nodeBorder: '#d4d4d4',
                    nodeTextColor: '#0d0d0d',
                    primaryColor: '#ffffff',
                    primaryTextColor: '#0d0d0d',
                    primaryBorderColor: '#0d0d0d',
                    lineColor: '#525252',
                    arrowheadColor: '#525252',
                    edgeLabelBackground: '#ffffff',
                    secondaryColor: '#f4f4f4',
                    secondaryTextColor: '#0d0d0d',
                    secondaryBorderColor: '#d4d4d4',
                    tertiaryColor: '#ffffff',
                    tertiaryTextColor: '#0d0d0d',
                    tertiaryBorderColor: '#d4d4d4',
                    clusterBkg: '#f9f9f9',
                    clusterBorder: '#d4d4d4',
                    fontFamily: '"Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif'
                } : {
                    darkMode: true,
                    background: '#171717',
                    mainBkg: '#212121',
                    nodeBorder: '#383838',
                    nodeTextColor: '#f4f4f4',
                    primaryColor: '#212121',
                    primaryTextColor: '#f4f4f4',
                    primaryBorderColor: '#383838',
                    lineColor: '#a1a1aa',
                    arrowheadColor: '#a1a1aa',
                    edgeLabelBackground: '#171717',
                    secondaryColor: '#262626',
                    secondaryTextColor: '#f4f4f4',
                    secondaryBorderColor: '#383838',
                    tertiaryColor: '#171717',
                    tertiaryTextColor: '#f4f4f4',
                    tertiaryBorderColor: '#383838',
                    clusterBkg: '#212121',
                    clusterBorder: '#383838',
                    fontFamily: '"Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif'
                }
            });
        }

        // Initialize modules in lifecycle order
        if (typeof window.initThemeToggle === 'function') {
            window.initThemeToggle();
        }
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
        if (typeof window.enhanceDiagrams === 'function') {
            window.enhanceDiagrams(document);
        }
        if (typeof window.initReportLinks === 'function') {
            window.initReportLinks();
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
