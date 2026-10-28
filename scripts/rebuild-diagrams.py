"""Rebuild readable diagram fragments and normalize legacy flow/sequence SVGs.

The layout model is captured once from PlantUML's semantic SVG groups. It keeps
all entities, member lines and relationships; it is editable and reproducible.
No network service or PlantUML installation is needed to reproduce published SVGs.
"""
import hashlib
import json
import re
from collections import defaultdict
from pathlib import Path
from xml.etree import ElementTree as ET

from diagram_layout import NS, families

ROOT = Path(__file__).resolve().parents[1]
DIAGRAMS = ROOT / 'docs/diagrams/puml'
MODELS = DIAGRAMS / 'layout-models.json'


def text_lines(element):
    rows = defaultdict(list)
    for node in element.iter('{' + NS + '}text'):
        value = ''.join(node.itertext()).replace('\xa0', ' ')
        rows[round(float(node.get('y', '0')), 1)].append((float(node.get('x', '0')), value))
    return [''.join(value for _, value in sorted(parts)).strip() for _, parts in sorted(rows.items()) if any(value.strip() for _, value in parts)]


def capture(path):
    root = ET.parse(path).getroot()
    title = root.find('{' + NS + '}title')
    nodes, edges, containers = [], [], {}
    original_links = [node for node in root.iter() if node.get('class') == 'link']
    used = {node.get(key) for node in original_links for key in ['data-entity-1', 'data-entity-2']}
    entities = [node for node in root.iter() if node.get('class') == 'entity']
    clusters = [node for node in root.iter() if node.get('class') == 'cluster']
    for cluster in clusters:
        qualified = cluster.get('data-qualified-name', '')
        containers[qualified] = ' / '.join(text_lines(cluster))
    for entity in entities:
        identifier = entity.get('id')
        lines = text_lines(entity)
        if not lines:
            lines = [entity.get('data-qualified-name', identifier)]
        qualified = entity.get('data-qualified-name', '')
        parent = max((name for name in containers if qualified.startswith(name + '.')), key=len, default='')
        if parent:
            lines.append('Контекст: ' + containers[parent])
        nodes.append([identifier, '\n'.join(lines)])
    for cluster in clusters:
        if cluster.get('id') not in used:
            continue
        lines = text_lines(cluster)
        qualified = cluster.get('data-qualified-name', '')
        members = [text_lines(node)[0] for node in entities if node.get('data-qualified-name', '').startswith(qualified + '.') and text_lines(node)]
        nodes.append([cluster.get('id'), '\n'.join(lines + members)])
    for link in original_links:
        relationship = '\n'.join(text_lines(link))
        kind = link.get('data-link-type', '')
        labels = {'composition': 'Композиция', 'aggregation': 'Агрегация', 'extension': 'Наследование', 'dependency': 'Зависимость', 'association': 'Ассоциация'}
        relationship = (labels.get(kind, kind) + ('\n' + relationship if relationship else '')).strip()
        edges.append([link.get('data-entity-1'), link.get('data-entity-2'), relationship])
    return {'title': title.text if title is not None else path.stem, 'nodes': nodes, 'edges': edges, 'source': str(path.with_suffix('.puml').relative_to(ROOT)), 'source_sha256': hashlib.sha256(path.with_suffix('.puml').read_bytes()).hexdigest()}


def normalize_flow(path):
    tree = ET.parse(path)
    root = tree.getroot()
    if root.get('data-layout') == 'legacy-flow-readable-v1':
        return
    for parent in list(root.iter()):
        for child in list(parent):
            if child.tag.endswith('text') and 'Please' in (child.text or '') and 'handwritten' in (child.text or ''):
                parent.remove(child)
            elif child.tag.endswith('rect') and child.get('fill') == '#FFFFCC' and child.get('y') == '5':
                parent.remove(child)
    # SVG/CSS background is not a reliable SVG canvas in rasterizers or themes.
    viewbox = [float(value) for value in root.get('viewBox').split()]
    background = ET.Element('{' + NS + '}rect', {'x': str(viewbox[0]), 'y': str(viewbox[1]), 'width': str(viewbox[2]), 'height': str(viewbox[3]), 'fill': '#ffffff'})
    root.insert(0, background)
    font_sizes = [float(node.get('font-size')) for node in root.iter() if node.tag.endswith('text') and node.get('font-size')]
    scale = 16 / min(font_sizes) if font_sizes else 1
    root.set('width', str(round(viewbox[2]*scale, 2)))
    root.set('height', str(round(viewbox[3]*scale, 2)))
    root.set('data-layout', 'legacy-flow-readable-v1')
    # Message labels remain above lifelines and arrows with a paper halo.
    for parent in root.iter():
        if parent.get('class') == 'link' or parent.tag.endswith('g'):
            for child in list(parent):
                if child.tag.endswith('text') and child.get('fill', '').lower() in ('#000000', '#333333', '#181818'):
                    child.set('stroke', '#ffffff')
                    child.set('stroke-width', '2')
                    child.set('stroke-linejoin', 'round')
                    child.set('paint-order', 'stroke')
    tree.write(path, encoding='utf-8', xml_declaration=True)


def main():
    if MODELS.exists():
        models = json.loads(MODELS.read_text())
    else:
        models = {}
        for path in sorted(DIAGRAMS.rglob('*.svg')):
            if path.parent.name in ('activity', 'sequence'):
                continue
            models[str(path.relative_to(DIAGRAMS))] = capture(path)
        MODELS.write_text(json.dumps(models, ensure_ascii=False, indent=2) + '\n')
    for relative, model in models.items():
        families(DIAGRAMS / relative, model['title'], model['nodes'], model['edges'], colors=model.get('colors'), edge_styles=model.get('edge_styles'))
    for category in ('activity', 'sequence'):
        for path in (DIAGRAMS / category).glob('*.svg'):
            normalize_flow(path)
    print(f'Rebuilt {len(models)} semantic diagrams; normalized 9 flow/sequence diagrams')


if __name__ == '__main__':
    main()
