# Stage 1 · Phase 5 — Interactive low-fidelity wireframe

A wireframe communicates how the UX solution works before any Dopamine
component is chosen. It makes content, hierarchy, actions, states, transitions,
and surface choices reviewable while remaining visibly low fidelity.

The fidelity boundary is not static versus interactive. A wireframe may be
precise and clickable. It crosses the line when it starts resolving Dopamine
components, semantic tokens, brand colour, or final type treatment — that is
Stage 2's job, and Stage 3 owns deliberate departures from it.

## Entry permission

Create a wireframe only when the user explicitly asks for one, or explicitly
accepts it after it is offered. An agreed solution direction, a completed brief,
or simply having enough context does **not** grant permission.

Check this before writing any HTML or calling any visualization tool. If
permission is missing, offer the interactive low-fidelity wireframe, ask whether
the user wants it, and stop.

## Preflight

Before constructing or materially revising the wireframe, load and pass
`wireframe-preflight.md`.

Two different things happen here, and they have opposite visibility rules:

- **The readiness checklist stays internal.** Show it only if it fails or the
  user asks. On failure, explain the design issue that blocks progress and the
  smallest next action — not the checklist.
- **The source-language extraction is an artifact.** It is written into
  `WIREFRAME.md` as a required section, every time a visual source was supplied.
  It is never internal, never summarised as "done", and never reduced to a
  pass/fail line.

That second rule exists because an invisible check is indistinguishable from a
check that never ran. If the extraction is not in the file, treat it as not
having happened.

After a material revision, rerun only the checks the change affected.

## Before drawing

Confirm:

- the user story and entry context;
- the purpose and completion condition of the flow;
- the product role and degree of user control;
- the main path, important branches, and recovery paths;
- what the user should understand at each stage (from `comprehend.md`);
- the product information, capabilities, and constraints that affect the experience.

If any of these are still assumptions, keep them visible in the wireframe notes.

If the wireframe depends on provisional assumptions, separate:

- what is stable enough to show as the working direction;
- what is assumption-led;
- what must be revisited when more is learned.

## Lock solution coverage

Before translating the solution into screens, create a coverage map:

- entry and parent context;
- agreed stages and outcome categories;
- decisions and information moments;
- alternate and recovery paths;
- explanations, support, and post-completion behavior;
- assumptions and unresolved branches.

Map every agreed item to a screen, surface, state, or interaction, marking each
**mapped**, **deferred with reason**, or **unresolved**. Preserve its intent and
terminology.

Do not silently add, remove, merge, rename, or replace agreed parts of the
solution. Mark a change as a proposal and explain its effect. Ask for
confirmation only when the wireframe would materially change the agreed
solution; otherwise continue without adding another approval step.

## Plan each stage

For every screen or surface, define:

1. **Purpose:** the single job of the stage.
2. **Arrives thinking:** the expectation or concern carried into it.
3. **Primary understanding:** what must become clear before the user continues.
4. **Primary information:** what deserves the strongest focus.
5. **Supporting information:** what helps the current decision without competing with it.
6. **Conditional information:** what appears only when relevant.
7. **Primary action:** the main action and its consequence.
8. **Secondary actions:** alternate, defer, back, change, cancel, or recovery actions.
9. **What is deferred:** information or choices intentionally moved elsewhere.
10. **Next state:** what the user and system expect after the action.

## Build the information hierarchy

Order content according to the user's decision process:

- orientation and current state;
- the primary takeaway;
- information required for the current decision;
- reassurance or explanation;
- primary action;
- secondary or reference details.

Change this order when the user context requires it, and explain why. Do not
give prominence to information only because it matters internally to the
product.

Use progressive disclosure when details are useful but not required for the
current decision. **Never** hide consequences, limitations, cost, risk, loss of
control, dosage, drug identity, or allergen information behind disclosure.

## Choose the surface

| Surface | Use when | Avoid when |
| --- | --- | --- |
| Page | The user enters a distinct destination, sustained task, or deep information space | The action is temporary and depends on the parent context |
| Bottom sheet | The user completes a bounded contextual task while retaining the parent context | The content is deep, high consequence, or needs substantial navigation |
| Inline disclosure | The information or lightweight choice belongs directly beside its trigger | Expansion would make the primary content difficult to scan |
| Dialog | An immediate acknowledgement or bounded decision must interrupt the current action | The content requires exploration, comparison, or multiple steps |
| System feedback | The product needs to show status or consequence without creating a new task | The user must make a considered decision or enter substantial information |

Base the choice on context continuity, task depth, decision weight, information
volume, reversibility, interruption, navigation expectation, and accessibility.
Do not default to a bottom sheet for every secondary action. Do not create a new
page merely because a state needs to be shown.

These map onto Dopamine's Bottomsheet, Dialog, Snackbar, and Sticky in Stage 2 —
but name the *surface*, not the component. Component selection is Stage 2's.

---

## Construction contract

### Viewport

`360 × 800px`. Mobile only, single viewport, no desktop variant and no other
device. The fold is the bottom of the frame — content above it must contain the
P1 element, and enough below-fold content must be visible to signal there is
more.

### Grayscale palette

Only these values. No brand colour, no tints, no accent. The absence of colour
is the point — it forces hierarchy through structure alone.

| Role | Value |
| --- | --- |
| Canvas | `#ffffff` |
| Content zones / grouped surfaces | `#f0f0f0` |
| Placeholder and secondary text | `#999999` |
| Primary text and primary ink | `#333333` |
| Zone borders, selected controls, primary action fill | `#000000` |

### Translating the product into black and white

**Source inspection is a mandatory gate.** Whenever screenshots, product
screens, a flow, or Storybook references are supplied: open and visually inspect
every relevant frame with the available image or board viewing tool. Do not
infer style from filenames or prompt descriptions.

Before constructing anything, show a **source-language extraction** in the
response covering the sources inspected, layout rhythm, density, navigation,
component proportions and shapes, grouping, hierarchy, action placement, icon
treatment, interaction patterns, the grayscale translation, and **at least three
markers that could only have come from those sources**. Generic statements like
"preserve the product style" do not satisfy this gate. `wireframe-preflight.md`
confirms the same evidence.

Do not construct or deliver the wireframe when supplied references were ignored,
described generically, or reduced to pass/fail booleans. If a reference is
unreadable or insufficient, say so and ask for a usable source rather than
silently falling back to the neutral system.

Carry forward the repeated visual language — information density, layout rhythm
and padding, navigation placement, component proportions, container shapes,
corner-radius character, content grouping, typographic hierarchy, placement of
primary and secondary actions, icon treatment, and disclosure behavior. Treat a
flow as evidence of both visual language and cross-screen continuity; do not
copy its board layout as interface structure.

| Product treatment | Wireframe treatment |
| --- | --- |
| Brand coral `#ff5443` | `#000000` |
| Secondary brand colour | `#999999` |
| Light brand surface | `#f0f0f0` |
| Brand-coloured primary action | `#000000` fill, white label |
| Selected state | `#000000` fill, white content |
| Unselected state | White fill, `#999999` border |
| Coloured status | Carried by label, icon, shape, and contrast — never colour alone |
| Decorative illustration | Omit, or a plain neutral placeholder only when structurally necessary |

Do not copy brand colours or gradients, final fonts or type tokens, decorative
illustration or photography, shadows or ornamental effects, exact component
tokens, or production styling.

If a supplied pattern would reduce clarity, accessibility, or comprehension,
preserve the familiar behavior where possible and note the structural deviation.
Do not silently reproduce a weak pattern.

### Construction system

Aligned to Dopamine 2.0. Where the system specifies a value, the system wins.

- **Spacing:** the Dopamine 4px rhythm — 0, 2, 4, 8, 10, 12, 16, 20, 24, 28, 32, 36, 40.
- **Screen padding:** `16px` (the Dopamine page margin). Gutter `8px`.
- **Radii:** the Dopamine set — 0, 2, 4, 6, 8, 12, 16. Use 12 or 16 for cards and containers; adjust only to reflect the referenced product's character.
- **Primary action height:** `48px` — the Dopamine 48dp default touch target.
- **Every interactive element:** `48dp` minimum. `24 × 24` is the absolute floor and applies only where the spacing exception permits it. High-stakes actions — OTP, payment, dosage — need `≥48 + 12dp`.
- **Type:** use Dopamine's type *roles*, not raw pixel sizes — Page title → Heading → Title → Body → Sub text. Show the role in the annotation (`[Body]`, `[Page title]`) and let relative weight and size carry the hierarchy. Do not specify a type scale here; Stage 2 resolves it from the real tokens. Cabinet Grotesk is display-only at `≥24pt`; everything else is Figtree.
- **Icons:** [Hugeicons Stroke Rounded](https://hugeicons.com/icons/stroke-rounded) at `20–24px` with consistent stroke weight. Dopamine's iconography derives from Hugeicons, so these carry through to Stage 2 cleanly.
- **Primary action:** black fill, white label. **Secondary action:** white fill, grey border, near-black label.

Precise spacing and alignment are required. Pixel-perfect reproduction of a
supplied screen is not, and this artifact never claims token-level or
component-level accuracy — it has no tokens and no components yet.

### Annotations

Every zone carries:

- **What it contains** — content type, and the Dopamine type role where text is involved.
- **Priority rank** from the brief — `P1`, `P2`, `P3`, or `secondary`, as a small dark badge in the zone corner.
- **Interaction behaviour** — tappable, scrollable, expandable, static.

Use real content, not lorem ipsum. "Amoxicillin 500mg Capsule", not "Product
Name Here". Where the real content isn't available, match the expected length
and type. Drug names, dosages, and allergens must appear at realistic full
length so truncation risk is visible at this stage rather than discovered in
Stage 2.

## Interaction and states

Build the minimum critical path first. **Default to one primary screen and no
more than four essential alternate, error, or recovery states.** Do not model
every business-rule variation, and do not build a large custom application when
a smaller wireframe communicates the decision. Add further states only when
comprehension genuinely requires it or the user asks.

An interactive HTML wireframe is the deliverable whenever interaction is needed
to understand the solution; prefer a smaller wireframe when it communicates the
decision on its own. Wire only the interactions that help a reviewer understand
the solution:

- primary and secondary actions;
- forward and back navigation;
- meaningful decisions and branches;
- bottom sheets, dialogs, and inline disclosures;
- change, cancel, retry, undo, and recovery;
- loading, processing, empty, unavailable, validation, error, success, and return states where they affect understanding;
- important entry and completion transitions.

Clickable behavior demonstrates the UX logic; it does not imitate a finished
product. Always describe the artifact as an **interactive low-fidelity
wireframe**, never as a prototype or a production interface.

Every state named in the coverage map is either built or marked **deferred with
reason** — never silently dropped. The four-state default is the budget for what
gets built; the coverage map is the record of what was left out and why.

## Motion

Use motion only where it explains behavior that would otherwise be unclear — how
a contextual surface enters or exits, how the user moves between important
states, how progress changes, how the system acknowledges an action, how a
reversible action is restored.

Keep it simple, functional, and secondary to comprehension. No decorative
animation, no brand expression, no cinematic transitions. Deliberate,
expressive motion is a Stage 3 departure and requires user approval there.

Respect `prefers-reduced-motion: reduce` even in the wireframe — it is on the
accessibility hard floor at every stage.

## Artifact presentation

- Place the screen-state switcher **outside** the device frame.
- Show one active screen at a time unless side-by-side comparison is the explicit purpose.
- Centre the device frame and keep it fully visible at review size.
- Use clear selected and unselected switcher states.
- Preserve the relevant entry or parent context instead of presenting isolated screens.
- Do **not** build a separate notes view, design-notes board, or explanation panel unless the user asks for one. The wireframe is the artifact; the reasoning goes in the delivery response.

## Delivery

Save the artifact as `wireframes/<surface>.html` at the project root and
reference it from `WIREFRAME.md`.

Attempt rendered visual verification **once**. If the renderer or browser is
unavailable, run the remaining checks, state the limitation briefly, and stop —
do not chain fallback environments.

Do not deliver screens alone. Include concise design notes explaining:

- why the main states exist;
- what the user should understand in each important state;
- why the hierarchy is arranged this way;
- what trade-off the flow accepts;
- what depends on ops, policy, or unresolved assumptions.

Do not produce a high-fidelity screen, a Dopamine component specification, a
polished visual prototype, a responsive production specification, or
design-to-code output. Those belong to Stage 2 and Stage 3.

## Output structure

```markdown
## Source language
<!-- REQUIRED whenever a screenshot, product screen, or flow was supplied.
     Omitting this section means the extraction did not happen. Do not write
     "extraction complete" — write what you actually saw. -->

**Sources inspected:** [file names / frame names, each one actually opened]

| Property | What the source does | Grayscale translation |
| --- | --- | --- |
| Surface fills | [flat / gradient — name the direction and both stops] | ... |
| Accent hue | [the hue carrying status, and where it appears] | ... |
| Tinted surfaces | [which surfaces are tinted rather than white or grey — for each, the **palette family** it reads as and the **stop** (95/97/99), plus the meaning it carries] | ... |
| Container geometry | [radius character, card vs full-bleed, separator style] | ... |
| Icon chips | [shape, size, radius, background treatment] | ... |
| Icon tinting | [uniform, or per-meaning — say which meanings map to which, naming the family and stop for each] | ... |
| Imagery | [photographic / illustrated / glyph, and at what size and radius] | ... |
| Container idiom | [the page's own construct: geometry, padding, border behaviour — what a new element must resemble to read as native rather than bolted on] | ... |
| Density and rhythm | [padding, gaps, where the page breathes vs tightens] | ... |
| Action placement | [where primary and secondary actions sit] | ... |
| Typographic hierarchy | [what is largest, what carries weight, what recedes] | ... |

**Three markers that could only have come from these sources:**
1. ...
2. ...
3. ...

**Deliberately not carried, and why:** [anything in the source the wireframe
drops on purpose — a weak pattern, an accessibility problem, brand colour]

## Solution coverage
| Agreed item | Screen / surface / state | Status |
| --- | --- | --- |
| ... | ... | mapped / deferred (reason) / unresolved |

## Screen and surface map
- ...

## Stage specifications

### [Stage]
- Purpose:
- Arrives thinking:
- Primary understanding:
- Primary information:
- Supporting information:
- Conditional or deferred information:
- Primary action and consequence:
- Secondary actions:
- Surface and rationale:
- Next state:

## States and recovery
- ...

## Interaction and motion notes
- ...

## Design notes
- Why the main states exist:
- Key hierarchy choices:
- Trade-offs accepted:
- Dependencies or unresolved assumptions:

## Assumptions and open decisions
- Stable enough to design with:
- Assumption-led:
- Must be revisited:

## Component candidates
| Wireframe zone | Likely Dopamine component(s) | Notes |
| --- | --- | --- |
| Top navigation bar | PageHeader, Navigation | Location context variant |
| Add to cart bar | AddToCartPill | Sticky bottom variant |

Advisory only. Stage 2 resolves the real selection against Storybook.

## Handoff boundary
- Decisions intentionally left to Stage 2 (compose):
- Decisions intentionally left to Stage 3 (polish):
```

## Wireframe check

Inspect the rendered artifact before delivering it.

- The user explicitly requested or accepted the wireframe before construction began.
- Every screen or surface has one clear purpose.
- The strongest focus matches the user's immediate need.
- The right information appears before the relevant decision.
- Primary and secondary actions are visually distinct.
- Spacing follows the 4px rhythm; alignment, grouping, and sizing are consistent.
- Every interactive element meets 48dp; high-stakes actions meet ≥48+12dp.
- Hierarchy is clear without brand colour.
- Icons are consistent in family, size, and stroke.
- Selected and unselected states are immediately understandable.
- Progressive disclosure hides nothing material — no consequence, cost, risk, dosage, drug identity, or allergen.
- Drug names, dosages, and allergens appear at full length; nothing truncates.
- Surface choices preserve context and match decision weight.
- The user can understand what happens next; back, change, cancel, exit, and recovery work.
- Motion only clarifies behavior, and a reduced-motion path exists.
- Every agreed solution element is represented, or marked deferred with a reason.
- The device is fully visible and remains the visual focus.
- `wireframe-preflight.md` passed before construction began.
- The mandatory source-language extraction was completed before construction, names the inspected sources, and records at least three markers that could only have come from them.
- Supplied screenshots, screens, or flows informed the grayscale language without being copied pixel for pixel.
- The delivery includes design notes strong enough to explain and defend the main choices.
- The artifact reads as visibly low fidelity and claims no component or token accuracy.
