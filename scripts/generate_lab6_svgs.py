#!/usr/bin/env python3
"""
Generate vector SVG diagrams for Lab 6:
1. usability_scorecard_radar.svg - Radar chart comparing 6 core UX metrics vs benchmark
2. goms_tlm_comparison.svg - Bar chart comparing GOMS 12 models and TLM 3 screens
3. sus_distribution_chart.svg - SUS score distribution (N=10) with Bangor-Kortum grading
4. treejack_paths_ia.svg - Treejack navigation path diagram
"""

import math
from pathlib import Path

OUT_DIR = Path("/Users/victoriaivanova/university/7_sem/pchmi/project/CampusMeet/docs/assets/lab6")
OUT_DIR.mkdir(parents=True, exist_ok=True)

# 1. Usability Scorecard Radar Chart
def generate_radar_svg():
    width = 720
    height = 540
    cx = width / 2
    cy = height / 2 + 10
    radius = 180

    categories = [
        {"name": "Успешность (Task Success)", "actual": 97.5, "target": 85.0},
        {"name": "Скорость (Time Efficiency)", "actual": 89.0, "target": 80.0},
        {"name": "Безошибочность (Error-Free)", "actual": 93.0, "target": 90.0},
        {"name": "Удовлетворённость (SUS Score)", "actual": 85.8, "target": 75.0},
        {"name": "Прямизна путей (Treejack)", "actual": 88.8, "target": 70.0},
        {"name": "Эргономика ввода (GOMS)", "actual": 91.2, "target": 75.0}
    ]

    num_axes = len(categories)
    angles = [i * (2 * math.pi / num_axes) - math.pi / 2 for i in range(num_axes)]

    svg = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="auto" class="cm-diagram">']
    svg.append('<defs>')
    svg.append('  <linearGradient id="actualGrad" x1="0" y1="0" x2="1" y2="1">')
    svg.append('    <stop offset="0%" stop-color="#3b82f6" stop-opacity="0.5"/>')
    svg.append('    <stop offset="100%" stop-color="#10b981" stop-opacity="0.3"/>')
    svg.append('  </linearGradient>')
    svg.append('  <filter id="shadow" x="-10%" y="-10%" width="120%" height="120%">')
    svg.append('    <feDropShadow dx="0" dy="4" stdDeviation="6" flood-opacity="0.08"/>')
    svg.append('  </filter>')
    svg.append('</defs>')
    svg.append('<rect width="100%" height="100%" fill="var(--surface-primary, #ffffff)" rx="12"/>')

    # Title
    svg.append('<text x="32" y="44" font-family="Inter, sans-serif" font-size="18" font-weight="700" fill="var(--text-primary, #0f172a)">Сводная лепестковая диаграмма юзабилити (Usability Scorecard)</text>')
    svg.append('<text x="32" y="68" font-family="Inter, sans-serif" font-size="12" fill="var(--text-secondary, #64748b)">Сопоставление фактических показателей CampusMeet с целевым отраслевым эталоном</text>')

    # Grid webs (20%, 40%, 60%, 80%, 100%)
    for level in [0.2, 0.4, 0.6, 0.8, 1.0]:
        r = radius * level
        pts = []
        for a in angles:
            x = cx + r * math.cos(a)
            y = cy + r * math.sin(a)
            pts.append(f"{x:.1f},{y:.1f}")
        poly = " ".join(pts)
        svg.append(f'<polygon points="{poly}" fill="none" stroke="var(--border-subtle, #e2e8f0)" stroke-width="1" stroke-dasharray="{"none" if level == 1.0 else "4 4"}"/>')
        # Label level on top axis
        svg.append(f'<text x="{cx + 6}" y="{cy - r + 12}" font-family="JetBrains Mono, monospace" font-size="10" fill="var(--text-tertiary, #94a3b8)">{int(level*100)}%</text>')

    # Axis spokes and labels
    for i, a in enumerate(angles):
        x = cx + radius * math.cos(a)
        y = cy + radius * math.sin(a)
        svg.append(f'<line x1="{cx}" y1="{cy}" x2="{x:.1f}" y2="{y:.1f}" stroke="var(--border-subtle, #cbd5e1)" stroke-width="1.2"/>')

        lx = cx + (radius + 28) * math.cos(a)
        ly = cy + (radius + 24) * math.sin(a)
        anchor = "middle"
        if math.cos(a) > 0.3: anchor = "start"
        elif math.cos(a) < -0.3: anchor = "end"
        svg.append(f'<text x="{lx:.1f}" y="{ly:.1f}" font-family="Inter, sans-serif" font-size="11" font-weight="600" fill="var(--text-primary, #1e293b)" text-anchor="{anchor}">{categories[i]["name"]}</text>')
        svg.append(f'<text x="{lx:.1f}" y="{ly + 14:.1f}" font-family="JetBrains Mono, monospace" font-size="11" font-weight="700" fill="#10b981" text-anchor="{anchor}">{categories[i]["actual"]:.1f}%</text>')

    # Target polygon
    target_pts = []
    for i, a in enumerate(angles):
        val = categories[i]["target"] / 100.0
        x = cx + radius * val * math.cos(a)
        y = cy + radius * val * math.sin(a)
        target_pts.append(f"{x:.1f},{y:.1f}")
    svg.append(f'<polygon points="{" ".join(target_pts)}" fill="none" stroke="#f59e0b" stroke-width="2" stroke-dasharray="6 4"/>')

    # Actual polygon
    actual_pts = []
    for i, a in enumerate(angles):
        val = categories[i]["actual"] / 100.0
        x = cx + radius * val * math.cos(a)
        y = cy + radius * val * math.sin(a)
        actual_pts.append(f"{x:.1f},{y:.1f}")
    svg.append(f'<polygon points="{" ".join(actual_pts)}" fill="url(#actualGrad)" stroke="#2563eb" stroke-width="2.5" filter="url(#shadow)"/>')

    # Dots on actual polygon
    for pt in actual_pts:
        px, py = pt.split(",")
        svg.append(f'<circle cx="{px}" cy="{py}" r="4.5" fill="#2563eb" stroke="#ffffff" stroke-width="2"/>')

    # Legend
    svg.append('<g transform="translate(480, 44)">')
    svg.append('  <rect x="0" y="0" width="16" height="16" rx="4" fill="#2563eb"/>')
    svg.append('  <text x="24" y="12" font-family="Inter, sans-serif" font-size="12" font-weight="500" fill="var(--text-primary, #1e293b)">CampusMeet (Факт)</text>')
    svg.append('  <line x1="0" y1="28" x2="16" y2="28" stroke="#f59e0b" stroke-width="2" stroke-dasharray="4 3"/>')
    svg.append('  <text x="24" y="32" font-family="Inter, sans-serif" font-size="12" font-weight="500" fill="var(--text-primary, #1e293b)">Целевой эталон (Target)</text>')
    svg.append('</g>')

    svg.append('</svg>')
    return "\n".join(svg)

# 2. GOMS & TLM Time Comparison Chart
def generate_goms_chart_svg():
    width = 820
    height = 560
    svg = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="auto" class="cm-diagram">']
    svg.append('<rect width="100%" height="100%" fill="var(--surface-primary, #ffffff)" rx="12"/>')
    svg.append('<text x="32" y="44" font-family="Inter, sans-serif" font-size="18" font-weight="700" fill="var(--text-primary, #0f172a)">Сравнение хронометража по моделям GOMS (Web) и TLM (Mobile)</text>')
    svg.append('<text x="32" y="68" font-family="Inter, sans-serif" font-size="12" fill="var(--text-secondary, #64748b)">Анализ сокращения времени взаимодействия при оптимизации компоновки и Tab-навигации</text>')

    groups = [
        {
            "title": "Форма 1: Создание митапа / CFP",
            "items": [
                {"label": "Вар. А (Мышь)", "val": 32.35, "color": "#ef4444"},
                {"label": "Вар. А (Tab)", "val": 20.90, "color": "#f97316"},
                {"label": "Вар. Б (Мышь)", "val": 24.10, "color": "#3b82f6"},
                {"label": "Вар. Б (Tab / Ctrl+Enter)", "val": 14.10, "color": "#10b981"}
            ]
        },
        {
            "title": "Форма 2: Регистрация участника",
            "items": [
                {"label": "Вар. А (Мышь)", "val": 38.15, "color": "#ef4444"},
                {"label": "Вар. А (Tab)", "val": 21.65, "color": "#f97316"},
                {"label": "Вар. Б (SSO + Мышь)", "val": 9.30, "color": "#3b82f6"},
                {"label": "Вар. Б (SSO + Tab)", "val": 4.85, "color": "#10b981"}
            ]
        },
        {
            "title": "Форма 3: Поиск и фильтрация",
            "items": [
                {"label": "Вар. А (Мышь)", "val": 24.75, "color": "#ef4444"},
                {"label": "Вар. А (Tab)", "val": 15.55, "color": "#f97316"},
                {"label": "Вар. Б (Omnibox Мышь)", "val": 12.05, "color": "#3b82f6"},
                {"label": "Вар. Б (Omnibox ⌘K Tab)", "val": 7.00, "color": "#10b981"}
            ]
        },
        {
            "title": "Мобильное приложение (TLM)",
            "items": [
                {"label": "Экран 1: SSO Вход", "val": 3.85, "color": "#8b5cf6"},
                {"label": "Экран 2: QR Билет", "val": 6.10, "color": "#06b6d4"},
                {"label": "Экран 3: Сканер допуска", "val": 4.65, "color": "#10b981"}
            ]
        }
    ]

    max_val = 40.0
    bar_width = 380
    start_y = 100

    curr_y = start_y
    for g in groups:
        svg.append(f'<text x="32" y="{curr_y + 16}" font-family="Inter, sans-serif" font-size="13" font-weight="700" fill="var(--text-primary, #0f172a)">{g["title"]}</text>')
        curr_y += 26
        for item in g["items"]:
            w = (item["val"] / max_val) * bar_width
            svg.append(f'<text x="44" y="{curr_y + 13}" font-family="Inter, sans-serif" font-size="11" fill="var(--text-secondary, #475569)">{item["label"]}</text>')
            svg.append(f'<rect x="230" y="{curr_y}" width="{w:.1f}" height="18" rx="4" fill="{item["color"]}"/>')
            svg.append(f'<text x="{230 + w + 8:.1f}" y="{curr_y + 13}" font-family="JetBrains Mono, monospace" font-size="11" font-weight="600" fill="var(--text-primary, #0f172a)">{item["val"]:.2f} с</text>')
            curr_y += 23
        curr_y += 12

    # Legend at bottom right
    svg.append('<g transform="translate(640, 110)">')
    svg.append('  <rect x="0" y="0" width="160" height="150" rx="8" fill="var(--surface-secondary, #f8fafc)" stroke="var(--border-subtle, #e2e8f0)"/>')
    svg.append('  <text x="12" y="22" font-family="Inter, sans-serif" font-size="11" font-weight="700" fill="var(--text-primary, #1e293b)">Обозначения:</text>')
    svg.append('  <rect x="12" y="32" width="10" height="10" rx="2" fill="#ef4444"/>')
    svg.append('  <text x="28" y="41" font-family="Inter, sans-serif" font-size="10" fill="var(--text-secondary, #475569)">Вар. А (Мышь)</text>')
    svg.append('  <rect x="12" y="52" width="10" height="10" rx="2" fill="#f97316"/>')
    svg.append('  <text x="28" y="61" font-family="Inter, sans-serif" font-size="10" fill="var(--text-secondary, #475569)">Вар. А (Tab-ввод)</text>')
    svg.append('  <rect x="12" y="72" width="10" height="10" rx="2" fill="#3b82f6"/>')
    svg.append('  <text x="28" y="81" font-family="Inter, sans-serif" font-size="10" fill="var(--text-secondary, #475569)">Вар. Б (Мышь)</text>')
    svg.append('  <rect x="12" y="92" width="10" height="10" rx="2" fill="#10b981"/>')
    svg.append('  <text x="28" y="101" font-family="Inter, sans-serif" font-size="10" fill="var(--text-secondary, #475569)">Вар. Б (Tab / Fast)</text>')
    svg.append('  <rect x="12" y="112" width="10" height="10" rx="2" fill="#8b5cf6"/>')
    svg.append('  <text x="28" y="121" font-family="Inter, sans-serif" font-size="10" fill="var(--text-secondary, #475569)">TLM Mobile Touch</text>')
    svg.append('</g>')

    svg.append('</svg>')
    return "\n".join(svg)

# 3. SUS Distribution Chart
def generate_sus_chart_svg():
    width = 720
    height = 420
    svg = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="auto" class="cm-diagram">']
    svg.append('<rect width="100%" height="100%" fill="var(--surface-primary, #ffffff)" rx="12"/>')
    svg.append('<text x="32" y="44" font-family="Inter, sans-serif" font-size="18" font-weight="700" fill="var(--text-primary, #0f172a)">Распределение оценок SUS (System Usability Scale, N=10)</text>')
    svg.append('<text x="32" y="68" font-family="Inter, sans-serif" font-size="12" fill="var(--text-secondary, #64748b)">Средний балл = 85.75 | Ранг A+ | «Лучший в классе» (Best Imaginable)</text>')

    # Benchmarks horizontal bands
    # 0 to 100 scale on X: from x=80 to x=660 (width 580)
    sx = 80
    ew = 580
    def to_x(val):
        return sx + (val / 100.0) * ew

    # Bands
    bands = [
        {"from": 0, "to": 50, "fill": "#fee2e2", "label": "Неприемлемо (F)"},
        {"from": 50, "to": 68, "fill": "#fef3c7", "label": "Ниже среднего (D/C)"},
        {"from": 68, "to": 80.3, "fill": "#e0f2fe", "label": "Хорошо (B)"},
        {"from": 80.3, "to": 100, "fill": "#dcfce7", "label": "Отлично / Grade A+ (Best)"}
    ]

    by = 100
    bh = 180
    for b in bands:
        bx1 = to_x(b["from"])
        bx2 = to_x(b["to"])
        svg.append(f'<rect x="{bx1:.1f}" y="{by}" width="{bx2 - bx1:.1f}" height="{bh}" fill="{b["fill"]}" opacity="0.6"/>')
        svg.append(f'<text x="{(bx1 + bx2)/2:.1f}" y="{by + 20}" font-family="Inter, sans-serif" font-size="11" font-weight="600" fill="#334155" text-anchor="middle">{b["label"]}</text>')

    # Cutoff lines
    for line_val, label in [(68.0, "Среднее в индустрии (68.0)"), (80.3, "Порог класса A (80.3)")]:
        lx = to_x(line_val)
        svg.append(f'<line x1="{lx:.1f}" y1="{by}" x2="{lx:.1f}" y2="{by + bh}" stroke="#64748b" stroke-width="1.5" stroke-dasharray="4 4"/>')
        svg.append(f'<text x="{lx:.1f}" y="{by + bh + 16}" font-family="JetBrains Mono, monospace" font-size="10" fill="#64748b" text-anchor="middle">{label}</text>')

    # Users points
    users_sus = [87.5, 85.0, 80.0, 92.5, 90.0, 87.5, 82.5, 77.5, 87.5, 85.0]
    for i, score in enumerate(users_sus):
        px = to_x(score)
        py = by + 60 + (i % 5) * 24
        svg.append(f'<circle cx="{px:.1f}" cy="{py}" r="6" fill="#2563eb" stroke="#ffffff" stroke-width="2"/>')
        svg.append(f'<text x="{px + 10:.1f}" y="{py + 4}" font-family="JetBrains Mono, monospace" font-size="10" font-weight="600" fill="#1e293b">U{i+1}: {score}</text>')

    # Mean marker
    mx = to_x(85.75)
    svg.append(f'<line x1="{mx:.1f}" y1="{by - 10}" x2="{mx:.1f}" y2="{by + bh + 25}" stroke="#10b981" stroke-width="3"/>')
    svg.append(f'<rect x="{mx - 60:.1f}" y="{by - 32}" width="120" height="24" rx="6" fill="#10b981"/>')
    svg.append(f'<text x="{mx:.1f}" y="{by - 16}" font-family="Inter, sans-serif" font-size="11" font-weight="700" fill="#ffffff" text-anchor="middle">Mean SUS: 85.8</text>')

    # X axis
    svg.append(f'<line x1="{sx}" y1="{by + bh}" x2="{sx + ew}" y2="{by + bh}" stroke="#0f172a" stroke-width="1.5"/>')
    for tick in [0, 20, 40, 60, 80, 100]:
        tx = to_x(tick)
        svg.append(f'<line x1="{tx:.1f}" y1="{by + bh}" x2="{tx:.1f}" y2="{by + bh + 6}" stroke="#0f172a" stroke-width="1.5"/>')
        svg.append(f'<text x="{tx:.1f}" y="{by + bh + 20}" font-family="JetBrains Mono, monospace" font-size="11" fill="#475569" text-anchor="middle">{tick}</text>')

    svg.append('<text x="32" y="380" font-family="Inter, sans-serif" font-size="11" fill="var(--text-tertiary, #64748b)">Шкала: Sauro &amp; Lewis (2012), Bangor, Kortum &amp; Miller (2009). Все 10 оценок выше среднего индустриального значения 68.0.</text>')
    svg.append('</svg>')
    return "\n".join(svg)

# 4. Treejack Paths Diagram
def generate_treejack_svg():
    width = 720
    height = 460
    svg = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="auto" class="cm-diagram">']
    svg.append('<rect width="100%" height="100%" fill="var(--surface-primary, #ffffff)" rx="12"/>')
    svg.append('<text x="32" y="44" font-family="Inter, sans-serif" font-size="18" font-weight="700" fill="var(--text-primary, #0f172a)">Результаты тестирования навигации Treejack (IA Sitemap)</text>')
    svg.append('<text x="32" y="68" font-family="Inter, sans-serif" font-size="12" fill="var(--text-secondary, #64748b)">Показатели Directness (прямолинейность пути) и Success Rate для ключевых задач</text>')

    tasks = [
        {"title": "Задача 1: Подача заявки спикера в CFP", "path": "События → AI Tech Meetup → Программа &amp; CFP → Подать заявку", "success": 100, "directness": 90, "time": "12.4 с"},
        {"title": "Задача 2: Выгрузка CSV списка для бейджей", "path": "Кабинет организатора → Мои митапы → Участники → Экспорт", "success": 90, "directness": 80, "time": "16.8 с"},
        {"title": "Задача 3: Поиск сохраненного офлайн QR-билета", "path": "Мой профиль → Мои билеты → Офлайн-билет (HMAC)", "success": 100, "directness": 100, "time": "8.5 с"},
        {"title": "Задача 4: Активация пакетного сканера допуска", "path": "Кабинет волонтёра → Сканер допуска → Офлайн-режим", "success": 90, "directness": 85, "time": "14.1 с"}
    ]

    ty = 105
    for t in tasks:
        # Card
        svg.append(f'<g transform="translate(32, {ty})">')
        svg.append('  <rect x="0" y="0" width="656" height="74" rx="8" fill="var(--surface-secondary, #f8fafc)" stroke="var(--border-subtle, #e2e8f0)"/>')
        svg.append(f'  <text x="16" y="24" font-family="Inter, sans-serif" font-size="13" font-weight="700" fill="var(--text-primary, #0f172a)">{t["title"]}</text>')
        svg.append(f'  <text x="16" y="44" font-family="JetBrains Mono, monospace" font-size="11" fill="#2563eb">{t["path"]}</text>')

        # Badges
        svg.append('  <g transform="translate(430, 16)">')
        # Success badge
        svg.append('    <rect x="0" y="0" width="95" height="42" rx="6" fill="#dcfce7" stroke="#86efac"/>')
        svg.append('    <text x="47" y="18" font-family="Inter, sans-serif" font-size="9" font-weight="600" fill="#166534" text-anchor="middle">УСПЕХ</text>')
        svg.append(f'    <text x="47" y="34" font-family="JetBrains Mono, monospace" font-size="12" font-weight="700" fill="#166534" text-anchor="middle">{t["success"]}%</text>')
        # Directness badge
        svg.append('    <rect x="105" y="0" width="110" height="42" rx="6" fill="#e0f2fe" stroke="#7dd3fc"/>')
        svg.append('    <text x="160" y="18" font-family="Inter, sans-serif" font-size="9" font-weight="600" fill="#075985" text-anchor="middle">ПРЯМИЗНА (DIR)</text>')
        svg.append(f'    <text x="160" y="34" font-family="JetBrains Mono, monospace" font-size="12" font-weight="700" fill="#075985" text-anchor="middle">{t["directness"]}% ({t["time"]})</text>')
        svg.append('  </g>')
        svg.append('</g>')
        ty += 86

    svg.append('</svg>')
    return "\n".join(svg)

# Write all SVGs
(OUT_DIR / "usability_scorecard_radar.svg").write_text(generate_radar_svg())
(OUT_DIR / "goms_tlm_comparison.svg").write_text(generate_goms_chart_svg())
(OUT_DIR / "sus_distribution_chart.svg").write_text(generate_sus_chart_svg())
(OUT_DIR / "treejack_paths_ia.svg").write_text(generate_treejack_svg())

print("Successfully generated all Lab 6 SVG assets!")
