# Stage 1 — Ideate

Understand the problem, choose a direction, structure the experience,
then produce the wireframe. This stage commits to *what* gets built and
*why*, and to the reasoning that survives review.

No visual decisions. No colour, no type treatment, no component selection,
no tokens. Those are Stage 2.

## Entry gate

Always open. This is where every surface starts.

## Reference load order

| Step | Load | When |
| --- | --- | --- |
| 0 | `ux/modes.md` | Always, first |
| 0 | `ux/read-board.md` | Figma / FigJam / multi-frame input |
| 0 | `ux/read-prd.md` | PRD or product brief supplied |
| 1 | `ux/user-story.md` | Move forward / Move carefully, unless story already agreed |
| 1 | `ux/articulate-problem.md` | Problem is new, broad, symptom-led, or ambiguous |
| 2 | `ux/solution.md` | New solution or meaningful redesign |
| 3 | `ux/user-understanding.md` | Multiple stages, consequential decisions, or new concepts |
| 3 | `ux/user-flow.md` | Flow, journey, sitemap, or state model needed |
| 3 | `ux/content-design.md` | Interface copy is part of the solution (it usually is) |
| 4 | `ux/wireframe-craft.md` | Always, before constructing the artifact |
| 4 | `accessibility-structural.md` | Always, before constructing the artifact |
| — | `ux/research-plan.md`, `ux/research-script.md` | Only if the user asks for a research guide |
| — | `ux/sticky-notes.md` | Board synthesis |

Load only what the current step needs. Do not reload what is in context.

Use the smallest version of this stage that produces a sound answer. A
one-screen modification does not need solution exploration. A new checkout
flow does.

---

## Phase 0 — Read and position

Inspect everything supplied before interpreting it. Build the context map
from `ux/modes.md`, tag every material statement, select a mode.

Say the read back briefly — user situation, difficulty, intended outcome,
only to the extent supported. This is a comprehension check, not a pitch.
Name assumptions next to the interpretations that depend on them.

**Learn first stops here.** Return what is known, what is missing, why it
matters, and 2–4 focused questions. Produce no story, no framing, no
direction, no flow, no wireframe.

## Phase 1 — Understand

Build the editable user story: the context they arrive from, what they are
trying to achieve, how they handle it today, where they get stuck, what
they think and feel, what progress would mean.

Present it as a draft with assumptions visible. When the user corrects it,
update the story, identify which design decisions change, preserve the ones
that remain valid, and continue from the revised story — do not restart.

Frame the design problem: separate the visible symptom from the underlying
user difficulty. Define user, desired progress, current breakdown, product
opportunity, success condition, and the assumptions that could change the
framing.

## Phase 2 — Direction

Explore meaningfully different approaches before committing. For each,
decide whether the product should explain, guide, recommend, act, or
combine those roles; how much control the user keeps and where consent,
review, change, or recovery is needed; whether this is a one-time task or
an ongoing relationship; how it behaves before, during, after, and over
time; which existing capabilities and data it relies on; what complexity,
risk, or behaviour change it introduces.

Compare against user fit, problem fit, product fit, safety, effort,
clarity, durability. Recommend one and say why it leads.

### GATE 1 — Direction sign-off

Present the brief and the recommended direction together in this format:

```markdown
# Brief: [Surface Name]

## Surface
[what it is, where it lives in the IA]

## User story
[the narrative, assumptions marked]

## Problem
[symptom → underlying difficulty → success condition]

## Goal
- User goal:
- Business goal:
- Success signal:

## Directions considered
| Direction | Product role | User control | Trade-off |
[2–3 meaningfully different options]

## Recommended direction
[which, and why it leads]

## Content inventory
[ordered, marked required/optional, dynamic/static]

## Flow
- Entry / Exit / Flow position

## Priority stack
1. / 2. / 3. — everything else is secondary

## States
- Empty / Error / Loading / Edge cases

## Constraints
[technical, regulatory, consistency]

## Evidence ledger
| Statement | Tag | What changes if wrong |
[every Assumed and Unknown from Phase 0]

## Deferred
[explicitly pushed to Stage 2 or Stage 3]
```

Read it back, ask whether it captures what is being built, and wait.
If they change anything, update and re-confirm. Do not enter Phase 3
without sign-off.

## Phase 3 — Structure

Map user understanding per stage: what they arrive thinking, what
information appears, what they must understand before moving on, what they
decide or do, what supports that decision, what may still worry them, what
they expect next.

Use the map to find decisions requested too early, explanations delivered
too late, unnecessary information, unresolved concerns, and transitions
that break the mental model.

Then plan content and hierarchy per stage: single purpose, primary
information and why it deserves focus, supporting information, what is
progressively disclosed, primary and secondary actions with consequences,
what should not be shown yet, and the surface — page, bottom sheet, inline
disclosure, dialog, or system feedback.

Treat copy as part of this, not as filler added later. Decide what meaning
must lead, what can be deferred, where the product must state a consequence
or limitation, and what the action label must promise.

## Phase 4 — Wireframe

Load `ux/wireframe-craft.md` and `accessibility-structural.md`. Lock
solution coverage, then construct.

Deliver:

1. **Interactive HTML wireframe** — the review artifact. States, branches,
   overlays, recovery, back behaviour. Notes in a secondary panel.
2. **`WIREFRAME.md`** — the Stage 2 contract. Brief, direction, coverage
   map, stage specs, static SVGs per state, evidence ledger, component
   candidates table, handoff boundary.

Run the craft check in `ux/wireframe-craft.md` against the rendered
artifact before presenting.

### GATE 2 — Wireframe sign-off

Present the interactive wireframe, walk the zones and their priorities,
surface the open decisions and the evidence ledger. Do not write
`WIREFRAME.md` until the user confirms. That file is the entry gate for
`compose`.

---

## What this stage does not do

Colour, type treatment, tokens, component variants or props, production
code, Storybook MCP, intentional departures. All downstream.

The wireframe is a structural contract. Everything visual is Stage 2.
