"""Fixed SVG layouts: measured text, separate relationship lanes, no edge crossings.

Complex models are drawn as named fragments. A repeated reference is the same
entity, not a duplicated domain object. Semantic nodes/edges remain in metadata.
"""
import json
import math
import re
from functools import lru_cache
from pathlib import Path
from xml.etree import ElementTree as ET

try:
    from PIL import ImageFont
except ImportError:
    ImageFont = None

NS = 'http://www.w3.org/2000/svg'
ET.register_namespace('', NS)
FONT = 'Arial, Helvetica, sans-serif'
INK, MUTED, LINE, PALE = '#171717', '#525252', '#d4d4d4', '#f7f7f7'


@lru_cache(maxsize=32)
def font(size):
    if ImageFont:
        bold = size in (20, 27)
        for candidate in ['/System/Library/Fonts/Supplemental/Arial Bold.ttf' if bold else '/System/Library/Fonts/Supplemental/Arial.ttf', '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf' if bold else '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf']:
            if Path(candidate).exists():
                return ImageFont.truetype(candidate, size)
    return None


@lru_cache(maxsize=8192)
def width(text, size=18):
    loaded = font(size)
    if loaded:
        return loaded.getlength(text)
    return sum(.32 if c in ' il.,:;|' else .64 for c in text) * size


def wrap(text, available, size=18):
    result = []
    for paragraph in str(text).replace('\xa0', ' ').split('\n'):
        line = ''
        for word in paragraph.split():
            if line and width(line + ' ' + word, size) > available:
                result.append(line)
                line = ''
            # Keep identifiers intact when possible; split a single long token.
            while width(word, size) > available:
                cut = len(word) - 1
                while cut > 1 and width(word[:cut], size) > available:
                    cut -= 1
                boundaries = [match.start() for match in re.finditer(r'(?<=[a-z0-9])(?=[A-Z])|(?<=_)|(?<=/)', word)]
                natural = [index for index in boundaries if 3 <= index <= cut and len(word)-index >= 3]
                if natural:
                    cut = max(natural)
                if line:
                    result.append(line)
                    line = ''
                result.append(word[:cut])
                word = word[cut:]
            line = (line + ' ' + word).strip()
        result.append(line)
    return result


class Canvas:
    def __init__(self, title, subtitle='', width_px=1120):
        self.width = width_px
        self.root = ET.Element('{' + NS + '}svg', {'width': str(width_px), 'role': 'img'})
        self.el('title', text=title)
        self.el('desc', text=subtitle)
        self.background = self.el('rect', x=0, y=0, width=width_px, height=1, fill='white')
        self.boxes, self.segments, self.text_boxes = [], [], []
        self.text(36, 34, 'CAMPUSMEET / ПРОЕКТНАЯ ДОКУМЕНТАЦИЯ', 13, MUTED)
        lines = wrap(title, width_px - 72, 27)
        self.text(36, 74, lines, 27, INK, 34, weight='bold')
        self.cursor = 80 + len(lines) * 34
        if subtitle:
            description = wrap(subtitle, width_px - 72, 17)
            self.text(36, self.cursor, description, 17, MUTED, 25)
            self.cursor += len(description) * 25 + 16
        self.el('line', x1=36, y1=self.cursor, x2=width_px - 36, y2=self.cursor, stroke=LINE)
        self.cursor += 30

    def el(self, tag, text=None, **attrs):
        node = ET.SubElement(self.root, '{' + NS + '}' + tag, {k.replace('_', '-'): str(v) for k, v in attrs.items()})
        if text is not None:
            node.text = str(text)
        return node

    def text(self, x, y, lines, size=18, color=INK, leading=None, weight=None):
        if isinstance(lines, str):
            lines = [lines]
        leading = leading or size * 1.4
        for index, line in enumerate(lines):
            attrs = {'x': x, 'y': y + index * leading, 'font_family': FONT, 'font_size': size, 'fill': color}
            if weight:
                attrs['font_weight'] = weight
            self.el('text', text=line, **attrs)
            if line:
                self.text_boxes.append((x, y + index * leading - size, x + width(line, size), y + index * leading + size * .25))

    @staticmethod
    def card_height(title, body, card_width, size=17):
        return 26 + len(wrap(title, card_width - 36, 20)) * 27 + (len(wrap(body, card_width - 36, size)) * 24 + 18 if body else 12)

    def card(self, x, y, w, title, body='', height=None, size=17, reference=False, accent=None):
        title_lines = wrap(title, w - 36, 20)
        body_lines = wrap(body, w - 36, size) if body else []
        h = height or self.card_height(title, body, w, size)
        self.el('rect', x=x, y=y, width=w, height=h, rx=7, fill='white', stroke='#a3a3a3', stroke_width=1.3)
        header_height = len(title_lines) * 27 + 24
        fill = accent or PALE
        self.el('path', d=f'M {x+7},{y} H {x+w-7} Q {x+w},{y} {x+w},{y+7} V {y+header_height} H {x} V {y+7} Q {x},{y} {x+7},{y}', fill=fill)
        title_color = INK
        if re.fullmatch(r'#[0-9a-fA-F]{6}', fill):
            channels = [int(fill[i:i+2], 16)/255 for i in (1,3,5)]
            channels = [c/12.92 if c <= .04045 else ((c+.055)/1.055)**2.4 for c in channels]
            luminance = sum(c*k for c, k in zip(channels, [.2126,.7152,.0722]))
            if 1.05/(luminance+.05) > (luminance+.05)/.05857:
                title_color = '#ffffff'
        self.text(x + 18, y + 27, title_lines, 20, title_color, 27, 'bold')
        if body_lines:
            self.text(x + 18, y + header_height + 23, body_lines, size, MUTED if reference else INK, 24)
        self.boxes.append((x, y, x+w, y+h))
        return h

    def line(self, points, arrow=True, dashed=False):
        points = [(round(x, 2), round(y, 2)) for x, y in points]
        attrs = {'points': ' '.join(f'{x},{y}' for x, y in points), 'fill': 'none', 'stroke': MUTED, 'stroke_width': 1.6, 'stroke_linejoin': 'round'}
        if dashed:
            attrs['stroke_dasharray'] = '6 5'
        self.el('polyline', **attrs)
        self.segments.extend(zip(points, points[1:]))
        if arrow:
            (ax, ay), (bx, by) = points[-2:]
            theta = math.atan2(by-ay, bx-ax)
            c, s = math.cos(theta), math.sin(theta)
            triangle = [(bx, by), (bx-9*c+4*s, by-9*s-4*c), (bx-9*c-4*s, by-9*s+4*c)]
            self.el('polygon', points=' '.join(f'{x:.2f},{y:.2f}' for x, y in triangle), fill=MUTED)

    def label(self, x, y, text, available=196):
        lines = wrap(text, available, 15)
        self.text(x, y, lines, 15, MUTED, 21)
        return len(lines) * 21

    def marker(self, x, y, kind, side):
        direction = 1 if side == 'source' else -1
        if kind == 'triangle':
            points = [(x,y),(x+15*direction,y-7),(x+15*direction,y+7)]
            self.el('polygon', points=' '.join(f'{a},{b}' for a,b in points), fill='white', stroke=MUTED, stroke_width=1.6)
        elif kind in ('composition', 'aggregation'):
            points = [(x,y),(x+8*direction,y-5),(x+16*direction,y),(x+8*direction,y+5)]
            self.el('polygon', points=' '.join(f'{a},{b}' for a,b in points), fill=MUTED if kind == 'composition' else 'white', stroke=MUTED, stroke_width=1.6)
        else:
            self.line([(x+10*direction,y-4),(x,y),(x+10*direction,y+4)], arrow=False)

    def save(self, path, height, model):
        self.root.set('height', str(math.ceil(height)))
        self.root.set('viewBox', f'0 0 {self.width} {math.ceil(height)}')
        self.root.set('data-layout', 'fixed-lanes-v1')
        self.background.set('height', str(math.ceil(height)))
        metadata = self.el('metadata', id='diagram-model')
        metadata.text = json.dumps({'model': model, 'boxes': self.boxes, 'segments': self.segments, 'text_boxes': self.text_boxes}, ensure_ascii=False)
        ET.ElementTree(self.root).write(path, encoding='utf-8', xml_declaration=True)


def requirements(path, nodes, edges):
    labels = dict(nodes)
    canvas = Canvas('Модель требований API', 'Каждая строка — самостоятельная цепочка: действующее лицо → User Story → Use Case. Общие роли повторены без пересекающихся связей.')
    y = canvas.cursor
    for story in sorted(key for key in labels if key.startswith('US-')):
        actors = [labels[a].split(' · ')[0] for a, b, _ in edges if b == story]
        cases = [labels[b] for a, b, _ in edges if a == story]
        actor = 'Все авторизованные роли' if len(actors) > 3 else '\n'.join(actors)
        title = labels[story].split('\n', 1)[-1]
        case_text = '\n'.join(cases)
        widths = [220, 362, 362]
        height = max(canvas.card_height('Действующее лицо', actor, widths[0]), canvas.card_height(story, title, widths[1]), canvas.card_height('Use Case', case_text, widths[2]))
        canvas.card(36, y, widths[0], 'Действующее лицо', actor, height)
        canvas.card(308, y, widths[1], story, title, height)
        canvas.card(722, y, widths[2], 'Use Case', case_text, height)
        canvas.line([(256, y+height/2), (308, y+height/2)])
        canvas.line([(670, y+height/2), (722, y+height/2)])
        y += height + 24
    canvas.save(path, y+12, {'nodes': nodes, 'edges': edges})


def families(path, title, nodes, edges, reverse=False, physical=False, colors=None, edge_styles=None):
    """Decompose a dense graph into separate stars; references keep all links."""
    canvas = Canvas(title, 'Модель разделена на фрагменты. Справа — ссылки на те же сущности, а не новые объекты. Каждая связь находится в отдельной полосе.')
    labels = dict(nodes)
    y = canvas.cursor
    for index, (identifier, label) in enumerate(nodes, 1):
        related = [(a if reverse else b, relation, (edge_styles or [{}]*len(edges))[edge_index]) for edge_index,(a,b,relation) in enumerate(edges) if (b if reverse else a) == identifier]
        title_text, _, details = label.partition('\n')
        details = details.replace('──────────────\n', '')
        card_width = 580
        full_height = canvas.card_height(title_text, details, card_width, 16)
        refs = []
        for target, relation, style in related:
            target_title = labels.get(target, target).split('\n')[0]
            ref_height = max(94, canvas.card_height(target_title, 'Ссылка на сущность', 270))
            label_lines = wrap(relation, 162, 15) if relation else []
            lane_height = max(ref_height, len(label_lines)*21+45)
            refs.append((target_title, relation, lane_height, style))
        row_height = max(full_height, sum(h+20 for _, _, h, _ in refs)-20 if refs else 0)
        canvas.text(36, y+14, f'{index:02d} / {len(nodes):02d}', 13, MUTED)
        y += 28
        canvas.card(36, y, card_width, title_text, details, row_height, 16, accent=(colors or {}).get(identifier))
        ref_y = y
        for target_title, relation, lane_height, style in refs:
            canvas.card(814, ref_y, 270, target_title, 'Ссылка на сущность', lane_height, reference=True)
            mid = ref_y + lane_height - 22
            custom = bool(edge_styles)
            canvas.line([(616, mid), (814, mid)], arrow=not reverse and not custom, dashed=style.get('dashed', False) or 'dependency' in relation)
            for marker in style.get('markers', []):
                canvas.marker(616 if marker['side'] == 'source' else 814, mid, marker['kind'], marker['side'])
            if style.get('kind') == 'crowfoot':
                canvas.text(624, mid+17, '1', 14)
                canvas.text(765, mid+17, '0..N', 14)
            if reverse:
                cardinality = '0..1' if '0..1' in relation else '0..N'
                canvas.text(624, mid-10, cardinality, 15)
                canvas.text(787, mid-10, '1', 15)
            elif relation:
                canvas.label(636, ref_y+22, relation, 162)
            ref_y += lane_height + 20
        y += row_height + 40
    canvas.save(path, y, {'nodes': nodes, 'edges': edges, 'edge_styles': edge_styles})


def compact(path, name, nodes, edges):
    titles = {'mcp_architecture': 'Архитектура MCP-сервера', 'infrastructure': 'Инфраструктура и проверка окружения', 'api_resources': 'Ресурсы REST API CampusMeet'}
    labels = dict(nodes)
    canvas = Canvas(titles[name], 'Каждый поток имеет собственную полосу; подписи вынесены из линий соединений.')
    y = canvas.cursor
    xs, w = [36, 416, 796], 288

    def node(identifier, x, top, height):
        title, _, body = labels[identifier].partition('\n')
        canvas.card(x, top, w, title, body, height)

    if name == 'mcp_architecture':
        height = 154
        for identifier, x in zip(['user', 'host', 'mcp'], xs):
            node(identifier, x, y, height)
        for a, b in [(324, 416), (704, 796)]:
            canvas.line([(a, y+77), (b, y+77)])
        canvas.label(336, y+58, 'запрос', 70)
        canvas.label(724, y+58, 'stdio', 60)
        bottom = y+height+150
        for identifier, x in zip(['rest', 'store', 'db'], xs):
            node(identifier, x, bottom, height)
        canvas.line([(940, y+height), (940, y+height+70), (560, y+height+70), (560, bottom)])
        canvas.label(646, y+height+48, 'Валидация и права', 220)
        canvas.line([(324, bottom+77), (416, bottom+77)])
        canvas.label(338, bottom+58, 'REST', 70)
        canvas.line([(704, bottom+77), (796, bottom+77)])
        canvas.label(726, bottom+58, 'SQL', 60)
        end = bottom+height+36
    elif name == 'infrastructure':
        height = 142
        for identifier, x in zip(['browser', 'web', 'api'], xs):
            node(identifier, x, y, height)
        canvas.line([(324, y+71), (416, y+71)])
        canvas.label(336, y+51, 'HTTP', 70)
        canvas.line([(704, y+71), (796, y+71)])
        canvas.label(716, y+51, 'REST', 70)
        bottom = y+height+100
        node('mcp', xs[1], bottom, height)
        node('sqlite', xs[2], bottom, height)
        canvas.line([(940, y+height), (940, bottom)])
        canvas.label(954, y+height+42, 'volume', 120)
        canvas.line([(704, bottom+71), (796, bottom+71)])
        canvas.label(716, bottom+51, 'SQLite', 70)
        end = bottom+height+62
        canvas.text(36, end, 'Проверки и выпуск', 24, weight='bold')
        end += 28
        for target, label in [('pg', 'Проверка PostgreSQL DDL'), ('api', 'Docker build и HTTP smoke'), ('sonar', 'Ручной workflow; нужны настройки')]:
            source_body = 'Тесты → DDL → Docker smoke' if target == 'pg' else 'Ссылка на тот же pipeline'
            canvas.card(36, end, 288, 'GitHub Actions', source_body, 142)
            title, _, body = labels[target].partition('\n')
            canvas.card(708, end, 376, title, body, 142)
            canvas.line([(324, end+110), (708, end+110)])
            canvas.label(348, end+44, label, 334)
            end += 170
    else:
        canvas.card(36, y, 288, 'Web / Mobile', 'Клиенты CampusMeet', 118)
        canvas.card(416, y, 668, '/api/v1', 'REST · JSON · версионированные ресурсы', 118)
        canvas.line([(324, y+59), (416, y+59)])
        canvas.label(338, y+40, 'HTTP', 70)
        event_y = y+198
        canvas.card(116, event_y, 968, 'events', 'Каталог и карточка события · schedule · proposals · teams', 118)
        fork = event_y+118
        child_y = fork+46
        for identifier, title in [('checkins', 'check-ins / check-in-batches'), ('jobs', 'announcements / attendance-exports / jobs')]:
            canvas.card(212, child_y, 872, title, labels[identifier], 118)
            canvas.line([(164, child_y+59), (212, child_y+59)])
            child_y += 152
        canvas.line([(164, fork), (164, child_y-152+59)], arrow=False)
        ticket_y = child_y+30
        canvas.card(116, ticket_y, 968, 'me/tickets · tickets/{id}', 'Собственные билеты, отмена регистрации и Wallet', 118)
        venue_y = ticket_y+154
        canvas.card(116, venue_y, 968, 'venues · integrations', 'Площадки, геокодирование и календарь праздников', 118)
        bus_start = y+118+38
        canvas.line([(450, y+118), (450, bus_start), (72, bus_start), (72, venue_y+59)], arrow=False)
        for top in [event_y, ticket_y, venue_y]:
            canvas.line([(72, top+59), (116, top+59)])
        end = venue_y+154
    canvas.save(path, end, {'nodes': nodes, 'edges': edges})


def render(path, name, nodes, edges):
    if name == 'requirements':
        requirements(path, nodes, edges)
    elif name in ('physical_erd', 'logical_erd'):
        families(path, 'Физическая модель PostgreSQL 16' if name == 'physical_erd' else 'Логическая модель данных', nodes, edges, reverse=True, physical=name == 'physical_erd')
    else:
        compact(path, name, nodes, edges)
