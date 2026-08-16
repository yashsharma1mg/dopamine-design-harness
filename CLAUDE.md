# Project instructions

## Dopamine 2.0 design harness

This project uses a governed three-stage design workflow powered by the
Dopamine 2.0 design system. The skill lives at `.claude/skills/dopamine/`.

### Stages

1. **Ideate** (`/dopamine ideate`) — Interrogation → wireframes.
   No visual decisions. Output: `WIREFRAME.md`.
2. **Compose** (`/dopamine compose`) — Wireframes → real components.
   Storybook MCP required. Output: composed surface code.
3. **Polish** (`/dopamine polish`) — Propose departures → user approves.
   Output: polished surface with documented exceptions.

### Rules

- Stages are sequential. Do not skip.
- Each stage has an entry gate checked by the skill.
- The Storybook MCP connection is used only in Stages 2 and 3.
- Token hierarchy is Base → Semantic → Component. Components never
  reference base tokens directly.
- The documentation site at https://dopamine2-0.dopamine-ds.workers.dev/
  is the canonical reference for tokens, foundations, and component APIs.

### Project files

- `PRODUCT.md` — Product context (created during first ideation).
- `WIREFRAME.md` — Stage 1 output (brief + wireframes + component candidates).
- `DESIGN_DECISIONS.md` — Stage 3 output (approved departures log).
