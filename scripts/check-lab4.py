"""Check documentation assets, local links, diagram XML and contract snapshots."""
import json
import re
import subprocess
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
from xml.etree import ElementTree

ROOT = Path(__file__).resolve().parents[1]


class Document(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = []
        self.links = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            self.ids.append(attrs['id'])
        for attribute in ('href', 'src', 'report'):
            if attribute in attrs:
                self.links.append(attrs[attribute])


def main():
    failures = []
    checks = 0
    for path in [ROOT / 'docs/pages/lab4.html', ROOT / 'docs/api/index.html']:
        doc = Document()
        doc.feed(path.read_text())
        if len(doc.ids) != len(set(doc.ids)):
            failures.append(f'{path.name}: duplicate ids')
        for value in doc.links:
            parsed = urlsplit(value)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            checks += 1
            if not (path.parent / unquote(parsed.path)).resolve().exists():
                failures.append(f'{path.name}: missing {value}')
    for path in [ROOT / 'docs/reports/Lab4_report.md', *[ROOT / 'wiki' / name for name in ('API_Requirements_and_Use_Cases.md', 'Database_Models_Lab4.md', 'MCP_Server.md', 'Infrastructure_and_CI.md')]]:
        for value in re.findall(r'!?\[[^\]]*\]\(([^)]+)\)', path.read_text()):
            parsed = urlsplit(value)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            checks += 1
            if not (path.parent / unquote(parsed.path)).resolve().exists():
                failures.append(f'{path.name}: missing {value}')
    for path in (ROOT / 'docs/diagrams/lab4').glob('*.svg'):
        ElementTree.parse(path)
        checks += 1
    subprocess.run([sys.executable, str(ROOT / 'scripts/sync-lab4.py'), '--check'], check=True)
    spec = json.loads((ROOT / 'docs/api/openapi.json').read_text())
    assert sum(len(methods) for methods in spec['paths'].values()) == 33
    bundle = (ROOT / 'docs/js/data/reports.js').read_text().split('window.CampusMeetReports = ', 1)[1].rstrip().removesuffix(';')
    reports = json.loads(bundle)
    for number in range(1, 5):
        name = f'Lab{number}_report.md'
        assert reports[name] == (ROOT / 'docs/reports' / name).read_text(), f'Stale report bundle: {name}'
    for path in [ROOT / 'docs/js/main.js', ROOT / 'docs/js/data/navigation.js', ROOT / 'docs/js/data/search.js', ROOT / 'docs/js/modules/report-viewer.js', ROOT / 'docs/js/modules/router.js', ROOT / 'docs/api/viewer.js']:
        subprocess.run(['node', '--check', str(path)], check=True)
    if failures:
        raise SystemExit('\n'.join(failures))
    print(f'PASS: {checks} documentation links/assets; 4 report snapshots; JavaScript syntax')


if __name__ == '__main__':
    main()
