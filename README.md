# 3D modeling harness

A local Codex workspace for building and reviewing reference-accurate 3D models in Blender. The project-local skill lives in `.agents/skills/reference-3d-modeling`; `AGENTS.md` makes the workflow discoverable in this directory. Art direction belongs to the individual project.

## Workflow

1. Inspect the supplied reference and collect useful distinct images widely. Seek the exact product/variant for specific targets, or similar examples for a coherent generic design. Continue until key views/details are covered and further searches mainly repeat evidence; record gaps.
2. Identify difficult regions for focused sketching/review: transparent boundaries, interwoven parts/small passages and complex mechanisms. Where surfaces are unclear, first review [component photo traces](.agents/skills/reference-3d-modeling/references/photo-contour-tracing.md) aligned to original pixels. For complex forms and assemblies, then generate and review a [color-coded structural interpretation](.agents/skills/reference-3d-modeling/references/generated-structure-studies.md) before schematics. Keep the original camera/geometry and distinguish interpretation from source evidence. Skip simple/already clear geometry or record unavailable image generation.
3. Have an author subagent draw detailed schematics. Independent critics inspect originals first, then compare drawing revisions against paginated reference boards and detail sheets. Revise until supported actionable discrepancies are resolved and relevant details have review status.
4. Have a builder subagent plan component construction before production geometry: methods/modifier order, surface continuity, local edge profiles, openings and mating surfaces. Build a proportion study, then inspect a representative difficult component before repeating its method. Independent critics review frozen `.blend` revisions and fresh Blender renders; complex production geometry also receives a dedicated topology pass using actual cage/evaluated-wire and clay diagnostics, repeated on the final revision. Repair and re-review until supported issues are resolved; revisit schematic errors when discovered.
5. Reopen and verify the final saved `.blend`, relevant motion states and requested exports in their target renderer/runtime.

The coordinator assigns complementary critics, maintains coverage and issue/revision records, and controls stage transitions. Schedule additional passes sequentially when agent slots are limited; disclose reduced independence if agents are unavailable. Unknown hidden construction stays explicitly unverified. Simple edits may reuse reviewed material. The [mesh-construction guidance](.agents/skills/reference-3d-modeling/references/mesh-construction.md) explains deliberate edge treatment, modifier/direct-edit choices, real cutouts and connected versus separate surfaces. It does not require every part to use booleans, subdivision, quads or one watertight mesh.

## Tools

- `scripts/build-reference-review.py`: assemble original images and focused crops into a provenance-aware review packet.
- `scripts/build-comparison-review.py`: generate paginated schematic/model-plus-reference overview boards, focused comparisons, and a coverage index for a frozen revision.
- `scripts/compare-model-reference.py`: create uniformly scaled reference/model comparison sheets.
- `scripts/model-comparison.md`: commands, input formats and limitations. Image scripts require Python and Pillow; examples use `uv run --with pillow python`.

Create a project directory with its own original references, manifests, editable schematics, canonical `.blend`, authoring scripts when used, renders and review notes. Export other formats as requested. The manifests in `examples/` demonstrate the formats; replace illustrative paths and crops with real source files and pixel coordinates. Never treat view labels or a generated sheet as proof of coverage.

The SuperRec art skill and its existing assets remain in SuperRec. This harness contains reusable methods, not a copy of its product-specific models or claims.
