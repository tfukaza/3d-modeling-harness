#!/usr/bin/env python3
"""Build a source-only multi-angle review packet with contextual detail crops.

uv run --with pillow python scripts/build-reference-review.py manifest.json --output /tmp/review
Paths are relative to the manifest. View labels are declarations requiring visual
review, not an automatic camera classifier. No source pixels are synthesized.
"""
import argparse
import hashlib
import html
import importlib.util
import json
import shutil
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('manifest', type=Path)
    parser.add_argument('--output', required=True, type=Path)
    parser.add_argument('--allow-incomplete', action='store_true',
                        help='Emit explicitly incomplete evidence; never an acceptance packet')
    args = parser.parse_args()
    data = json.loads(args.manifest.read_text())
    sources = {}
    hashes = set()
    gaps = []
    for source in data['sources']:
        identifier = source['id']
        if identifier in sources:
            parser.error(f'Duplicate source ID: {identifier}')
        path = (args.manifest.parent / source['image']).resolve()
        with Image.open(path) as image:
            size = image.size
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        sources[identifier] = {**source, 'path': path, 'size': size, 'sha256': digest}
        hashes.add(digest)
        if not source.get('view') or not source.get('provenance'):
            parser.error(f'{identifier}: view and provenance are required')
    if len(hashes) < 3 or len({s['view'] for s in sources.values()}) < 3:
        gaps.append('Need at least three distinct originals and declared views for whole-object coverage.')
    for region in data['regions']:
        observations = region['observations']
        views = set()
        originals = set()
        for observation in observations:
            source = sources[observation['source']]
            views.add(source['view'])
            originals.add(source['sha256'])
            x0, y0, x1, y1 = observation['crop']
            width, height = source['size']
            if not (0 <= x0 < x1 <= width and 0 <= y0 < y1 <= height):
                parser.error(f"{region['id']}: crop falls outside {source['id']}")
        if len(views) < 2 or len(originals) < 2:
            gaps.append(f"{region['id']}: need focused observations from two different originals/views.")
    if gaps and not args.allow_incomplete:
        parser.error('\n'.join(gaps) + '\nFind additional views or use --allow-incomplete to document the gap.')

    spec = importlib.util.spec_from_file_location('comparison', Path(__file__).with_name('compare-model-reference.py'))
    comparison = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(comparison)
    args.output.mkdir(parents=True, exist_ok=True)
    try:
        font = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 18)
    except OSError:
        font = ImageFont.load_default(size=18)
    escape = html.escape
    pages = ['<!doctype html><meta charset="utf-8"><title>Reference review</title>',
             '<style>body{font:18px system-ui;max-width:1500px;margin:32px auto;padding:20px}img{max-width:100%}figure{margin:24px 0}li{margin:12px 0}</style>',
             '<h1>Source-only multi-view review</h1>',
             '<p>Inspect all views and crops. Declared angles require verification using shared landmarks; pose changes do not establish another side. This packet covers only the listed regions and states, not complete mechanical acceptance or hidden construction.</p>']
    if gaps:
        pages.append('<h2>INCOMPLETE — unresolved coverage</h2><ul>' + ''.join(f'<li>{escape(gap)}</li>' for gap in gaps) + '</ul>')
    pages.append('<h2>Whole-object context</h2>')
    for index, source in enumerate(sources.values()):
        filename = f'source-{index:02}.png'
        image, _ = comparison.context_panel(source['path'], None, 900, 650)
        image.save(args.output / filename)
        original = f'original-{index:02}{source["path"].suffix.lower()}'
        shutil.copyfile(source['path'], args.output / original)
        pages.append(f'<figure><a href="{original}"><img src="{filename}"></a><figcaption>{escape(source["id"])} — {escape(source["view"])} — {escape(source.get("state", "state unspecified"))} — {escape(source["provenance"])}</figcaption><a href="{original}">Native-resolution original: {source["size"][0]} × {source["size"][1]} pixels</a></figure>')
    for region_index, region in enumerate(data['regions']):
        pages.append(f'<h2>{escape(region["id"])}</h2><p>{escape(region["question"])}</p>')
        for observation_index, observation in enumerate(region['observations']):
            source = sources[observation['source']]
            crop = observation['crop']
            sheet = Image.new('RGB', (1600, 650), '#fafafa')
            focus = comparison.panel(source['path'], crop, 0, None, 800, 580)
            context, _ = comparison.context_panel(source['path'], crop, 800, 580)
            sheet.paste(focus, (0, 60))
            sheet.paste(context, (800, 60))
            draw = ImageDraw.Draw(sheet)
            draw.text((16, 16), f'{source["id"]}: focused crop', fill='#111', font=font)
            draw.text((816, 16), 'Full original; pink box locates detail', fill='#111', font=font)
            filename = f'region-{region_index:02}-{observation_index:02}.png'
            sheet.save(args.output / filename)
            pages.append(f'<figure><img src="{filename}"><figcaption>{escape(source["view"])}; original-pixel crop {escape(str(crop))}</figcaption></figure>')
        pages.append('<p>Record: visible evidence · cross-view agreement · alternative optical explanations · unresolved depth/ownership. Revisit originals before constructing a component.</p>')
    pages.append('<p>Next: draw detailed schematics and use build-comparison-review.py for independent critique against these originals. After schematic approval, model in Blender and regenerate comparison packets for model revisions. Source coverage alone is not drawing or model acceptance.</p>')
    (args.output / 'index.html').write_text('\n'.join(pages))
    evidence = {'status': 'incomplete' if gaps else 'ready-for-visual-review', 'gaps': gaps,
                'sources': [{k: str(v) if isinstance(v, Path) else v for k, v in source.items()} for source in sources.values()],
                'regions': data['regions']}
    (args.output / 'evidence.json').write_text(json.dumps(evidence, indent=2) + '\n')
    print(args.output / 'index.html')


if __name__ == '__main__':
    main()
