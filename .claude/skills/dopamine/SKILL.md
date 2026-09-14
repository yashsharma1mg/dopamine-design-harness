---
name: dopamine
description: >
  Use when the user wants to design, build, compose, audit, or polish a
  mobile-first interface using the Dopamine 2.0 design system. Covers UX
  problem framing, user stories, research planning, solution direction,
  journeys and flows, information hierarchy, interface copy, wireframing,
  component composition from the governed token-backed library, and visual
  polish. Handles page flows, cart surfaces, PDP, navigation, forms, feedback
  patterns, health indicators, and pharmacy commerce UI for the 1mg product
  family. Also use when reading a Figma or FigJam board, a screenshot, or a
  product brief or PRD as design input; when critiquing a screen or flow;
  when reviewing existing surfaces against Dopamine 2.0 compliance;
  extracting component usage from Figma specs; or proposing intentional
  departures from the system for visual distinction.
  Not for backend-only, API-only, or non-UI tasks.
argument-hint: "[ideate | compose | polish] [target]"
user-invocable: true
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash(node *)
  # Dopamine 2.0 design system over MCP — Stage 2 component APIs, tokens, variants.
  # Server name must be literal; `mcp__` rules cannot use parentheses or glob the server.
  - mcp__dopamine2-remote__*
  # Stage 1 Phase 0 mandates visually inspecting supplied Figma/FigJam frames.
  - mcp__plugin_figma_figma__*
  # Stage 1 Phase 8 mandates one rendered verification of the HTML wireframe.
  - mcp__claude-in-chrome__*
license: Internal — Dopamine 2.0 design system
---

Designs mobile-first interfaces through the Dopamine 2.0 design system.
Three stages: ideate → compose → polish. Each stage has a gate; do not skip.

## Setup (non-optional)

You MUST do these steps before proceeding:

1. **Read the project context.** Check whether a `PRODUCT.md` exists at the
   project root. If it does, read it — it carries the surface name, user
   persona, and any prior stage outputs (wireframe decisions, component
   inventory, polish approvals). If it does not exist, the only valid
   command is `ideate` — tell the user they need to start there.

2. **If the user invoked a stage command** (`ideate`, `compose`, `polish`),
   you MUST read `reference/<command>.md` next. Non-optional. The reference
   defines the stage's protocol; without it you will skip steps.
   For `ideate`, also load `reference/effort-and-speed.md` — it governs how
   much of the stage actually runs. Load the `reference/ideate/*` phase files
   lazily, only as each phase is reached.

3. **Familiarise yourself with the existing codebase.** Read at least one
   project file (token JSON, CSS variables, a representative component or
   page). If no codebase exists yet, note that — it affects which stage
   is valid.

4. **Check stage prerequisites.** Each stage has an entry gate:
   - `ideate` — always valid; this is the starting point. Accepts a text
     prompt, a Figma or FigJam board, a screenshot, or a product brief /
     PRD as input.
   - `compose` — requires a completed wireframe artifact from Stage 1
     (a `WIREFRAME.md` or equivalent checked into the project).
     The Dopamine MCP must be reachable — verify with `list_components`.
   - `polish` — requires a composed surface from Stage 2 with all
     components rendering correctly against the token system, and
     all accessibility constraints from `reference/accessibility.md`
     passing. If anything is broken, send them back to `compose`.

## Dopamine 2.0 system knowledge

The design system uses a three-layer token architecture:

- **Base** — Raw palette values and scales. Reference material for the
  system. Never used directly in components.
  Pattern: `token.base.color.{palette}.{stop}`
- **Semantic** — Meaning-bearing roles that survive theme and brand changes.
  The default choice for product UI.
  Pattern: `token.semantic.color.{category}.{role}`
- **Component** — Slot-specific decisions for stable component contracts.
  Pattern: `token.component.{name}.{variant}.{property}`

Key constraints:
- Components never reference base tokens directly.
- Semantic tokens are the API between design intent and component surface.
- Every component value must resolve through the canonical token JSON.
- 360px mobile only. Single viewport, no desktop. 16px page margin, 8px gutter.
- Typography: Cabinet Grotesk for display, Figtree for all other roles.
- Spacing: 4px rhythm (0, 2, 4, 8, 10, 12, 16, 20, 24, 28, 32, 36, 40).
- Radii: 0, 2, 4, 6, 8, 12, 16.
- Brand colour: coral #ff5443 (token.base.color.brand.coral).

### Expressive palettes — the tinted-surface vocabulary

Beyond cool-neutral, the base layer carries eight expressive families:
**sunrise-glow, wellness-green, precision-blue, vital-red, sunshine-yellow,
comfort-pink, healing-mauve, corporate-horizon-blue.**

Their **95 / 97 / 99 stops are the tinted-surface language** — the faint washes
that make a status band, a callout, or an intervention read as a *surface with
meaning* rather than a grey box. A tint at 99 with its own family at 95 as the
border is the house construct (e.g. `sunrise-glow.99` fill + `sunrise-glow.95`
border for a warm, brand-adjacent active surface).

**The semantic layer has no roles for these.** `semantic.color.background.*` is
cool-neutral only. So a tinted surface is the one sanctioned case for reaching
into a base expressive palette directly — take the tint from the family whose
meaning matches, and say why in the surface report. Everything else still
resolves through semantic.

Meaning already mapped: success/offer → wellness-green.40, error →
vital-red.40, warning → sunshine-yellow.50, rapid → healing-mauve.50,
corporate → corporate-horizon-blue.30. Health-in-Hand severity has its own
scale (`semantic.color.hih.*`) from wellness-green through vital-red.

### Component library — 38 ready

**`list_components` is authoritative. This list is a convenience and it goes
stale.** It was wrong once already: it said 35 and omitted StatusCard,
ActionCard and HealthInsights — the three that mattered most for a labs nudge —
so a run hand-rolled a `<div>` for a job a component already did. Never conclude
"no component exists" from this list. Conclude it from `search_components`.

Actions: Button, Stepper, FloatingActionButton, ActionBar
Navigation: PageHeader, SearchBar, Navigation, HorizontalTabs, VerticalTabs,
  SwipeIndicator, QuickLinks
Forms: InputField, Toggle, Checkbox, Radio
Selection: SuggestionChip, QuantitySelector
Display: **StatusCard**, **ActionCard**, **HealthInsights**, EventBanner, Tag,
  Product, ProductLabel, Offer, ProductInformation
Feedback: Sticky, Snackbar, Tooltip, Bottomsheet, Dialog
Cart: CouponWidget, SavingStrip, AmountWidget, CarePlanCard, OrderStrip,
  AddToCartPill, PackOfMultiples

**The three that get missed**, because they sound like layout rather than
components:

- **ActionCard** — the nudge and cross-sell widget. Its own docs name
  "test recommendation card" and "labs cross sell". `tone` is a prop
  (`neutral | peach | mauve | blue`), so the tinted surface comes for free, and
  its Don't list says: *do not build a separate cross-sell component.*
- **StatusCard** — the order-status widget: a tinted parent card holding white
  child cards.
- **HealthInsights** — the HIH widget: patient tabs over insight cards with
  tags, readings and CTAs.

If a surface needs "a card that nudges the user toward something", that is
ActionCard. Reaching for a custom div there is the most common way this system
gets bypassed.

All components import from `@dopamine2.0/ui` and use typed props that
mirror Figma variant names (type / state / size / style).

### Interface principles

The design-conviction layer sits in `reference/interface-principles.md`: six
ranked principles (trust through explainability, calm over alarm, context aware,
answer first, progressively disclose, participation creates ownership) and five
laws that translate them into design rules. One bias overrides everything:

> **Clarity and safety always beat delight.**

Compulsory in Stage 1 before the structure is final; the audit vocabulary for
Stage 3. A visual decision that cannot trace back up to a law and a principle is
decoration, not design.

### Accessibility (WCAG 2.2 AA · IS 17802 · RPwD Act 2016)

Accessibility is legally binding in India (Article 21, SC Apr 2025).
Full reference at `reference/accessibility.md`, loaded by Stage 2.

Critical constraints that affect all stages:
- Two tokens fail WCAG on white: States/Warning (2.79:1) and
  Branding/Coral (3.18:1). Restricted usage. Content/Tertiary (#626a7a)
  passes at 5.43:1 — verify any contrast claim against `get_tokens`,
  not memory.
- Drug names, dosages, allergens: NEVER truncate. Wrap, never ellipsis.
- Touch: 48dp default, ≥48+12dp for high-stakes (OTP, payment, dosage).
- Cabinet Grotesk only at ≥24pt.
- Six applicable states per interactive element: default, hover, pressed,
  loading, disabled, selected. **Focus is not applicable** — Dopamine 2.0
  components are mobile UI and carry no focus-ring styling by design. State
  this whenever the accessibility pass runs; never flag it as a defect.

## Commands

| Command            | Stage | Description                                          | Reference              |
| ------------------ | ----- | ---------------------------------------------------- | ---------------------- |
| `ideate [target]`  | 1     | Understand, frame, choose a direction, then wireframe | reference/ideate.md    |
| `compose [target]` | 2     | Build with real components and design principles     | reference/compose.md   |
| `polish [target]`  | 3     | Propose intentional departures for visual distinction | reference/polish.md   |

### Routing rules

1. **No argument**: check the project state and recommend the next step.
   Stage 1 is long enough to be interrupted part-way, so check in this order:
   - No `PRODUCT.md` → recommend `ideate` (start from the beginning).
   - `PRODUCT.md` but no `WIREFRAME.md` → Stage 1 was interrupted after the
     understanding work. Recommend resuming `ideate`, and say which phase it
     left off at — read `PRODUCT.md` to find out. Do not restart the
     interrogation from scratch.
   - `WIREFRAME.md` but no composed surface → recommend `compose`.
   - A composed surface exists → recommend `polish`.

   Never auto-run a stage; recommend and let the user confirm.

2. **First word matches a stage command**: check the entry gate, then load
   its reference file and follow its protocol.

3. **First word doesn't match but intent is clear** (e.g. "wireframe the
   cart page" → `ideate`, "hook up the real components" → `compose`,
   "make it pop" → `polish`): load the matching reference and proceed.

4. **No clear match**: ask which stage the user is in. Do not guess.

Setup is always complete before any stage begins. Stages do not re-invoke
`/dopamine`.
