# Independent review packet

Apply the shared source-first review and repair procedure in the active asset-family
skill. See [evaluation](evaluation.md) and [mechanical assembly](assembly-modeling.md) when applicable.
This reference provides the harness packet and prompts rather than another copy
of that procedure. Keep author interpretations and prior pass claims separate from
original evidence.

For reference-accurate reviews follow [reviewer-owned contour comparison](paired-contour-review.md).
Inspect and account for every retained original; create independent paired
source/candidate contours for geometry-informing views. Camera/state matching and
held-out boundary checks precede alignment claims. A paginated overview, builder
annotation or clean mesh is not evidence of completed per-source review.

For [component photo traces](photo-contour-tracing.md), save source-only observations
before seeing the author's paths or explanation. Review rendered overlays against
the unchanged photo and line-only views, naming affected paths/regions. Follow
the [difficult-region priorities](photo-contour-tracing.md#prioritize-difficult-regions)
for transparent boundaries, crowded passages and complex mechanisms: record focused
coverage and uncertainty, not just a whole-object plausibility judgment.

For early [generated structural studies](generated-structure-studies.md), retain
the same source-first independence: save the critic's original-image inventory
before showing the generated interpretation. Review its actual pixels and record
the permitted use and excluded regions before handing it to schematic/model authors.
Keep generated studies out of original-source manifests; their wire lines are
illustrative and cannot satisfy the actual-mesh topology evidence requirement.

## Select construction guidance

Use object-family references for construction, not a growing list of product fixes
in the common reviewer prompt. Ordinary props use proportion, surface and placement
checks; mechanical assemblies and vehicles use the existing assembly workflow and
specialized vehicle skills where applicable. Characters require character-specific
anatomy, deformation and pose guidance when such a task is undertaken; do not apply
mechanical access checks to every asset or claim the prop workflow covers character
rigging. Add a family reference when a real task establishes its requirements.

## Source-grounded schematics

For substantial creation, delegate a detailed schematic before dependent Blender
modeling, following the [drawing standard](schematic-workflow.md). Establish a consistent object frame from
available originals; show the views, states, interfaces and motion needed to
explain the assembly. Mark measured or observed features separately from proposed
hidden construction, cite evidence, and label unresolved assumptions. SVG is a
useful editable format, not a manufacturing authority.

Have complementary independent critics first inventory the original sources without seeing
the author's diagram. Then compare each diagram view and relationship to those
sources; use focused structural and alignment critics in parallel when useful.
Revise and re-review until no actionable supported discrepancies remain. A reviewed
schematic can serve as a qualified modeling brief, but cannot prove 3D clearances,
construct hidden factory details or supersede the originals. Record uncertainties
that the model and motion must test. If delegation is unavailable, disclose reduced
independence rather than describing a self-review as independent.

## Multi-view evidence before construction

Before drawing, follow the [collection procedure](reference-modeling.md): seek the exact variant for a specific target, or similar specimens for a documented coherent generic design. Actively seek front, rear, both ends/sides and oblique/operating views as relevant. Prefer official photos/video, supplement with independent hands-on views, and retain originals with URLs or user-provided provenance. Several crops of one photo or near-identical marketing angles do not provide independent depth evidence. If a required view cannot be found, record the gap and keep the affected geometry provisional.

Before modeling a difficult interface, assemble a source-only packet using `scripts/build-reference-review.py` and its JSON manifest (see `scripts/model-comparison.md`). Give each image a view/pose and map shared landmarks. For each difficult region, provide readable crops from at least two materially different angles **and full originals with crop boxes**. Inspect the generated images directly. Do not count metadata or a generated board as proof that angles actually differ.

Record each consequential construction claim against the views that support it. Challenge whether apparent boundaries come from transparency, reflection, shadow, occlusion, or another part seen behind the casing. A bright patch does not establish an opaque plate; a dark line does not establish an aperture. Check the interpretation against a second angle or motion state before constructing a visible component. If evidence remains ambiguous, state that and avoid adding unsupported visible hardware.

The critic must examine the source-only multi-view packet before the schematic/model. After export, regenerate matching model closeups for those same regions and review the combined evidence. Structural tests prove properties of the chosen geometry; they cannot establish that a reference contains the component.

## Prepare the packet

- First supply original photographs/artwork and relevant operation footage, plus
  the permitted style departures. The critic saves its source inventory
  before it sees generated structural studies, schematics, model images or author notes.
- Then supply the frozen editable schematic or canonical `.blend` revision and
  requested exports, current Blender multi-angle renders for models,
  delivered browser/card views, and meaningful motion states if the asset moves.
  Exclude older captures; a filename alone does not establish revision provenance.
- For a mechanically complex interface, isolate a readable close-up of the relevant
  original photograph or footage frame and pass that crop directly to the reviewer
  for focused inspection. Include corresponding model close-ups in the same pose
  and similar camera when available. Keep the full originals and identifying
  landmarks alongside the crop; magnification alone must not erase object axes,
  surrounding connections, or view/pose differences. Use several original views
  when one crop cannot resolve depth or operation.
- Make paginated all-reference overviews and focused comparisons with
  `scripts/build-comparison-review.py`, including stage/revision identity.
  `scripts/compare-model-reference.py` remains useful for individual model pairs.
  The batch tool always retains context; use `--context` for individual pairs so
  full originals and crop boxes remain visible. Map view orientation with full-object landmarks; similar close-ups alone
  do not establish corresponding sides. Scale uniformly, do not mirror or stretch,
  and label any camera/pose mismatch. Regenerate evidence after repairs.
- Keep source/model observation and inference distinguishable. Use a compact
  component coverage table; detailed confidence, consequences and required actions
  belong to findings or unresolved questions, not every matched component.
- For complex production geometry include the [topology diagnostics](mesh-construction.md#diagnostic-evidence-from-the-saved-revision):
  actual authored cage, evaluated wire overlay, clay/grazing-light views and useful
  interface sections. Add export triangulation when exporting. Label representation,
  part, revision, modifier visibility and pose using the existing revision field,
  descriptive `view`/`state` labels and comparison `note` text, without a new
  schema. Wire views are not photo-appearance matches: mark paired comparisons
  diagnostic or keep a separate unpaired diagnostic overview. Its intentional
  coverage gaps do not replace the normal surface/reference comparison gate.
  Include full-part context and keep temporary overrides out of the canonical `.blend`.

## Focused critic assignments

For a complex asset, give independently scoped critics the same originals and style
brief first. After each saves a source-only inventory, provide the same frozen revision
and, for modeling, the reviewed schematic. Use complementary geometry/detail and
construction critics for substantial creation, adding relevant scopes below.
Roles can run in parallel or sequentially when slots are limited:

- **Construction:** enclosing volumes, support/attachment ownership, interfaces,
  physical use and meaningful operating states.
- **Alignment and proportion:** map views into shared object axes and compare
  landmark positions, face-plane alignment, dimensions/ratios, angles and where
  adjoining surfaces begin or end. Check depth with a suitable alternate view or
  geometry, and account for projection and uncertainty rather than accepting a
  plausible front silhouette as proof of coplanarity or correct boundaries.
- **Appearance:** source-defining details, silhouette, allowed style, feature-edge
  ink, material response, dithering and object/ground shadows at delivered size.
- **Topology and surface construction:** for complex production geometry, dedicate
  a critic to [topology review](evaluation.md#topology-review) at the early difficult
  component checkpoint and final frozen revision. Inspect actual cage/evaluated
  geometry, local edge treatment, continuous versus assembled surfaces, openings,
  and suitability for subdivision/deformation/export. This scope supplements
  reference fidelity and construction review; a clean mesh can still depict the
  wrong assembly. Schedule the pass sequentially when slots are limited.
- **Motion and delivery:** actual runtime states, attachment/clearance through the
  transition, reversal, framing, reduced motion and exported-asset consistency.

Choose roles relevant to the asset; a simple change does not need four reviewers.
The coordinator reconciles findings against originals and retains whole-asset
coverage. Do not let a schematic override contradictory source evidence.

## Staged prompts

Start the critic with no inherited builder conversation. Fill in artifact paths and
style constraints, not suspected defects or expected answers.

**Source stage:**

> Independently study originals at [references] using [applicable family skills].
> Target identity or selected generic-design brief: [brief].
> Permitted style departures: [brief]. Do not open schematics, model images, implementation,
> author notes or previous reviews yet. Save a compact source-only inventory with
> object/view correspondence, defining features, relevant relationships and
> uncertainties to [inventory]. Apply functional or pose checks appropriate to this
> object's purpose. Cite specific source regions. Return it and wait for the candidate.

**Component photo-trace stage (unclear surfaces before interpretation/schematics):**

> Inspect the original [photo] and save your independent observations of [component]
> and consequential uncertain regions before opening [trace revision]. Then compare
> the rendered overlay, original-only, line-only and interface closeups following
> [photo contour tracing]. Check pixel registration, surface/boundary ownership,
> transparency/occlusion, openings and retained adjacent material. Cite path IDs and
> source regions for supported discrepancies and unresolved questions. Do not read
> author rationale or prior verdicts first. A trace cannot establish hidden geometry
> or measurements. Re-review supported repairs before dependent schematic detail.

**Generated structural-study stage (before schematics for complex forms):**

> Compare your saved source-only inventory and original images at [sources] with
> generated study [revision/image], following [generated structural studies].
> Inspect camera/pose, silhouette, counts, curvature, part boundaries, openings,
> attachments and occlusion. Separate useful clarification from unsupported
> interpretation. Record discrepancies, uncertainty, status and permitted use in
> [report], excluding misleading regions from dependent work. Do not read author
> conclusions or previous reviews before recording your findings. Generated wire
> lines do not establish actual topology or missing source coverage.

**Schematic stage:**

> Compare your saved inventory with schematic revision [revision] at [source] and
> paginated boards/detail sheets at [comparisons]. Apply the detailed schematic
> standard and assigned scope [scope]. Inspect originals again as needed. Cover all
> relevant components/details; report supported discrepancies and unresolved coverage
> to [report]. Distinguish omitted geometry from unsupported hidden construction.
> Do not read other reviews or author explanations during this pass. For a generic
> subject evaluate the selected coherent design.

**Model stage:**

> Compare the saved inventory with frozen revision [hash] at [saved .blend], paired
> images at [comparisons], reviewed schematic [drawing revision], and requested
> delivered-runtime evidence at [captures]. Inspect originals again as needed.
> You may make read-only views, sections or geometry
> checks where useful. Do not read other reviews or contact the builder during this
> independent pass. Report evidenced discrepancies and unresolved coverage to
> [report]. Actively challenge your assigned scope for consequential structural or
> functional mistakes, and seek evidence that could disprove your first interpretation.
> Follow reviewer-owned contour comparison: personally inspect all relevant
> originals, save a per-source coverage ledger, fit and lock corresponding cameras
> using stable landmarks, then independently trace both source and actual render.
> Compare panel/cutout/junction contours and held-out landmarks, not only gross
> silhouette. Keep raw images, individual/combined contours, residual observations
> and hashes. Diagnostic camera mismatches cannot close critical alignment claims.
> Prioritize meaningful failures, not cosmetic nitpicks; do not invent defects. Separate
> source/model observations from inference and explain source-inventory corrections.
> Use the applicable family's review criteria.

**Topology stage (complex production geometry):**

> Independently study originals at [references] and save your source interpretation
> of surfaces, part boundaries, edge profiles and relevant use before opening the
> model. Then inspect frozen [revision/hash] at [saved .blend] and [cage/evaluated-wire,
> clay/grazing-light, section and state evidence]. Follow [mesh construction] and
> [topology review], considering the actual delivery/deformation requirements.
> Verify suspected mesh problems on the saved geometry where images are insufficient;
> separate demonstrated defects, source mismatches and missing evidence. Identify
> affected regions, evidence, consequences and repair goals in [report]. Evaluate
> the geometry, not compliance with a favored operator or an all-quads rule. Do not
> read builder rationale or other critics' reports before recording your independent
> findings. Afterward, inspect [construction plan] as claims to verify. Request
> repairs/review only for supported issues, retaining legitimate separate components
> and intentional openings. Re-review affected diagnostics and the final revision.

When testing the reviewer itself, preserve these exact prompts, model revision and
reports. The coordinator retains any answer rubric; do not include it in this packet.
