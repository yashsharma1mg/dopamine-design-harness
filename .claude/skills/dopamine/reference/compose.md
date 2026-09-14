# Stage 2 — Compose

Translate the approved wireframe into real Dopamine 2.0 components with correct
token resolution, variant selection, and prop configuration. This stage commits
to *what it is built from*. It does not revisit the structure — that was Stage 1
— and it does not depart from the system — that is Stage 3.

## Entry gate

Requires all of:

- An approved `WIREFRAME.md` at the project root, with its solution coverage
  table and component candidates. Without it, send the user back to `ideate`.
- The Dopamine MCP reachable. Verify with `list_components` before anything
  else. If it fails, see **Degraded mode** below — do not silently guess.

## Mandatory references

1. `reference/accessibility.md` — loaded in full, not skimmed. Every composed
   surface must pass every constraint before Stage 3. Non-optional:
   accessibility on a healthcare product is legally binding and clinically
   necessary.
2. `reference/interface-principles.md` — the surface must still serve the
   principles the Stage 1 brief recorded. Compose is where that quietly slips.
3. `reference/content-design.md` — when composing copy into real components.

## The MCP is the source of truth

Never write a component from memory. The tools return the real contract,
extracted from the actual TypeScript types:

| Need | Tool |
| --- | --- |
| What exists at all | `list_components` |
| Find the right one by intent | `search_components` |
| **Props, variants, states, a11y, usage** | `get_component_docs` |
| Composed multi-component recipes | `list_patterns` / `get_pattern_docs` |
| Token values | `get_tokens` (`base`/`semantic`/`component`/`space`/`radius`/`layout`/`font`/`shadow`) |
| Install, theming, conventions | `get_general_docs` |
| Project-level agent rules | `get_agent_rules` |
| See it rendered | `preview_component` / `preview_pattern` |

`get_component_docs` before every component you use. Not once per session —
once per component. A prop you remember is a prop you are inventing.

---

## Protocol

### Phase 1 — Resolve the candidates

The wireframe's component candidates table is **advisory**. Stage 1 wrote it
without the MCP; treat it as a hypothesis to check, not a decision to apply.

For every zone in the coverage table:

1. `search_components` on the zone's *intent*, not the candidate's name.
2. `get_component_docs` on each plausible match.
3. Pick one, and record why — including why the Stage 1 candidate was wrong
   where it was.
4. Before hand-rolling anything, check `list_patterns`. A composed pattern
   (`cart-checkout`, `for-you`, `homepage`, `pdp`) may already cover the whole
   surface, and a pattern beats assembling its parts yourself.

Output a resolved mapping: zone → component → variant → why.

**If a zone maps to no component**, say so explicitly. Do not approximate with
a component that nearly fits and then override its styling — that is the single
most common way a design system gets quietly abandoned. Options, in order:
reshape the zone to what the system offers (cheapest), raise it as a genuine
system gap (honest), or compose it from primitives and flag it for the DS team.

### Phase 2 — Resolve the tokens

Every value resolves through the three-layer hierarchy. Components never
reference base tokens.

```
base       raw primitives      {base.color.brand.coral}      never used directly
semantic   meaning-bearing     semantic.color.branding.1mg   the default choice
component  slot-specific       component.<name>.<variant>    stable contracts
```

In CSS, reference the variables:

```css
background: var(--semantic-color-background-primary);
color: var(--semantic-color-content-primary);
padding: var(--space-16);
border-radius: var(--radius-8);
box-shadow: var(--shadow-level-2);
```

In TS: `tokens["semantic.color.branding.1mg"]`.

Naming, confirmed from the live token set:

- Colours are nested — `--semantic-color-content-primary`, `--semantic-color-content-cta`, `--semantic-color-stroke-subtle`, `--semantic-color-branding-1mg`. `--base-color-*` exists; do not use it directly.
- Spacing, radius, type and shadow are top-level — `--space-16`, `--radius-8`, `--font-size-body-14`, `--shadow-level-2`.
- The brand role is `branding.1mg`; the raw value is `base.color.brand.coral` (`#ff5443`). Inline CTA text has its own role, `content.cta`.

**Resolve the Stage 1 type roles now.** The wireframe annotated text by role —
Page title → Heading → Title → Body → Sub text — precisely because Stage 1 had
no tokens. Map each to its real `--font-size-*` token via `get_tokens`. Do not
carry a pixel value forward from the wireframe.

Never hardcode a hex, a px spacing, or a radius that a token expresses.

### Phase 2b — Restore the source language

Stage 1's wireframe was grayscale **on purpose**. Its `## Source language`
section in `WIREFRAME.md` is the record of everything the greyscale dropped, and
Phase 2b is where it comes back. Read that section before composing. If it is
missing, the extraction never happened — stop and send the surface back to
Stage 1 rather than inventing a visual language.

Walk the extraction row by row and restore each property with real tokens:

| Recorded | Restore as |
| --- | --- |
| Gradient surface fills | The real gradient, both stops as tokens. A gradient flattened to a flat fill is a defect, not a simplification. |
| Accent hue and what it signals | The semantic role that carries that meaning. A status blue does not become grey, and it does not become a different hue. |
| Icon-chip shape and size | The recorded geometry. A rounded square does not become a circle. |
| Per-meaning icon tinting | The per-meaning tints. Collapsing them to one uniform grey destroys the signal the source was carrying. |
| Imagery | Real images where the source had real images. Substituting a glyph for a photograph changes what the row communicates. |
| Density, action placement, hierarchy | The recorded rhythm, not a default. |

The test: **put the composed surface next to the source screenshot.** If a
reviewer can tell which is which by anything other than the new intervention,
the restoration is incomplete. Say so rather than shipping it.

### Phase 3 — Compose

**Never hand-write CSS that emulates a component.** A `.btn-primary-l` class
with a comment reading `/* Button type=Fill size=Large */` is not a Button — it
is a drawing of one that will drift from the real component the moment either
changes. This is the single most common way a composed surface turns out to be a
mock. If a component exists, use it. If it does not, see Phase 1.

- Import from the barrel: `import { X } from "@dopamine2.0/ui"`. Import
  `@dopamine2.0/ui/styles.css` once, at the app root.
- Match each prop contract exactly. Props and their literal union values come
  from `get_component_docs`. **Inventing a prop, or a value outside a
  documented union, is a defect** — not a shortcut.
- Do not restyle a component with ad-hoc CSS. Use its variants and states. If
  no variant expresses what you need, that is a Stage 3 departure requiring
  user approval, or a system gap — not a local override.
- Do not add an icon library. Icons ship inside the components.
- Icon sizing: `DsIcon`/`Icon` render the glyph at the given `size` with no
  built-in padding, while Figma insets the glyph in a larger frame. Size to the
  **visible glyph**, roughly `Figma frame × 0.6`. Inline row-affordance chevrons
  land at 9–12px, never 16–20px.
- Selection controls (Checkbox, Radio, Toggle) are uncontrolled-capable: they
  self-toggle when no `checked` is passed and still fire their change callback.
  Do not wire redundant state around them.
- Build every state the coverage table names. A state marked *deferred with
  reason* in Stage 1 stays deferred; a state marked *mapped* gets built.

### What Stage 2 delivers

`@dopamine2.0/ui` is a React package (ESM, React 18+) whose stylesheet carries
the tokens, fonts, and component styles. That fact decides the format.

**The deliverable is TSX** — real components, imported from the barrel, props
matching the contracts from `get_component_docs`. This is the surface. It is
what an engineer picks up and what Stage 3 polishes.

**A review artifact is optional and is built one of two ways:**

1. `preview_component` / `preview_pattern` return a self-contained HTML render
   of the *real* component, every variant included. Assemble review artifacts
   from these. The markup and styling are the system's, not yours.
2. Render the TSX with a bundler that resolves the `exports` map.

**A standalone hand-written HTML file is not a composed surface.** It cannot
import the package, so every "component" in it is an approximation. If one is
produced anyway — as a quick visual for a stakeholder — it must be labelled a
**mock** in its title and in the surface report, and it may not claim component
or token fidelity. Never call it composed, and never let Stage 3 polish it.

The failure this prevents: a hand-rolled HTML file that looks finished, passes a
token-value check because the hex values were copied correctly, and is nowhere
near the design system because not one real component is in it.

### Phase 4 — Verify

Run all four. Report failures; do not quietly fix them by bending a rule.

**1 · Coverage.** Every item in the `WIREFRAME.md` coverage table is built, or
still carries its Stage 1 deferral reason. Nothing dropped silently.

**2 · Tokens.** No hardcoded hex, px spacing, or radius that a token expresses.
No component referencing a base token directly. No font weight outside the real
set — light 300, regular 400, medium 500, bold 700, extrabold 800. **There is no
semibold**; a `600` in the output is invented.

**2b · Source fidelity.** Every row of the `## Source language` extraction is
restored: gradients are gradients, the accent hue is the source's hue, chip
geometry matches, per-meaning tints survive, imagery is imagery. Side-by-side
with the source screenshot, nothing but the intervention should read as
different. List anything deliberately not restored, with the reason.

**2c · Real components.** Every interactive element is a `@dopamine2.0/ui`
import. Zero hand-written CSS classes emulating a component. If the artifact is
a mock, it says so in its title and here.

**3 · Accessibility — the full `accessibility.md` pass.** This is the gate to
Stage 3, and the whole list runs:

- Contrast: 4.5:1 body, 3:1 large, 3:1 UI. The two restricted tokens
  (States/Warning 2.79:1, Branding/Coral 3.18:1) fail
  on white — honour their restricted-use rules.
- Touch targets: 48dp default, 24×24 absolute floor, ≥48+12dp for high-stakes
  (OTP, payment, dosage).
- Drug names, dosages, allergens, frequency: **never truncate**. Wrap, never
  ellipsis. Verify at the longest real content, not placeholder length.
- Text scaling at 130% and 200% without loss.
- Screen-reader labels specified alongside every visual label.
- Six applicable states per interactive element: default, hover, pressed,
  loading, disabled, selected. **Focus is not applicable** — see below.
- `prefers-reduced-motion: reduce` on every animation.
- Form fields: persistent labels, errors explained and associated.
- Grade 7–8 reading level on consumer-facing copy.

> **State this every time the accessibility pass runs. Do not omit it, and do
> not re-open it as a question.**
>
> **Dopamine 2.0 components are mobile UI components. They do not carry
> focus-ring styling, and that is by design.**
>
> Focus rings are a pointer-and-keyboard affordance; these components target a
> touch surface at a single 360px viewport. A Dopamine component without a
> visible focus ring is **correct**. Do not flag it as a defect, do not add one
> with a CSS override, and do not fail the surface on it. Every other constraint
> above applies in full.
>
> The surface report carries this as a stated fact under **Accessibility pass**,
> so a reader knows focus was considered and correctly found not applicable —
> not that it was skipped.

**4 · Principles.** The surface still serves what the Stage 1 brief said it
would. Drift here is a compose defect, not a polish opportunity.

Use `preview_component` to see a component rendered when the prop contract is
ambiguous, rather than guessing and verifying later.

---

## Degraded mode — MCP unavailable

If `list_components` fails, say so before doing anything else, and offer to
stop. Composing without the MCP means inventing props and token values, which
is worse than not composing.

If the user chooses to proceed anyway, every output is provisional:

- Flag every component and every value as unverified.
- Use only the type-scale fallback below, and mark each use.
- Do not claim design-system accuracy.
- Re-resolve everything against the MCP before Stage 3.

### Type scale fallback

Stopgap only. Resolve from `get_tokens` whenever the MCP is reachable.

| Role | Fallback | Notes |
| --- | --- | --- |
| Page title | `title-22` 22px, bold 700 | Cabinet Grotesk only at ≥24pt; below that, Figtree |
| Heading | `heading-18` 18px, medium 500 or bold 700 | Figtree |
| Title | `body-16` 16px, medium 500 | Figtree |
| Body | `body-14` 14px, regular 400 | Figtree. 16px bold is the iOS input floor |
| Sub text / caption | `body-12` 12px, regular 400 | Never below the accessibility size floors |
| Tag | `tag-11` 11px, bold 700 | Tags and badges only, never sustained reading |

Weights are **light 300, regular 400, medium 500, bold 700, extrabold 800**.
There is no semibold. A `600` anywhere in the output is invented.

A fallback value is never a token. A hardcoded size that survives into the
committed surface is a defect.

---

## Output — the composed surface

Deliver the surface plus a short report:

```markdown
# Composed: [Surface Name]

## Resolved components
| Zone | Component | Variant | Why | Stage 1 candidate |
| --- | --- | --- | --- | --- |

## Patterns used
[pattern name, or none]

## Unmapped zones
[zone → what the system lacks → reshaped / raised as gap / composed from primitives]

## Token resolution
- Type roles → tokens: [Page title → --font-size-…, …]
- Any value not expressible as a token: [none, or what and why]

## States built
[from the coverage table: built / still deferred with reason]

## Artifact format
[TSX composed from real components | HTML assembled from preview_component |
**MOCK** — hand-written, no component fidelity, not for polish]

## Source fidelity
[each row of the Stage 1 extraction: restored | deliberately not restored + why]
[side-by-side with the source: what still reads as different, and why]

## Accessibility pass
[each hard-floor item: pass, or the specific failure]

> Focus states: **not applicable.** Dopamine 2.0 components are mobile UI
> components and carry no focus-ring styling by design. The six applicable
> states were verified.

## Principle check
[principles the brief recorded → still served? drift?]

## Ready for Stage 3
[yes | what must go back through compose first]
```

### Exit

When the surface renders correctly, tokens resolve, and the full accessibility
pass is clean:

> Stage 2 is complete. The surface composes from real Dopamine 2.0 components
> with tokens resolved, and the accessibility pass is clean.
>
> Next: **`/dopamine polish`** — propose intentional departures for visual
> distinction, each one approved by you before it is applied.

If anything failed the accessibility pass, do **not** advance. Stage 3 refuses a
broken foundation, and polishing one produces polished garbage.

## What this stage does NOT do

- Revisit information architecture or priority (Stage 1 — ideate)
- Depart from the system for visual distinction (Stage 3 — polish)
- Override accessibility constraints (never, at any stage)
- Invent props, prop values, or token names
- Restyle components with ad-hoc CSS
