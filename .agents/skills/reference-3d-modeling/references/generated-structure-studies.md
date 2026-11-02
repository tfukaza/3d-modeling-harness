# Generated structural studies before schematics

After inspecting originals, use image generation by default for complex forms and
assemblies to make component boundaries, curved surfaces and connections easier
to reason about. Skip simple or already clear geometry and repairs with adequate
reviewed studies. This stage precedes schematics and needs no Blender mockup.
It produces a visual interpretation, not reconstructed geometry or a measured mesh.

## Make the initial study

When transparency, overlap or unclear interfaces obscure boundaries, first make
and review [component photo traces](photo-contour-tracing.md). Keep the original
photo authoritative; an overlay can constrain the interpretation but does not
validate hidden geometry. Do not trace a generated image as though it were a source.

Choose one informative original view with readable detail and full-object context.
Record visible parts, landmarks, state and uncertainties first, following
[the source workflow](reference-modeling.md#describe-the-originals). Supply the
actual original image to an available image-generation/editing tool, using the
imagegen skill when available. A text description alone loses the image anchor.

Ask for a shaded 3D-style reinterpretation in the **same camera and pose**, with
distinct component colors and readable wire lines following the apparent surfaces.
Preserve silhouette, proportions, counts, openings, attachment positions and
occlusion. Color identifies components for discussion; it does not assert their
original materials, physical separability or manufacturing boundaries. Keep a
short color/part legend in the study notes and reuse those identities in later views.
Do not split an uncertain continuous surface just to assign another color.

Use a neutral background and restrained transparency where the source already
shows transparent material. Do not automatically reveal opaque interiors, explode
parts, straighten perspective or move components for visibility. Record known
source anomalies and omissions; do not silently invent their repair. A different
original may resolve them. Do not use the user's illustrative generated example
as product evidence unless the user explicitly defines it as the target design.

### Prompt recipe

Adapt the bracketed fields; omit irrelevant clauses rather than inventing details.

> Re-render the attached original photograph as a shaded 3D structural study with
> thin, readable wire lines following its apparent surfaces. Keep the original
> camera, perspective, silhouette, relative proportions, visible component counts,
> openings, attachment positions, operating state and occlusion. Use distinct
> restrained colors for [observed components], with consistent identities; colors
> explain the parts rather than reproduce the material palette. Preserve curved
> transitions, thickness and the visible depth ordering. Use a neutral background
> and only the transparency supported by the source. Do not add internals,
> fasteners, cutouts or connections, separate continuous parts, or complete hidden
> geometry. Keep [uncertain/occluded regions] unresolved. Known source limits:
> [limits, if any]. Do not repair missing features without source evidence. Wire
> lines are an illustrative surface interpretation, not verified mesh topology.

Generate one initial image. Request another original-view interpretation, focused
detail, or a targeted revision only when it answers a named structural question.
Keep full context alongside enlarged details. Changed-camera, cutaway and exploded
studies are separate, explicitly labeled hypotheses; do not present them as
observed geometry. For later mockup-anchored angle studies use
[generated angle hypotheses](reference-modeling.md#optional-generated-angle-hypotheses).
If a revision keeps inventing the same interface, return to originals or a direct
schematic/proportion study rather than repeating generation without new evidence.

If image generation is unavailable, record the skipped step and continue from
originals. Do not introduce an unrequested paid API/CLI fallback or make image
generation a blocker for otherwise source-grounded work.

## Review before using the image

A reviewer records its source-only interpretation **before** seeing the generated
study, prompt rationale or author conclusions. Then inspect the actual original
and generated pixels together, including closeups at important interfaces. Reuse
the schematic critic for this pass when appropriate; another role is not required
just to review a study. Preserve independent review when agents are available;
otherwise disclose that the pass was self-review.

Check camera/pose and silhouette; part counts and color identities; curvature,
thickness, openings, attachment ownership and depth ordering. Look for omitted
features, invented joins, disconnected paths and occlusion changes. Separate a
useful clarification from a plausible but unsupported interpretation. Dense regular
wire lines do not establish quads, connectivity, valid booleans or a clean mesh.

Use these statuses for early structural and later generated-angle studies:

- **PENDING:** generated but not yet inspected; cannot drive dependent work.
- **PASS:** inspected and usable for a named interpretive purpose. Record useful
  regions, source support, uncertainties and any excluded region explicitly.
- **REJECTED:** misleading or contradictory for its intended use; revise or set
  aside. Do not pass a defective region because the rest looks attractive.

The review note identifies source and study files/revisions, purpose, observations,
discrepancies, unresolved regions and status. PASS does not verify hidden geometry,
measurements or original-source coverage. Pending, rejected and excluded regions
cannot be used as the basis for dependent geometry. A rejected study does not
block choices supported directly by originals; defer affected detail only while
critical geometry itself remains unresolved.

## Handoff and provenance

Keep originals unchanged. Store generated images, exact prompts, source-image
links/IDs, color legends and review notes together, for example under a project's
`studies/structure/`, separate from its collected-reference manifest. Retain distinct
filenames for revisions and label each image as generated in review packets.
Use existing comparison tools only as presentation aids, labeling generated studies
diagnostic rather than source evidence; no new packet schema is needed.

Give schematic authors and model builders the originals plus reviewed studies and
their limits. Use them to articulate profiles, part boundaries and questions for
the [construction plan](mesh-construction.md), then verify those choices against
originals. Schematics remain editable, separately reviewed deliverables. Actual
[saved-mesh diagnostics](mesh-construction.md#diagnostic-evidence-from-the-saved-revision)
and topology review remain necessary; generated wire lines cannot replace them.
