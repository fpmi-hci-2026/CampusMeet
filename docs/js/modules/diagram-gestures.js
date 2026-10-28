/**
 * CampusMeet / EventHub — Diagram Gestures Engine
 * Provides natural mouse drag-to-pan, pinch-to-zoom, and trackpad gestures.
 * Allows effortless inspection of wide/tall PlantUML, Mermaid, and vector diagrams.
 */
(function (root, factory) {
    if (typeof module === 'object' && module.exports) module.exports = factory();
    else root.CampusMeetDiagramGestures = factory();
}(typeof window !== 'undefined' ? window : globalThis, function () {
    'use strict';

    function distance(touches) {
        return Math.hypot(touches[0].clientX - touches[1].clientX, touches[0].clientY - touches[1].clientY);
    }

    function bind(surface, controller) {
        let pinch = null;
        let safariZoom = null;
        let firstTouch = null;
        let moved = false;

        // Mouse Drag-to-Pan state
        let isDragging = false;
        let dragStartX = 0;
        let dragStartY = 0;
        let startScrollLeft = 0;
        let startScrollTop = 0;

        // Pointer down: initiate drag-to-pan for mouse left-click
        surface.addEventListener('pointerdown', function (event) {
            // Ignore if clicking on interactive controls (buttons, links, inputs)
            if (event && event.target && event.target.closest && event.target.closest('button, a, select, input, textarea, .diagram-btn, .lightbox-btn')) {
                return;
            }

            moved = false;

            // Left mouse button or pen
            if (event && event.pointerType === 'mouse' && event.button !== 0) return;

            isDragging = true;
            dragStartX = event ? (event.clientX || 0) : 0;
            dragStartY = event ? (event.clientY || 0) : 0;
            startScrollLeft = surface.scrollLeft || 0;
            startScrollTop = surface.scrollTop || 0;

            if (surface.classList) surface.classList.add('is-panning');
            try {
                if (surface.setPointerCapture && event && event.pointerId) {
                    surface.setPointerCapture(event.pointerId);
                }
            } catch (err) {
                // Ignore if pointer capture is not supported
            }
        });

        surface.addEventListener('pointermove', function (event) {
            if (!isDragging || !event) return;

            const dx = (event.clientX || 0) - dragStartX;
            const dy = (event.clientY || 0) - dragStartY;

            if (Math.hypot(dx, dy) > 5) {
                moved = true;
            }

            surface.scrollLeft = startScrollLeft - dx;
            surface.scrollTop = startScrollTop - dy;
            if (typeof event.preventDefault === 'function') {
                event.preventDefault();
            }
        });

        function endDrag(event) {
            if (!isDragging) return;
            isDragging = false;
            if (surface.classList) surface.classList.remove('is-panning');
            try {
                if (event && event.pointerId && surface.hasPointerCapture && surface.hasPointerCapture(event.pointerId)) {
                    surface.releasePointerCapture(event.pointerId);
                }
            } catch (err) {}
        }

        surface.addEventListener('pointerup', endDrag);
        surface.addEventListener('pointercancel', endDrag);

        // Native scroll events mark moved so accidental clicks are suppressed
        surface.addEventListener('scroll', function () {
            moved = true;
        }, { passive: true });

        // Ctrl + Wheel (or trackpad pinch) zooms the diagram
        surface.addEventListener('wheel', function (event) {
            if (!event || !event.ctrlKey) return;
            event.preventDefault();
            moved = true;
            const delta = event.deltaY * (event.deltaMode === 1 ? 16 : event.deltaMode === 2 ? surface.clientHeight : 1);
            if (controller && typeof controller.setZoom === 'function' && typeof controller.getZoom === 'function') {
                controller.setZoom(controller.getZoom() * Math.exp(-delta * 0.002));
            }
        }, { passive: false });

        // Touch Pinch-to-Zoom
        surface.addEventListener('touchstart', function (event) {
            if (event.touches.length === 2) {
                event.preventDefault();
                moved = true;
                firstTouch = null;
                if (controller && typeof controller.getZoom === 'function') {
                    pinch = { distance: distance(event.touches), zoom: controller.getZoom() };
                }
            } else if (event.touches.length === 1) {
                pinch = null;
                firstTouch = [event.touches[0].clientX, event.touches[0].clientY];
                moved = false;
            }
        }, { passive: false });

        surface.addEventListener('touchmove', function (event) {
            if (pinch && event.touches.length === 2) {
                event.preventDefault();
                moved = true;
                if (pinch.distance > 0 && controller && typeof controller.setZoom === 'function') {
                    controller.setZoom(pinch.zoom * distance(event.touches) / pinch.distance);
                }
            } else if (firstTouch && event.touches.length === 1) {
                if (Math.hypot(event.touches[0].clientX - firstTouch[0], event.touches[0].clientY - firstTouch[1]) > 6) {
                    moved = true;
                }
            }
        }, { passive: false });

        function endTouch(event) {
            if (event.touches.length < 2) pinch = null;
            firstTouch = null;
        }
        surface.addEventListener('touchend', endTouch, { passive: true });
        surface.addEventListener('touchcancel', endTouch, { passive: true });

        // Safari GestureEvent trackpad pinch
        surface.addEventListener('gesturestart', function (event) {
            if (pinch) return;
            event.preventDefault();
            moved = true;
            if (controller && typeof controller.getZoom === 'function') {
                safariZoom = controller.getZoom();
            }
        }, { passive: false });

        surface.addEventListener('gesturechange', function (event) {
            if (pinch || safariZoom === null) return;
            event.preventDefault();
            if (Number.isFinite(event.scale) && event.scale > 0 && controller && typeof controller.setZoom === 'function') {
                controller.setZoom(safariZoom * event.scale);
            }
        }, { passive: false });

        surface.addEventListener('gestureend', function () {
            safariZoom = null;
        }, { passive: true });

        return {
            hasMoved: function () { return moved; },
            resetMoved: function () { moved = false; }
        };
    }

    return { bind: bind };
}));
