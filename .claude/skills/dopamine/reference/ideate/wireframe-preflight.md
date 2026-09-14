# Stage 1 · Wireframe preflight


Use this checklist immediately before creating or materially revising a wireframe. This is an internal design-readiness check, not a technical workflow.

Do not create a manifest, ledger, JSON file, task transcript, or separate user-facing artifact. Do not show the checklist when it passes unless the user asks. If an item fails, explain only the design issue that blocks progress and the smallest next action needed.

**One exception, and it is absolute.** The source-language extraction is not part
of this internal checklist. It is a required section of `WIREFRAME.md`. Confirming
it here does not satisfy it — the written section does. An extraction that exists
only as a passed check has not happened.

## Required checks

Confirm all applicable statements:

- The user, goal, journey moment, product context, constraints, evidence, assumptions, and important unknowns are sufficiently understood for this decision.
- The research decision is explicit: move forward, learn first, or proceed provisionally. Do not wireframe while `learn first` remains unresolved.
- The competitive-research decision is explicit: run it because it can change the solution, or skip it with a clear design reason.
- The solution direction is agreed with the user.
- The user explicitly permitted wireframe creation.
- Agreed requirements, stages, screens, states, branches, overlays, recovery paths, and deferred items are mapped in the solution-coverage matrix.
- Relevant interface principles were checked and any failures were resolved or clearly identified.
- No unresolved issue makes the proposed interaction unsafe, misleading, or structurally unsound.

## Visual-source check

When screenshots, product screens, or flows were supplied, also confirm:

- Every relevant source was opened and visually inspected. Not inferred from a filename, a prompt description, or a previous summary.
- **The `## Source language` section is written into `WIREFRAME.md`**, filled with observations rather than the word "complete".
- It names surface fills (flat or gradient, with both stops), the accent hue and what it signals, container geometry, icon-chip shape and size, whether icon tinting is uniform or per-meaning, imagery type and treatment, density, action placement, and typographic hierarchy.
- At least three markers are recorded that could only have come from these sources.
- Anything deliberately not carried forward is named, with the reason.
- The wireframe translates that language into black, white, and neutral greys.
- The proposal resembles the source product family without claiming pixel-perfect or design-system accuracy.

When no visual source was supplied, use the neutral construction system in `wireframe.md` and do not invent source-specific styling.

## Outcome

- If every applicable check passes, construct the wireframe.
- If a check fails, stop before construction and resolve that specific gap.
- After a material revision, rerun only the checks affected by the change.
