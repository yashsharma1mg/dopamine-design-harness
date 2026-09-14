# Stage 3 — Polish

Propose intentional departures from the design system. The user approves
each one before it is applied. This stage makes a correct surface
memorable. It does not fix problems — that is Stage 2's job.

## Entry gate

Requires a composed surface from Stage 2 where:
- The surface is built from **real `@dopamine2.0/ui` components**, not
  hand-written CSS approximating them. Check the Stage 2 report's
  **Artifact format** line. If it says **MOCK**, stop — there is nothing here
  to polish.
- The Stage 2 **Source fidelity** check passed, or its gaps are named. Polish
  cannot restore a gradient the compose step dropped; that is a Stage 2 defect.
- All components render correctly against the token system.
- Accessibility constraints from `reference/accessibility.md` pass.
- No broken layouts, missing states, or unresolved tokens.

If any of these fail, send the user back to `compose`. Polish on a
broken foundation produces polished garbage.

**Polishing a mock is the worst failure this stage has**, because it looks like
success. Departures get proposed, traced to principles, and applied to a drawing
— producing a decorated mock and a decisions log that reads as though a real
surface were improved. If the artifact is hand-written HTML, say so plainly and
send it back.

## The hard floor

Accessibility constraints are NEVER candidates for departure. These
are non-negotiable regardless of visual justification:

- Contrast ratios (4.5:1 body, 3:1 large, 3:1 UI)
- Touch target minimums (48dp default, ≥48+12dp high-stakes)
- Screen reader labels and alt text
- Text scaling at 130% and 200%
- Drug name / dosage / allergen truncation ban
- States/Warning and Coral usage restrictions
- Form field persistent labels and error association
- `prefers-reduced-motion` alternative on every animation
- The six applicable interactive states per element
- Plain language (Grade 7–8) on consumer-facing copy

> **Focus rings are not on this list, and that is deliberate.** Dopamine 2.0
> components are mobile UI components and carry no focus-ring styling by design.
> State this whenever the hard floor is checked, so a reader knows focus was
> considered and correctly found not applicable. Do not propose adding focus
> rings as a departure, and do not fail a surface for lacking them.

If a departure proposal would violate any of the above, do not propose
it. There is no "but it looks better" exception. A user who cannot read
their dosage because you chased a visual effect is a patient harmed.

---

## Protocol

The stage has three phases: Audit, Propose, Apply. They are sequential.

---

## Phase 1 — Audit the composed surface

Before proposing anything, read the surface. You need to understand what
is there before you can see what is missing.

### The vocabulary for this audit

Load `reference/interface-principles.md` before auditing. It supplies the terms
this phase is actually judging against — the six ranked principles, the five
laws, and the overriding bias:

> **Clarity and safety always beat delight.**

Stage 3 is the one stage where delight may push back, but it may never reduce
clarity, safety, legibility, or user control. That bias and the hard floor below
are the same conviction stated twice; where they appear to disagree, the hard
floor wins because it is the measurable form.

Law 5 (*aesthetically pleasing designs work better*) is what the lenses below
are testing. When a departure proposal cannot trace back up to a law and a
principle, it is decoration, not design — say so and drop it.

### What to look at

#### Visual hierarchy
- Does the eye move through the surface in priority order (P1 → P2 → P3
  as defined in the wireframe brief)?
- Is there a clear focal point, or does everything compete equally?
- Are there dead zones where the eye skips?

#### Rhythm and pacing
- Does the spacing create a rhythm, or is it metronomically uniform?
- Is there a deliberate shift in density between sections (tight for
  scanning, open for breathing)?
- Does the scroll feel like it has sections, or is it one undifferentiated
  stream?

#### Brand presence
- Does this surface feel like 1mg, or could it belong to any pharmacy app?
- Where does the coral show up? Is it earning attention or just decorating?
- Does the typography create any personality, or is it purely functional?

#### Signature opportunity
- Is there one moment on this surface that a user would remember?
- If not, where could one be created without disrupting the hierarchy?

#### Micro-interaction gaps
- Are transitions between states instant where they could be smoother?
- Do loading states feel considered, or are they afterthoughts?
- Does tapping a primary action feel rewarding?

#### Content and copy
- Does the copy have a voice, or is it generic?
- Are there opportunities for specificity (a number, a name, a detail
  that makes the content feel real)?
- Can any label be shorter without losing meaning?

#### Principle trace

Run the same check Stage 1 ran, on the composed surface this time. From
`reference/interface-principles.md`, answer all five:

1. Which principle(s) is this surface serving most directly?
2. Which principle(s) are in tension here?
3. Which law is shaping the most important action, hierarchy, or recovery?
4. Does anything violate the overriding bias — **clarity and safety beat delight**?
5. What should change before this is strong enough to share?

If `PRODUCT.md` recorded a principle check from Stage 1, compare against it.
A surface that served *Answer first* in the brief and serves it no longer
drifted during compose — that is an audit finding, not a polish opportunity,
and it goes back to Stage 2.

### Audit output

Write an internal assessment (share it with the user) structured as:

```markdown
## Polish audit: [Surface Name]

### What's working
[2–3 things the composed surface does well — be specific]

### Where it flatlines
[The specific moments where the surface is correct but unremarkable.
These become the departure candidates.]

### Principle trace
- Serving most directly: [principle(s)]
- In tension: [principle(s), and where]
- Governing law for the primary action: [law]
- Drift from the Stage 1 principle check: [none | what changed]
- Overriding bias holds: [yes | what violates it]

### Signature opportunity
[The one moment that could make this surface memorable. Could be a
transition, a type treatment, a layout break, a micro-interaction,
a copy choice, or a use of the brand.]
```

---

## Phase 2 — Propose departures

Based on the audit, propose specific departures. Each proposal is a
structured unit. Do not propose vague improvements ("make it feel more
premium"). Every proposal must name the exact element, the exact system
rule being bent, and the exact visual outcome.

### Departure categories

#### Spacing departures
Breaking the 4px rhythm for visual tension. Examples: asymmetric section
padding to create weight, tighter-than-system grouping to imply
relationship, generous whitespace around a focal point to create
isolation.

#### Typography departures
Stretching beyond the documented type scale for a specific moment.
Examples: a hero number at a size the scale doesn't define, a label
set in Cabinet Grotesk at a weight the system doesn't use for that
role, letterspacing adjustments outside the default.

Constraint: Cabinet Grotesk stays ≥24pt. This is accessibility, not
system preference. It is on the hard floor.

#### Colour departures
Using a semantic token outside its defined role, or introducing a
treatment the token system doesn't account for. Examples: a background
tint derived from the palette but not defined as a semantic token, coral
used in a non-CTA context for brand warmth, a HIH severity colour used
as an accent in a health dashboard.

Constraint: contrast ratios are on the hard floor. Any colour departure
must pass the same ratios the system requires.

#### Elevation and depth departures
Using shadow levels, layering, or z-index in ways the system doesn't
prescribe. Examples: a sticky bar with a more dramatic shadow than
the default level, a card that lifts on interaction beyond the system's
hover elevation, a frosted-glass overlay not in the standard set.

#### Motion departures
Adding animation that goes beyond the functional 300ms ceiling for a
moment of delight. Examples: a staggered entrance for a list that
reveals items in priority order, a success state that breathes before
settling, a page transition that carries context from the previous
surface.

Constraint: `prefers-reduced-motion` alternative is still mandatory.
The 300ms ceiling is a system guideline, not an accessibility rule —
it can be stretched. But flashes ≥3/sec and missing reduced-motion
fallbacks are on the hard floor.

#### Layout departures
Breaking the grid, margin, or gutter rules for a specific section.
Examples: a full-bleed image that breaks the 16px page margin, an
asymmetric split that the grid doesn't prescribe, overlapping elements
that create depth.

#### Component departures
Using a component in a non-standard configuration. Examples: a Tag
used decoratively rather than informationally, a Bottomsheet with a
custom transition not in the standard set, an ActionBar with a layout
the documented variants don't include.

Constraint: the component must still function correctly for assistive
tech. A Tag used decoratively still needs correct ARIA roles.

#### Copy departures
Rewriting a label or message to have more voice than the system's
neutral default. Examples: a success toast that's specific instead of
generic ("Your Crocin is on its way" vs "Item added to cart"), an
empty state that guides instead of stating ("Search for your medicine"
vs "No results").

Constraint: Grade 7–8 reading level is on the hard floor. Voice does
not mean complexity.

### Proposal format

Present all proposals together, grouped by risk level. Use exactly
this structure for each:

```markdown
### [P1/P2/P3] — [Short name]

**Element:** [Exact element or section being changed]
**Serves:** [The principle it serves, and the law it acts through — from
  `reference/interface-principles.md`. A departure that cannot name both is
  decoration, not design. Drop it rather than propose it.]
**System rule being bent:** [The specific Dopamine 2.0 rule this departs from]
**Current state:** [What the composed surface has now]
**Proposed state:** [What the departure would look like — be precise]
**Why:** [The visual or experiential problem this solves]
**Risk:** [What could go wrong, and how to mitigate]
**Accessibility impact:** None — [confirm explicitly, or do not propose]
```

### Risk levels

**Safe** — departures within the spirit of the system that the design
team would not question. Spacing adjustments, copy specificity, subtle
motion. These are "the system didn't prescribe this, but it wouldn't
object."

**Moderate** — departures that visibly break a system rule for a clear
reason. A type size outside the scale, a colour used in a non-standard
role, a layout break. These need justification and the user should
understand the trade-off.

**Aggressive** — departures that significantly alter the surface's
relationship with the system. A component used in a fundamentally
non-standard way, a section that doesn't look like a Dopamine surface.
These should be rare, well-justified, and reversible.

### Proposal rules

- **Propose 3–7 departures.** Fewer than 3 means the surface is either
  already polished or you're not looking hard enough. More than 7 and
  you're redesigning — send them back to compose.

- **At least one must be safe, at least one must be moderate.** A
  proposal set of all-safe departures isn't polish, it's finishing.
  A set of all-aggressive departures isn't polish, it's redesign.

- **The signature moment gets a proposal.** The audit identified one.
  It must appear in the proposals, with enough specificity that the
  user can imagine it.

- **Each proposal stands alone.** The user can approve any combination.
  No proposal should depend on another being approved. If two are
  linked, merge them into one.

- **Name what you're NOT proposing.** If the audit found something that
  looked like a departure opportunity but you rejected it, say so
  briefly and say why. This builds trust that the proposals are curated,
  not exhaustive.

---

## Phase 3 — Apply

After the user responds to the proposals:

### Approval handling

- **Approved** — apply exactly as proposed. Do not embellish.
- **Rejected** — drop it. Do not argue, do not propose an alternative
  unless the user asks.
- **Modified** — the user wants the departure but adjusted. Confirm
  the modification, then apply.
- **"Tell me more"** — the user wants to see it before deciding. If
  the departure can be demonstrated (a colour swatch, a motion
  description, a before/after sketch), show it. Then ask again.

### Application rules

- Apply approved departures one at a time, verifying after each that
  nothing breaks. Token resolution, component rendering, and
  accessibility constraints must all still pass.

- If applying a departure breaks something unexpected, stop and tell
  the user. Do not silently fix the breakage by bending another rule.

- After all approved departures are applied, do a final accessibility
  check. Run through the hard floor list. If anything fails, revert
  the departure that caused it and inform the user.

### Phase 3 output — The Decisions Log

Save a `DESIGN_DECISIONS.md` at the project root documenting every
approved departure. This file is the institutional memory for why
the surface departs from the system. Use exactly this format:

```markdown
# Design decisions: [Surface Name]

Date: [date]
Stage 2 surface: [file or component reference]
Polish author: [who ran the session]

## Approved departures

### [Short name]
- **Element:** [what was changed]
- **Serves:** [principle → law]
- **System rule bent:** [what rule]
- **Change:** [before → after, precise values]
- **Rationale:** [why, from the proposal]
- **Risk level:** [safe / moderate / aggressive]
- **Accessibility verified:** Yes

### [Next departure...]

## Rejected proposals
[List what was proposed and rejected, with the user's reason if given.
Future polish sessions should not re-propose these without new context.]

## Hard floor confirmation
All accessibility constraints from reference/accessibility.md verified
after final application:
- [ ] Contrast ratios pass
- [ ] Touch targets pass
- [ ] Screen reader labels present
- [ ] Text scaling 130% and 200% verified
- [ ] Drug name / dosage / allergen truncation: none
- [ ] prefers-reduced-motion alternatives present
- [ ] Six applicable interactive states present (focus N/A — mobile UI)
- [ ] Form labels persistent and errors associated

## Principle confirmation
Checked against reference/interface-principles.md after final application:
- [ ] Every approved departure names the principle and law it serves
- [ ] No departure violates: clarity and safety beat delight
- [ ] Principles served in the Stage 1 brief are still served here
```

**The user must confirm the decisions log before it is saved.**

---

## What this stage does NOT do

- Fix broken components or missing states (that's Stage 2 — compose)
- Redesign the information architecture (that's Stage 1 — ideate)
- Override accessibility constraints (never, in any stage)
- Make unsupervised changes (every departure requires user approval)
- Propose departures without specific, implementable descriptions
- Apply departures that depend on other unapproved departures
