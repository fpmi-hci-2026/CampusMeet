/**
 * CampusMeet / EventHub — Declarative DOM Component Renderers
 */

(function () {
    'use strict';

    function getAppData() {
        return (typeof window !== 'undefined' && window.CampusMeetData) ? window.CampusMeetData : {};
    }

    function renderPainPoints() {
        const tbody = document.getElementById('pain-points-body');
        const data = getAppData();
        if (!tbody || !data.painPoints) return;
        tbody.innerHTML = data.painPoints.map(item => {
            const tagClass = item.severity === 'Критический' ? 'tag-anti' : (item.severity === 'Высокий' ? 'tag-key' : 'tag-supp');
            return `
            <tr>
                <td><strong>${item.issue}</strong></td>
                <td>${item.n}</td>
                <td>${item.pct}</td>
                <td><span class="persona-tag ${tagClass}">${item.severity}</span></td>
            </tr>
        `;
        }).join('');
    }

    function resolveAssetPath(relPath) {
        if (!relPath) return '';
        if (typeof window !== 'undefined' && window.location) {
            const pathName = window.location.pathname || '';
            const inPages = pathName.includes('/pages/') || (!pathName.endsWith('index.html') && pathName.includes('/pages'));
            if (inPages && !relPath.startsWith('../') && !relPath.startsWith('http') && !relPath.startsWith('/')) {
                return '../' + relPath;
            }
        }
        return relPath;
    }

    function renderPersonas() {
        const container = document.getElementById('personas-grid');
        const data = getAppData();
        if (!container || !data.personas) return;
        container.innerHTML = data.personas.map(p => `
            <div class="persona-card">
                <img src="${resolveAssetPath(p.avatar)}" alt="${p.name.split(',')[0]}" class="persona-avatar">
                <div class="persona-body">
                    <span class="persona-tag ${p.tagClass}">${p.tag}</span>
                    <div class="persona-title">${p.name}</div>
                    <div class="persona-meta">${p.role}</div>
                    <div class="persona-desc">${p.desc}</div>
                </div>
            </div>
        `).join('');
    }

    function renderCjmTable() {
        const tbody = document.getElementById('cjm-table-body');
        const data = getAppData();
        if (!tbody || !data.cjmMatrix) return;
        tbody.innerHTML = data.cjmMatrix.map(p => `
            <tr>
                <td><strong>${p.name}</strong><br/>(${p.role})</td>
                ${p.stages.map(st => `<td>${st}</td>`).join('')}
            </tr>
        `).join('');
    }

    function renderCjmBreakdowns() {
        const container = document.getElementById('cjm-breakdowns-grid');
        const data = getAppData();
        if (!container || !data.cjmBreakdowns) return;
        container.innerHTML = data.cjmBreakdowns.map(p => {
            const borderStyle = p.dangerBorder ? ' style="border-left: 2px solid var(--border-strong);"' : '';
            const body = p.goal
                ? `<strong>Ключевая цель:</strong> ${p.goal}<br/>
                   <strong>Эмоциональный трек:</strong> ${p.emotion}<br/>
                   <strong>Интерфейсное решение:</strong> ${p.solution}`
                : `<strong>Паттерн:</strong> ${p.pattern}<br/>
                   <strong>Эмоциональный трек:</strong> ${p.emotion}<br/>
                   <strong>Барьеры системы:</strong> ${p.barrier}`;
            return `
                <div class="profile-card"${borderStyle}>
                    <h3>${p.title}</h3>
                    <p style="color: var(--text-muted); font-size: 0.85rem;">
                        ${body}
                    </p>
                </div>
            `;
        }).join('');
    }

    function renderStoryboards() {
        const container = document.getElementById('storyboards-grid');
        const data = getAppData();
        if (!container || !data.storyboards) return;
        container.innerHTML = data.storyboards.map(s => {
            const borderStyle = s.dangerBorder ? ' style="border-left: 2px solid var(--border-strong);"' : '';
            const frames = s.frames.map((fr, idx) => `<li><strong>Кадр ${idx + 1}:</strong> ${fr}</li>`).join('');
            return `
                <div class="profile-card"${borderStyle}>
                    <h4>${s.title}</h4>
                    <ol style="font-size: 0.85rem; padding-left: 18px; color: var(--text-muted);">
                        ${frames}
                    </ol>
                </div>
            `;
        }).join('');
    }

    function renderEdgeCases() {
        const tbody = document.getElementById('edge-cases-body');
        const data = getAppData();
        if (!tbody || !data.edgeCases) return;
        tbody.innerHTML = data.edgeCases.map(ec => `
            <tr>
                <td><strong>${ec.code}</strong></td>
                <td><strong>${ec.scenario}</strong></td>
                <td>${ec.condition}</td>
                <td>${ec.behavior}</td>
                <td>${ec.result}</td>
            </tr>
        `).join('');
    }

    function renderUserStories() {
        const tbody = document.getElementById('user-stories-body');
        const data = getAppData();
        if (!tbody || !data.userStories) return;
        tbody.innerHTML = data.userStories.map(us => `
            <tr>
                <td><strong>${us.code}</strong></td>
                <td>${us.role}</td>
                <td>${us.story}</td>
                <td><span class="persona-tag ${us.priorityClass}">${us.priority}</span></td>
                <td>${us.platform}</td>
            </tr>
        `).join('');
    }

    function renderTraceability() {
        const tbody = document.getElementById('traceability-body');
        const data = getAppData();
        if (!tbody || !data.traceabilityMatrix) return;
        tbody.innerHTML = data.traceabilityMatrix.map(tm => `
            <tr>
                <td><code>${tm.srsId}</code></td>
                <td>${tm.us}</td>
                <td>${tm.uc}</td>
                <td>${tm.component}</td>
                <td>${tm.test}</td>
            </tr>
        `).join('');
    }

    window.initDynamicComponents = function () {
        renderPainPoints();
        renderPersonas();
        renderCjmTable();
        renderCjmBreakdowns();
        renderStoryboards();
        renderEdgeCases();
        renderUserStories();
        renderTraceability();
    };
})();
