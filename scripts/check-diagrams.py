"""Audit diagram boxes, connector lanes, label bounds and paginated assets."""
import json
import math
import hashlib
import re
from pathlib import Path
from xml.etree import ElementTree as ET

from diagram_layout import NS, width

ROOT = Path(__file__).resolve().parents[1]


def overlap(a, b):
    return min(a[2], b[2])-max(a[0], b[0]) > 1 and min(a[3], b[3])-max(a[1], b[1]) > 1


def cross(a, b, c, d):
    def turn(p, q, r):
        return (q[0]-p[0])*(r[1]-p[1])-(q[1]-p[1])*(r[0]-p[0])
    return turn(a,b,c)*turn(a,b,d) < -.01 and turn(c,d,a)*turn(c,d,b) < -.01


def hits_box(a, b, box):
    x1,y1,x2,y2 = box
    inner = (x1+1,y1+1,x2-1,y2-1)
    if a[1] == b[1]:
        return inner[1] < a[1] < inner[3] and min(max(a[0],b[0]),inner[2]) > max(min(a[0],b[0]),inner[0])
    if a[0] == b[0]:
        return inner[0] < a[0] < inner[2] and min(max(a[1],b[1]),inner[3]) > max(min(a[1],b[1]),inner[1])
    return False


def main():
    errors, results = [], []
    for path in sorted((ROOT/'docs/diagrams').rglob('*.svg')):
        if '.page-' in path.name:
            ET.parse(path)
            continue
        root = ET.parse(path).getroot()
        text_content = ''.join(root.itertext())
        if 'Please' in text_content and 'handwritten' in text_content:
            errors.append(f'{path.name}: compiler warning is visible')
        fixed = root.get('data-layout') == 'fixed-lanes-v1'
        if fixed:
            info = json.loads(root.find('{' + NS + '}metadata').text)
            boxes, segments, labels = info['boxes'], info['segments'], info['text_boxes']
            box_hits = [(a,b) for i,a in enumerate(boxes) for b in boxes[i+1:] if overlap(a,b)]
            label_hits = [(a,b) for i,a in enumerate(labels) for b in labels[i+1:] if overlap(a,b)]
            edge_hits = [pair for i,pair in enumerate(segments) for other in segments[i+1:] if cross(*pair,*other)]
            obstacle_hits = [(a,b) for a,b in segments for box in boxes if hits_box(a,b,box)]
            label_edge_hits = [(a,b) for a,b in segments for box in labels if hits_box(a,b,box)]
            w,h = float(root.get('width')),float(root.get('height'))
            outside = [box for box in labels if box[0]<0 or box[1]<0 or box[2]>w or box[3]>h]
            for name,hits in [('overlapping cards',box_hits),('overlapping text',label_hits),('crossing connectors',edge_hits),('connectors through cards',obstacle_hits),('connectors through labels',label_edge_hits),('clipped labels',outside)]:
                if hits:
                    errors.append(f'{path.name}: {name}: {len(hits)}; first={hits[0]}')
            results.append({'file':str(path.relative_to(ROOT)), 'layout':'separate lanes', 'cards':len(boxes),'labels':len(labels),'connectors':len(segments),'overlaps':len(box_hits)+len(label_hits),'crossings':len(edge_hits)+len(obstacle_hits)+len(label_edge_hits),'clipped_labels':len(outside)})
        else:
            _,_,view_w,view_h = map(float,root.get('viewBox').split())
            width_str = root.get('width') or str(view_w)
            scale = float(width_str.replace('px', ''))/view_w
            labels=[]
            for item in root.iter('{' + NS + '}text'):
                text=''.join(item.itertext())
                x,y=float(item.get('x',0)),float(item.get('y',0))
                size=float(item.get('font-size',16))
                length=float(item.get('textLength',width(text,int(size))))
                labels.append((x,y-size,x+length,y+size*.15))
            hits=[(a,b) for i,a in enumerate(labels) for b in labels[i+1:] if overlap(a,b)]
            if hits:
                errors.append(f'{path.name}: legacy text overlaps: {len(hits)}; first={hits[0]}')
            results.append({'file':str(path.relative_to(ROOT)),'layout':'UML activity / sequence','labels':len(labels),'overlapping_labels':len(hits),'body_font_px':round(11*scale,2),'note':'Messages crossing lifelines and explicit branch joins are UML notation.'})
    script=(ROOT/'docs/js/data/diagram-pages.js').read_text().split('window.CampusMeetDiagramPages = ',1)[1].strip().removesuffix(';')
    manifest=json.loads(script)
    for source,pages in manifest.items():
        for page in pages:
            assert (ROOT/'docs/diagrams'/source).with_name(page['file']).is_file(),page
    models=json.loads((ROOT/'docs/diagrams/puml/layout-models.json').read_text())
    preserved_nodes=preserved_links=0
    for relative,model in models.items():
        source=ROOT/model['source']
        assert hashlib.sha256(source.read_bytes()).hexdigest()==model['source_sha256'], f'Update layout model after source change: {source}'
        root=ET.parse(ROOT/'docs/diagrams/puml'/relative).getroot()
        actual=json.loads(root.find('{' + NS + '}metadata').text)['model']
        assert actual['nodes']==model['nodes'] and actual['edges']==model['edges'], relative
        identifiers={identifier for identifier,_ in model['nodes']}
        assert all(a in identifiers and b in identifiers for a,b,_ in model['edges']), relative
        visible=''.join(''.join(node.itertext()) for node in root.iter('{' + NS + '}text'))
        visible=re.sub(r'\s+','',visible)
        for _,label in model['nodes']:
            for line in label.splitlines():
                assert re.sub(r'\s+','',line) in visible, f'{relative}: lost entity text: {line}'
        preserved_nodes+=len(model['nodes'])
        preserved_links+=len(model['edges'])
    summary={'canonical_diagrams':len(results),'paginated_diagrams':len(manifest),'fragments':sum(map(len,manifest.values())),'preserved_legacy_nodes':preserved_nodes,'preserved_legacy_relationships':preserved_links,'errors':errors,'diagrams':results}
    notes = ROOT/'.local-review'
    notes.mkdir(exist_ok=True)
    (notes/'layout-audit.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
    if errors:
        raise SystemExit('\n'.join(errors))
    print(f'PASS: {len(results)} diagrams, no card/text overlap or unintended connector crossings; {summary["fragments"]} complete fragments')


if __name__ == '__main__':
    main()
