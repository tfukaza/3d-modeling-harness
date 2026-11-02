# Shared source-to-model workflow

## Collect references before drawing

Inspect the user's reference first and identify the target. For a specific product
or model, actively seek images of that exact variant: official photos/video,
manuals and independent hands-on views. Label related variants as supplemental;
do not silently mix their features. For a generic subject (for example a steam
locomotive without a named class), gather similar examples from several specimens
and define the intended design in project notes. Record which specimen supports
each selected feature; review the result for coherent construction rather than
requiring agreement with every incompatible example.

Search available web and connected sources using the target's identifiers or
category, then refine searches for missing views and details. Search broadly for
front/rear, both sides, top/end, oblique, close-up and operating
views as relevant. Retain all useful distinct references, source URLs/provenance,
identity/variant, view/state and missing coverage in the project manifest/notes.
Extra crops or near-duplicate marketing photos do not add independent depth evidence.
Start drawing when important shapes, details and interfaces are covered and further
searches mainly repeat evidence. Return to collection when a critique exposes a gap.
If useful evidence is inaccessible, record that specific limit; do not substitute
generated images or invent a hidden mechanism.

Build the source-only packet with `scripts/build-reference-review.py` before the
schematic. Inspect its actual images and readable crops with full-image context.
An incomplete packet documents gaps; it does not approve dependent geometry.

## Describe the originals

Identify the target asset and source variant. Every author/reviewer, including delegated component agents, personally opens the relevant original images. Give delegated tasks those source files; inventories and generated/model images supplement rather than replace them. Record source-specific observations, not merely a list of opened filenames.

Before reference generation, describe observable features, repeated counts/arrangement, axes, proportions, material/shape boundaries and group relationships. Separate visible facts from inferred function or occluded construction; identify which photo/region supports each important observation. Do not silently combine conflicting variants or invent measurements.

List the consequential regions that need extra attention in sketching and review,
using the [difficult-region priorities](photo-contour-tracing.md#prioritize-difficult-regions).
Name the question to resolve and the evidence needed, especially for transparent
boundaries, tightly interwoven parts/passages and complex mechanisms. Track actual
focused coverage and uncertainty instead of accepting a plausible overview.

Record visible minimum counts per photo/region and repeated pair patterns. Distinguish whole parts from concentric details, brackets and duplicate views of the same part; do not sum photos as additional components. Unknown hidden totals cannot excuse fewer parts than a source visibly shows. Resolve disputed counts with clearer original views, retaining specific uncertainty rather than labeling the entire assembly unknown. Record coverage and continuity too: two end panels do not necessarily reproduce an enclosing rear/side structure.

Name the plane/axis of important shapes. Image-space down may represent forward depth, not lower physical height; an apparent V in perspective is not evidence for a deep vertical V. Compare matched-perspective mockups plus orthographic views to resolve this. Explicit functional inferences, such as room for a hand, legs or a hidden mechanism, can constrain a plausible design without proving its hidden geometry.

When defining shapes depend on curvature, taper, thickness or slope, record where these change and compare the trend as well as the silhouette. Treat dimensions and shape as coupled constraints; document tradeoffs rather than silently changing the source shape.

## Trace ambiguous component surfaces before interpretation

For transparency, overlap or unclear interfaces, use
[photo contour tracing](photo-contour-tracing.md) after source inspection and before
generated interpretations or schematics. Trace one component's actual image-space
surface boundaries, preserving the original camera/pixels and distinguishing
observations from uncertainty/inference. Review the rendered overlays and reconcile
interfaces between component traces. A small repair need not trace the whole asset;
simple clear regions can proceed without tracing. Critical unresolved geometry
continues to limit dependent detail rather than being silently closed in a sketch.

## Interpret complex structure before schematics

For complex forms and assemblies, make a [color-coded generated structural study](generated-structure-studies.md)
after the source inventory and before drawing. Begin with one original-view image,
preserving camera, geometry and state while making component boundaries and surfaces
readable. Review it against originals before using it as an interpretive aid for
the schematic and construction plan. Skip simple/already clear geometry; if image
generation is unavailable, record the skip and continue source-grounded work.
Keep these studies separate from collected references and actual mesh diagnostics.

## Draw, critique and approve the schematic

Follow the [schematic workflow](schematic-workflow.md) for substantial creation,
including subjects without an ambiguous mechanism. Use object-appropriate shape,
contour and detail views; sections are needed where they explain construction.
Delegate the drawing and independent critique when available. Compare each frozen
revision against all retained references using paginated overview boards and
focused detail sheets. Review every relevant component/detail, repair supported
discrepancies and re-review until the stage gate is met. A preliminary Blender
study may help derive a drawing or resolve a projection, but is provisional and
does not bypass schematic approval for dependent production modeling.

## Model in Blender, beginning with a proportion study

After schematic approval, give the Blender builder the originals, reviewed drawing,
selected design/style and unresolved evidence. Before production geometry, record
the [mesh construction plan](mesh-construction.md#construction-plan-before-production-geometry):
how significant parts will be made, where surfaces connect or stay separate,
local edge profiles, modifier order and how difficult regions will be inspected.
Keep this proportional to the task; a provisional study needs only the decisions
it actually tests. Resolve construction choices before dependent detail work.
Build a neutral structural/proportion
study before detailed modeling, recording controlling ratios or estimated dimensions,
thicknesses, major masses, spacing and clearances. Compare matching photo views and
orthographic views before bevels, hardware or textures. Correct flattened volumes,
oversized parts and missing structure, then develop geometry and materials. Save
the editable `.blend` and authoring scripts when used; renders alone are not the asset.
Inspect a representative difficult component with cage, evaluated-wire and clay
views before repeating its construction, then obtain the dedicated
[topology review](evaluation.md#topology-review) for complex production geometry.
Revise the method when its geometry fails rather than hiding it with surface polish.

For human-used props, use a suitably scaled human/hand proxy when helpful; record estimated dimensions and pose. Inspect anatomy, posture, intended support/contact and interpenetration, not just bounding-box fit. Preserve usable reach and limb space, and retain a clean object view so the proxy does not conceal evidence. A generated proxy is not proof of ergonomic correctness. Use the [mechanical workflow](assembly-modeling.md) for functional interfaces and movement-critical states.

## Optional generated angle hypotheses

These later changed-angle studies are optional and distinct from the early
[original-view structural study](generated-structure-studies.md), which needs no
mockup. Neither replaces missing source evidence. Keep them separate
from collected references. If useful, generate **one angle per image**, defaulting
to exact orthographic front/side/back/top under flat diffuse neutral illumination.
Secondary three-quarter views or close-ups explore construction hypotheses.

Supply the actual mockup render at the requested angle as structure/camera/scale/occlusion anchor, plus the same original photographs as appearance/construction authority. Previously checked generated angles are secondary consistency inputs. Prompts or labels claiming an angle are not substitutes for the actual render. Preserve feature counts, relative scale, axes and source identity; do not force all known components to be visible through natural occlusion.

Inspect actual generated pixels for parallelism, expected occlusion and cross-view correspondence. Transverse identical components overlap in exact side projection; upright faces should not appear fully frontal in a top view. Check consistent counts, forward axes, landmarks, volumes and interfaces. Generated hidden views remain hypotheses. Reject mislabeled pseudo-orthographic views, contradictory construction or impossible proportions. Assemble a multi-view sheet only from accepted individual images.

Apply the shared [generated-study statuses and review](generated-structure-studies.md#review-before-using-the-image), checking camera/occlusion, counts, axes and relevant interfaces. Defer dependent detailed work while critical geometry remains unresolved; continue source-grounded studies that resolve the uncertainty.

## Iterate and review

Cross-reference originals, the reviewed schematic and the actual Blender model;
accepted generated studies remain secondary hypotheses. Follow [evaluation](evaluation.md)
with complementary independent critics. Freeze the `.blend` revision, render
matching views/details and relevant motion states, and rebuild the comparison
packet after each repair. Include the final frozen revision's topology diagnostics
for complex production geometry, even if the early representative component passed.
Critics inspect the actual asset with read-only alternate
views/sections when renders cannot settle depth or geometry. If a finding exposes
a schematic error, correct and re-review that drawing before dependent model work.

Spend geometry on recognizable contour, thickness and construction; place shallow grain/weave in materials. Low polygon count does not justify omitted defining components or blocky forms. Smooth shading cannot repair a wrong silhouette. For connected inorganic shells and controlled bevels use [mechanical props](assembly-modeling.md); for fitted artwork inspect the actual mesh UV layout and mapped result.

Finish one prototype through the requested stages before multiplying the kit. A
component/detail coverage table and issue/revision ledger must show no remaining
supported actionable discrepancies before signoff. Explicit unsupported hidden
details stay unverified; critical unresolved geometry means incomplete review.
Reopen the final saved `.blend`, verify its Blender renders and relevant motion,
and check requested exports in their target renderer/runtime. Carry known deviations
and missing evidence prominently into handoff. Keep references, editable schematics,
`.blend`, scripts, renders, prompts and reviews together in the project directory.
