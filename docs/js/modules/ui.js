/**
 * CampusMeet / EventHub — Mobile Drawer & Code Copy Helpers
 */

(function () {
    'use strict';

    window.openMobileSidebar = function () {
        const sidebar = document.getElementById('sidebar');
        const backdrop = document.getElementById('sidebar-backdrop');
        if (sidebar) sidebar.classList.add('open');
        if (backdrop) backdrop.classList.add('active');
    };

    window.closeMobileSidebar = function () {
        const sidebar = document.getElementById('sidebar');
        const backdrop = document.getElementById('sidebar-backdrop');
        if (sidebar) sidebar.classList.remove('open');
        if (backdrop) backdrop.classList.remove('active');
    };

    window.initCodeCopy = function () {
        document.querySelectorAll('pre').forEach(pre => {
            if (pre.querySelector('.code-copy-btn')) return;

            const btn = document.createElement('button');
            btn.className = 'code-copy-btn';
            btn.textContent = 'Копировать';

            btn.addEventListener('click', async () => {
                const code = pre.querySelector('code') || pre;
                const text = code.innerText;
                try {
                    await navigator.clipboard.writeText(text);
                    btn.textContent = 'Скопировано!';
                    setTimeout(() => { btn.textContent = 'Копировать'; }, 2000);
                } catch (err) {
                    btn.textContent = 'Ошибка';
                }
            });

            pre.appendChild(btn);
        });
    };

    window.initThemeToggle = function () {
        function getStoredTheme() {
            try {
                return localStorage.getItem('cm_theme');
            } catch (e) {
                return null;
            }
        }

        function applyTheme(theme) {
            document.documentElement.setAttribute('data-theme', theme);
            try {
                localStorage.setItem('cm_theme', theme);
            } catch (e) {}

            document.querySelectorAll('.theme-toggle-btn').forEach(btn => {
                const isDark = theme === 'dark';
                btn.setAttribute('aria-label', isDark ? 'Переключить на светлую тему' : 'Переключить на темную тему');
                btn.setAttribute('title', isDark ? 'Светлая тема' : 'Темная тема');
            });

            if (typeof mermaid !== 'undefined') {
                const isLight = theme === 'light';
                try {
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
                } catch (e) {}
            }
        }

        // Attach event listeners to all theme toggle buttons (desktop sidebar, mobile topbar, etc.)
        document.querySelectorAll('.theme-toggle-btn').forEach(btn => {
            btn.addEventListener('click', function () {
                const current = document.documentElement.getAttribute('data-theme') || 'dark';
                const nextTheme = current === 'dark' ? 'light' : 'dark';
                applyTheme(nextTheme);
            });
        });

        // Initialize state
        const initial = document.documentElement.getAttribute('data-theme') || getStoredTheme() || 'dark';
        applyTheme(initial);
    };
})();
