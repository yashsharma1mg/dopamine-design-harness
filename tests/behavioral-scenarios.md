# Behavioral scenarios

`test_harness.py` checks that the instruction files are internally consistent.
It cannot check whether an agent *following* them behaves correctly. These
scenarios do.

## How to run one

Give a fresh agent this preamble, substituting the scenario:

> You are running the Dopamine 2.0 design harness as a design agent.
> Read `.claude/skills/dopamine/SKILL.md` and follow its setup protocol exactly.
> The project root for this session is `<fixture>`.
> The user has invoked: `<command>`
> Load whatever reference files the protocol tells you to load. Follow them literally.
> Write no files. Produce your actual response to the user.
>
> Then add `---BEGIN TRACE---` recording: which reference files you loaded in
> order; which branch decisions you selected verbatim; which artifacts you
> produced (yes/no each); and any exact headings you used.

Grade the trace against the expectations below. **Do not tell the agent what is
being tested** — a described test is a performed test.

## Fixtures

| Fixture | Contents | Represents |
| --- | --- | --- |
| `empty/` | nothing | new project |
| `midstage/` | `PRODUCT.md` only | Stage 1 interrupted after branch point 2 |
| `wireframed/` | `PRODUCT.md`, `WIREFRAME.md`, `wireframes/*.html` | Stage 1 complete |
| `composed/` | above + composed surface | Stage 2 complete — buildable once B5 has run once |

`midstage/PRODUCT.md` must record both branch decisions and an agreed direction,
and must leave at least one evidence label as `assumed` — B3-C checks that the
label survives the session boundary and re-opens as a question.

---

## B1 · A vague prompt must halt the stage

Fixture `empty/`, command `/dopamine ideate`, request: *"we need an onboarding flow"*.

**Expect:** branch 1 = `Stop for research first`, stated visibly with reasoning.
**Expect none of:** user story, design mismatch, solution direction, brief, wireframe.
**Expect:** exact heading `Answer me few questions`. No `Shall I proceed with` —
nothing was offered, so there is nothing to approve.
**Expect:** `effort-and-speed.md` loaded unprompted; `read-input.md` skipped for a
text prompt; unreached phase files not loaded.

Fails if the agent designs an onboarding flow. "Onboarding flow" is a solution
shape, not a problem — designing it means inventing the user.

## B2 · A well-evidenced prompt must proceed

Fixture `empty/`, command `/dopamine ideate`, request: the diagnostics SRP case —
seven near-identical urine tests, doctor-initiated traffic, prescription shorthand,
session recordings showing comparison then drop-off, conversion 40% below baseline.

**Expect:** branch 1 = `Research not needed` **or** `Move ahead with assumptions`,
stated visibly with reasoning. Both are defensible: the breakdown is well evidenced,
but *which of the 7 tests are clinically equivalent* is not a design call, so
carrying it as a visible assumption is the stronger read. Grade the reasoning, not
the label. Competitive research decision stated either way, and `Skip` is correct
here — no competitor teardown resolves our own catalog naming.
**Expect:** a design mismatch naming the *translation vs shopping* gap; ≥2 distinct
directions compared; one named centre of gravity (prevention / support / recovery).
**Expect:** permission asked before any wireframe.

Fails if it jumps to UI suggestions, or produces a wireframe unasked.

## B3 · Stage gates and routing

| # | Fixture | Command | Expect |
| --- | --- | --- | --- |
| A | `empty/` | `/dopamine compose` | Refuse; cite missing `WIREFRAME.md`; point to `ideate` |
| B | `wireframed/` | `/dopamine polish` | Refuse; cite missing composed surface; point to `compose`; verify compose's own gate first |
| C | `midstage/` | `/dopamine` (no arg) | **Resume** ideate at Phase 6 — not restart. Derive the phase from `PRODUCT.md` |

C is the important one: it exercises the routing branch for an interrupted Stage 1.
Fails if it restarts the interrogation from scratch.

## B4 · Hand-off and consent

Fixture `midstage/` (direction already agreed).

**A.** *"Build me the final UI for this PDP using real Dopamine components and
tokens, production ready."*
**Expect:** does not build it; names Stage 2; cites the unmet gate; **never** says
"out of scope"; produces no substitute artifact; asks with `Shall I proceed with`.

**B.** *"Write the PRD with acceptance criteria and success metrics."*
**Expect:** hands sideways to product using ownership framing, not refusal framing;
writes no PRD and no disguised PRD under another name; may *name* the Brief as
design's input to a PRD but must not write it unasked.

---

## Stage 2 and 3 scenarios

Now runnable — `compose.md` has a protocol and the MCP is authenticated.

### B5 · Compose resolves against the MCP, not from memory

Fixture `wireframed/`, command `/dopamine compose`.

**Expect:** verifies the MCP with `list_components` before anything else; checks
`list_patterns` before assembling parts by hand; calls `get_component_docs` per
component rather than once; treats the Stage 1 candidates table as a hypothesis
and says where it was wrong; resolves Stage 1 type *roles* to real `--font-size-*`
tokens; names any unmapped zone as a system gap instead of approximating it.

**Fails if** it invents a prop or a union value, restyles a component with ad-hoc
CSS, or carries a pixel value forward from the wireframe.

### B6 · Compose degrades honestly

Same fixture, MCP deliberately unreachable (drop the auth header).

**Expect:** says so *before* doing anything else and offers to stop. If told to
proceed, marks every component and value provisional, uses only the documented
type-scale fallback, and claims no design-system accuracy.

**Fails if** it composes silently from memory.

### B7 · Polish traces every departure to a principle

Fixture `composed/` (buildable once B5 has run once).

**Expect:** loads `interface-principles.md` during the Phase 1 audit and emits the
principle trace; every proposal names the principle *and* the law it serves;
proposals that cannot name both are dropped rather than offered; the decisions log
carries the principle confirmation block.

**Fails if** a departure is proposed with no principle trace, or if the accessibility
hard floor is treated as negotiable.

---

## The focus-ring fact — check it surfaces, every run

**Ruled by the design-system team: Dopamine 2.0 components are mobile UI
components and carry no focus-ring styling by design.** This is settled, not an
open question.

Any run that touches the accessibility pass — Stage 2 Phase 4, or the Stage 3
hard floor — must **state the fact**, so a reader can tell focus was considered
and correctly found not applicable.

Three failure modes, all worth grading:

1. **Silent omission.** The pass runs, focus is never mentioned. A reader cannot
   distinguish "not applicable" from "forgot to check".
2. **Flagged as a defect.** The agent reports missing focus rings as an
   accessibility failure, or proposes adding them as a Stage 3 departure.
3. **Re-opened as a question.** The agent treats it as a conflict to escalate
   rather than a fact to state.

`test_focus_ring_fact_surfaces_wherever_accessibility_runs` guards that the fact
is written down in `accessibility.md`, `compose.md`, `polish.md` and `SKILL.md`,
and `test_seven_states_became_six` guards that the state count followed. Only a
behavioural run can check that an agent actually says it out loud.

## Still not testable

**Rendered wireframe verification.** Phase 8 mandates one rendered check of the
HTML artifact. Testing it requires letting an agent write files, which these
scenarios forbid — run it manually.
