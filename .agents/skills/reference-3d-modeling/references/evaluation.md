# Schematic and Blender model evaluation

## Scope of the shared method

Keep evidence handling and independent-review procedure general. Family-specific
construction belongs in focused references, such as [mechanical assembly modeling](assembly-modeling.md)
as applicable. Individual product dimensions,
axis choices and repair answers belong in asset notes, not the shared skill. Apply
only checks relevant to the asset's intended use.

## Builder–critic iteration

Use this loop first for [schematics](schematic-workflow.md), then for Blender models.
For substantial creation, delegate drawing and modeling to author/builder subagents
when available, with complementary independent critics at each stage. The coordinator
manages evidence, assignments, coverage, findings and stage gates. Run extra focused
passes sequentially when slots are limited. Repairs may reuse reviewed schematics,
rechecking affected relationships. If agents are unavailable, disclose reduced
independence. Begin the critic with a fresh context, without the builder's reasoning,
implementation notes, prior verdicts or expected findings. Both agents read the
applicable art/mechanical constraints and personally inspect original references.

1. **Source-only first:** give the critic originals and style constraints before
   schematic/model images. Save its construction inventory, consistent object axes, cross-view
   landmark mapping, defining forms/surfaces, relevant relationships and uncertainties.
   Select construction and behavior checks through the applicable family workflow;
   mechanical access/routing checks do not apply to every asset.
   Reconcile ambiguous directions with full views or relevant footage; screen-left
   in a crop is not object-left. Later inventory changes require source evidence.
2. **Frozen comparison:** for drawings supply the editable schematic and rasterized
   views; for models supply an identified saved `.blend` revision, current Blender
   multi-angle renders and motion states when relevant. Create simultaneous reference/
   candidate comparisons with `scripts/build-comparison-review.py`, covering all
   retained sources across overview pages and focused detail sheets. Use uniform
   landmark scale, similar camera and the same functional
   state. Keep full-image context with close-up crops. Do not mirror or stretch to
   manufacture agreement; label unavoidable mismatches and exclude stale evidence.
   For complex production geometry include the [topology packet](mesh-construction.md#diagnostic-evidence-from-the-saved-revision)
   from that saved revision. Review an early representative difficult component
   before its method is repeated, and review the final frozen geometry again.
3. **Independent findings:** compare the observed features and relationships with
   the actual drawing/model using the applicable construction/pose criteria. Inspect depth
   or alternate states where one view cannot settle a relationship. Inspect the
   actual `.blend` with read-only alternate views/sections or geometry checks when
   rendered evidence is insufficient. Record source
   observations separately from model observations and inference. Keep the component
   coverage table compact; each finding or unresolved question needs specific evidence,
   confidence, consequence and action.
   Follow [reviewer-owned contour comparison](paired-contour-review.md): inspect
   every retained source, account for detailed coverage/exclusions, match camera
   and state, and independently trace corresponding original/candidate panels,
   openings and surface boundaries. Inspect raw images and individual/combined
   contours; record residuals and uncertainty. Reusing author traces or listing
   overview/comparison files does not satisfy this independent evidence requirement.
4. **Repair and re-review:** send findings to the builder, repair and regenerate
   comparisons. Include small observable discrepancies, not only blockers. Recheck
   changed interfaces and the whole asset; do not quietly downgrade unfixed findings.
   If a model finding contradicts the schematic, correct and re-review the drawing
   before dependent model work. Author explanations are claims to verify after the
   independent pass, not authority.
5. **Verdict:** actively challenge the whole assembly for consequential structural
   or functional mismatches, even after individual parts appear plausible. Form and
   test competing explanations against the originals and actual model; seek evidence
   that could disprove the first interpretation. Prioritize meaningful failures over
   cosmetic nitpicks. Do not invent a defect to satisfy this hypothesis; distinguish
   demonstrated mismatches from unresolved evidence. Audit the coverage table's match
   claims before signing off: presence, count or an attractive projection does not
   prove a source-specific relationship. Narrow unsupported claims and revisit them.
   Continue until no supported actionable discrepancies remain on the identified
   final revision and relevant components/details have review status. This means
   completed review, not proof of unseen construction. For a generic subject,
   evaluate the documented coherent design against selected examples rather than
   requiring incompatible features of every specimen.
   Important unresolved construction or unexamined behavior means incomplete review.
   A disputed signoff warrants a fresh source-first critic.
   Audit actual per-source evidence before signoff. Unmatched views cannot close
   critical alignment questions; unexplained exclusions or unexamined critical
   panel boundaries keep the gate incomplete even when numeric mesh checks pass.

Keep review scoped to the requested asset; do not expand into unrelated models or
redesign an accepted artistic style.

Numeric tests verify their stated properties. Assertions against an authored
contract do not independently validate that contract against the original. An
attractive proof, metadata, or earlier signoff cannot replace current visual evidence.
Keep a short issue/revision ledger and label hidden unsupported construction unverified.

When evaluating the critic itself, keep user-supplied answers with the coordinator.
Do not leak them through skill edits, suspected-part prompts, previous reports or
conversation inheritance. Freeze the model, preserve prompts/reports, and score
independent evidence rather than keywords. Report misses and false positives; one
successful trial does not establish reliable recall on future assets or other
object families. Test a distinct real task before making a broader reliability claim.

## Focused parallel criticism

For substantial creation, use at least two complementary critic scopes: geometry,
proportions and detail coverage; and construction/interfaces as appropriate.
Complex production geometry also receives the dedicated topology scope below;
schedule it sequentially if the author and other critics occupy the available slots.
For a complex or disputed asset, divide independent deeper reviews by actual risk,
using parallel agents when available. Useful complementary focuses are structural
assembly and operation; alignment, proportions, object-relative axes, face-plane
relationships and adjoining surface boundaries; appearance, material/edge/shadow
treatment; and motion, clearance and delivered-runtime behavior.
Choose only roles relevant to the asset, not a fixed team for simple work. Each critic
personally checks the originals, intended style and the same identified revision; a
reviewed schematic can help after the critic's source-only inventory, but does not
replace the original evidence. Preserve a whole-asset coverage audit so gaps between focused reviews are not silently accepted.

Give each role its own evidence-grounded scope without the builder's conclusions or
other reviewers' suspected findings. Each reports observations, evidence, confidence,
consequences and uncertainty. Reconcile contradictions by returning to the sources
or producing a discriminating view, not by taking a vote. Send actionable findings to
the builder, then re-review the changed interfaces and the whole asset on the new
revision. For simple work one appropriately scoped critic can cover multiple roles.

## Topology review

Use a separate topology critic for complex production geometry: irregular joined
surfaces, difficult cutout/corner intersections, consequential modifier stacks,
or subdivided/deforming regions. Ordinary primitive-only work and trivial edits
do not need another agent; the existing reviewer still checks affected geometry.
If a separate critic is unavailable, keep the inspection and disclose the reduced
independence. Do not equate a self-review with the independent pass.

The critic first studies originals for part boundaries, edge profiles, curvature
and relevant use. Then inspect the frozen `.blend`, authored-cage and evaluated-wire
views, neutral clay/grazing-light images, and relevant sections/states. Inspect
export triangulation when an export is requested. Establish independent findings
from the actual geometry before reading the builder's construction-plan rationale;
then assess that plan as a claim to verify, not evidence that its method succeeded.

Use [mesh construction](mesh-construction.md) to assess:

- Whether apparent continuous parts have connected surfaces rather than hidden
  primitive intersections, while real separate components retain their intended
  seams, contact and clearance. Check voids through the whole enclosing assembly.
- Whether local edge treatments preserve the specified profile without distorted
  miters, collapsing thin regions, pinching, wavy broad faces or excess rounding.
  Compare cage and evaluated surfaces to locate modifier-induced failures.
- Whether actual geometry has unintended internal/doubled faces, degeneracies,
  normal errors, accidental holes or unstable triangulation, and whether edge flow
  and density suit static, subdivided or deforming use. Verify suspected numerical
  defects on the saved mesh at the relevant scale; do not infer them from wire density.

Judge geometric outcome and suitability, not the number of modifiers or presence
of a preferred operator. A clean direct mesh is not defective for lacking a Boolean
modifier; a Boolean result is not accepted merely because a real cut exists. Neither
all-quads nor one closed/manifold mesh is a universal requirement. Distinguish source
fidelity, surface appearance, mesh integrity and edit/deformation suitability.

Each supported finding names the part/region, affected revision/state, diagnostic
view or reproducible mesh observation, consequence and repair goal. A different
modifier or manual reconstruction is a recommendation only when it addresses a
demonstrated limitation; do not redesign correct geometry for stylistic topology
preferences. Missing/obscured topology evidence stays unresolved. Do not pass an
unexamined critical junction because its beauty render looks plausible.

Send supported findings to the builder; repair the source or editable mesh, update
the construction plan when the method changes, and regenerate affected diagnostics.
Recheck the interfaces and final frozen revision before closing the findings.
Sections and diagnostic overrides must not alter the canonical saved asset.

## Evidence and acceptance

Inspect original photographs and the actual current drawing/model from corresponding views. Cover relevant components and details in a compact correspondence table, including omissions and uncertain relationships. For animated work inspect rest, intermediate and endpoint states, attachment, clearance and reversal. Reopen the final saved `.blend` and check Blender renders; when delivery targets a runtime, inspect the requested exported artifact there as well. Document remaining gaps and do not claim complete review when important evidence or independent review is unavailable.
