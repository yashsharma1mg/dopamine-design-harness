# Dopamine Design Harness

A Claude skill for turning vague mobile product intent into a governed design handoff: an approved brief, a structural wireframe, a token-backed composition, and explicitly approved visual departures.

This repository is the workflow layer in a three-part design-to-interface pipeline:

- [Dopamine 2.0](https://github.com/yashsharma1mg/dopamine-2.0) provides the canonical tokens, components, Storybook, and MCP server.
- This harness governs how a Claude agent reasons about and moves through a design task.
- [DesMania](https://github.com/yashsharma1mg/DesMania) demonstrates the process in a concrete diagnostics checkout prototype.

The harness contains instructions and reference material for Claude. It is not a renderer, a design editor, or an automated end-to-end validator.

## What It Does

The workflow has three sequential stages:

```text
ideate  --->  compose  --->  polish
   |             |             |
   v             v             v
PRODUCT.md   surface code   DESIGN_DECISIONS.md
WIREFRAME.md compliance     approved departures
```

### Stage 1: Ideate

The agent resolves the surface identity, user context, goal, content, entry and exit flow, priority hierarchy, states, edge cases, and existing patterns. It then produces an approved brief and annotated grayscale wireframes at 360px.

Output: `PRODUCT.md` and `WIREFRAME.md`.

### Stage 2: Compose

The agent maps wireframe zones to real Dopamine 2.0 components, verifies props and variants through Storybook MCP, resolves values through the token hierarchy, and checks the interface principles and accessibility floor.

Output: composed surface code, a zone-to-component map, a compliance record, and any composition gaps.

### Stage 3: Polish

The agent audits the composed surface and proposes 3-7 specific departures grouped by risk. Each departure requires user approval. Accessibility remains a hard floor and cannot be traded away for visual distinction.

Output: `DESIGN_DECISIONS.md`.

Stages are sequential. The skill describes entry gates and handoffs, but those gates are protocol-level Claude instructions rather than a separate executable enforcement system.

## How To Use

Open this repository in Claude Code or another Claude surface that can load project instructions. The root `CLAUDE.md` and `.claude/skills/dopamine/SKILL.md` provide the entry point.

Use these commands in a target product repository:

```text
/dopamine ideate [surface]
/dopamine compose [surface]
/dopamine polish [surface]
```

Prerequisites:

1. Start with `ideate`. It is the only stage that does not require an existing handoff artifact.
2. Keep `PRODUCT.md` and `WIREFRAME.md` at the target project root before composing.
3. Configure the [Dopamine 2.0 Storybook MCP server](https://github.com/yashsharma1mg/dopamine-2.0/tree/main/packages/mcp) before using `compose` or `polish`.
4. Use an existing codebase when composing so component, token, and accessibility decisions can be checked against real implementation context.

## Artifact Contract

| Artifact | Created by | Purpose |
| --- | --- | --- |
| `PRODUCT.md` | Ideate setup | Product and surface context carried across stages. |
| `WIREFRAME.md` | Ideate | Approved brief, structural wireframes, states, and component candidates. |
| `DESIGN_DECISIONS.md` | Polish | Approved and rejected departures plus hard-floor confirmation. |

The repository currently contains the protocols, not a checked-in sample run of these artifacts. The most useful verification is to run the skill against a real surface and inspect the resulting handoffs.

## Stage Gates And Outputs

### Ideate

- Entry: always open for a new surface.
- Gate: the brief must resolve all eight interrogation dimensions and receive user approval.
- Output: grayscale, annotated wireframes for meaningful states and a component-candidate table.

### Compose

- Entry: an approved `WIREFRAME.md` exists and Storybook MCP is available.
- Gate: every zone maps to a real component, every value resolves through canonical tokens, and accessibility gaps are either fixed or explicitly surfaced.
- Output: composed code, compliance record, and composition-gap list.

### Polish

- Entry: the composed surface passes its foundation checks.
- Gate: every departure is independently approved and the final accessibility sweep passes.
- Output: `DESIGN_DECISIONS.md` documenting approved and rejected proposals.

## Design-System And Accessibility Principles

The harness is designed around Dopamine 2.0's three-layer token hierarchy:

```text
base  ->  semantic  ->  component
```

It also carries the system's intent layer: trust through explainability, calm over alarm, context awareness, answer first, progressive disclosure, and participation that creates ownership. The overriding bias is that clarity and safety beat delight.

Healthcare surfaces must preserve critical content, readable contrast, persistent form labels, meaningful screen-reader names, adequate touch targets, reduced-motion alternatives, and non-truncated drug names, dosages, allergens, and frequencies. The full constraints live in [`reference/accessibility.md`](.claude/skills/dopamine/reference/accessibility.md).

## Current Status

| Area | Status | Notes |
| --- | --- | --- |
| Ideate protocol | Complete | Interrogation, brief, wireframe, and handoff rules are documented. |
| Compose protocol | Complete | Four-phase map, resolve, check, and gate protocol is documented. |
| Polish protocol | Complete | Audit, proposal, approval, application, and final sweep are documented. |
| Accessibility reference | Complete | WCAG, clinical, form, motion, and content constraints are documented. |
| Interface principles | Complete | Intent and design-conviction layer is documented. |
| Real-surface end-to-end validation | Pending | No sample run or automated workflow validator is committed here. |

## Limitations And Non-Goals

- This repository does not render UI or provide a visual canvas.
- The stage gates are instructions for Claude, not a compiler or CI policy engine.
- Compose and polish depend on an external Storybook MCP connection.
- The harness targets Dopamine 2.0's 360px mobile contract; it does not define a desktop system.
- Accessibility references guide design decisions but do not replace product-specific testing with assistive technology.

## Repository Structure

```text
.
├── README.md
├── CLAUDE.md
└── .claude/
    └── skills/
        └── dopamine/
            ├── SKILL.md
            └── reference/
                ├── ideate.md
                ├── compose.md
                ├── interface-principles.md
                ├── accessibility.md
                └── polish.md
```

`SKILL.md` is the router and compressed system reference. The reference files contain the detailed stage protocols and the two constraint layers loaded during composition.

## Verification

Verification for this repository is documentation-level:

- All three stage reference files are present and describe their entry gates and outputs.
- The compose protocol is no longer a placeholder; it documents Storybook discovery, API validation, token resolution, accessibility checks, and the exit gate.
- The repository contains no automated test suite or renderer.
- End-to-end confidence requires running the skill against a real target project with Dopamine MCP connected.

## License And Asset Restrictions

Original source and generic workflow material are licensed under the [Apache License 2.0](LICENSE). Dopamine-specific internal reference material, brand content, Figma-derived material, and third-party content are excluded from that license as described in [`LICENSE-ASSETS.md`](LICENSE-ASSETS.md).
