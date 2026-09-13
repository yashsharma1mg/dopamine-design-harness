# Project instructions

## Dopamine 2.0 design harness

This project uses a governed three-stage design workflow powered by the
Dopamine 2.0 design system. The skill lives at `.claude/skills/dopamine/`.

### Stages

1. **Ideate** (`/dopamine ideate`) — Understand → frame → choose a direction →
   interactive wireframe. No Dopamine components, no tokens, no brand colour.
   Outputs: `PRODUCT.md`, `WIREFRAME.md`, `wireframes/<surface>.html`.
2. **Compose** (`/dopamine compose`) — Wireframes → real components.
   Dopamine MCP required (`list_components` must answer). Output: composed
   surface code with tokens resolved and the full accessibility pass clean.
3. **Polish** (`/dopamine polish`) — Propose departures → user approves.
   Output: polished surface with documented exceptions.

### Rules

- Stages are sequential. Do not skip.
- Each stage has an entry gate checked by the skill.
- The Dopamine MCP (`dopamine2-remote`) is used only in Stages 2 and 3.
- Token hierarchy is Base → Semantic → Component. Components never
  reference base tokens directly.
- The documentation site at https://dopamine2-0.dopamine-ds.workers.dev/
  is the canonical reference for tokens, foundations, and component APIs.

### Project files

- `PRODUCT.md` — Durable product context, carried across surfaces. User story,
  design mismatch, evidence labels, product role, chosen direction. Created
  during first ideation, updated on later ones.
- `WIREFRAME.md` — Stage 1 output for one surface: brief, understanding map,
  solution coverage, component candidates, link to the wireframe.
- `wireframes/<surface>.html` — The interactive low-fidelity wireframe.
  Grayscale, 360×800, no components and no tokens.
- `DESIGN_DECISIONS.md` — Stage 3 output (approved departures log).

### Stage 1 phases

Stage 1 is a main path with two branch points, not a single pass.
`reference/ideate.md` routes it:

| Phase | Reference |
| --- | --- |
| 0 · Read the input (board, screenshot, brief, PRD) | `reference/ideate/read-input.md` |
| 1 · Understand and map the context | `reference/ideate/understand.md` |
| **↳ Branch 1 · Do we know enough?** | `reference/ideate/understand.md` |
| — · Research branch (only from **Stop for research first**) | `reference/ideate/research.md` |
| 2 · Read the signals | `reference/ideate/understand.md` |
| 2b · Competitive research (default: skip) | `reference/ideate/competitive-research.md` |
| 3 · Frame the real problem | `reference/ideate/frame.md` |
| 4 · Understand the user situation | `reference/ideate/understand.md` |
| 5 · Explore possible ways to solve it | `reference/ideate/explore.md` |
| **↳ Branch 2 · Do we agree on the direction?** | `reference/ideate/review-direction.md` |
| 6 · Shape the experience | `reference/ideate/comprehend.md` |
| 6b · Stress-test against the principles | `reference/interface-principles.md` |
| 7 · Plan content and hierarchy | `reference/ideate/comprehend.md` + `reference/content-design.md` |
| 8 · Interactive wireframe | `reference/ideate/wireframe.md` → `reference/ideate/wireframe-preflight.md` |

Cross-stage references:

- `reference/effort-and-speed.md` — **always loaded by Stage 1.** The brake on process for its own sake.
- `reference/interface-principles.md` — 6 principles + 5 laws. Compulsory in Stage 1 before the structure is final; also the vocabulary for the Stage 3 polish audit.
- `reference/content-design.md` — interface copy, shared by Stages 1 and 2.

### Rules specific to Stage 1

- **Both branch decisions must be visible in the response.** Never decide either silently.
- **Branch 1 = `Stop for research first` halts the stage.** No user story, framing, direction, brief, or wireframe until the gap closes.
- Competitive research **defaults to skip**. Healthcare, trust, or the existence of competitors is not by itself a reason to run it.
- Approval to build a wireframe confirms the artifact, not the direction.
- Use the exact headings **Answer me few questions** and **Shall I proceed with**.
- The overriding bias, from `interface-principles.md`: **clarity and safety always beat delight.**
