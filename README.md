# Dopamine 2.0 — AI Design Harness

An agent harness for designing mobile interfaces through the [Dopamine 2.0](https://dopamine2-0.dopamine-ds.workers.dev/) design system. Built for Claude, structured on the [Impeccable](https://github.com/pbakaus/impeccable) open-source agent harness pattern.

Dopamine 2.0 is the internal design system for [1mg](https://www.1mg.com), a health and pharmacy product. The harness enforces a governed three-stage design workflow where each stage has an entry gate, a defined protocol, and a handoff artifact.

## The three stages

```
ideate ──→ compose ──→ polish
  │            │           │
  ▼            ▼           ▼
WIREFRAME.md   Surface    DESIGN_DECISIONS.md
(brief +       (real       (approved departures
 wireframes +   components   + hard floor
 candidates)    + tokens)    confirmation)
```

**Stage 1 — Ideate.** The agent interrogates the user across eight dimensions (surface identity, user context, goals, content inventory, entry/exit flow, priority hierarchy, states/edges, existing patterns) until a complete brief can be written. The user approves the brief, then the agent produces annotated structural wireframes at 360px. No visual decisions — no colour, no type treatment, no components. Output: `WIREFRAME.md`.

**Stage 2 — Compose.** The wireframe zones get translated into real Dopamine 2.0 components using the Storybook MCP connection. Every decision resolves through the three-layer token hierarchy (base → semantic → component). The accessibility guidelines are loaded as a mandatory constraint layer — every composed surface must pass before advancing. Output: a rendered surface with correct token resolution.

**Stage 3 — Polish.** The agent audits the composed surface for visual hierarchy, rhythm, brand presence, and signature opportunities, then proposes 3–7 specific departures from the design system grouped by risk level. The user approves each departure individually before it is applied. Accessibility constraints are a hard floor — never candidates for departure. Output: `DESIGN_DECISIONS.md`.

Stages are sequential. Each has an entry gate checked by the skill. You cannot skip to polish without a composed surface, and you cannot compose without an approved wireframe.

## Repository structure

```
.
├── README.md                                          ← you are here
├── CLAUDE.md                                          ← project-level instructions (auto-read by Claude)
└── .claude/
    └── skills/
        └── dopamine/
            ├── SKILL.md                               ← entry point, router, system knowledge
            └── reference/
                ├── ideate.md                          ← Stage 1 protocol (complete)
                ├── compose.md                         ← Stage 2 protocol (placeholder)
                ├── accessibility.md                   ← WCAG/IS 17802/RPwD constraints (complete)
                └── polish.md                          ← Stage 3 protocol (complete)
```

## File reference

### `CLAUDE.md`
Project-level instructions that Claude reads automatically at the start of every session. Points to the skill, summarises the three stages, and lists the project files the workflow produces (`PRODUCT.md`, `WIREFRAME.md`, `DESIGN_DECISIONS.md`).

### `SKILL.md`
The skill entry point. Contains:
- **Frontmatter** — name, keyword-rich description for auto-triggering, argument hints, allowed tools.
- **Setup protocol** — mandatory steps that run before any stage: read project context, load the stage reference file, familiarise with the codebase, check entry gates.
- **System knowledge** — compressed Dopamine 2.0 reference: three-layer token architecture, key constraints (360px viewport, 4px spacing rhythm, typography roles, radii, brand colour), the full 35-component library, and critical accessibility constraints.
- **Command router** — maps `ideate`, `compose`, and `polish` to their reference files with routing rules for exact match, fuzzy intent, and no-argument recommendations.

### `reference/ideate.md`
**Status: Complete**

Stage 1 protocol in two gated phases:

*Phase 1 — Interrogation.* Eight dimensions the agent must resolve through conversation: surface identity, user and context, goal and success, content inventory, entry and exit, priority hierarchy, states and edges, existing patterns. Includes interrogation rules (batch 2–3 questions, propose don't just ask, name the gaps, resolve conflicts, know when to stop). Outputs a structured brief in a fixed format that the user must approve before proceeding.

*Phase 2 — Wireframe.* Produces annotated structural SVGs at 360px. Rules enforce grayscale only, real content not lorem ipsum, priority-ranked zones, a visible fold line, and one wireframe per state. Also outputs a component candidates table mapping wireframe zones to likely Dopamine 2.0 components. The user approves before the wireframe is saved as `WIREFRAME.md`.

### `reference/accessibility.md`
**Status: Complete**

Extracted from the Dopamine 2.0 accessibility guidelines (WCAG 2.2 AA, IS 17802, RPwD Act 2016, GIGW 3.0). Loaded as a mandatory constraint layer by Stage 2. Covers:

- **Colour and contrast** — the four ratios (4.5:1, 3:1, 3:1, exempt) and the three tokens that fail WCAG today (Content/Tertiary, States/Warning, Branding/Coral) with specific restricted-use rules and fixes.
- **Typography** — minimum size floors from 11pt bold (tags only) to 16pt bold (iOS inputs), Cabinet Grotesk ≥24pt threshold, text scaling requirements at 130% and 200%, and the four truncation failure modes.
- **Touch targets** — 24×24 floor, 48×48 default, ≥48+12dp for high-stakes actions, plus the spacing exception rule.
- **Interactive states** — all seven states required for every interactive element (default, hover, focus, pressed, loading, disabled, selected).
- **Screen reader** — component specs must include audio spec alongside visual spec, alt text rules for five image types.
- **Forms** — three rules: persistent labels, explain what's wrong, suggest the fix.
- **Motion and time** — 300ms ceiling, no flashes ≥3/sec, prefers-reduced-motion mandatory.
- **Language** — Grade 7–8 reading level with clinical-to-plain examples.

### `reference/compose.md`
**Status: Placeholder — pending MCP integration**

Will contain the Stage 2 protocol for translating wireframe zones into real Dopamine 2.0 components via the Storybook MCP connection. Currently documents the entry gate, the mandatory accessibility reference load, and a preview of key constraints.

### `reference/polish.md`
**Status: Complete**

Stage 3 protocol in three gated phases:

*Phase 1 — Audit.* The agent reads the composed surface before proposing anything, evaluating visual hierarchy against the wireframe's priority stack, rhythm and pacing, brand presence, signature opportunity, micro-interaction gaps, and copy voice. Outputs a structured assessment shared with the user.

*Phase 2 — Propose.* The agent presents 3–7 departure proposals grouped by risk level (safe, moderate, aggressive). Seven departure categories defined: spacing, typography, colour, elevation/depth, motion, layout, component, and copy — each with concrete examples and constraints noting which accessibility rules remain non-negotiable within that category. Each proposal uses a fixed format: element, system rule bent, current state, proposed state, rationale, risk, accessibility impact. Proposals must stand alone (user can approve any combination).

*Phase 3 — Apply.* Handles four response types (approved, rejected, modified, "tell me more"). Departures applied one at a time with verification. Final accessibility sweep against the full hard floor checklist. Outputs `DESIGN_DECISIONS.md` documenting every approved departure and rejected proposal.

The hard floor — accessibility constraints that are never candidates for departure — is listed at the top of the file and referenced throughout.

## Design system reference

- **Documentation:** https://dopamine2-0.dopamine-ds.workers.dev/
- **Viewport:** 360px mobile only, no desktop
- **Token architecture:** base → semantic → component (255 tokens across 7 foundation groups)
- **Components:** 35 ready (actions, navigation, forms, selection, display, feedback, cart)
- **Typography:** Cabinet Grotesk (display, ≥24pt), Figtree (all other roles)
- **Spacing:** 4px rhythm (0, 2, 4, 8, 10, 12, 16, 20, 24, 28, 32, 36, 40)
- **Brand:** coral #ff5443

## Current status

| File | Status | Notes |
| --- | --- | --- |
| `SKILL.md` | ✅ Complete | Entry point and router |
| `reference/ideate.md` | ✅ Complete | Stage 1 — interrogation + wireframes |
| `reference/accessibility.md` | ✅ Complete | WCAG 2.2 AA constraint layer |
| `reference/compose.md` | 🔲 Placeholder | Blocked on Storybook MCP wire-up |
| `reference/polish.md` | ✅ Complete | Stage 3 — audit, propose, apply |
| `CLAUDE.md` | ✅ Complete | Project-level instructions |

## What's next

1. Complete the MCP connection to the Dopamine 2.0 Storybook instance
2. Build out `reference/compose.md` with the full Stage 2 protocol (wireframe-to-component translation using live design system data)
3. End-to-end test across all three stages against a real surface

## Structural model

This harness follows the [Impeccable](https://github.com/pbakaus/impeccable) pattern: one skill entry point with a lean router, stage-specific knowledge loaded lazily via reference files, and project state tracked through handoff artifacts (`WIREFRAME.md`, `DESIGN_DECISIONS.md`). The base skill stays small and keyword-rich for auto-triggering; heavy instructions only load on demand.
