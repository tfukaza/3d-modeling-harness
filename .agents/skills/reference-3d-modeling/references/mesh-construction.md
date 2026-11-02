# Plan and inspect mesh construction

Use this guidance before production modeling and when repairing complex surfaces.
The goal is a controllable mesh that represents the subject's surfaces and assembly,
not a particular modifier stack or a uniformly dense, all-quad mesh.

Reviewed [generated structural studies](generated-structure-studies.md) may help
articulate part boundaries and profiles before this plan. Their drawn wire lines
are suggestions to reason about, not a cage to copy or proof of connectivity.
Choose topology for the actual surfaces, intended use and original evidence.

## Construction plan before production geometry

After reference/schematic review, the builder records a compact construction plan
with the project. For each significant component or repeated family, identify:

| Component and surface intent | Construction sequence | Edges and interfaces | Risk and inspection |
| --- | --- | --- | --- |
| Physical part, controlling profile, continuous versus separate surfaces, static versus deforming use | Starting profile/cage, direct edits, modifiers in intended order, operations kept editable or applied | Sharp/chamfered/rounded regions, local radii and resolution, wall thickness, openings, mating surfaces and separate hardware | Likely corner/transition failures, representative prototype, clay/cage/evaluated views or sections needed to verify it |

Tie decisions to the originals, reviewed drawing and deliverable. Explain the
non-obvious choices; do not write an exhaustive operator log. Plan a proportion
study too, but keep its detail provisional. The coordinator checks unresolved
construction choices before dependent production work; this is an internal stage
check, not a new user-approval requirement.

Build and inspect one representative difficult junction or surface before repeating
the method. When a method produces pinching, messy intersections or the wrong
profile, revise the construction plan and rebuild the cause rather than accumulating
corrective modifiers on top. Recheck a drawing if the failure exposes a design error.

## Choose a method for the actual shape

| Required geometry | Useful methods to consider | Decision to resolve |
| --- | --- | --- |
| Constant cross-section or rotational part | Extrude a designed profile; revolve/lathe a section | Preserve steps, inner/outer walls and local curvature in the profile rather than approximating them with intersecting primitives. |
| Continuous irregular junction | Direct mesh construction, extrusion, bridged loops, local retopology; boolean union where suitable | Establish a shared boundary and intended transition. Joining objects alone does not connect their surfaces. |
| Aperture, recess or intersecting volume | Designed inner loops or boolean difference/intersection | Make the actual void and its walls; inspect the resulting intersections and triangulation. A dark insert is not a cutout. |
| Smooth curved or deforming surface | Deliberate cage/edge flow, lofting, support loops or creases, selective subdivision | Put curvature and deformation support where needed; keep poles and abrupt density changes out of sensitive transitions. |
| Thin shell or ribbon | Explicit inner/outer surfaces or thickness from a suitable surface | Resolve rims, offsets, bends and thickness without self-intersection. |
| Symmetric or repeated construction | Mirror, array, instancing or shared parameters | Verify welds where continuity is intended and preserve real part separation elsewhere. |

Primitives are useful blockout and construction inputs. They are finished parts
only when their geometry actually describes the part. Modifiers are tools, not
evidence that a part is well made. Choose order deliberately: a cut may need to
precede a local edge treatment, while another design may need a shaped cutter or
a finished profile first. Inspect the result rather than imposing one universal order.

Direct vertex/edge/face editing is appropriate when it gives better control of a
profile or transition. Use scripts/BMesh or Blender Edit Mode as suitable; use
computer interaction when useful and available. Mouse manipulation is not inherently
more accurate than scripted geometry. Preserve the editable `.blend` and record
important manual changes so a generator does not silently overwrite them.

## Edge treatment is an explicit local decision

- Start with the simplest geometry that preserves the intended profiles. Newly
  authored primitive helpers default to **no automatic bevel**. This does not mean
  flattening an observed curve: construct that curve in the profile or cage.
- Classify meaningful edges as sharp, chamfered or rounded. Choose affected edges,
  width/radius, profile, segment count and corner treatment from reference, local
  thickness/spacing and viewing distance. Do not assign one radius or subdivision
  level to every part. A deliberate whole-part treatment is valid when the source
  actually supports it.
- Select edges explicitly or use suitable weights/groups; inspect whether an
  angle-based selection includes unwanted corners. Resolve object scale before
  interpreting widths. Inspect concave, acute and multi-edge intersections, bevel
  terminations, thin sections, and transitions between different radii.
- Overlap clamping is a guard, not proof of the intended profile. A clamped bevel
  can become uneven or collapse locally. Do not disable safeguards simply to force
  a larger radius through bad topology; adjust the profile, edge selection or mesh.
- Check broad-face planarity and curved highlights under grazing light. Smooth
  shading, weighted normals and extra subdivision cannot repair incorrect volume,
  collapsed geometry, intersecting skins or a pinched corner.

## Assemble physical components, not overlapping silhouettes

For a continuous part, build shared surface boundaries or clean the result of a
solid operation. Remove unintended internal faces, slivers, doubled skins and
unmatched edges at the junction. For separate assembled parts, retain the actual
gap, seam, bearing/contact or fastener relationship. Do not union a whole assembly
merely to make it one object, and do not treat all touching surfaces as duplicate
geometry. Matching a silhouette from one camera does not establish a clean junction.

Openings must have the required depth, interior walls and access. A hole through
an attached feature must not be blocked by an uncut parent shell behind it. Check
the relevant parts together with an oblique, section or operating state. Boolean
operations are optional; a directly modeled opening is equally valid. Hidden
factory construction stays unverified rather than being invented to justify a join.

## Cleanliness depends on use

Inspect after topology-changing operations and before surface polish. Repair actual
zero-area faces/zero-length edges, unintended duplicates/internal faces, bad normals,
accidental holes and self-intersections in the affected region. Use scale-aware
measurements: a tiny valid feature is not automatically degenerate. Preserve intended
seams and attribute splits; do not globally merge nearby vertices as a cleanup recipe.

Planar static faces may use n-gons or triangles when their evaluated/exported
triangulation is stable. Curved, subdivided and deforming regions need suitable
edge flow, support and sampling for their intended behavior. Avoid problematic
nonplanar faces, skinny slivers and dense corner fans when they cause shading,
triangulation, editing or deformation failures. Do not reject a valid planar cap
just because it is not a quad. Require closed/manifold solids only where the part
and deliverable call for them; separate hardware and intentional open surfaces
are not errors by themselves.

## Diagnostic evidence from the saved revision

For complex production geometry, provide focused diagnostics at the representative
component checkpoint and final frozen revision. Reopen that saved `.blend` and show:

- **Authored cage:** actual base-mesh edges, with relevant modifier visibility and
  whether construction operations have already been applied identified.
- **Evaluated surface:** actual mesh edges after the intended modifier stack, over
  neutral clay with readable occlusion. Inspect export triangulation too when an
  export is requested, without mistaking normal/UV splits for broken surfaces.
- **Surface and interface views:** clay under grazing light, plus a useful alternate
  angle or labeled section for difficult corners, cuts and joins. Show relevant
  deformation/motion states when applicable.

Pair wire views with shaded surfaces: a dense wireframe alone cannot establish
smoothness or correct construction. Use readable closeups with full-part context,
not an entire asset reduced to an opaque tangle of lines. Wire edges must come from
the identified mesh, not a decorative grid or a different reconstruction. If cage
and evaluated geometry are identical, say so rather than inventing a distinction.

Use existing manifest fields: `revision` and `asset` identify the frozen model
(the packet records its hash); `views[].view` and `state` label representation,
part, camera, modifier visibility and pose. A paired comparison can add `note`.
No new packet schema is required. Keep topology evidence supplementary to matched
surface/reference comparisons. An unpaired diagnostic overview can use
`comparisons: []`; its intentional coverage gaps do not establish source matches
or close unresolved source review. Do not invent photo matches to make its status
look complete.

Generate temporary diagnostic materials, modifier visibility changes or sections
in a disposable inspection scene and never save them over the canonical asset.
Feed these views and the actual saved mesh into the [topology review](evaluation.md#topology-review).

For version-specific controls consult the matching Blender manual, for example
[Bevel](https://docs.blender.org/manual/en/5.1/modeling/modifiers/generate/bevel.html),
[Boolean](https://docs.blender.org/manual/en/5.1/modeling/modifiers/generate/booleans.html)
and [Subdivision Surface](https://docs.blender.org/manual/en/5.1/modeling/modifiers/generate/subdivision_surface.html).
