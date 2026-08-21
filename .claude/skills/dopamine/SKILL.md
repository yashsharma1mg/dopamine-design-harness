---
name: dopamine
description: >
  Use when the user wants to design, build, compose, audit, or polish a
  mobile-first interface using the Dopamine 2.0 design system. Covers
  ideation, wireframing, component composition from the governed token-backed
  library, and visual polish. Handles page flows, cart surfaces, PDP,
  navigation, forms, feedback patterns, health indicators, and pharmacy
  commerce UI for the 1mg product family. Also use when reviewing existing
  surfaces against Dopamine 2.0 compliance, extracting component usage from
  Figma specs, or proposing intentional departures from the system for
  visual distinction.
  Not for backend-only, API-only, or non-UI tasks.
argument-hint: "[ideate | compose | polish] [target]"
user-invocable: true
allowed-tools:
  - Bash(node *)
  - Read
  - Write
  - MCP(storybook-*)
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

3. **Familiarise yourself with the existing codebase.** Read at least one
   project file (token JSON, CSS variables, a representative component or
   page). If no codebase exists yet, note that — it affects which stage
   is valid.

4. **Check stage prerequisites.** Each stage has an entry gate:
   - `ideate` — always valid; this is the starting point.
   - `compose` — requires a completed wireframe artifact from Stage 1
     (a `WIREFRAME.md` or equivalent checked into the project).
     The Storybook MCP connection must be available. Stage 2 loads both
     `reference/interface-principles.md` and `reference/accessibility.md`.
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

### Component library (35 ready)

Actions: Button, Stepper, FloatingActionButton, ActionBar
Navigation: PageHeader, SearchBar, Navigation, HorizontalTabs, VerticalTabs,
  SwipeIndicator, QuickLinks
Forms: InputField, Toggle, Checkbox, Radio
Selection: SuggestionChip, QuantitySelector
Display: EventBanner, Tag, Product, ProductLabel, Offer,
  ProductInformation
Feedback: Sticky, Snackbar, Tooltip, Bottomsheet, Dialog
Cart: CouponWidget, SavingStrip, AmountWidget, CarePlanCard, OrderStrip,
  AddToCartPill, PackOfMultiples

All components import from `@dopamine2.0/ui` and use typed props that
mirror Figma variant names (type / state / size / style).

### Accessibility (WCAG 2.2 AA · IS 17802 · RPwD Act 2016)

Accessibility is legally binding in India (Article 21, SC Apr 2025).
Full reference at `reference/accessibility.md`, loaded by Stage 2.

Critical constraints that affect all stages:
- Three tokens fail WCAG on white: Content/Tertiary (3.29:1),
  States/Warning (2.79:1), Branding/Coral (3.18:1). Restricted usage.
- Drug names, dosages, allergens: NEVER truncate. Wrap, never ellipsis.
- Touch: 48dp default, ≥48+12dp for high-stakes (OTP, payment, dosage).
- Cabinet Grotesk only at ≥24pt.
- Seven states per interactive element: default, hover, focus, pressed,
  loading, disabled, selected.

### Interface principles (the design-conviction layer)

The system's intent layer: three tiers — Principles (what kind of
experience), Laws (how it's designed), Visual (how it's built) — under one
overriding bias: **clarity and safety always beat delight.** Full reference
at `reference/interface-principles.md`, loaded alongside accessibility by
Stage 2.

Six principles (ranked): Trust through explainability · Calm over alarm ·
Context aware · Answer first · Progressively disclose · Participation creates
ownership. Five laws: next action obvious · assume mistakes · consistency over
creativity · low cognitive load · aesthetics aid usability.

## Commands

| Command            | Stage | Description                                          | Reference              |
| ------------------ | ----- | ---------------------------------------------------- | ---------------------- |
| `ideate [target]`  | 1     | Question until clear, then produce wireframes        | reference/ideate.md    |
| `compose [target]` | 2     | Build with real components and design principles     | reference/compose.md   |
| `polish [target]`  | 3     | Propose intentional departures for visual distinction | reference/polish.md   |

### Routing rules

1. **No argument**: check the project state. If no PRODUCT.md exists,
   recommend `ideate`. If wireframes exist but no composed surface,
   recommend `compose`. If a composed surface exists, recommend `polish`.
   Never auto-run a stage; recommend and let the user confirm.

2. **First word matches a stage command**: check the entry gate, then load
   its reference file and follow its protocol.

3. **First word doesn't match but intent is clear** (e.g. "wireframe the
   cart page" → `ideate`, "hook up the real components" → `compose`,
   "make it pop" → `polish`): load the matching reference and proceed.

4. **No clear match**: ask which stage the user is in. Do not guess.

Setup is always complete before any stage begins. Stages do not re-invoke
`/dopamine`.
