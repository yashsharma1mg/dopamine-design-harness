# Stage 2 — Compose

Translate the approved wireframe into a real surface built from Dopamine 2.0
components with correct token resolution. This stage commits to *how* the
surface is built — components, variants, props, tokens — under the design
system's interface principles and its accessibility floor. It makes the
surface correct. It does not make it memorable — that is Stage 3.

## Entry gate

Compose refuses to start unless both are true:

1. **An approved `WIREFRAME.md` exists at the project root** (Stage 1 output:
   brief + annotated wireframes + component candidates). If it is missing,
   send the user back to `ideate`. Do not compose from a verbal description.
2. **The Storybook MCP connection is available.** This stage cannot resolve
   component APIs or validate props without it. If the MCP is not connected,
   stop and tell the user to connect it before proceeding — do not guess
   component props from memory.

## Mandatory references — load both before composing

Both are non-optional. Read them now, not later.

1. **`reference/interface-principles.md`** — the design-conviction layer
   (six principles, five laws, the visual system, and the overriding bias:
   *clarity and safety beat delight*). Every zone is composed *toward* this.

2. **`reference/accessibility.md`** — the legal and clinical floor
   (WCAG 2.2 AA · IS 17802 · RPwD Act 2016). Every composed surface must pass
   *every* constraint here before it can advance to Stage 3. Accessibility on
   a healthcare app is legally binding and clinically necessary — a user who
   cannot read a dosage may take the wrong medicine.

The two are complementary: interface-principles is the intent to build
toward; accessibility is the floor you may never fall below. When principle
and floor appear to conflict, the floor wins — always.

---

## The Storybook MCP wire-up

This is where the MCP connection earns its place. Use the `storybook-*` tools
for four operations, in this order, and never substitute memory for them:

1. **Discover** — list and search the component library to confirm which
   components actually exist and what they are called. The candidate list in
   `WIREFRAME.md` is advisory; the MCP is authoritative.
2. **Read the API** — pull each component's documented props, variant axes
   (type / state / size / style), and token slots. Do not invent props or
   assume a variant exists. If the wireframe needs a variant the component
   does not expose, that is a gap — flag it, do not fake it.
3. **Validate** — check that the specific prop and variant combination you
   intend is a documented, supported configuration. Unsupported combinations
   are departures and belong to Stage 3, not here.
4. **Preview / confirm** — render the component to confirm the visual output
   matches the wireframe zone's intent before you commit it to the surface.

Also pull the canonical token values through the MCP (or the documentation
site at https://dopamine2-0.dopamine-ds.workers.dev/) rather than hardcoding —
every component value must resolve through the canonical token JSON.

---

## Protocol

Four phases, sequential. Map → Resolve → Check → Gate. Do not jump to code
before the mapping and token resolution are settled.

---

### Phase 1 — Map zones to real components

Take each zone from `WIREFRAME.md` and bind it to a real Dopamine 2.0
component via the MCP.

- Start from the wireframe's **component candidates** table, but verify every
  entry against the MCP `Discover` and `Read the API` steps. Candidates are a
  starting guess, not a contract.
- For each zone, select the component, the variant (type / state / size /
  style), and the props that realise the wireframe's intent and priority rank.
- Preserve the wireframe's **priority stack.** The P1 zone must map to the
  component and placement that makes it the strongest thing on the surface
  (Law 1 — make the next action obvious).
- If a zone has no matching component, stop and record it as a **composition
  gap.** Do not force an unrelated component into the slot and do not invent
  one. Gaps are surfaced to the user, not papered over.

Output of this phase: a zone → component map, with variant and prop notes.

---

### Phase 2 — Resolve tokens

Every value on the surface resolves through the token architecture. No raw
hex, no magic numbers.

- **Semantic tokens are the API.** Default to `token.semantic.*` for colour,
  spacing, and type roles. Reach for `token.component.*` only where a
  component contract requires it.
- **Components never reference base tokens** (`token.base.*`) directly. Base
  is reference material only.
- **The three failing tokens have restricted usage** (from `accessibility.md`):
  Content/Tertiary (3.29:1), States/Warning (2.79:1), Branding/Coral (3.18:1).
  Do not use them for body text on white. Follow the escalation rules in the
  accessibility reference.
- Honour the system constants: 360px mobile only, 16px page margin, 8px
  gutter, 4px spacing rhythm, the defined radii scale, Figtree for functional
  and expressive type, Cabinet Grotesk only at ≥24pt.

---

### Phase 3 — Check against principles, laws, and the floor

Run every composed zone through both references. This is the substance of the
stage — a surface that renders but fails these checks is not composed, it is
just assembled.

**Interface principles** (`interface-principles.md`) — for each zone ask:

- **Trust through explainability** — is anything shown (a recommendation, a
  price, a substitute, a flag) without a plain-words *why*?
- **Calm over alarm** — does any state use alarming colour or language, or
  fabricate scarcity, where a neutral frame with a clear next step would do?
- **Context aware** — does the surface adjust emphasis to the user from the
  brief, or treat them as generic? Does it re-ask for known information?
- **Answer first** — does the P1 zone deliver what the user came for before
  proof, choices, and extras — not after a link, banner, or ad?
- **Progressively disclose** — is anything safety- or clarity-critical hidden
  behind a disclosure? (Essential content stays in view; only extras collapse.)
- **Participation creates ownership** — are the real choices honest, with no
  confirm-shaming or dark patterns?
- **The laws** — is the next action obvious (Law 1); are mistakes prevented
  and recoverable (Law 2); is every pattern consistent with the rest of the
  app (Law 3); is the cognitive load chunked and are defaults smart (Law 4);
  is the surface calm, readable, and responsive (Law 5)?

When a principle and a law disagree, apply the overriding bias: **clarity and
safety beat delight.**

**Accessibility floor** (`accessibility.md`) — non-optional, every constraint:

- Contrast ratios pass (4.5:1 body, 3:1 large, 3:1 UI).
- Drug names, dosages, allergens, frequency **never truncate** — wrap, never
  ellipsis.
- Every interactive element has all seven states (default, hover, focus,
  pressed, loading, disabled, selected) — or the gap is flagged.
- Screen-reader label specified alongside every visual label; alt text follows
  the content rules.
- Touch targets ≥48dp (≥48+12dp for high-stakes: OTP, payment, dosage,
  destructive, allergy acknowledgment, KYC).
- Layout survives 130% and 200% text scaling; containers use `min-height`.
- Form fields carry persistent labels; errors are programmatically associated
  and say what's wrong and how to fix it.
- `prefers-reduced-motion: reduce` alternative on every animation.
- Consumer copy at Grade 7–8 reading level.

Where a component in the library lacks exhaustive state coverage, verify the
missing states yourself or flag the gap — do not assume the component handles
it.

---

### Phase 4 — Exit gate to Stage 3

The surface may advance to `polish` only when:

- Every zone maps to a real component with resolved tokens (no raw values, no
  unresolved slots).
- Every interface principle and law check in Phase 3 is either satisfied or
  logged as an explicit, user-acknowledged trade-off.
- **Every** accessibility constraint passes. This is a hard gate — a single
  failing constraint sends the surface back, not forward.
- All composition gaps are surfaced to the user, not hidden.

If anything fails, the surface stays in compose. Polish on a broken or
inaccessible foundation produces polished garbage.

---

## Output — the composed surface

Deliver:

1. **The surface code** — real `@dopamine2.0/ui` components with typed props
   mirroring the Figma variant names, all values resolving through tokens.
2. **The zone → component map** from Phase 1, with variant and prop choices.
3. **A compliance record** confirming Phase 3 — a short checklist showing each
   accessibility constraint passing and any principle/law trade-off the user
   acknowledged.
4. **The composition gaps list** — any zone with no matching component, any
   component missing states, any variant the wireframe needed but the library
   does not expose. This carries forward as context for Stage 3.

The user should be able to see, from the output alone, that the surface is
correct and accessible before anyone talks about making it memorable.

---

## What this stage does NOT do

- Interrogate or wireframe (that's Stage 1 — ideate)
- Make intentional departures from the system for visual distinction
  (that's Stage 3 — polish)
- Override or negotiate any accessibility constraint (never, in any stage)
- Invent components, props, or variants the MCP does not confirm
- Hardcode values that should resolve through tokens
- Advance a surface with any failing accessibility constraint
