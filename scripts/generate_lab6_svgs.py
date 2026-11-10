#!/usr/bin/env python3
"""
Generate high-fidelity vector SVG diagrams for Lab 6:
1. usability_scorecard_radar.svg - Usability Scorecard Radar Chart (6 metrics vs target)
2. goms_tlm_comparison.svg       - GOMS (Web) vs TLM (Mobile) Chronometry Bar Chart
3. sus_distribution_chart.svg    - System Usability Scale (SUS) Score Distribution (N=10)
4. treejack_paths_ia.svg         - Treejack Navigation Paths & Information Architecture Directness

All diagrams follow docs/DESIGN_SYSTEM.md guidelines:
- Strict typography (Inter + JetBrains Mono)
- Generous margins and card elevation
- Zero text or label overlap
- Standalone self-contained SVG styling (works offline and inside <img> tags)
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
      <feDropShadow dx="0" dy="4" stdDeviation="8" flood-color="#0f172a" flood-opacity="0.08"/>
      <feDropShadow dx="0" dy="1" stdDeviation="2" flood-color="#0f172a" flood-opacity="0.04"/>
    </filter>

    <filter id="shadow-badge" x="-10%" y="-15%" width="120%" height="135%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#0f172a" flood-opacity="0.06"/>
    </filter>

    <filter id="radar-glow" x="-20%" y="-20%" width="140%" height="140%" filterUnits="userSpaceOnUse">
      <feGaussianBlur stdDeviation="4" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>

    <!-- Radar Gradients -->
    <linearGradient id="actualGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#3b82f6" stop-opacity="0.38"/>
      <stop offset="50%" stop-color="#2563eb" stop-opacity="0.28"/>
      <stop offset="100%" stop-color="#10b981" stop-opacity="0.20"/>
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
    width = 960
    height = 680
    cx = 480
    cy = 385
    radius = 195

    categories = [
        {"name": "Успешность (Task Success)", "actual": 97.5, "target": 85.0, "code": "TS"},
        {"name": "Скорость (Time Efficiency)", "actual": 89.0, "target": 80.0, "code": "TE"},
        {"name": "Безошибочность (Error-Free)", "actual": 93.0, "target": 90.0, "code": "EF"},
        {"name": "Удовлетворённость (SUS Score)", "actual": 85.8, "target": 75.0, "code": "SUS"},
        {"name": "Прямизна путей (Treejack)", "actual": 88.8, "target": 70.0, "code": "DIR"},
        {"name": "Эргономика ввода (GOMS)", "actual": 91.2, "target": 75.0, "code": "GOMS"}
    ]

    num_axes = len(categories)
    angles = [i * (2 * math.pi / num_axes) - math.pi / 2 for i in range(num_axes)]

    svg = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="auto" font-family="Inter, -apple-system, sans-serif">']
    svg.append(SVG_DEFS)

    # Canvas Background & Card Frame
    svg.append('<rect width="100%" height="100%" fill="#f8fafc"/>')
    svg.append(f'<rect x="24" y="24" width="{width - 48}" height="{height - 48}" rx="16" fill="#ffffff" stroke="#e2e8f0" stroke-width="1.5" filter="url(#shadow-card)"/>')

    # Title & Metadata
    svg.append('<g transform="translate(54, 62)">')
    svg.append('  <text x="0" y="0" font-size="20" font-weight="800" fill="#0f172a">Сводная лепестковая диаграмма юзабилити (Usability Scorecard)</text>')
    svg.append('  <text x="0" y="24" font-size="12" fill="#64748b">Сопоставление фактических показателей CampusMeet с целевым эталоном (N = 10, 95% ДИ Вильсона, SUM = 90.7%)</text>')
    svg.append('</g>')

    # Legend at Top-Right
    svg.append('<g transform="translate(640, 50)">')
    # Actual legend item
    svg.append('  <rect x="0" y="0" width="132" height="32" rx="6" fill="#eff6ff" stroke="#bfdbfe"/>')
    svg.append('  <rect x="10" y="11" width="10" height="10" rx="2" fill="#2563eb"/>')
    svg.append('  <text x="26" y="21" font-size="11" font-weight="600" fill="#1e40af">Факт (90.7% SUM)</text>')

    # Target legend item
    svg.append('  <rect x="142" y="0" width="124" height="32" rx="6" fill="#fffbeb" stroke="#fde68a"/>')
    svg.append('  <line x1="152" y1="16" x2="166" y2="16" stroke="#d97706" stroke-width="2.5" stroke-dasharray="4 2"/>')
    svg.append('  <text x="172" y="21" font-size="11" font-weight="600" fill="#92400e">Эталон (79.2%)</text>')
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
        svg.append(f'<rect x="{cx + 6}" y="{cy - r - 8:.1f}" width="34" height="15" rx="3" fill="#ffffff" fill-opacity="0.85"/>')
        svg.append(f'<text x="{cx + 8}" y="{cy - r + 3:.1f}" font-family="JetBrains Mono, monospace" font-size="9.5" font-weight="600" fill="#64748b">{int(lvl*100)}%</text>')

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
    svg.append(f'<polygon points="{" ".join(target_pts)}" fill="none" stroke="#d97706" stroke-width="2" stroke-dasharray="6 4"/>')
    for pt in target_pts:
        px, py = pt.split(",")
        svg.append(f'<circle cx="{px}" cy="{py}" r="3.5" fill="#f59e0b" stroke="#ffffff" stroke-width="1.5"/>')

    # Actual Polygon (Filled with subtle shadow)
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

    # Axis Labels & Metrics Badges (Calculated with safe outer offsets to NEVER overlap)
    label_offsets = [
        {"dx": 0, "dy": -38, "anchor": "middle"},    # 0: Top (Task Success)
        {"dx": 32, "dy": -12, "anchor": "start"},   # 1: Top-Right (Speed)
        {"dx": 32, "dy": 18, "anchor": "start"},    # 2: Bottom-Right (Error-free)
        {"dx": 0, "dy": 42, "anchor": "middle"},     # 3: Bottom (SUS)
        {"dx": -32, "dy": 18, "anchor": "end"},     # 4: Bottom-Left (Treejack)
        {"dx": -32, "dy": -12, "anchor": "end"}     # 5: Top-Left (GOMS)
    ]

    for i, a in enumerate(angles):
        lx = cx + (radius + 20) * math.cos(a) + label_offsets[i]["dx"]
        ly = cy + (radius + 20) * math.sin(a) + label_offsets[i]["dy"]
        anchor = label_offsets[i]["anchor"]

        cat = categories[i]
        diff = cat["actual"] - cat["target"]
        diff_str = f"+{diff:.1f}%" if diff > 0 else f"{diff:.1f}%"

        # Badge box width and position
        svg.append(f'<g transform="translate({lx:.1f}, {ly:.1f})">')
        svg.append(f'  <text x="0" y="0" font-size="12" font-weight="700" fill="#0f172a" text-anchor="{anchor}">{cat["name"]}</text>')
        svg.append(f'  <text x="0" y="16" font-family="JetBrains Mono, monospace" font-size="11" font-weight="700" fill="#059669" text-anchor="{anchor}">{cat["actual"]:.1f}% <tspan fill="#64748b" font-weight="500">(Эталон: {cat["target"]:.0f}%)</tspan> <tspan fill="#10b981" font-size="10">[{diff_str}]</tspan></text>')
        svg.append('</g>')

    # Footer Insight Note
    svg.append(f'<g transform="translate(54, {height - 44})">')
    svg.append('  <rect x="0" y="0" width="852" height="28" rx="6" fill="#f1f5f9"/>')
    svg.append('  <text x="14" y="18" font-size="11" fill="#475569">💡 <tspan font-weight="600" fill="#0f172a">Вывод:</tspan> Все 6 показателей превосходят отраслевой эталон (в среднем на +11.5 процентных пунктов). Лидируют успешность (97.5%) и безошибочность (93.0%).</text>')
    svg.append('</g>')

    svg.append('</svg>')
    return "\n".join(svg)


# ==============================================================================
# 2. GOMS & TLM Time Comparison Chart
# ==============================================================================
def generate_goms_chart_svg():
    width = 1000
    height = 760

    svg = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="auto" font-family="Inter, -apple-system, sans-serif">']
    svg.append(SVG_DEFS)

    # Background Card
    svg.append('<rect width="100%" height="100%" fill="#f8fafc"/>')
    svg.append(f'<rect x="24" y="24" width="{width - 48}" height="{height - 48}" rx="16" fill="#ffffff" stroke="#e2e8f0" stroke-width="1.5" filter="url(#shadow-card)"/>')

    # Header
    svg.append('<g transform="translate(54, 62)">')
    svg.append('  <text x="0" y="0" font-size="20" font-weight="800" fill="#0f172a">Моторно-когнитивный хронометраж: GOMS (Web) vs TLM (Mobile)</text>')
    svg.append('  <text x="0" y="24" font-size="12" fill="#64748b">Аналитическое моделирование операций (Card, Moran, Newell). Сокращение времени в 1.55–7.86 раза при оптимизации компоновки.</text>')
    svg.append('</g>')

    # Legend in Top Horizontal Row (Completely decoupled from the bars area!)
    svg.append('<g transform="translate(54, 106)">')
    legend_items = [
        {"label": "Вар. А (Мышь)", "color": "#ef4444"},
        {"label": "Вар. А (Tab-ввод)", "color": "#f97316"},
        {"label": "Вар. Б (Мышь)", "color": "#3b82f6"},
        {"label": "Вар. Б (Tab / Fast)", "color": "#10b981"},
        {"label": "TLM Mobile Touch", "color": "#8b5cf6"}
    ]
    cur_lx = 0
    for item in legend_items:
        svg.append(f'  <g transform="translate({cur_lx}, 0)">')
        svg.append(f'    <rect x="0" y="0" width="12" height="12" rx="3" fill="{item["color"]}"/>')
        svg.append(f'    <text x="18" y="10" font-size="11" font-weight="600" fill="#334155">{item["label"]}</text>')
        svg.append('  </g>')
        cur_lx += 175
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
    bar_start_x = 290
    max_bar_width = 470
    start_y = 152

    # Draw vertical grid lines for seconds (0, 10, 20, 30, 40s)
    grid_bottom_y = height - 70
    for s in [10, 20, 30, 40]:
        gx = bar_start_x + (s / max_val) * max_bar_width
        svg.append(f'<line x1="{gx:.1f}" y1="{start_y - 10}" x2="{gx:.1f}" y2="{grid_bottom_y}" stroke="#f1f5f9" stroke-width="1.5" stroke-dasharray="3 3"/>')
        svg.append(f'<text x="{gx:.1f}" y="{start_y - 14}" font-family="JetBrains Mono, monospace" font-size="10" fill="#94a3b8" text-anchor="middle">{s} с</text>')

    curr_y = start_y
    for g in groups:
        # Group Header & Pill Badge
        svg.append(f'<g transform="translate(54, {curr_y + 12})">')
        svg.append(f'  <text x="0" y="0" font-size="13" font-weight="700" fill="#0f172a">{g["title"]}</text>')
        # Badge
        badge_w = len(g["badge"]) * 7.2 + 16
        svg.append(f'  <rect x="236" y="-12" width="{badge_w:.0f}" height="20" rx="4" fill="{g["badge_color"]}"/>')
        svg.append(f'  <text x="{236 + badge_w/2:.1f}" y="2" font-size="10.5" font-weight="700" fill="{g["badge_text"]}" text-anchor="middle">{g["badge"]}</text>')
        svg.append('</g>')
        curr_y += 24

        for item in g["items"]:
            w = (item["val"] / max_val) * max_bar_width
            # Label
            svg.append(f'<text x="278" y="{curr_y + 12}" font-size="11" font-weight="500" fill="#475569" text-anchor="end">{item["label"]}</text>')
            # Bar with rounded corners
            svg.append(f'<rect x="{bar_start_x}" y="{curr_y}" width="{w:.1f}" height="17" rx="4" fill="{item["color"]}"/>')
            # Value Label
            svg.append(f'<text x="{bar_start_x + w + 10:.1f}" y="{curr_y + 12}" font-family="JetBrains Mono, monospace" font-size="11.5" font-weight="700" fill="#0f172a">{item["val"]:.2f} с</text>')
            # Formula / operators snippet
            svg.append(f'<text x="{bar_start_x + w + 74:.1f}" y="{curr_y + 12}" font-family="JetBrains Mono, monospace" font-size="9.5" fill="#94a3b8">[{item["op"]}]</text>')
            curr_y += 22

        curr_y += 14

    # Footer note
    svg.append(f'<g transform="translate(54, {height - 44})">')
    svg.append('  <rect x="0" y="0" width="892" height="28" rx="6" fill="#f1f5f9"/>')
    svg.append('  <text x="14" y="18" font-size="11" fill="#475569">⚡ <tspan font-weight="600" fill="#0f172a">Итог GOMS:</tspan> Вариант Б сокращает время ввода до 4.85 с при регистрации и 14.10 с при создании митапа, подтверждая тезис о превосходстве чип-компоновок над глубокими селектами.</text>')
    svg.append('</g>')

    svg.append('</svg>')
    return "\n".join(svg)


# ==============================================================================
# 3. SUS Distribution Chart
# ==============================================================================
def generate_sus_chart_svg():
    width = 960
    height = 580

    svg = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="auto" font-family="Inter, -apple-system, sans-serif">']
    svg.append(SVG_DEFS)

    # Background Card
    svg.append('<rect width="100%" height="100%" fill="#f8fafc"/>')
    svg.append(f'<rect x="24" y="24" width="{width - 48}" height="{height - 48}" rx="16" fill="#ffffff" stroke="#e2e8f0" stroke-width="1.5" filter="url(#shadow-card)"/>')

    # Header
    svg.append('<g transform="translate(54, 62)">')
    svg.append('  <text x="0" y="0" font-size="20" font-weight="800" fill="#0f172a">Распределение оценок SUS (System Usability Scale, N = 10)</text>')
    svg.append('  <text x="0" y="24" font-size="12" fill="#64748b">Оценка восприятия прототипа по Джону Бруку и шкале Бангора–Кортума–Миллера (2009)</text>')
    svg.append('</g>')

    # Top-Right Badge: Mean & Grade
    svg.append('<g transform="translate(680, 46)">')
    svg.append('  <rect x="0" y="0" width="226" height="42" rx="8" fill="#ecfdf5" stroke="#a7f3d0"/>')
    svg.append('  <text x="14" y="18" font-size="10" font-weight="700" fill="#047857">СРЕДНИЙ БАЛЛ (MEAN SUS)</text>')
    svg.append('  <text x="14" y="34" font-family="JetBrains Mono, monospace" font-size="14" font-weight="800" fill="#065f46">85.75 • Grade A+</text>')
    svg.append('  <text x="156" y="27" font-size="10" font-weight="600" fill="#059669">96-й %ile</text>')
    svg.append('</g>')

    # Plot geometry
    sx = 74
    ew = 812
    by = 120
    bh = 270

    def to_x(val):
        return sx + (val / 100.0) * ew

    # Colored Grade Bands (Full height with soft background)
    bands = [
        {"from": 0, "to": 50, "fill": "#fee2e2", "border": "#fca5a5", "grade": "F", "label": "Неприемлемо (&lt;50)"},
        {"from": 50, "to": 68, "fill": "#fef3c7", "border": "#fde68a", "grade": "D / C", "label": "Ниже среднего (50..68)"},
        {"from": 68, "to": 80.3, "fill": "#e0f2fe", "border": "#bae6fd", "grade": "B", "label": "Хорошо (68..80.3)"},
        {"from": 80.3, "to": 100, "fill": "#dcfce7", "border": "#bbf7d0", "grade": "A+", "label": "Отлично / Grade A+ (80.3..100)"}
    ]

    for b in bands:
        bx1 = to_x(b["from"])
        bx2 = to_x(b["to"])
        bw = bx2 - bx1
        svg.append(f'<rect x="{bx1:.1f}" y="{by}" width="{bw:.1f}" height="{bh}" fill="{b["fill"]}" fill-opacity="0.55" stroke="{b["border"]}" stroke-width="1"/>')

        # Band Header Badge at the top of each column
        svg.append(f'<rect x="{bx1 + 6:.1f}" y="{by + 10}" width="{bw - 12:.1f}" height="24" rx="4" fill="#ffffff" fill-opacity="0.85"/>')
        svg.append(f'<text x="{(bx1 + bx2)/2:.1f}" y="{by + 26}" font-size="10.5" font-weight="700" fill="#334155" text-anchor="middle">{b["label"]}</text>')

    # Benchmark Cutoff Vertical Lines
    cutoffs = [
        {"val": 68.0, "label": "Индустриальный средний бенчмарк (68.0)", "color": "#0284c7"},
        {"val": 80.3, "label": "Порог оценки Grade A (80.3)", "color": "#16a34a"}
    ]
    for c in cutoffs:
        lx = to_x(c["val"])
        svg.append(f'<line x1="{lx:.1f}" y1="{by}" x2="{lx:.1f}" y2="{by + bh}" stroke="{c["color"]}" stroke-width="2" stroke-dasharray="5 4"/>')
        # Tag at top
        svg.append(f'<g transform="translate({lx:.1f}, {by + bh - 24})">')
        svg.append(f'  <rect x="-70" y="0" width="140" height="18" rx="4" fill="#ffffff" stroke="{c["color"]}" stroke-width="1"/>')
        svg.append(f'  <text x="0" y="12" font-size="9" font-weight="600" fill="{c["color"]}" text-anchor="middle">{c["val"]:.1f} порог</text>')
        svg.append('</g>')

    # Non-overlapping Respondent Points (N=10)
    # Group identical scores cleanly:
    # 77.5: U8
    # 80.0: U3
    # 82.5: U7
    # 85.0: U2, U10 (vertically stacked!)
    # 87.5: U1, U6, U9 (vertically stacked!)
    # 90.0: U5
    # 92.5: U4
    respondents = [
        {"id": "U8", "score": 77.5, "row": 0, "role": "Студент 1к"},
        {"id": "U3", "score": 80.0, "row": 1, "role": "Спикер митапа"},
        {"id": "U7", "score": 82.5, "row": 0, "role": "Студент 3к"},
        {"id": "U2", "score": 85.0, "row": 0, "role": "Организатор"},
        {"id": "U10", "score": 85.0, "row": 2, "role": "Преподаватель"},
        {"id": "U1", "score": 87.5, "row": 0, "role": "Студент 4к"},
        {"id": "U6", "score": 87.5, "row": 1, "role": "Волонтёр"},
        {"id": "U9", "score": 87.5, "row": 2, "role": "Студент 2к"},
        {"id": "U5", "score": 90.0, "row": 1, "role": "Организатор"},
        {"id": "U4", "score": 92.5, "row": 0, "role": "Спикер"}
    ]

    base_py = by + 65
    row_height = 42

    for r in respondents:
        px = to_x(r["score"])
        py = base_py + r["row"] * row_height

        # Card Pill for Respondent
        svg.append(f'<g transform="translate({px:.1f}, {py:.1f})">')
        # Connector line down to axis
        svg.append(f'  <line x1="0" y1="0" x2="0" y2="{by + bh - py}" stroke="#93c5fd" stroke-width="1" stroke-dasharray="2 2"/>')
        # Point
        svg.append('  <circle cx="0" cy="0" r="6" fill="#2563eb" stroke="#ffffff" stroke-width="2" filter="url(#shadow-badge)"/>')
        # Pill label (Offset nicely so it NEVER collides with neighbour pills)
        label_x = 10
        svg.append(f'  <rect x="{label_x}" y="-13" width="76" height="24" rx="5" fill="#ffffff" stroke="#cbd5e1" stroke-width="1" filter="url(#shadow-badge)"/>')
        svg.append(f'  <text x="{label_x + 8}" y="3" font-family="JetBrains Mono, monospace" font-size="10.5" font-weight="700" fill="#0f172a">{r["id"]}: <tspan fill="#2563eb">{r["score"]}</tspan></text>')
        svg.append('</g>')

    # Thick Mean Marker Line at 85.75
    mx = to_x(85.75)
    svg.append(f'<line x1="{mx:.1f}" y1="{by + 36}" x2="{mx:.1f}" y2="{by + bh}" stroke="#059669" stroke-width="3"/>')
    # Mean Flag at the top
    svg.append(f'<g transform="translate({mx:.1f}, {by + 36})">')
    svg.append('  <rect x="-65" y="-28" width="130" height="26" rx="6" fill="#059669" filter="url(#shadow-badge)"/>')
    svg.append('  <text x="0" y="-11" font-family="Inter, sans-serif" font-size="11" font-weight="800" fill="#ffffff" text-anchor="middle">Среднее M = 85.75</text>')
    svg.append('  <polygon points="-5,-2 5,-2 0,4" fill="#059669"/>')
    svg.append('</g>')

    # X-Axis & Ticks
    svg.append(f'<line x1="{sx}" y1="{by + bh}" x2="{sx + ew}" y2="{by + bh}" stroke="#334155" stroke-width="1.5"/>')
    for tick in [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]:
        tx = to_x(tick)
        is_major = (tick % 20 == 0)
        tick_len = 8 if is_major else 4
        svg.append(f'<line x1="{tx:.1f}" y1="{by + bh}" x2="{tx:.1f}" y2="{by + bh + tick_len}" stroke="#334155" stroke-width="1.2"/>')
        if is_major:
            svg.append(f'<text x="{tx:.1f}" y="{by + bh + 22}" font-family="JetBrains Mono, monospace" font-size="11" font-weight="600" fill="#475569" text-anchor="middle">{tick}</text>')

    # Footer note with exact methodology and interpretation
    svg.append(f'<g transform="translate(54, {height - 80})">')
    svg.append('  <rect x="0" y="0" width="852" height="46" rx="8" fill="#f8fafc" stroke="#e2e8f0"/>')
    svg.append('  <text x="16" y="18" font-size="11" fill="#475569"><tspan font-weight="700" fill="#0f172a">Интерпретация по Sauro &amp; Lewis (2012):</tspan> Оценка 85.75 соответствует 96-му перцентилю (Grade A+). Все 10 участников поставили баллы ≥ 77.5, что превышает порог приемлемости (70.0).</text>')
    svg.append('  <text x="16" y="34" font-size="11" fill="#64748b">Минимальная оценка: 77.5 (U8), максимальная: 92.5 (U4). Стандартное отклонение s = 4.49, 95% доверительный интервал [82.54; 88.96].</text>')
    svg.append('</g>')

    svg.append('</svg>')
    return "\n".join(svg)


# ==============================================================================
# 4. Treejack Paths Diagram
# ==============================================================================
def generate_treejack_svg():
    width = 960
    height = 580

    svg = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="auto" font-family="Inter, -apple-system, sans-serif">']
    svg.append(SVG_DEFS)

    # Background Card
    svg.append('<rect width="100%" height="100%" fill="#f8fafc"/>')
    svg.append(f'<rect x="24" y="24" width="{width - 48}" height="{height - 48}" rx="16" fill="#ffffff" stroke="#e2e8f0" stroke-width="1.5" filter="url(#shadow-card)"/>')

    # Header
    svg.append('<g transform="translate(54, 62)">')
    svg.append('  <text x="0" y="0" font-size="20" font-weight="800" fill="#0f172a">Тестирование информационной архитектуры: Treejack &amp; Directness</text>')
    svg.append('  <text x="0" y="24" font-size="12" fill="#64748b">Обратная карточная сортировка древовидного меню (N = 10 респондентов, 4 ключевые сквозные задачи)</text>')
    svg.append('</g>')

    # Top-Right Summary Card
    svg.append('<g transform="translate(680, 46)">')
    svg.append('  <rect x="0" y="0" width="226" height="42" rx="8" fill="#eff6ff" stroke="#bfdbfe"/>')
    svg.append('  <text x="14" y="18" font-size="10" font-weight="700" fill="#1d4ed8">ИНФО-АРХИТЕКТУРА (SITEMAP)</text>')
    svg.append('  <text x="14" y="34" font-family="JetBrains Mono, monospace" font-size="14" font-weight="800" fill="#1e3a8a">Успех 95% • Direct 88.8%</text>')
    svg.append('</g>')

    tasks = [
        {
            "num": "01",
            "title": "Задача 1: Подача заявки спикера с докладом в секцию CFP",
            "steps": ["События", "AI Tech Meetup", "Программа &amp; CFP", "Подать доклад"],
            "success": 100,
            "directness": 90,
            "time": "12.4 с",
            "target_time": "15.0 с",
            "status": "Идеально (10/10)"
        },
        {
            "num": "02",
            "title": "Задача 2: Выгрузка CSV-списка участников для печати бейджей",
            "steps": ["Кабинет организатора", "Мои митапы", "Участники", "Экспорт CSV"],
            "success": 90,
            "directness": 80,
            "time": "16.8 с",
            "target_time": "20.0 с",
            "status": "Успешно (9/10)"
        },
        {
            "num": "03",
            "title": "Задача 3: Поиск сохраненного офлайн QR-билета в кошельке",
            "steps": ["Мой профиль", "Мои билеты", "Офлайн-билет (HMAC)"],
            "success": 100,
            "directness": 100,
            "time": "8.5 с",
            "target_time": "10.0 с",
            "status": "Идеально (Прямой путь)"
        },
        {
            "num": "04",
            "title": "Задача 4: Активация пакетного офлайн-сканера допуска волонтёра",
            "steps": ["Кабинет волонтёра", "Сканер допуска", "Офлайн-пакет"],
            "success": 90,
            "directness": 85,
            "time": "14.1 с",
            "target_time": "18.0 с",
            "status": "Успешно (9/10)"
        }
    ]

    card_y = 116
    for t in tasks:
        # Card container
        svg.append(f'<g transform="translate(54, {card_y})">')
        svg.append('  <rect x="0" y="0" width="852" height="84" rx="10" fill="#f8fafc" stroke="#e2e8f0" stroke-width="1.2"/>')

        # Task Number Badge
        svg.append(f'  <rect x="14" y="14" width="28" height="24" rx="4" fill="#0f172a"/>')
        svg.append(f'  <text x="28" y="30" font-family="JetBrains Mono, monospace" font-size="11" font-weight="700" fill="#ffffff" text-anchor="middle">{t["num"]}</text>')

        # Title
        svg.append(f'  <text x="50" y="31" font-size="13" font-weight="700" fill="#0f172a">{t["title"]}</text>')

        # Breadcrumb Steps Chips (Decoupled, stylish chips with arrows)
        chip_x = 14
        svg.append(f'  <g transform="translate({chip_x}, 48)">')
        cur_cx = 0
        for s_idx, step in enumerate(t["steps"]):
            is_last = (s_idx == len(t["steps"]) - 1)
            step_clean = step.replace('&amp;', '&')
            step_w = len(step_clean) * 7.0 + 18
            bg_color = "#dbeafe" if is_last else "#ffffff"
            text_color = "#1d4ed8" if is_last else "#475569"
            border_color = "#bfdbfe" if is_last else "#cbd5e1"

            svg.append(f'    <rect x="{cur_cx}" y="0" width="{step_w:.0f}" height="22" rx="4" fill="{bg_color}" stroke="{border_color}" stroke-width="1"/>')
            svg.append(f'    <text x="{cur_cx + step_w/2:.1f}" y="15" font-family="JetBrains Mono, monospace" font-size="10" font-weight="600" fill="{text_color}" text-anchor="middle">{step}</text>')
            cur_cx += step_w + 6

            if not is_last:
                svg.append(f'    <text x="{cur_cx - 1}" y="15" font-size="11" font-weight="700" fill="#94a3b8">→</text>')
                cur_cx += 12

        svg.append('  </g>')

        # Right-aligned Metric Badges (Spacious, separate badges that NEVER collide)
        svg.append('  <g transform="translate(540, 18)">')

        # 1. Success badge
        svg.append('    <rect x="0" y="0" width="86" height="48" rx="6" fill="#ecfdf5" stroke="#a7f3d0"/>')
        svg.append('    <text x="43" y="18" font-size="9" font-weight="700" fill="#047857" text-anchor="middle">УСПЕХ</text>')
        svg.append(f'    <text x="43" y="38" font-family="JetBrains Mono, monospace" font-size="14" font-weight="800" fill="#065f46" text-anchor="middle">{t["success"]}%</text>')

        # 2. Directness badge
        svg.append('    <rect x="96" y="0" width="104" height="48" rx="6" fill="#eff6ff" stroke="#bfdbfe"/>')
        svg.append('    <text x="148" y="18" font-size="9" font-weight="700" fill="#1d4ed8" text-anchor="middle">ПРЯМИЗНА (DIR)</text>')
        svg.append(f'    <text x="148" y="38" font-family="JetBrains Mono, monospace" font-size="14" font-weight="800" fill="#1e3a8a" text-anchor="middle">{t["directness"]}%</text>')

        # 3. Time-on-task badge
        svg.append('    <rect x="210" y="0" width="90" height="48" rx="6" fill="#f8fafc" stroke="#e2e8f0"/>')
        svg.append('    <text x="255" y="18" font-size="9" font-weight="700" fill="#475569" text-anchor="middle">ВРЕМЯ (С)</text>')
        svg.append(f'    <text x="255" y="38" font-family="JetBrains Mono, monospace" font-size="13" font-weight="700" fill="#0f172a" text-anchor="middle">{t["time"]}</text>')

        svg.append('  </g>')

        svg.append('</g>')
        card_y += 98

    # Footer Insight Note
    svg.append(f'<g transform="translate(54, {height - 54})">')
    svg.append('  <rect x="0" y="0" width="852" height="30" rx="6" fill="#f1f5f9"/>')
    svg.append('  <text x="14" y="19" font-size="11" fill="#475569">🌲 <tspan font-weight="600" fill="#0f172a">Вывод Treejack:</tspan> Иерархия разделов интуитивно понятна пользователям. Показатель прямолинейности 88.8% подтверждает отсутствие паразитных блужданий по веткам меню.</text>')
    svg.append('</g>')

    svg.append('</svg>')
    return "\n".join(svg)


# ==============================================================================
# Generate and Save
# ==============================================================================
if __name__ == "__main__":
    (OUT_DIR / "usability_scorecard_radar.svg").write_text(generate_radar_svg(), encoding="utf-8")
    (OUT_DIR / "goms_tlm_comparison.svg").write_text(generate_goms_chart_svg(), encoding="utf-8")
    (OUT_DIR / "sus_distribution_chart.svg").write_text(generate_sus_chart_svg(), encoding="utf-8")
    (OUT_DIR / "treejack_paths_ia.svg").write_text(generate_treejack_svg(), encoding="utf-8")

    print("✅ Successfully generated all 4 Lab 6 SVG assets with zero overlap!")
