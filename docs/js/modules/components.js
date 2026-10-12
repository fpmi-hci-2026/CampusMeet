/**
 * CampusMeet / EventHub — Declarative Custom Elements (Syntactic Sugar)
 * Light-DOM Web Components for Rapid, Boilerplate-Free Lab Page Authoring
 */

(function () {
    'use strict';

    if (typeof customElements === 'undefined') {
        console.warn('Custom Elements API not supported in this environment');
        return;
    }

    const nav = window.CampusMeetNavigation || null;

    function getResolvedHref(path) {
        if (!path) return '';
        if (window.CampusMeetNavigation && typeof window.CampusMeetNavigation.resolvePath === 'function') {
            return window.CampusMeetNavigation.resolvePath(path);
        }
        return path;
    }

    /**
     * <lab-hero>
     * Declarative Hero Header for Lab Pages
     * Attributes: lab, title, subtitle, status, report, badge
     */
    class LabHeroElement extends HTMLElement {
        connectedCallback() {
            if (this.dataset.rendered) return;
            this.dataset.rendered = 'true';

            const labNum = this.getAttribute('lab') || '1';
            const title = this.getAttribute('title') || `Лабораторная работа №${labNum}`;
            const subtitle = this.getAttribute('subtitle') || this.getAttribute('desc') || '';
            const status = this.getAttribute('status') || 'done';
            const reportAttr = this.getAttribute('report') || `reports/Lab${labNum}_report.md`;
            const reportHref = getResolvedHref(reportAttr);
            const badge = this.getAttribute('badge') || (status === 'done' ? 'ВЫПОЛНЕНО' : 'ЗАПЛАНИРОВАНО');
            const statusClass = status === 'done' ? 'tag-key' : 'tag-supp';

            this.classList.add('content-header');
            this.innerHTML = `
                <div class="badge-group" style="display: flex; gap: 8px; align-items: center; margin-bottom: 12px; flex-wrap: wrap;">
                    <span class="badge" style="background: var(--surface-secondary); color: var(--text-primary); border: 1px solid var(--border-subtle); padding: 3px 8px; border-radius: var(--radius-xs); font-size: 0.75rem; font-weight: 600;">ПЧМИ • БГУ ФПМИ</span>
                    <span class="badge" style="background: var(--surface-secondary); color: var(--text-primary); border: 1px solid var(--border-subtle); padding: 3px 8px; border-radius: var(--radius-xs); font-size: 0.75rem; font-weight: 500;">Лабораторная работа №${labNum}</span>
                    <span class="persona-tag ${statusClass}" style="font-size: 0.75rem;">${badge}</span>
                </div>
                <h1 style="font-size: 2.2rem; font-weight: 700; letter-spacing: -0.03em; margin: 0 0 12px 0; color: var(--text-primary); line-height: 1.2;">${title}</h1>
                ${subtitle ? `<p class="lead" style="font-size: 1.1rem; color: var(--text-secondary); max-width: 880px; line-height: 1.6; margin-bottom: 20px;">${subtitle}</p>` : ''}
                <div class="header-meta" style="display: flex; gap: 24px; align-items: center; flex-wrap: wrap; padding-top: 12px; border-top: 1px solid var(--border-subtle);">
                    <div style="font-size: 0.85rem; color: var(--text-secondary);"><strong style="color: var(--text-primary);">Курс:</strong> 2025–2026 (6 семестр)</div>
                    <div style="font-size: 0.85rem; color: var(--text-secondary);"><strong style="color: var(--text-primary);">Команда:</strong> Минчук С., Иванова В., Шварцман Д.</div>
                    ${reportHref ? `
                    <div style="margin-left: auto;">
                        <a href="${reportHref}" id="report-lab${labNum}" class="btn btn-secondary" style="display: inline-flex; align-items: center; gap: 6px; padding: 6px 14px; font-size: 0.85rem; border-radius: var(--radius-sm); text-decoration: none;" target="_blank" rel="noopener noreferrer">
                            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line></svg>
                            <span>Открыть академический отчет .md</span>
                        </a>
                    </div>` : ''}
                </div>
            `;
        }
    }

    /**
     * <stat-grid>
     * Responsive KPI Statistics Container
     */
    class StatGridElement extends HTMLElement {
        connectedCallback() {
            this.classList.add('stats-grid');
        }
    }

    /**
     * <stat-card>
     * Individual Metric Card with Layout Overflow Protection
     * Attributes: value, unit, label
     */
    class StatCardElement extends HTMLElement {
        connectedCallback() {
            if (this.dataset.rendered) return;
            this.dataset.rendered = 'true';

            const value = this.getAttribute('value') || '0';
            const unit = this.getAttribute('unit') || '';
            const label = this.getAttribute('label') || this.textContent.trim();

            this.classList.add('stat-card');
            this.innerHTML = `
                <div class="stat-value">${value}${unit ? `<span class="stat-unit">${unit}</span>` : ''}</div>
                <div class="stat-label">${label}</div>
            `;
        }
    }

    /**
     * <doc-section>
     * Standard Document Section with Header, Anchor Link, and Content Wrapper
     * Attributes: id, title, badge
     */
    class DocSectionElement extends HTMLElement {
        connectedCallback() {
            if (this.dataset.rendered) return;
            this.dataset.rendered = 'true';

            const id = this.getAttribute('id') || `sec-${Math.random().toString(36).substring(2, 7)}`;
            const title = this.getAttribute('title') || '';
            const badge = this.getAttribute('badge') || '';

            this.classList.add('doc-section');
            this.id = id;

            // Preserve inner HTML of the author's content
            const contentHtml = this.innerHTML;

            this.innerHTML = `
                <div class="section-header">
                    <div style="display: flex; align-items: baseline; gap: 8px;">
                        <h2 style="margin: 0; font-size: 1.55rem; font-weight: 600; letter-spacing: -0.02em;">${title}</h2>
                        <a href="#${id}" class="anchor-link" aria-label="Ссылка на раздел ${title}" style="color: var(--text-tertiary); text-decoration: none; font-size: 1.1rem;">#</a>
                    </div>
                    ${badge ? `<span class="persona-tag tag-supp">${badge}</span>` : ''}
                </div>
                <div class="section-content">
                    ${contentHtml}
                </div>
            `;
        }
    }

    /**
     * <callout-card>
     * Monochrome Notice and Callout Block
     * Attributes: type (info|success|warning|danger), title
     */
    class CalloutCardElement extends HTMLElement {
        connectedCallback() {
            if (this.dataset.rendered) return;
            this.dataset.rendered = 'true';

            const type = this.getAttribute('type') || 'info';
            const title = this.getAttribute('title') || '';
            const bodyHtml = this.innerHTML;

            const iconMap = {
                info: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line></svg>',
                success: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>',
                warning: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3Z"></path><line x1="12" y1="9" x2="12" y2="13"></line><line x1="12" y1="17" x2="12.01" y2="17"></line></svg>',
                danger: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="15" y1="9" x2="9" y2="15"></line><line x1="9" y1="9" x2="15" y2="15"></line></svg>'
            };

            this.style.display = 'block';
            this.style.margin = '20px 0';
            this.style.padding = '16px 20px';
            this.style.borderRadius = 'var(--radius-md)';
            this.style.border = '1px solid var(--border-default)';
            this.style.background = 'var(--surface-secondary)';

            this.innerHTML = `
                <div style="display: flex; gap: 12px; align-items: flex-start;">
                    <div style="color: var(--text-primary); flex-shrink: 0; margin-top: 2px;">
                        ${iconMap[type] || iconMap.info}
                    </div>
                    <div style="flex: 1; min-width: 0;">
                        ${title ? `<div style="font-weight: 600; margin-bottom: 6px; color: var(--text-primary); font-size: 0.95rem;">${title}</div>` : ''}
                        <div style="color: var(--text-secondary); font-size: 0.9rem; line-height: 1.5;">${bodyHtml}</div>
                    </div>
                </div>
            `;
        }
    }

    /**
     * <diagram-frame>
     * Interactive Pan-Zoom Diagram Container
     * Attributes: title, badge, src, type (mermaid|svg|image)
     */
    class DiagramFrameElement extends HTMLElement {
        connectedCallback() {
            if (this.dataset.rendered) return;
            this.dataset.rendered = 'true';

            const title = this.getAttribute('title') || 'Архитектурная схема';
            const badge = this.getAttribute('badge') || 'СХЕМА';
            const type = this.getAttribute('type') || 'mermaid';
            const src = this.getAttribute('src') || '';
            const resolvedSrc = src ? getResolvedHref(src) : '';
            const innerCode = this.innerHTML.trim();

            this.style.display = 'block';
            this.style.margin = '24px 0';

            let contentHtml = '';
            if (type === 'mermaid') {
                contentHtml = `<div class="mermaid">${innerCode}</div>`;
            } else if (resolvedSrc) {
                contentHtml = `<img src="${resolvedSrc}" alt="${title}" style="max-width: 100%; display: block; margin: 0 auto;">`;
            } else {
                contentHtml = innerCode;
            }

            this.innerHTML = `
                <div class="diagram-pan-wrapper" style="border: 1px solid var(--border-subtle); border-radius: var(--radius-md); overflow: hidden; background: var(--surface-primary);">
                    <div class="diagram-pan-header" style="display: flex; justify-content: space-between; align-items: center; padding: 10px 16px; border-bottom: 1px solid var(--border-subtle); background: var(--surface-secondary);">
                        <div style="display: flex; align-items: center; gap: 8px;">
                            <span style="font-size: 0.85rem; font-weight: 600; color: var(--text-primary);">${title}</span>
                            <span class="persona-tag tag-key" style="font-size: 0.7rem;">${badge}</span>
                        </div>
                        <div class="diagram-pan-controls" style="display: flex; gap: 6px; align-items: center;">
                            <button type="button" class="pan-ctrl-btn" data-action="zoom-out" title="Уменьшить" style="padding: 2px 8px; border: 1px solid var(--border-subtle); background: var(--surface-primary); border-radius: var(--radius-xs); cursor: pointer;">−</button>
                            <span class="pan-zoom-badge" style="font-size: 0.75rem; color: var(--text-secondary); min-width: 44px; text-align: center;">100%</span>
                            <button type="button" class="pan-ctrl-btn" data-action="zoom-in" title="Увеличить" style="padding: 2px 8px; border: 1px solid var(--border-subtle); background: var(--surface-primary); border-radius: var(--radius-xs); cursor: pointer;">+</button>
                            <button type="button" class="pan-ctrl-btn" data-action="zoom-reset" title="Сбросить (1:1)" style="padding: 2px 8px; border: 1px solid var(--border-subtle); background: var(--surface-primary); border-radius: var(--radius-xs); cursor: pointer;">1:1</button>
                        </div>
                    </div>
                    <div class="diagram-pan-container" style="padding: 24px; display: flex; justify-content: center; align-items: center; overflow: auto; min-height: 220px;">
                        ${contentHtml}
                    </div>
                </div>
            `;

            // If mermaid, enhance on next tick
            if (type === 'mermaid' && typeof window.renderTabMermaid === 'function') {
                setTimeout(() => window.renderTabMermaid(this), 100);
            }
        }
    }

    /**
     * <tab-group> & <tab-pane>
     * Declarative Tabs Sugar
     */
    class TabGroupElement extends HTMLElement {
        connectedCallback() {
            if (this.dataset.rendered) return;
            this.dataset.rendered = 'true';

            const panes = Array.from(this.querySelectorAll('tab-pane'));
            if (panes.length === 0) return;

            const tabHeader = document.createElement('div');
            tabHeader.className = 'tab-list';
            tabHeader.style.cssText = 'display: flex; gap: 8px; border-bottom: 1px solid var(--border-subtle); margin-bottom: 20px;';

            panes.forEach((pane, idx) => {
                const label = pane.getAttribute('label') || `Вкладка ${idx + 1}`;
                const isActive = pane.hasAttribute('active') || idx === 0;

                const btn = document.createElement('button');
                btn.className = `tab-btn ${isActive ? 'active' : ''}`;
                btn.textContent = label;
                btn.style.cssText = 'padding: 8px 16px; border: none; background: transparent; cursor: pointer; font-size: 0.9rem; font-weight: 500; border-bottom: 2px solid transparent; color: var(--text-secondary); transition: all 0.15s ease;';
                if (isActive) {
                    btn.style.borderColor = 'var(--text-primary)';
                    btn.style.color = 'var(--text-primary)';
                    pane.style.display = 'block';
                } else {
                    pane.style.display = 'none';
                }

                btn.addEventListener('click', () => {
                    tabHeader.querySelectorAll('.tab-btn').forEach(b => {
                        b.classList.remove('active');
                        b.style.borderColor = 'transparent';
                        b.style.color = 'var(--text-secondary)';
                    });
                    btn.classList.add('active');
                    btn.style.borderColor = 'var(--text-primary)';
                    btn.style.color = 'var(--text-primary)';

                    panes.forEach(p => p.style.display = 'none');
                    pane.style.display = 'block';

                    // Lazy render mermaid inside active pane if needed
                    if (typeof window.renderTabMermaid === 'function') {
                        window.renderTabMermaid(pane);
                    }
                });

                tabHeader.appendChild(btn);
            });

            this.insertBefore(tabHeader, this.firstChild);
        }
    }

    class TabPaneElement extends HTMLElement {
        connectedCallback() {
            this.classList.add('tab-pane');
        }
    }

    /**
     * <responsive-table>
     * Table Container with Automatic Horizontal Scroll and Border Isolation
     */
    class ResponsiveTableElement extends HTMLElement {
        connectedCallback() {
            this.classList.add('table-responsive');
        }
    }

    // Register all Custom Elements
    customElements.define('lab-hero', LabHeroElement);
    customElements.define('stat-grid', StatGridElement);
    customElements.define('stat-card', StatCardElement);
    customElements.define('doc-section', DocSectionElement);
    customElements.define('callout-card', CalloutCardElement);
    customElements.define('diagram-frame', DiagramFrameElement);
    customElements.define('tab-group', TabGroupElement);
    customElements.define('tab-pane', TabPaneElement);
    customElements.define('responsive-table', ResponsiveTableElement);

})();
