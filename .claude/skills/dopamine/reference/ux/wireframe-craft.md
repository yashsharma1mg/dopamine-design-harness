---
name: wireframe-craft
description: Construction contract for Dopamine 2.0 low-fidelity wireframes. Merge of senior-designer wireframe.md + wireframe-visual-language.md, with Dopamine numbers substituted.
---

# Wireframe Craft

A wireframe communicates how the solution works before UI production. It
commits to content, hierarchy, actions, states, transitions, and surface
choice. It commits to nothing visual.

It stops being a wireframe when it resolves brand styling, Dopamine tokens,
real components, or visual polish. Those are Stage 2 and Stage 3.

## Lock solution coverage first

Before drawing, map the agreed experience:

- entry and parent context;
- agreed stages and outcome categories;
- decisions and information moments;
- alternate and recovery paths;
- explanations, support, and post-completion behaviour;
- assumptions and unresolved branches.

Every agreed item maps to a screen, surface, state, or interaction.
Preserve its intent and terminology. Do not silently add, remove, merge,
rename, or replace agreed parts. Mark any change as a proposal, explain
its effect, and confirm only when it would materially change the agreed
solution.

## Plan each stage

For every screen or surface define: purpose, arrives thinking, primary
understanding, primary information, supporting information, conditional
information, primary action and consequence, secondary actions, what is
deferred, next state.

## Information hierarchy

Order content by the user's decision process: orientation and current
state → primary takeaway → information required for this decision →
reassurance or explanation → primary action → secondary or reference
detail. Deviate when context requires it, and say why.

Use progressive disclosure for detail that is useful but not required.
Never hide consequence, limitation, cost, risk, or loss of control behind
disclosure. On this product that includes price changes, substitution,
prescription requirement, delivery slip, and dosage.

## Surface choice

| Surface | Use when | Avoid when |
| --- | --- | --- |
| Page | Distinct destination, sustained task, deep information space | The action is temporary and depends on parent context |
| Bottom sheet | Bounded contextual task while keeping parent context | Content is deep, high consequence, or needs navigation |
| Inline disclosure | Information or light choice belongs beside its trigger | Expansion makes primary content hard to scan |
| Dialog | Immediate acknowledgement or bounded decision must interrupt | Content needs exploration, comparison, or multiple steps |
| System feedback | Show status or consequence without creating a task | The user must decide or enter substantial information |

Base the choice on context continuity, task depth, decision weight,
information volume, reversibility, interruption, and accessibility.
Do not pick a surface from habit. Carry the rationale into the artifact.

---

## Visual language

### Source priority

1. Dopamine 2.0 surfaces supplied by the user;
2. patterns repeated across those surfaces;
3. platform convention;
4. the default construction system below.

Do not infer a design system from one screen. Do not claim pixel-perfect,
token-level, or component-level accuracy.

### Grayscale translation

| Product treatment | Wireframe treatment |
| --- | --- |
| Coral / brand colour | Black or near-black |
| Secondary brand colour | Mid grey |
| Light brand surface | Light grey |
| Coral primary action | Black fill, white label |
| Selected state | Black fill, white content |
| Unselected state | White fill, grey border |
| Colour-coded status | Label, icon, shape, contrast — never colour alone |
| Decorative illustration | Omit, or neutral placeholder only when structurally necessary |

Palette: canvas `#ffffff`, primary ink `#333333`, borders `#000000` at 1px,
grouped surfaces `#f0f0f0`, placeholder text `#999999`, selected and primary
actions near-black with white content. No brand colour. No tints.

### Construction system

Dopamine numbers govern anything that survives into Stage 2. Wireframe-only
craft rules are marked as such.

| Property | Value | Source |
| --- | --- | --- |
| Viewport | 360 × 800px, fold marked at 640px | Dopamine |
| Spacing rhythm | 4px (0, 2, 4, 8, 10, 12, 16, 20, 24, 28, 32, 36, 40) | Dopamine |
| Screen padding | 16px margin, 8px gutter | Dopamine |
| Container radius | 0, 2, 4, 6, 8, 12, 16 | Dopamine |
| Primary action height | 48px | a11y floor |
| Compact interactive control | ≥40–44px, never below 24×24 | a11y floor |
| Page title | 20–22px semibold | wireframe-only |
| Section heading | 16–18px medium | wireframe-only |
| Body | 14–16px regular | wireframe-only |
| Helper / caption | 12px regular | wireframe-only |
| Annotation labels | monospace 11–12px | wireframe-only |
| Icons | Hugeicons Stroke Rounded, 20–24px, consistent stroke | wireframe-only |

Stage 2 replaces the wireframe type scale with Dopamine roles (Cabinet
Grotesk ≥24pt display, Figtree elsewhere) and replaces Hugeicons with the
Dopamine icon set. Do not treat wireframe type sizes or Hugeicons as a
handoff commitment.

Precise spacing and alignment are required. Pixel reproduction of a
supplied screen is not.

### Zone annotation

Every zone carries: content type, priority rank from the brief (P1/P2/P3/
secondary), interaction behaviour (tappable, scrollable, expandable,
static). Use real content — "Amoxicillin 500mg Capsule", not "Product Name".
Mark the fold. P1 sits above it.

---

## Artifact

Produce two things.

**1. Interactive HTML wireframe** — the review surface. Clickable states,
overlays, branches, back behaviour, recovery, and explanatory motion only
where it clarifies a state change. Presentation rules:

- state switcher outside the device frame;
- one active phone screen at a time, centred, fully visible;
- clear selected/unselected switcher states;
- preserve the parent or entry context, not isolated screens;
- design reasoning in a separate notes tab or collapsible panel — it must
  not compete with the screen.

Describe it as an interactive low-fidelity wireframe. Never as a prototype
or production-ready interface.

**2. `WIREFRAME.md`** — the Stage 2 contract. Static SVGs, coverage map,
stage specs, component candidates table. This is the greppable artifact
`compose` gates on. The HTML is for humans; the markdown is for the pipeline.

### `WIREFRAME.md` structure

```markdown
# [Surface Name]

## Brief
[approved brief, evidence-tagged]

## Direction
[chosen direction + why it won over the alternatives]

## Journey context

## Solution coverage
| Agreed item | Screen / surface / state / interaction |

## Screen and surface map

## Stage specifications
### [Stage]
- Purpose / Arrives thinking / Primary understanding / Primary information
- Supporting / Conditional / Deferred
- Primary action and consequence / Secondary actions
- Surface and rationale / Next state

## Wireframes
[SVG per meaningful state — loaded, empty, error, and any branch]

## States and recovery

## Interaction and motion notes

## Assumptions and open decisions
[carry the Assumed and Unknown tags forward]

## Component candidates
| Wireframe zone | Likely component(s) | Notes |

## Handoff boundary
- Decisions intentionally left to Stage 2:
- Decisions intentionally left to Stage 3:
```

## Craft check

Inspect the rendered artifact before delivery.

- Every screen has one clear purpose.
- Strongest focus matches the user's immediate need.
- Required information appears before the relevant decision.
- Primary and secondary actions are distinguishable without colour.
- Spacing, alignment, grouping, proportions are consistent and on the 4px rhythm.
- Icons consistent in family, size, stroke.
- Selected and unselected states are immediately readable.
- Progressive disclosure hides no material consequence.
- Surface choices preserve context and match decision weight.
- Back, change, cancel, exit, and recovery work where needed.
- Motion clarifies behaviour only.
- The phone is the visual focus; notes are secondary.
- The device is fully visible, uncropped, at review size.
- Every agreed solution element is represented, or its change was confirmed.
- Structural accessibility constraints pass — see `reference/accessibility-structural.md`.
- The artifact is visibly low fidelity and claims no design-system accuracy.
