# Schematic and Blender model comparison packets

Build the source-only packet first (command below) and let critics inspect it before
candidate drawings or models. Then build a separate comparison packet for each
frozen schematic or Blender model revision:

```sh
uv run --with pillow python scripts/build-comparison-review.py \
  references/manifest.json review/comparisons.json \
  --output review/schematic-r01
```

The first input uses the existing reference manifest format. Retain all useful
distinct collected images in `sources`; optional `identity` text records the exact
variant or supplemental specimen, and `state` identifies an operating state. Keep
target identity or the selected coherent generic-design brief in project notes.
Generated angle hypotheses belong separately, not among collected source evidence.

The comparison manifest has `stage` (`schematic` or `model`), a nonempty `revision`,
optional `asset` (editable SVG, `.blend`, etc.), `views`, and `comparisons`. Each view
has `id`, `image`, `view`, and optional `state`. Each comparison maps a `source` ID to
a `candidate` view ID and declares `camera` as `matched` or `diagnostic`. Optional
fields are `region` (an existing reference region containing that source),
`reference_crop`, `candidate_crop`, `reference_anchor`, `candidate_anchor`, `note`,
boolean `overlay`, and paired `reference_contours` / `candidate_contours` paths.
See [the example](../examples/comparison-manifest.json).

Image and asset paths resolve relative to their own manifest, not the working
directory. Crops use original image pixels; anchors use coordinates after cropping.
Boxes must be inside their image/frame. This batch tool does not rotate images;
render/rasterize corresponding views first. For individual rotated model pairs,
use the tool below. Camera matching is a human declaration to verify, not a script
inference. Overlays require `matched`; diagnostic comparisons cannot establish
acceptance. Do not use overlays to compare a cut section with an exterior photo
unless the displayed boundaries actually correspond.

Overview PNGs paginate four references and two candidate views per board, repeating
candidate views alongside each reference group. Additional candidate groups get
their own pages. Every retained reference and candidate appears, even without a
pair mapping. Focused sheets show the paired views and full originals with crop
boxes, with uniform scaling and no stretching or mirroring. Optional anchors align
body landmark framing; the compositor cannot correct camera or pose differences.
Inspect native originals and enlarged sheets rather than relying on thumbnails.

The output must be a new or empty directory, preventing stale revision captures.
It contains overview/detail PNGs, byte-identical reference/candidate snapshots,
`index.html`, input-manifest copies, and `evidence.json` with image hashes, optional
asset hash, revision, region metadata and source-to-comparison coverage. Every
focused comparison records its image-derived crop, rotation, framing bounds,
anchor, uniform scale, rounded resize dimensions and panel translation. Supplied
contour PNGs receive byte-identical snapshots and input hashes as well. Archive
manifests retain their original path semantics; snapshot links identify portable
native images within the packet. The canonical editable asset stays in the project.
An asset hash records the supplied file; it does not prove renders came from it.
Freeze/save that asset, render it, and regenerate the packet after every repair.

Empty comparison lists are allowed for diagnostic overviews. Missing pair/region
coverage and camera mismatches are explicitly listed as unresolved. Even complete
mapping means only ready for visual review, never automatic signoff. Critics must
check all relevant components/details and resolve supported findings before moving
from schematics to dependent Blender modeling or from modeling to delivery.

## Individual reference/model pair

```sh
uv run --with pillow python scripts/compare-model-reference.py \
  --reference references/example-angle.png \
  --reference-crop 220,430,1400,890 \
  --model renders/example-view.png \
  --model-crop 265,375,490,447 \
  --context \
  --output review/example-comparison.png \
  --width 850 --height 500 --title 'Example comparison'
```

Crop coordinates are `left,top,right,bottom` in original image pixels. Optional
`--reference-rotate` / `--model-rotate` rotate counterclockwise before framing.
`--reference-anchor` / `--model-anchor` identify the same main-body landmarks in
each image **after** cropping/rotation, so a long cable or strap does not change
body scale. The script scales uniformly and preserves proportions. `--overlay`
adds a third 50/50 panel; only use it for sufficiently matched views.

## Paired reviewer contours

For difficult shape reviews, reviewers may author one editable SVG trace over the
native reference and another over the native candidate render, then rasterize each
to a transparent PNG at exactly its original image dimensions. Draw only observed
boundaries and meaningful landmarks; retain the editable SVG companions with the
project. These tools consume the reviewer-authored PNGs and never extract edges,
infer a trace, score geometric agreement, or grant automatic geometry acceptance.
Keep uncertain/occluded boundaries identified in the review notes or SVG.

```sh
uv run --with pillow python scripts/compare-model-reference.py \
  --reference references/example-angle.png \
  --model renders/example-view.png \
  --reference-contours review/traces/reference.png \
  --model-contours review/traces/model.png \
  --camera matched \
  --reference-crop 220,430,1400,890 \
  --model-crop 265,375,490,447 \
  --output review/example-contours.png
```

Supply both contour paths or neither. Each PNG must contain visible marks and
fully transparent background pixels; empty overlays, opaque images and mismatched
dimensions are rejected before output. Stroke RGB colors are preserved on the
individual image-plus-contour panels. The line-only comparison recolors reference
strokes magenta and candidate strokes cyan. Each contour receives **exactly the
same crop, rotation, resize and translation as its own image**, including anchor
framing and integer rounding. Contour stroke bounds never determine framing:
an intentionally misplaced stroke stays misplaced in the comparison.

With contours, the individual CLI requires `--camera matched` or `--camera
diagnostic` and automatically includes the full unrotated originals. A matched
declaration enables the dual-color line-only alignment; reviewers must still
verify camera, pose, state and corresponding boundaries. Diagnostic views retain
their separate image-plus-contour panels, omit the registered line overlay and
cannot establish acceptance. `--overlay` is rejected with an explicitly diagnostic
camera. The normal raw comparison panels and full context remain visible.

The individual CLI writes `OUTPUT.evidence.json` (replacing the image suffix),
including image/contour SHA256 hashes, exact transforms, declared camera and whether
a line overlay was emitted. Use `--evidence PATH` to override this location or to
request evidence for a comparison without contours. Legacy calls without contour
or evidence arguments retain their original panel layout and output behavior.

For batch packets, add both paths to each relevant comparison, relative to the
**comparison manifest** (including the reference contour path):

```json
{
  "source": "source-side",
  "candidate": "render-side",
  "camera": "matched",
  "reference_contours": "traces/reference-side.png",
  "candidate_contours": "traces/render-side.png"
}
```

Optional batch crops and anchors work as before; rotation remains an individual
CLI option. Focused sheets add a reviewer contour row between raw comparisons and
full context. `evidence.json` and the HTML index link the native PNG snapshots.
Diagnostic pairs may carry both traces for inspection, but receive no combined
line alignment. Missing contour pairs are errors; absence of both preserves the
existing comparison behavior.

Crop comparisons automatically include context; `--context` also enables it for uncropped views. It appends the full, unrotated original
reference and model images, uniformly fitted without applying crop, rotation,
or anchor framing. Pink rectangles mark the requested crop boxes; labels report
the original pixel coordinates and the rotation applied to each comparison view.
Full-object axes and identifying landmarks must agree with the claimed view:
similar-looking crops alone do not prove that the model's orientation is correct.

Render the model from the same side, approximate elevation/perspective, and
functional state as the original. This compositor cannot correct a different
camera. Label initial unmatched comparisons as diagnostic, then make matched
views for acceptance. Ask the critic to inspect the combined image, list factual
shape/attachment/mechanism discrepancies, and distinguish allowed artistic
changes. Regenerate the sheet from the final export after repairs.

## Source-only packet

For substantial work, prepare source evidence before drawing or interpreting a mechanism:

```sh
uv run --with pillow python scripts/build-reference-review.py \
  references/manifest.json \
  --output review/reference-packet
```

The JSON manifest contains `sources` (`id`, `image`, `view`, `provenance`) and
`regions` (`id`, `question`, `observations`). Each observation identifies a
`source` ID and a `crop` in original pixels. Paths resolve relative to the
manifest. See `examples/reference-manifest.json` for the schema.

The builder requires at least three distinct originals/declared whole-object views
and two different originals/views per difficult region. These are minimum coverage
checks: seek additional sides, obliques and operating states when necessary. Merely
renaming the same view does not provide depth evidence. Inspect shared landmarks
personally. Duplicate pixels do not count as additional originals.

Each detail sheet retains the full original with its crop box. The HTML index
provides context previews, links to byte-identical native-resolution originals, pixel dimensions, source provenance, detail sheets and the question being
investigated. `evidence.json` records source hashes and unresolved coverage. If a
view cannot be obtained, `--allow-incomplete` emits an explicitly incomplete packet;
it does not grant acceptance. Reject out-of-bounds crops rather than silently
padding missing source pixels. After source review, create schematic comparisons
with `build-comparison-review.py`; after schematic approval, use it again for
Blender model revisions covering the same regions.

For specific products, keep variant differences explicit. For generic subjects,
references may depict different similar specimens; record the selected design and
do not mistake specimen differences for additional views of one physical object.
The minimum view counts above are bookkeeping checks, not proof of coherent design.

For every consequential part, record evidence from more than one angle and check
alternative explanations such as transparency, reflection, occlusion and shadow.
An attractive comparison or a passing collision test cannot establish that a
component exists in the original product.

Run the compositor's behavioral tests with
`uv run --with pillow python scripts/test-comparison-review.py`.
