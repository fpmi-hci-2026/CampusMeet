const test = require('node:test');
const assert = require('node:assert/strict');
const { bind } = require('../docs/js/modules/diagram-gestures.js');

function fixture() {
    const handlers = new Map();
    let zoom = 1;
    const updates = [];
    const surface = {
        clientHeight: 600,
        addEventListener(name, callback) { handlers.set(name, callback); },
    };
    const gestures = bind(surface, {
        getZoom: () => zoom,
        setZoom: value => { zoom = value; updates.push(value); },
    });
    function send(name, fields = {}) {
        const event = { prevented: false, preventDefault() { this.prevented = true; }, ...fields };
        handlers.get(name)?.(event);
        return event;
    }
    return { handlers, send, updates, gestures, zoom: () => zoom };
}

test('ordinary and Meta+wheel scrolling never zoom or prevent native scrolling', () => {
    const view = fixture();
    for (const fields of [{}, { metaKey: true }]) {
        assert.equal(view.send('wheel', { deltaY: 100, deltaMode: 0, ...fields }).prevented, false);
    }
    assert.equal(view.zoom(), 1);
    assert.equal(view.updates.length, 0);
});

test('Ctrl+wheel / browser trackpad pinch zooms within the diagram', () => {
    const view = fixture();
    const event = view.send('wheel', { ctrlKey: true, deltaY: -100, deltaMode: 0 });
    assert.equal(event.prevented, true);
    assert.ok(view.zoom() > 1);
    view.send('wheel', { ctrlKey: true, deltaY: 100, deltaMode: 0 });
    assert.ok(Math.abs(view.zoom() - 1) < 1e-10);
});

test('a one-finger swipe remains native scrolling and cannot drag the diagram', () => {
    const view = fixture();
    assert.equal(view.send('touchstart', { touches: [{ clientX: 10, clientY: 10 }] }).prevented, false);
    assert.equal(view.send('touchmove', { touches: [{ clientX: 10, clientY: 150 }] }).prevented, false);
    assert.equal(view.updates.length, 0);
    assert.equal(view.gestures.hasMoved(), true);
    assert.equal(view.handlers.has('mousedown'), false);
    assert.equal(view.handlers.has('mousemove'), false);
    assert.equal(view.handlers.has('dblclick'), false);
});

test('two-finger pinch scales by distance and ends when one finger is lifted', () => {
    const view = fixture();
    const start = view.send('touchstart', { touches: [{ clientX: 0, clientY: 0 }, { clientX: 100, clientY: 0 }] });
    const move = view.send('touchmove', { touches: [{ clientX: 0, clientY: 0 }, { clientX: 200, clientY: 0 }] });
    assert.equal(start.prevented, true);
    assert.equal(move.prevented, true);
    assert.equal(view.zoom(), 2);
    view.send('touchend', { touches: [{ clientX: 0, clientY: 0 }] });
    const swipe = view.send('touchmove', { touches: [{ clientX: 0, clientY: 70 }] });
    assert.equal(swipe.prevented, false);
    assert.equal(view.zoom(), 2);
});

test('Safari trackpad pinch is handled without a double-click zoom listener', () => {
    const view = fixture();
    assert.equal(view.send('gesturestart').prevented, true);
    assert.equal(view.send('gesturechange', { scale: 1.5 }).prevented, true);
    assert.equal(view.zoom(), 1.5);
    view.send('gestureend');
    view.send('gesturechange', { scale: 2 });
    assert.equal(view.zoom(), 1.5);
});

test('native scrolling suppresses an accidental fullscreen click, a new tap resets it', () => {
    const view = fixture();
    view.send('scroll');
    assert.equal(view.gestures.hasMoved(), true);
    view.send('pointerdown');
    assert.equal(view.gestures.hasMoved(), false);
});
