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
})();
