/**
 * CampusMeet / EventHub — Omnibox Quick Search (⌘K / Ctrl+K)
 */

(function () {
    'use strict';

    function getSearchRegistry() {
        return (window.CampusMeetData && window.CampusMeetData.searchRegistry) ? window.CampusMeetData.searchRegistry : [];
    }

    window.initOmnibox = function () {
        const dialog = document.getElementById('omnibox-dialog');
        const input = document.getElementById('omnibox-input');
        const resultsList = document.getElementById('omnibox-results');
        const triggers = document.querySelectorAll('.omnibox-trigger-btn');
        if (!dialog || !input || !resultsList) return;

        function openOmnibox() {
            const registry = getSearchRegistry();
            input.value = '';
            renderResults(registry.slice(0, 7));
            dialog.showModal();
            setTimeout(() => input.focus(), 50);
        }

        triggers.forEach(btn => btn.addEventListener('click', openOmnibox));

        // Keyboard Shortcut: ⌘K or Ctrl+K
        document.addEventListener('keydown', function (e) {
            if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === 'k') {
                e.preventDefault();
                if (dialog.open) {
                    dialog.close();
                } else {
                    openOmnibox();
                }
            }
        });

        function renderResults(items) {
            resultsList.innerHTML = '';
            if (items.length === 0) {
                resultsList.innerHTML = '<li class="omnibox-empty">Ничего не найдено по вашему запросу</li>';
                return;
            }

            items.forEach((item, index) => {
                const li = document.createElement('li');
                li.className = 'omnibox-item' + (index === 0 ? ' selected' : '');
                li.innerHTML = `
                    <span class="omnibox-item-title">${item.title}</span>
                    <span class="omnibox-item-meta">${item.category}</span>
                `;
                li.addEventListener('click', () => {
                    dialog.close();
                    if (item.url) {
                        const parts = item.url.split('#');
                        const targetPath = parts[0];
                        const targetHash = parts[1];
                        const currentPath = window.location.pathname || '';
                        const currentPage = currentPath.split('/').pop() || 'index.html';
                        const inPages = currentPath.includes('/pages/') || (!currentPath.endsWith('index.html') && currentPath.includes('/pages'));
                        const targetFile = targetPath.split('/').pop();

                        if (currentPage === targetFile || (currentPage === '' && targetFile === 'index.html')) {
                            if (targetHash && typeof window.switchTab === 'function') {
                                window.switchTab(targetHash);
                            } else {
                                window.scrollTo({ top: 0, behavior: 'smooth' });
                            }
                        } else {
                            let finalUrl = item.url;
                            if (inPages) {
                                if (targetFile === 'index.html') {
                                    finalUrl = '../' + targetFile + (targetHash ? '#' + targetHash : '');
                                } else {
                                    finalUrl = targetFile + (targetHash ? '#' + targetHash : '');
                                }
                            } else {
                                finalUrl = item.url;
                            }
                            window.location.href = finalUrl;
                        }
                    } else if (typeof window.switchTab === 'function') {
                        window.switchTab(item.id);
                    }
                });
                resultsList.appendChild(li);
            });
        }

        input.addEventListener('input', function () {
            const query = input.value.trim().toLowerCase();
            const registry = getSearchRegistry();
            if (!query) {
                renderResults(registry.slice(0, 7));
                return;
            }

            const filtered = registry.filter(item => {
                return item.title.toLowerCase().includes(query) ||
                    item.category.toLowerCase().includes(query) ||
                    item.keywords.toLowerCase().includes(query);
            });

            renderResults(filtered);
        });

        // Close on backdrop click
        dialog.addEventListener('click', (e) => {
            if (e.target === dialog) dialog.close();
        });
    };
})();
