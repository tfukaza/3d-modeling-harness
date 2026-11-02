# Trace component surfaces on the original photograph

Use photo tracing before schematics when transparency, overlapping parts, weak
contrast or a difficult interface makes surface boundaries uncertain. Start with
the component that needs interpretation; a simple clear shape or reviewed repair
does not need a new tracing pass. Trace before generated structural interpretations
for these regions, so generated contours do not become the source of the drawing.

This is an editable image-space observation aid. It is not a mesh, an orthographic
drawing, a measurement reference or proof of unseen construction.

## Prioritize difficult regions

Before sketching, list the few regions most likely to be misread, the concrete
question each raises, and the source views, traces, sections or operating states
needed to resolve it. Carry this list into schematic and model review; assign a
component or interface-focused pass where useful, rather than spending equal
effort on obvious broad faces and crowded uncertain boundaries.

- **Transparent or reflective surfaces:** distinguish outer/inner walls, openings,
  transmitted edges, reflections and the material that remains around a feature.
  Seek another angle when a single bright line cannot establish a boundary.
- **Tight passages and interwoven parts:** track which part owns each surface,
  what passes in front/behind or through an aperture, and whether the whole
  assembled passage stays accessible. Inspect entry/exit, local wall thickness,
  mating boundaries and clearance rather than a plausible isolated part silhouette.
  Seek occupied and removed/deployed states when one part masks an opening; the
  inserted part's silhouette is not automatically the housing's cutout boundary.
- **Complex mechanisms:** identify relevant axes, supports, engagement and motion
  before detailing. For gears/linkages, inspect source-supported profiles, repeated
  counts and layout, mating relationships and operating clearance as applicable.
  Do not substitute decorative disks/teeth for the mechanism, or invent hidden
  gearing or precise dimensions where the source cannot establish them.

Record which difficult regions were actually examined, what resolved their
questions and what remains uncertain. A checked overview is not focused coverage
of an obscured interface. Use these priorities during source interpretation,
sketching and review even when a particular region does not need an SVG trace.

Unresolved structural questions trigger targeted reference collection: seek and
inspect another original angle, readable closeup or relevant operating/video state
that could distinguish the competing interpretations. Recheck the exact variant,
map shared landmarks and return to the trace with that evidence. Repeated crops
of one photo do not resolve missing depth. Record the search and its result; retain
an unresolved label only when useful evidence remains unavailable or inconclusive,
not as a substitute for trying to find it. See [reference collection](reference-modeling.md#collect-references-before-drawing).

## Anchor the drawing to actual pixels

Inspect the original full image and readable detail crops before drawing. Record
component scope, visible landmarks, camera/state and uncertain boundaries. Supply
the actual original to each author, not just an inventory or another agent's sketch.

Create an SVG with a `viewBox` matching the original image's native width/height.
Embed the unchanged photograph at its original coordinates, with tracing paths in
that same coordinate system. Keep photo, component contours, uncertainty, inference
and annotations in named, independently toggleable groups/layers. Retain the source
file identity/hash and trace revision in notes. Do not stretch, mirror, rectify or
redraw the photograph to make paths agree. A crop uses an explicitly recorded
offset/viewBox, not an unexplained new coordinate system.

Use paths with stable identifiers and thin readable strokes. Keep a full-image
overlay and enlarged interface views; make the photo visible beneath strokes and
inspect a photo-only view where lines might conceal evidence. A line-only view is
useful too, but must remain linked to the image it interprets. Render and personally
inspect the actual SVG after edits, rather than trusting coordinate lists.

## Trace one component's surfaces

Trace silhouettes, visible face boundaries, curvature/step changes, opening rims,
thickness cues and occlusion boundaries relevant to that component. Show which
surfaces an edge bounds and which neighboring component hides a continuation.
Omit unrelated interior parts except as context or occluders. Do not replace a
small local feature with an oversimplified silhouette that erases adjacent material.

Use a consistent legend, for example solid lines for supported boundaries, dashed
lines for ambiguous image lines, and a distinct dotted/color treatment for inferred
continuations. Component/surface colors help discussion but do not establish
manufactured part separation. Distinguish evidence type as well as component color.

For transparent objects, separate a surface's own edge from an edge seen through
it, a reflection/highlight, an overlap and a possible opening. Preserve competing
interpretations when pixels cannot settle ownership. Do not turn every bright
line into a seam, erase a real boundary as a reflection without evidence, or close
an occluded contour simply because a closed polygon is convenient. Mark where
observed paths stop; hypothetical closure belongs in the inference layer.

Keep compact notes keyed to path IDs: claimed surface/boundary, source region or
landmark, observed versus inferred status, uncertainty, and consequential alternatives.
User explanations may resolve intended construction; label them as user-supplied
information rather than claiming to have discovered them in the photograph.

For larger assemblies, delegate component-focused traces when useful. All authors
use the same original coordinates and shared landmarks, and own distinct output
files/layers. Reconcile shared edges, contact, occlusion and surface ownership
before combining traces. Do not assume independently plausible components agree
at their interfaces. A small repair need not trace the whole asset.

## Review the overlay before deriving a schematic

An independent reviewer first saves source-only observations before seeing paths,
author interpretations or earlier verdicts. Then inspect the rendered overlay,
original-only image, line-only view and relevant closeups on the identified revision.
Check registration and contour placement, which faces each path bounds, retained
material around openings, depth order and unsupported connections. A plausible
box outline or elaborate path list does not establish an unexamined interface.

Record supported repairs and unresolved regions with path IDs and image evidence.
Revise and re-review affected boundaries. If a critical region cannot be settled,
actively collect and inspect discriminating references as above. If those attempts
still cannot settle it, preserve that limit and defer its dependent detail;
continue work supported directly by originals elsewhere. Do not make an attractive
trace a new authority over the photograph. When independent review is unavailable,
retain the inspection and disclose self-review.

For a blind evaluation, freeze the photo-only trace and independent review before
revealing a user explanation or annotated example. Preserve those artifacts and
score discovery separately from subsequent correction. Rough user annotations
illustrate intent; they are not automatically pixel-accurate ground truth.

## Handoff to schematics and construction

Keep source images, trace SVGs/renders, notes and review revisions together, for
example under `studies/traces/`. Original photographs remain in the source manifest;
traces and annotations are derivative candidates, not extra source views. Existing
comparison tools may display them; no new schema is required.

Give the schematic author the original, reviewed component trace and explicit
limits. Convert supported surface relationships into the separately editable
[schematic](schematic-workflow.md), including enlarged interfaces or sections as
needed. Keep perspective tracing distinct from derived orthographic estimates;
label estimated dimensions and user-supplied/inferred hidden relationships.
Check that the schematic retains the local features and surrounding surfaces
identified in the trace. Reconcile component interfaces before production geometry.

[Generated structural studies](generated-structure-studies.md) may follow as
secondary interpretations; a reviewed trace can constrain them but cannot make
invented geometry factual. Tracing does not replace the
[construction plan](mesh-construction.md), actual saved-mesh diagnostics, or
source-grounded review of the eventual model.

During schematic/model evaluation, reviewers repeat source interpretation and
trace both the original and candidate themselves. Follow
[paired contour review](paired-contour-review.md) for per-source coverage,
camera/state correspondence, native transparent contour exports and alignment
evidence. Builder overlays do not count as the critic's independent observations.
