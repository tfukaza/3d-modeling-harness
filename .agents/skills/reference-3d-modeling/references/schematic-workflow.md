# Source-grounded mechanical schematics

For substantial reference-driven creation, collect references following the
[shared workflow](reference-modeling.md), then establish detailed technical
schematics before dependent production modeling. Also do this when requested.
Apply sections and mechanical checks where relevant; other subjects still need
precise shape, proportion and detail views. Simple edits may reuse reviewed drawings.

## Drawing standard

By default, aim for the geometric specificity of a CAD section or cutaway. A small
number of views is sufficient when they resolve the relevant relationships, but
each must describe the actual shapes. Follow an explicit request for a rough
conceptual sketch instead when that is the user's intended deliverable.

- Draw the relevant parts' supported profiles, curvature, tapers, steps, recesses,
  openings and wall thicknesses. Show both inner and outer boundaries where known.
  Generic boxes, circles or single strokes are acceptable only when they describe
  the actual geometry at that scale; they cannot replace a complex part's shape.
- Resolve interfaces with explicit mating and support surfaces, attachment
  geometry, pivot/shaft locations, gaps and depth ordering. Labels and motion
  arrows supplement the geometry; they do not establish contact or connection.
  Add enlarged detail views when an interface is too small to read in the assembly
  view, retaining labels or landmarks that locate it in the assembly.
- Identify each section's cutting plane and viewing direction in a parent view.
  Distinguish intersected material from visible geometry beyond the cut. Hatch
  only intersected solids, keeping holes and cavities unhatched; distinguish
  adjacent cut parts by hatch angle or spacing. For a cutaway, identify the removed
  region and its boundary so removal cannot be mistaken for a real opening.
- Use a consistent, legended line hierarchy: strongest for cut boundaries,
  medium for visible edges, lighter dashed for necessary hidden edges, and thin
  chain lines for axes/centerlines. Distinguish inferred geometry with a separate
  annotation or style; hidden does not mean inferred. Keep line weights and hatch
  spacing readable at the intended output size, and avoid hidden-line clutter.
- Keep corresponding contours, axes, part identities and dimensions consistent
  across views of the same state. Mark view scales and changed operating states.
  Across operating states in a common projection/scale, reuse rigid component
  profiles and dimensions; change their pose, not their size to fit the drawing.
  Label an actual projection change explicitly before comparing fit or clearance.
  Include dimensions or ratios that control shape, fit and clearance, identifying
  measured, estimated and assumed values; do not imply precision absent from the
  sources. Use restrained callouts that do not obscure boundaries.

Unexplained empty regions, arbitrary lines and labels in place of complex geometry
are incomplete work. Where the source cannot establish construction, annotate the
specific unknown region and preserve the supported surrounding geometry. Do not
invent internals, fasteners or manufacturing detail to make the drawing look
complete. A bounded, explicit unknown is different from an omitted visible part.

## Source-to-drawing workflow

1. Personally inspect the available primary references and user brief, including
   operation footage where relevant and available. Establish object axes and map
   each relevant view into that frame. Record visible landmarks and the
   state shown in each reference before drawing hidden parts. For a complex
   interface, inspect focused crops or frames at readable scale as well as the
   full views that establish orientation and neighboring connections.
2. Before drawing, resolve the [difficult-region questions](photo-contour-tracing.md#prioritize-difficult-regions)
   with focused evidence. Where surfaces are unclear, first make and review
   [component photo traces](photo-contour-tracing.md), keeping original pixels and
   observed/inferred boundaries distinct. Reconcile neighboring component traces
   at their interfaces; supply reviewed overlays and limits to the drawing author.
   For complex forms and assemblies, then make and review the
   [original-view structural study](generated-structure-studies.md). Supply its
   reviewed image and limits alongside originals to the drawing author; generated
   wire lines do not establish hidden construction or substitute for an editable
   schematic. Skip simple/already clear cases or record tool unavailability.
   Delegate drawing to an author subagent when available, supplying originals,
   the target identity or coherent generic-design brief, and this drawing standard.
   Draw the views and states needed to explain the subject: for example,
   front/end or side sections and stored/intermediate/deployed positions. Mark
   parts, intended interfaces, fixed and moving components, pivots, and relevant
   dimensions or ratios, meeting the drawing standard above. Use precise editable
   2D geometry (for example SVG) or sections derived from preliminary 3D geometry;
   actual CAD software is optional. If using a 3D study, keep its dependent details
   provisional until schematic review. Preserve the editable source and a rendered
   image with the project's references and review notes.
3. Separate observations from inferred construction: use a legend and distinct
   lines or annotations for hidden or proposed paths, identify alternatives, and
   cite the original image regions or frames. Do not convert a plausible mechanism
   into a claim about unseen manufacturing. Indicate camera or dimensional limits.
4. Freeze the drawing revision and build a comparison packet with
   `scripts/build-comparison-review.py`: all retained references across paginated
   overview boards, plus matched-view and enlarged interface sheets. Inspect the
   actual images, retaining originals and crop context. Assign complementary
   independent critics for geometry/proportions/detail coverage and relevant
   construction/interfaces/operation. Schedule passes sequentially if slots are
   limited. Each first records
   an independent source-only interpretation before seeing the author's schematic or
   notes, then compares the diagram to available references and the user brief. Cover
   every diagram view and meaningful relationship. Check axes, relative
   dimensions, hidden/exposed boundaries, attachment ownership and whether the
   proposed operation can clear its interfaces. Inspect the actual rendered drawing
   at sheet scale for readability and at enlarged interface scale for contour,
   thickness, mating-surface and clearance detail. Check section cuts, hatch
   placement and cross-view consistency. Require revision for visible geometry
   replaced by placeholders, unexplained voids or ambiguous lines. Assess drawing
   quality and source fidelity separately: a polished layout cannot compensate
   for missing geometry, and detailed geometry cannot validate an unsupported
   interpretation. Require concrete source evidence. Revisit the pre-drawing list
   of difficult regions and verify each received focused inspection; transparency,
   crowded passages and mechanism engagement cannot be passed by overview alone.
   Unresolved relationships trigger targeted collection of another original view,
   closeup or operating state, followed by a revised trace/drawing and re-review.
5. Send findings to the schematic author, revise, regenerate the packet and re-review affected views and
   the whole assembly until the critic has no actionable discrepancies supported by
   the available evidence. Preserve unresolved assumptions explicitly. If independent
   review or decisive evidence is unavailable, report that limit rather than calling
   the schematic verified. Maintain a component/detail coverage table and issue/revision
   ledger. Advance only when relevant details have a review status and supported
   actionable discrepancies are resolved. Unresolved critical geometry blocks its
   dependent modeling; explicit unknown hidden details remain unverified rather
   than being declared perfect. If delegation is unavailable, disclose reduced
   independence. Do not start dependent production modeling on an unreviewed diagram.
6. Construct from the reviewed relationships, then compare the actual rendered
   model and animation with both the original references and the schematic. Originals
   remain authoritative for visible details; a schematic is a reasoning aid, not
   proof of source fidelity. Recheck it when later model evidence exposes a conflict.
