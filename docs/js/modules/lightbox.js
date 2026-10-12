/**
 * CampusMeet / EventHub — Diagram Lightbox & Zoom Controller
 */

(function () {
    'use strict';

    let currentZoom = 1;

    window.initLightbox = function () {
        const dialog = document.getElementById('lightbox-dialog');
        const img = document.getElementById('lightbox-img');
        const title = document.getElementById('lightbox-title');
        const openTabLink = document.getElementById('lightbox-open-link');
        if (!dialog || !img) return;

        // Delegated click handler on diagrams & mockups
        document.addEventListener('click', function (e) {
            const targetImg = e.target.closest('.diagram-img, .profile-card img, .hero-card img');
            // Exclude avatar images
            if (targetImg && !targetImg.classList.contains('persona-avatar')) {
                currentZoom = 1;
                img.style.transform = `scale(${currentZoom})`;
                img.src = targetImg.src;
                img.alt = targetImg.alt || 'Диаграмма';
                
                if (targetImg.src.includes('mockup') || targetImg.src.includes('wireframe')) {
                    img.classList.add('dark-render');
                } else {
                    img.classList.remove('dark-render');
                }

                if (title) title.textContent = targetImg.alt || 'Просмотр схемы';
                if (openTabLink) openTabLink.href = targetImg.src;

                dialog.showModal();
            }
        });

        // Zoom Controls
        const zoomInBtn = document.getElementById('lightbox-zoom-in');
        const zoomOutBtn = document.getElementById('lightbox-zoom-out');
        const zoomResetBtn = document.getElementById('lightbox-zoom-reset');
        const closeBtn = document.getElementById('lightbox-close');

        if (zoomInBtn) {
            zoomInBtn.addEventListener('click', () => {
                currentZoom = Math.min(currentZoom + 0.25, 3.5);
                img.style.transform = `scale(${currentZoom})`;
            });
        }

        if (zoomOutBtn) {
            zoomOutBtn.addEventListener('click', () => {
                currentZoom = Math.max(currentZoom - 0.25, 0.5);
                img.style.transform = `scale(${currentZoom})`;
            });
        }

        if (zoomResetBtn) {
            zoomResetBtn.addEventListener('click', () => {
                currentZoom = 1;
                img.style.transform = `scale(1)`;
            });
        }

        if (closeBtn) {
            closeBtn.addEventListener('click', () => dialog.close());
        }

        dialog.addEventListener('click', (e) => {
            if (e.target === dialog) dialog.close();
        });
    };
})();
