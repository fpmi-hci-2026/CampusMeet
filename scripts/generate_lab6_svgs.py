#!/usr/bin/env python3
"""
Generate ultra-clean, spacious vector SVG diagrams for Lab 6:
1. usability_scorecard_radar.svg - Usability Scorecard Radar Chart (6 metrics vs target)
2. goms_tlm_comparison.svg       - GOMS (Web) vs TLM (Mobile) Chronometry Bar Chart
3. sus_distribution_chart.svg    - System Usability Scale (SUS) Score Distribution (N=10)
4. treejack_paths_ia.svg         - Treejack Navigation Paths & Information Architecture Directness

Design Principles (docs/DESIGN_SYSTEM.md):
- 100% decoupled multi-row header structure: Titles NEVER share lines with Legend/Badges
- Dedicated full-width horizontal legend strips with generous margins
- Separate <g transform="translate(x, 0)"> for EVERY badge to mathematically guarantee ZERO text collisions
- Self-contained SVG styling with embedded fonts and fallbacks
"""

import math
from pathlib import Path

OUT_DIR = Path("/Users/victoriaivanova/university/7_sem/pchmi/project/CampusMeet/docs/assets/lab6")
OUT_DIR.mkdir(parents=True, exist_ok=True)

# Common SVG filter defs
SVG_DEFS = """
  <defs>
    <!-- Drop Shadow Standard -->
    <filter id="shadow-card" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="4" stdDeviation="8" flood-color="#0f172a" flood-opacity="0.07"/>
      <feDropShadow dx="0" dy="1" stdDeviation="2" flood-color="#0f172a" flood-opacity="0.03"/>
    </filter>

    <filter id="shadow-badge" x="-10%" y="-15%" width="120%" height="135%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#0f172a" flood-opacity="0.05"/>
    </filter>

    <!-- Radar Gradients -->
    <linearGradient id="actualGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#3b82f6" stop-opacity="0.35"/>
      <stop offset="50%" stop-color="#2563eb" stop-opacity="0.25"/>
      <stop offset="100%" stop-color="#10b981" stop-opacity="0.18"/>
    </linearGradient>

    <!-- Bar Gradients -->
    <linearGradient id="bar-red" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#f87171"/>
      <stop offset="100%" stop-color="#ef4444"/>
    </linearGradient>
    <linearGradient id="bar-orange" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#fb923c"/>
      <stop offset="100%" stop-color="#f97316"/>
    </linearGradient>
    <linearGradient id="bar-blue" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#60a5fa"/>
      <stop offset="100%" stop-color="#3b82f6"/>
    </linearGradient>
    <linearGradient id="bar-green" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#34d399"/>
      <stop offset="100%" stop-color="#10b981"/>
    </linearGradient>
    <linearGradient id="bar-purple" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#a78bfa"/>
      <stop offset="100%" stop-color="#8b5cf6"/>
    </linearGradient>
  </defs>
"""

# ==============================================================================
# 1. Usability Scorecard Radar Chart
# ==============================================================================
def generate_radar_svg():
    width = 1000
    height = 760
    cx = 500
    cy = 440
    radius = 185

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

    svg = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="auto" font-family="Inter, -apple-system, BlinkMacSystemFont, sans-serif">']
    svg.append(SVG_DEFS)

    # Background Card
    svg.append('<rect width="100%" height="100%" fill="#f8fafc"/>')
    svg.append(f'<rect x="24" y="24" width="{width - 48}" height="{height - 48}" rx="16" fill="#ffffff" stroke="#e2e8f0" stroke-width="1.5" filter="url(#shadow-card)"/>')

    # ROW 1: Header (Full-width, isolated from legend)
    svg.append('<g transform="translate(50, 60)">')
    svg.append('  <text x="0" y="0" font-size="20" font-weight="800" fill="#0f172a">Сводная лепестковая диаграмма юзабилити (Usability Scorecard)</text>')
    svg.append('  <text x="0" y="24" font-size="12" fill="#64748b">Сопоставление фактических показателей CampusMeet с целевым эталоном (N = 10, 95% ДИ Вильсона, SUM = 90.7%)</text>')
    svg.append('</g>')

    # ROW 2: Dedicated Horizontal Legend Strip (y = 105..140, ZERO overlap with title)
    svg.append('<g transform="translate(50, 105)">')
    
    # Pill 1: Actual
    svg.append('  <g transform="translate(0, 0)">')
    svg.append('    <rect x="0" y="0" width="280" height="34" rx="8" fill="#eff6ff" stroke="#bfdbfe"/>')
    svg.append('    <rect x="14" y="12" width="10" height="10" rx="2" fill="#2563eb"/>')
    svg.append('    <text x="32" y="22" font-size="12" font-weight="700" fill="#1e40af">CampusMeet (Факт) — среднее 90.7%</text>')
    svg.append('  </g>')

    # Pill 2: Target Benchmark
    svg.append('  <g transform="translate(295, 0)">')
    svg.append('    <rect x="0" y="0" width="310" height="34" rx="8" fill="#fffbeb" stroke="#fde68a"/>')
    svg.append('    <line x1="14" y1="17" x2="30" y2="17" stroke="#d97706" stroke-width="2.5" stroke-dasharray="4 2"/>')
    svg.append('    <text x="38" y="22" font-size="12" font-weight="700" fill="#92400e">Целевой отраслевой эталон — 79.2%</text>')
    svg.append('  </g>')

    # Pill 3: Summary Delta
    svg.append('  <g transform="translate(620, 0)">')
    svg.append('    <rect x="0" y="0" width="280" height="34" rx="8" fill="#ecfdf5" stroke="#a7f3d0"/>')
    svg.append('    <text x="140" y="22" font-size="12" font-weight="800" fill="#065f46" text-anchor="middle">★ Превышение эталона: +11.5 п.п.</text>')
    svg.append('  </g>')

    svg.append('</g>')

    # Grid Webs (20%, 40%, 60%, 80%, 100%)
    levels = [0.2, 0.4, 0.6, 0.8, 1.0]
    for lvl in levels:
        r = radius * lvl
        pts = []
        for a in angles:
            x = cx + r * math.cos(a)
            y = cy + r * math.sin(a)
            pts.append(f"{x:.1f},{y:.1f}")
        poly = " ".join(pts)
        is_outer = (lvl == 1.0)
        stroke_color = "#94a3b8" if is_outer else "#e2e8f0"
        stroke_dash = "none" if is_outer else "4 4"
        stroke_w = "1.5" if is_outer else "1"
        svg.append(f'<polygon points="{poly}" fill="none" stroke="{stroke_color}" stroke-width="{stroke_w}" stroke-dasharray="{stroke_dash}"/>')

        # Web % label badge on the right side of the vertical axis
        svg.append(f'<rect x="{cx + 6}" y="{cy - r - 8:.1f}" width="36" height="16" rx="3" fill="#ffffff" stroke="#e2e8f0" stroke-width="1"/>')
        svg.append(f'<text x="{cx + 24}" y="{cy - r + 4:.1f}" font-family="JetBrains Mono, monospace" font-size="10" font-weight="700" fill="#64748b" text-anchor="middle">{int(lvl*100)}%</text>')

    # Axis Spokes
    for a in angles:
        x = cx + radius * math.cos(a)
        y = cy + radius * math.sin(a)
        svg.append(f'<line x1="{cx}" y1="{cy}" x2="{x:.1f}" y2="{y:.1f}" stroke="#cbd5e1" stroke-width="1.2"/>')

    # Target Polygon
    target_pts = []
    for i, a in enumerate(angles):
        val = categories[i]["target"] / 100.0
        x = cx + radius * val * math.cos(a)
        y = cy + radius * val * math.sin(a)
        target_pts.append(f"{x:.1f},{y:.1f}")
    svg.append(f'<polygon points="{" ".join(target_pts)}" fill="none" stroke="#d97706" stroke-width="2.2" stroke-dasharray="6 3"/>')

    # Actual Polygon
    actual_pts = []
    for i, a in enumerate(angles):
        val = categories[i]["actual"] / 100.0
        x = cx + radius * val * math.cos(a)
        y = cy + radius * val * math.sin(a)
        actual_pts.append(f"{x:.1f},{y:.1f}")
    svg.append(f'<polygon points="{" ".join(actual_pts)}" fill="url(#actualGrad)" stroke="#2563eb" stroke-width="2.8"/>')

    for pt in actual_pts:
        px, py = pt.split(",")
        svg.append(f'<circle cx="{px}" cy="{py}" r="5.5" fill="#2563eb" stroke="#ffffff" stroke-width="2.5" filter="url(#shadow-badge)"/>')

    # Axis Labels & Metrics Badges
    label_positions = [
        {"lx": cx,       "ly": cy - radius - 36, "anchor": "middle"}, # 0: Top (Task Success)
        {"lx": cx + 195, "ly": cy - 105,         "anchor": "start"},  # 1: Top-Right (Speed)
        {"lx": cx + 195, "ly": cy + 105,         "anchor": "start"},  # 2: Bottom-Right (Error-free)
        {"lx": cx,       "ly": cy + radius + 48, "anchor": "middle"}, # 3: Bottom (SUS)
        {"lx": cx - 195, "ly": cy + 105,         "anchor": "end"},    # 4: Bottom-Left (Treejack)
        {"lx": cx - 195, "ly": cy - 105,         "anchor": "end"}     # 5: Top-Left (GOMS)
    ]

    for i, cat in enumerate(categories):
        pos = label_positions[i]
        diff = cat["actual"] - cat["target"]
        diff_str = f"+{diff:.1f}%" if diff > 0 else f"{diff:.1f}%"

        svg.append(f'<g transform="translate({pos["lx"]}, {pos["ly"]})">')
        svg.append(f'  <text x="0" y="0" font-size="12" font-weight="700" fill="#0f172a" text-anchor="{pos["anchor"]}">{cat["name"]}</text>')
        svg.append(f'  <text x="0" y="16" font-family="JetBrains Mono, monospace" font-size="11" font-weight="700" fill="#059669" text-anchor="{pos["anchor"]}">{cat["actual"]}% <tspan fill="#64748b" font-weight="400">(Эталон: {cat["target"]:.0f}%) [{diff_str}]</tspan></text>')
        svg.append('</g>')

    # ROW 3: Footer Insight Note
    svg.append(f'<g transform="translate(50, {height - 44})">')
    svg.append(f'  <rect x="0" y="0" width="{width - 100}" height="28" rx="6" fill="#f1f5f9"/>')
    svg.append('  <text x="14" y="18" font-size="11.5" fill="#475569">💡 <tspan font-weight="700" fill="#0f172a">Вывод Usability Scorecard:</tspan> Все 6 показателей выше эталона (+11.5 п.п. в среднем). Лидируют успешность (97.5%) и безошибочность (93.0%).</text>')
    svg.append('</g>')

    svg.append('</svg>')
    return "\n".join(svg)


# ==============================================================================
# 2. GOMS & TLM Time Comparison Chart
# ==============================================================================
def generate_goms_chart_svg():
    width = 1040
    height = 800

    svg = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="auto" font-family="Inter, -apple-system, BlinkMacSystemFont, sans-serif">']
    svg.append(SVG_DEFS)

    # Background Card
    svg.append('<rect width="100%" height="100%" fill="#f8fafc"/>')
    svg.append(f'<rect x="24" y="24" width="{width - 48}" height="{height - 48}" rx="16" fill="#ffffff" stroke="#e2e8f0" stroke-width="1.5" filter="url(#shadow-card)"/>')

    # ROW 1: Header (Full-width, isolated from legend)
    svg.append('<g transform="translate(50, 60)">')
    svg.append('  <text x="0" y="0" font-size="20" font-weight="800" fill="#0f172a">Моторно-когнитивный хронометраж: GOMS (Web) vs TLM (Mobile)</text>')
    svg.append('  <text x="0" y="24" font-size="12" fill="#64748b">Аналитическое моделирование операций (Card, Moran, Newell). Сокращение времени в 1.55–7.86 раза при оптимизации компоновки.</text>')
    svg.append('</g>')

    # ROW 2: Dedicated Horizontal Legend Strip (y = 105..138, ZERO overlap with bars or title)
    svg.append('<g transform="translate(50, 105)">')
    legend_items = [
        {"label": "Вар. А (Мышь)", "color": "#ef4444", "w": 150},
        {"label": "Вар. А (Tab-ввод)", "color": "#f97316", "w": 165},
        {"label": "Вар. Б (Мышь)", "color": "#3b82f6", "w": 150},
        {"label": "Вар. Б (Tab / Fast)", "color": "#10b981", "w": 165},
        {"label": "TLM Mobile Touch", "color": "#8b5cf6", "w": 170}
    ]
    cur_lx = 0
    for item in legend_items:
        svg.append(f'  <g transform="translate({cur_lx}, 0)">')
        svg.append('    <rect x="0" y="0" width="12" height="12" rx="3" fill="' + item["color"] + '"/>')
        svg.append(f'    <text x="18" y="10" font-size="11.5" font-weight="600" fill="#334155">{item["label"]}</text>')
        svg.append('  </g>')
        cur_lx += item["w"] + 20
    svg.append('</g>')

    groups = [
        {
            "title": "Форма 1: Создание митапа / CFP",
            "badge": "Ускорение: в 2.29 раза (-56.4%)",
            "badge_color": "#ecfdf5",
            "badge_text": "#047857",
            "items": [
                {"label": "Вар. А (Мышь)", "val": 32.35, "color": "url(#bar-red)", "op": "11M + 8P + 11K"},
                {"label": "Вар. А (Tab-ввод)", "val": 20.90, "color": "url(#bar-orange)", "op": "13T + 11K + 1M"},
                {"label": "Вар. Б (Мышь, 2 колонки)", "val": 24.10, "color": "url(#bar-blue)", "op": "7M + 5P + 11K"},
                {"label": "Вар. Б (Tab + Ctrl+Enter)", "val": 14.10, "color": "url(#bar-green)", "op": "8T + 11K + 1Chord"}
            ]
        },
        {
            "title": "Форма 2: Регистрация участника",
            "badge": "Ускорение: в 7.86 раза (-87.3%)",
            "badge_color": "#ecfdf5",
            "badge_text": "#047857",
            "items": [
                {"label": "Вар. А (Мышь, 6 инпутов)", "val": 38.15, "color": "url(#bar-red)", "op": "14M + 10P + 24K"},
                {"label": "Вар. А (Tab-ввод)", "val": 21.65, "color": "url(#bar-orange)", "op": "16T + 24K + 1M"},
                {"label": "Вар. Б (SSO + Мышь)", "val": 9.30, "color": "url(#bar-blue)", "op": "3M + 2P + 4K"},
                {"label": "Вар. Б (SSO + 1-Click)", "val": 4.85, "color": "url(#bar-green)", "op": "1M + 1K (Enter)"}
            ]
        },
        {
            "title": "Форма 3: Поиск и фильтрация",
            "badge": "Ускорение: в 3.54 раза (-71.7%)",
            "badge_color": "#ecfdf5",
            "badge_text": "#047857",
            "items": [
                {"label": "Вар. А (Мышь, дропдауны)", "val": 24.75, "color": "url(#bar-red)", "op": "9M + 6P + 8K"},
                {"label": "Вар. А (Tab по селектам)", "val": 15.55, "color": "url(#bar-orange)", "op": "10T + 8K"},
                {"label": "Вар. Б (Omnibox Мышь)", "val": 12.05, "color": "url(#bar-blue)", "op": "4M + 2P + 6K"},
                {"label": "Вар. Б (Omnibox ⌘K + Tab)", "val": 7.00, "color": "url(#bar-green)", "op": "1Chord + 6K + 1T"}
            ]
        },
        {
            "title": "Мобильное приложение (Touch Level Model, TLM)",
            "badge": "Сенсорный ввод: 3.85 – 6.10 с",
            "badge_color": "#f5f3ff",
            "badge_text": "#6d28d9",
            "items": [
                {"label": "Экран 1: SSO Вход (BSU ID)", "val": 3.85, "color": "url(#bar-purple)", "op": "1T_init + 1Tap + 1FaceID"},
                {"label": "Экран 2: QR Билет (Офлайн)", "val": 6.10, "color": "url(#bar-purple)", "op": "2Tap + 1Scroll + 1HMAC"},
                {"label": "Экран 3: Сканер допуска волонтёра", "val": 4.65, "color": "url(#bar-purple)", "op": "1Tap + 1CamFocus + 1Haptic"}
            ]
        }
    ]

    max_val = 40.0
    bar_start_x = 310
    max_bar_width = 460
    curr_y = 185

    # Axis grid lines
    for t_val in [10, 20, 30, 40]:
        gx = bar_start_x + (t_val / max_val) * max_bar_width
        svg.append(f'<line x1="{gx:.1f}" y1="175" x2="{gx:.1f}" y2="735" stroke="#f1f5f9" stroke-width="1.5" stroke-dasharray="3 3"/>')
        svg.append(f'<text x="{gx:.1f}" y="170" font-family="JetBrains Mono, monospace" font-size="10" fill="#94a3b8" text-anchor="middle">{t_val} с</text>')

    for g in groups:
        title_width = len(g["title"]) * 7.5
        badge_w = len(g["badge"]) * 7.0 + 20

        svg.append(f'<g transform="translate(50, {curr_y + 12})">')
        svg.append(f'  <text x="0" y="0" font-size="13" font-weight="700" fill="#0f172a">{g["title"]}</text>')
        # Badge
        svg.append(f'  <rect x="{title_width + 12}" y="-12" width="{badge_w:.0f}" height="20" rx="4" fill="{g["badge_color"]}"/>')
        svg.append(f'  <text x="{title_width + 12 + badge_w/2:.1f}" y="2" font-size="10.5" font-weight="700" fill="{g["badge_text"]}" text-anchor="middle">{g["badge"]}</text>')
        svg.append('</g>')
        curr_y += 24

        for item in g["items"]:
            w = (item["val"] / max_val) * max_bar_width
            # Left label (Right-aligned against bar start)
            svg.append(f'<text x="296" y="{curr_y + 13}" font-size="11.5" font-weight="500" fill="#475569" text-anchor="end">{item["label"]}</text>')
            # Bar with rounded corners
            svg.append(f'<rect x="{bar_start_x}" y="{curr_y}" width="{w:.1f}" height="18" rx="4" fill="{item["color"]}"/>')
            # Value Label
            svg.append(f'<text x="{bar_start_x + w + 10:.1f}" y="{curr_y + 13}" font-family="JetBrains Mono, monospace" font-size="11.5" font-weight="700" fill="#0f172a">{item["val"]:.2f} с</text>')
            # Formula / operators snippet
            svg.append(f'<text x="{bar_start_x + w + 74:.1f}" y="{curr_y + 13}" font-family="JetBrains Mono, monospace" font-size="9.5" fill="#94a3b8">[{item["op"]}]</text>')
            curr_y += 24

        curr_y += 14

    # Footer note (Concise to fit nicely within width)
    svg.append(f'<g transform="translate(50, {height - 44})">')
    svg.append(f'  <rect x="0" y="0" width="{width - 100}" height="28" rx="6" fill="#f1f5f9"/>')
    svg.append('  <text x="14" y="18" font-size="11.5" fill="#475569">⚡ <tspan font-weight="700" fill="#0f172a">Итог GOMS:</tspan> Вариант Б сокращает время ввода до 4.85 с при регистрации и 14.10 с при создании митапа (выигрыш в 2.3–7.9 раза).</text>')
    svg.append('</g>')

    svg.append('</svg>')
    return "\n".join(svg)


# ==============================================================================
# 3. SUS Distribution Chart
# ==============================================================================
def generate_sus_chart_svg():
    width = 1000
    height = 680

    svg = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="auto" font-family="Inter, -apple-system, BlinkMacSystemFont, sans-serif">']
    svg.append(SVG_DEFS)

    # Background Card
    svg.append('<rect width="100%" height="100%" fill="#f8fafc"/>')
    svg.append(f'<rect x="24" y="24" width="{width - 48}" height="{height - 48}" rx="16" fill="#ffffff" stroke="#e2e8f0" stroke-width="1.5" filter="url(#shadow-card)"/>')

    # ROW 1: Header (Full-width, zero overlap with summary strip)
    svg.append('<g transform="translate(50, 60)">')
    svg.append('  <text x="0" y="0" font-size="20" font-weight="800" fill="#0f172a">Распределение оценок SUS (System Usability Scale, N = 10)</text>')
    svg.append('  <text x="0" y="24" font-size="12" fill="#64748b">Стандартизированная оценка юзабилити по шкале Джона Брука и Бангора–Кортума–Миллера (2009)</text>')
    svg.append('</g>')

    # ROW 2: Dedicated Horizontal Summary Strip (y = 105..143, Isolated Transforms)
    svg.append('<g transform="translate(50, 105)">')
    
    # Badge 1: Mean SUS
    svg.append('  <g transform="translate(0, 0)">')
    svg.append('    <rect x="0" y="0" width="220" height="38" rx="8" fill="#ecfdf5" stroke="#a7f3d0"/>')
    svg.append('    <text x="14" y="16" font-size="9.5" font-weight="700" fill="#047857">СРЕДНИЙ БАЛЛ (MEAN SUS)</text>')
    svg.append('    <text x="14" y="30" font-family="JetBrains Mono, monospace" font-size="13" font-weight="800" fill="#065f46">85.75 • Grade A+</text>')
    svg.append('  </g>')

    # Badge 2: Percentile
    svg.append('  <g transform="translate(235, 0)">')
    svg.append('    <rect x="0" y="0" width="210" height="38" rx="8" fill="#eff6ff" stroke="#bfdbfe"/>')
    svg.append('    <text x="14" y="16" font-size="9.5" font-weight="700" fill="#1d4ed8">МИРОВОЙ ПЕРЦЕНТИЛЬ</text>')
    svg.append('    <text x="14" y="30" font-family="JetBrains Mono, monospace" font-size="13" font-weight="800" fill="#1e40af">96-й %ile (Top 4%)</text>')
    svg.append('  </g>')

    # Badge 3: Confidence Interval
    svg.append('  <g transform="translate(460, 0)">')
    svg.append('    <rect x="0" y="0" width="235" height="38" rx="8" fill="#f8fafc" stroke="#cbd5e1"/>')
    svg.append('    <text x="14" y="16" font-size="9.5" font-weight="700" fill="#475569">95% ДИ &amp; ОТКЛОНЕНИЕ</text>')
    svg.append('    <text x="14" y="30" font-family="JetBrains Mono, monospace" font-size="12" font-weight="700" fill="#0f172a">[82.54; 88.96] • s = 4.49</text>')
    svg.append('  </g>')

    # Badge 4: Range
    svg.append('  <g transform="translate(710, 0)">')
    svg.append('    <rect x="0" y="0" width="190" height="38" rx="8" fill="#f8fafc" stroke="#cbd5e1"/>')
    svg.append('    <text x="14" y="16" font-size="9.5" font-weight="700" fill="#475569">ДИАПАЗОН БАЛЛОВ</text>')
    svg.append('    <text x="14" y="30" font-family="JetBrains Mono, monospace" font-size="12" font-weight="700" fill="#0f172a">77.5 – 92.5 (все ≥ 77.5)</text>')
    svg.append('  </g>')

    svg.append('</g>')

    # Plot geometry
    sx = 65
    ew = 870
    by = 180
    bh = 340

    def to_x(val):
        return sx + (val / 100.0) * ew

    # Colored Grade Bands
    # Optimized label length and width to strictly prevent any text overflow across columns!
    bands = [
        {"from": 0, "to": 50, "fill": "#fee2e2", "border": "#fca5a5", "label": "Неприемлемо (F: &lt;50)"},
        {"from": 50, "to": 68, "fill": "#fef3c7", "border": "#fde68a", "label": "Ниже среднего (D/C: 50..68)"},
        {"from": 68, "to": 80.3, "fill": "#e0f2fe", "border": "#bae6fd", "label": "Хорошо (B)"},
        {"from": 80.3, "to": 100, "fill": "#dcfce7", "border": "#bbf7d0", "label": "Отлично / Grade A+ (≥80.3)"}
    ]

    for b in bands:
        bx1 = to_x(b["from"])
        bx2 = to_x(b["to"])
        bw = bx2 - bx1
        svg.append(f'<rect x="{bx1:.1f}" y="{by}" width="{bw:.1f}" height="{bh}" fill="{b["fill"]}" fill-opacity="0.55" stroke="{b["border"]}" stroke-width="1"/>')

        # Band Header Badge at the top of each column
        svg.append(f'<rect x="{bx1 + 4:.1f}" y="{by + 8}" width="{bw - 8:.1f}" height="22" rx="4" fill="#ffffff" fill-opacity="0.90"/>')
        svg.append(f'<text x="{(bx1 + bx2)/2:.1f}" y="{by + 23}" font-size="10.5" font-weight="700" fill="#334155" text-anchor="middle">{b["label"]}</text>')

    # Benchmark Cutoff Vertical Lines (68.0 and 80.3)
    cutoffs = [
        {"val": 68.0, "color": "#0284c7"},
        {"val": 80.3, "color": "#16a34a"}
    ]
    for c in cutoffs:
        lx = to_x(c["val"])
        svg.append(f'<line x1="{lx:.1f}" y1="{by}" x2="{lx:.1f}" y2="{by + bh}" stroke="{c["color"]}" stroke-width="2" stroke-dasharray="5 4"/>')
        # Tag at bottom of plot
        svg.append(f'<g transform="translate({lx:.1f}, {by + bh - 24})">')
        svg.append(f'  <rect x="-55" y="0" width="110" height="18" rx="4" fill="#ffffff" stroke="{c["color"]}" stroke-width="1"/>')
        svg.append(f'  <text x="0" y="12" font-size="9.5" font-weight="700" fill="{c["color"]}" text-anchor="middle">{c["val"]:.1f} порог</text>')
        svg.append('</g>')

    # Respondent Nodes (N=10)
    # ZERO OVERLAP ARCHITECTURE:
    # 77.5: U8 (left)
    # 80.0: U3 (left)
    # 82.5: U7 (left)
    # 85.0: U2, U10 -> pill points LEFT! (ends at x <= 800)
    # 85.75: Mean Line -> at x=811.0 (sits cleanly between 800 and 832)
    # 87.5: U1, U6, U9 -> pill points RIGHT! (starts at x >= 832)
    # 90.0: U5 (right)
    # 92.5: U4 (right)
    respondents = [
        {"id": "U8", "score": 77.5, "y": by + 190, "dir": "left", "role": "Студент 1к"},
        {"id": "U3", "score": 80.0, "y": by + 110, "dir": "left", "role": "Спикер митапа"},
        {"id": "U7", "score": 82.5, "y": by + 265, "dir": "left", "role": "Студент 3к"},
        # 85.0 cluster (pills point left!)
        {"id": "U2", "score": 85.0, "y": by + 80,  "dir": "left", "role": "Организатор"},
        {"id": "U10", "score": 85.0, "y": by + 160, "dir": "left", "role": "Преподаватель"},
        # 87.5 cluster (pills point right!)
        {"id": "U1", "score": 87.5, "y": by + 80,  "dir": "right", "role": "Студент 4к"},
        {"id": "U6", "score": 87.5, "y": by + 160, "dir": "right", "role": "Волонтёр"},
        {"id": "U9", "score": 87.5, "y": by + 240, "dir": "right", "role": "Студент 2к"},
        # 90.0 & 92.5
        {"id": "U5", "score": 90.0, "y": by + 120, "dir": "right", "role": "Организатор"},
        {"id": "U4", "score": 92.5, "y": by + 200, "dir": "right", "role": "Спикер"}
    ]

    for r in respondents:
        px = to_x(r["score"])
        py = r["y"]
        svg.append(f'<g transform="translate({px:.1f}, {py:.1f})">')
        # Connector line down to axis
        svg.append(f'  <line x1="0" y1="0" x2="0" y2="{by + bh - py}" stroke="#93c5fd" stroke-width="1" stroke-dasharray="2 2"/>')
        # Point node
        svg.append('  <circle cx="0" cy="0" r="5.5" fill="#2563eb" stroke="#ffffff" stroke-width="2" filter="url(#shadow-badge)"/>')

        # Directional Pill Label
        pill_w = 78
        if r["dir"] == "left":
            pill_x = -pill_w - 8
        else:
            pill_x = 8
        svg.append(f'  <rect x="{pill_x}" y="-12" width="{pill_w}" height="24" rx="5" fill="#ffffff" stroke="#cbd5e1" stroke-width="1" filter="url(#shadow-badge)"/>')
        svg.append(f'  <text x="{pill_x + pill_w/2:.1f}" y="4" font-family="JetBrains Mono, monospace" font-size="10.5" font-weight="700" fill="#0f172a" text-anchor="middle">{r["id"]}: <tspan fill="#2563eb">{r["score"]}</tspan></text>')
        svg.append('</g>')

    # Thick Mean Marker Line at 85.75
    mx = to_x(85.75)
    svg.append(f'<line x1="{mx:.1f}" y1="{by}" x2="{mx:.1f}" y2="{by + bh}" stroke="#059669" stroke-width="3"/>')
    # Mean Flag placed ABOVE the plot (y = by - 14) with downward pointer: ZERO COLLISION with band labels!
    svg.append(f'<g transform="translate({mx:.1f}, {by - 15})">')
    svg.append('  <rect x="-65" y="-22" width="130" height="24" rx="5" fill="#059669" filter="url(#shadow-badge)"/>')
    svg.append('  <text x="0" y="-6" font-family="Inter, sans-serif" font-size="11" font-weight="800" fill="#ffffff" text-anchor="middle">Среднее M = 85.75</text>')
    svg.append('  <polygon points="-5,2 5,2 0,7" fill="#059669"/>')
    svg.append('</g>')

    # X-Axis & Ticks
    svg.append(f'<line x1="{sx}" y1="{by + bh}" x2="{sx + ew}" y2="{by + bh}" stroke="#334155" stroke-width="1.5"/>')
    for tick in [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]:
        tx = to_x(tick)
        is_major = (tick % 20 == 0)
        tick_len = 8 if is_major else 4
        svg.append(f'<line x1="{tx:.1f}" y1="{by + bh}" x2="{tx:.1f}" y2="{by + bh + tick_len}" stroke="#334155" stroke-width="1.2"/>')
        svg.append(f'<text x="{tx:.1f}" y="{by + bh + 20}" font-family="JetBrains Mono, monospace" font-size="10" font-weight="600" fill="#64748b" text-anchor="middle">{tick}</text>')

    # Footer note (Concise to fit cleanly)
    svg.append(f'<g transform="translate(50, {height - 48})">')
    svg.append(f'  <rect x="0" y="0" width="{width - 100}" height="32" rx="6" fill="#f8fafc" stroke="#e2e8f0" stroke-width="1"/>')
    svg.append('  <text x="14" y="20" font-size="11.5" fill="#475569">🎯 <tspan font-weight="700" fill="#0f172a">Интерпретация Sauro &amp; Lewis (2012):</tspan> Оценка 85.75 соответствует 96-му перцентилю (Grade A+). Все 10 участников поставили ≥ 77.5 баллов.</text>')
    svg.append('</g>')

    svg.append('</svg>')
    return "\n".join(svg)


# ==============================================================================
# 4. Treejack Paths & Information Architecture Directness
# ==============================================================================
def generate_treejack_svg():
    width = 1000
    height = 700

    svg = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="auto" font-family="Inter, -apple-system, BlinkMacSystemFont, sans-serif">']
    svg.append(SVG_DEFS)

    # Background Card
    svg.append('<rect width="100%" height="100%" fill="#f8fafc"/>')
    svg.append(f'<rect x="24" y="24" width="{width - 48}" height="{height - 48}" rx="16" fill="#ffffff" stroke="#e2e8f0" stroke-width="1.5" filter="url(#shadow-card)"/>')

    # ROW 1: Header (Full-width, zero overlap with summary strip)
    svg.append('<g transform="translate(50, 60)">')
    svg.append('  <text x="0" y="0" font-size="20" font-weight="800" fill="#0f172a">Тестирование информационной архитектуры: Treejack &amp; Directness</text>')
    svg.append('  <text x="0" y="24" font-size="12" fill="#64748b">Обратная карточная сортировка древовидного меню (N = 10 респондентов, 4 ключевые сквозные задачи)</text>')
    svg.append('</g>')

    # ROW 2: Dedicated Horizontal Summary Strip (y = 105..142, Isolated Transforms)
    svg.append('<g transform="translate(50, 105)">')
    
    # Badge 1: Task Success
    svg.append('  <g transform="translate(0, 0)">')
    svg.append('    <rect x="0" y="0" width="220" height="38" rx="8" fill="#ecfdf5" stroke="#a7f3d0"/>')
    svg.append('    <text x="14" y="16" font-size="9.5" font-weight="700" fill="#047857">УСПЕШНОСТЬ (TASK SUCCESS)</text>')
    svg.append('    <text x="14" y="30" font-family="JetBrains Mono, monospace" font-size="13" font-weight="800" fill="#065f46">95.0% • 38 из 40 тестов</text>')
    svg.append('  </g>')

    # Badge 2: Directness
    svg.append('  <g transform="translate(235, 0)">')
    svg.append('    <rect x="0" y="0" width="220" height="38" rx="8" fill="#eff6ff" stroke="#bfdbfe"/>')
    svg.append('    <text x="14" y="16" font-size="9.5" font-weight="700" fill="#1d4ed8">ПРЯМИЗНА ПУТЕЙ (DIRECTNESS)</text>')
    svg.append('    <text x="14" y="30" font-family="JetBrains Mono, monospace" font-size="13" font-weight="800" fill="#1e40af">88.8% • Без блужданий</text>')
    svg.append('  </g>')

    # Badge 3: Average Time
    svg.append('  <g transform="translate(470, 0)">')
    svg.append('    <rect x="0" y="0" width="220" height="38" rx="8" fill="#f8fafc" stroke="#cbd5e1"/>')
    svg.append('    <text x="14" y="16" font-size="9.5" font-weight="700" fill="#475569">СРЕДНЕЕ ВРЕМЯ ПОИСКА</text>')
    svg.append('    <text x="14" y="30" font-family="JetBrains Mono, monospace" font-size="13" font-weight="800" fill="#0f172a">12.95 с (Ориентир: 16 с)</text>')
    svg.append('  </g>')

    # Badge 4: Test Size
    svg.append('  <g transform="translate(705, 0)">')
    svg.append('    <rect x="0" y="0" width="195" height="38" rx="8" fill="#f8fafc" stroke="#cbd5e1"/>')
    svg.append('    <text x="14" y="16" font-size="9.5" font-weight="700" fill="#475569">ОБЪЁМ ТЕСТИРОВАНИЯ</text>')
    svg.append('    <text x="14" y="30" font-family="JetBrains Mono, monospace" font-size="12" font-weight="700" fill="#0f172a">4 задачи × 10 чел.</text>')
    svg.append('  </g>')

    svg.append('</g>')

    tasks = [
        {
            "num": "01",
            "title": "Задача 1: Подача заявки спикера с докладом в секцию CFP",
            "steps": ["События", "AI Tech Meetup", "Программа &amp; CFP", "Подать доклад"],
            "success": 100,
            "success_sub": "10 из 10 тестов",
            "directness": 90,
            "directness_sub": "прямой путь",
            "time": "12.4 с",
            "target_time": "15.0 с"
        },
        {
            "num": "02",
            "title": "Задача 2: Выгрузка CSV-списка участников для печати бейджей",
            "steps": ["Кабинет организатора", "Мои митапы", "Участники", "Экспорт CSV"],
            "success": 90,
            "success_sub": "9 из 10 тестов",
            "directness": 80,
            "directness_sub": "1 возврат",
            "time": "16.8 с",
            "target_time": "20.0 с"
        },
        {
            "num": "03",
            "title": "Задача 3: Поиск сохраненного офлайн QR-билета в кошельке",
            "steps": ["Мой профиль", "Мои билеты", "Офлайн-билет (HMAC)"],
            "success": 100,
            "success_sub": "10 из 10 тестов",
            "directness": 100,
            "directness_sub": "без возвратов",
            "time": "8.5 с",
            "target_time": "10.0 с"
        },
        {
            "num": "04",
            "title": "Задача 4: Активация пакетного офлайн-сканера допуска волонтёра",
            "steps": ["Кабинет волонтёра", "Сканер допуска", "Офлайн-пакет"],
            "success": 90,
            "success_sub": "9 из 10 тестов",
            "directness": 85,
            "directness_sub": "1 возврат",
            "time": "14.1 с",
            "target_time": "18.0 с"
        }
    ]

    card_y = 165
    card_w = width - 100
    card_h = 102

    for t in tasks:
        # Card container
        svg.append(f'<g transform="translate(50, {card_y})">')
        svg.append(f'  <rect x="0" y="0" width="{card_w}" height="{card_h}" rx="10" fill="#f8fafc" stroke="#e2e8f0" stroke-width="1.2"/>')

        # Task Number Badge
        svg.append('  <rect x="16" y="14" width="28" height="22" rx="4" fill="#0f172a"/>')
        svg.append(f'  <text x="30" y="29" font-family="JetBrains Mono, monospace" font-size="11" font-weight="700" fill="#ffffff" text-anchor="middle">{t["num"]}</text>')

        # Title: Full clear run from x=52 to x=630 (578px space!), ZERO collision with anything
        svg.append(f'  <text x="52" y="30" font-size="13.5" font-weight="700" fill="#0f172a">{t["title"]}</text>')

        # Breadcrumb Steps Chips (Row decoupled at y=52, ends comfortably before x=630)
        chip_x = 16
        svg.append(f'  <g transform="translate({chip_x}, 52)">')
        cur_cx = 0
        for s_idx, step in enumerate(t["steps"]):
            is_last = (s_idx == len(t["steps"]) - 1)
            step_clean = step.replace('&amp;', '&')
            step_w = len(step_clean) * 7.0 + 16
            bg_color = "#dbeafe" if is_last else "#ffffff"
            text_color = "#1d4ed8" if is_last else "#475569"
            border_color = "#bfdbfe" if is_last else "#cbd5e1"

            svg.append(f'    <rect x="{cur_cx}" y="0" width="{step_w:.0f}" height="24" rx="4" fill="{bg_color}" stroke="{border_color}" stroke-width="1"/>')
            svg.append(f'    <text x="{cur_cx + step_w/2:.1f}" y="16" font-family="JetBrains Mono, monospace" font-size="10" font-weight="600" fill="{text_color}" text-anchor="middle">{step}</text>')
            cur_cx += step_w + 6

            if not is_last:
                svg.append(f'    <text x="{cur_cx}" y="16" font-size="11" font-weight="700" fill="#94a3b8">→</text>')
                cur_cx += 14

        svg.append('  </g>')

        # Right-aligned Metric Badges (Start at x = 640 to 884, ZERO collision)
        svg.append('  <g transform="translate(640, 16)">')

        # 1. Success badge
        svg.append('    <rect x="0" y="0" width="76" height="68" rx="6" fill="#ecfdf5" stroke="#a7f3d0"/>')
        svg.append('    <text x="38" y="18" font-size="9" font-weight="700" fill="#047857" text-anchor="middle">УСПЕХ</text>')
        svg.append(f'    <text x="38" y="42" font-family="JetBrains Mono, monospace" font-size="15" font-weight="800" fill="#065f46" text-anchor="middle">{t["success"]}%</text>')
        svg.append(f'    <text x="38" y="58" font-size="8.5" fill="#059669" text-anchor="middle">{t["success_sub"]}</text>')

        # 2. Directness badge
        svg.append('    <rect x="84" y="0" width="76" height="68" rx="6" fill="#eff6ff" stroke="#bfdbfe"/>')
        svg.append('    <text x="122" y="18" font-size="9" font-weight="700" fill="#1d4ed8" text-anchor="middle">ПРЯМИЗНА</text>')
        svg.append(f'    <text x="122" y="42" font-family="JetBrains Mono, monospace" font-size="15" font-weight="800" fill="#1e40af" text-anchor="middle">{t["directness"]}%</text>')
        svg.append(f'    <text x="122" y="58" font-size="8.5" fill="#2563eb" text-anchor="middle">{t["directness_sub"]}</text>')

        # 3. Time-on-task badge
        svg.append('    <rect x="168" y="0" width="76" height="68" rx="6" fill="#ffffff" stroke="#cbd5e1"/>')
        svg.append('    <text x="206" y="18" font-size="9" font-weight="700" fill="#475569" text-anchor="middle">ВРЕМЯ</text>')
        svg.append(f'    <text x="206" y="42" font-family="JetBrains Mono, monospace" font-size="14" font-weight="800" fill="#0f172a" text-anchor="middle">{t["time"]}</text>')
        svg.append(f'    <text x="206" y="58" font-size="8.5" fill="#64748b" text-anchor="middle">≤ {t["target_time"]}</text>')

        svg.append('  </g>')

        svg.append('</g>')
        card_y += 116

    # ROW 3: Footer Insight Note
    svg.append(f'<g transform="translate(50, {height - 44})">')
    svg.append(f'  <rect x="0" y="0" width="{width - 100}" height="28" rx="6" fill="#f1f5f9"/>')
    svg.append('  <text x="14" y="18" font-size="11.5" fill="#475569">🌲 <tspan font-weight="700" fill="#0f172a">Вывод Treejack:</tspan> Информационная архитектура эффективна: прямолинейность 88.8% и среднее время 12.95 с подтверждают логичность меню.</text>')
    svg.append('</g>')

    svg.append('</svg>')
    return "\n".join(svg)


def main():
    print("Generating Lab 6 SVGs...")

    # 1. Usability Radar
    radar_content = generate_radar_svg()
    (OUT_DIR / "usability_scorecard_radar.svg").write_text(radar_content, encoding="utf-8")
    print("✓ usability_scorecard_radar.svg written")

    # 2. GOMS Bar Chart
    goms_content = generate_goms_chart_svg()
    (OUT_DIR / "goms_tlm_comparison.svg").write_text(goms_content, encoding="utf-8")
    print("✓ goms_tlm_comparison.svg written")

    # 3. SUS Distribution
    sus_content = generate_sus_chart_svg()
    (OUT_DIR / "sus_distribution_chart.svg").write_text(sus_content, encoding="utf-8")
    print("✓ sus_distribution_chart.svg written")

    # 4. Treejack Paths
    treejack_content = generate_treejack_svg()
    (OUT_DIR / "treejack_paths_ia.svg").write_text(treejack_content, encoding="utf-8")
    print("✓ treejack_paths_ia.svg written")

    print("\nAll 4 diagrams generated successfully!")


if __name__ == "__main__":
    main()
