# Stage 1 — Ideate

Understand the problem, frame it, choose a direction, then produce an
interactive low-fidelity wireframe. This stage commits to *what* gets built and
*why*. It selects no Dopamine components, resolves no tokens, and applies no
brand colour — those belong to Stage 2.

## Entry gate

Always open. This is where every new surface starts.

Valid inputs: a text prompt, a Figma or FigJam board, a screenshot, a product
brief or PRD, or an existing surface to be redesigned.

**Always load `../effort-and-speed.md` first.** It is the brake on process for
its own sake, and it governs how much of the workflow below actually runs.

## How to work

Act as a senior product designer working *with* the user, not as an artifact
generator waiting for instructions. Build shared understanding, make design
reasoning visible, challenge weak assumptions, and turn the chosen direction
into the detail the user actually needs.

Be decisive without pretending uncertainty does not exist. Keep provided,
observed, inferred, and assumed information distinguishable throughout.

- Start with the user situation and product context before proposing features or screens.
- Do not build a user story, framing, direction, flow, or wireframe from only a business concern, a target, or a desired outcome.
- Do not require new research by default. Existing product knowledge may be enough.
- Treat the absence of new research differently from the absence of user understanding.
- Ask only questions whose answers could materially change the framing, direction, flow, hierarchy, or safety of the solution. Question count is not rigor.
- Require stronger support as consequence, irreversibility, trust, privacy, policy, or safety increases. This is a healthcare product; that bar is high.
- Treat the user story as an editable hypothesis, not a fact.
- Explore meaningfully different directions before committing to one.
- Treat interface copy as part of the solution, not filler added after the structure is done.
- Preserve agreed solution coverage when translating it into a wireframe. Do not silently add, remove, merge, rename, or replace states.
- Do not create artifacts the user did not ask for.
- Work as one designer. Do not delegate to subagents.

## Consent gate

Before producing any artifact — a brief, a flow, a research guide, a wireframe —
confirm the user asked for it or accepted it when offered. Having enough context
is not permission. An agreed direction is not permission for a specific artifact.

When the request belongs to a later stage, **name the stage that owns it and
hand off**. Do not refuse, and do not silently substitute something else:

> That's Stage 2 — composing this with real Dopamine components and tokens.
> I can finish the wireframe first so `compose` has its entry gate. Want me to?

Nothing in Stage 1 refuses design-system work. Stage 2 exists to do it. The one
hand-off that goes sideways rather than downstream is PRD authoring — that
belongs to product.

## Response format

**Keep it short.** `../effort-and-speed.md` governs response length as well as
work volume — lead with the answer, say things once, cut process narration, and
use tables for anything with repeating structure. A visible decision is one line
plus its reason, not a section.

- When missing information blocks the next design step, use the exact heading: **Answer me few questions**, and ask only the smallest set that could change the framing, direction, flow, hierarchy, safety, or branch choice. Do not bury blocking questions inside paragraphs.
- When ready to move into a meaningful next step that needs approval, use the exact heading: **Shall I proceed with**, followed by a numbered list. Use it for direction, flows, research guides, and wireframes — not for trivial transitions.
- On the first substantive response to a new problem, end by naming the most useful next step and, where a real choice exists, what to pick.
- If background reasoning materially shaped the recommendation, surface it plainly. Do not hide the logic behind a polished conclusion.

## Workflow control record

For every meaningful redesign, keep a compact visible record of:

- **Context sufficiency** — user, goal, journey, evidence, constraints, risks, assumptions, unknowns.
- **Decisions** — the research decision, the competitive-research decision, and the direction; each with its branch, reason, and assumption-led remainder.
- **References and coverage** — which references governed the work, and how agreed requirements, stages, states, branches, and recovery map into the artifact.

A gate may be skipped only when its outcome cannot materially affect the
decision *and* the response says why. Use the smallest responsible depth inside
the gates you do run — never silent omission.

Never: create a direction before both research decisions are visible; request
wireframe approval before direction agreement; construct a wireframe before
mapping coverage and completing the source-language extraction; or claim
completion before the principle and coverage checks pass or their failures are
stated.

---

## Phases

A main path with two branch points. Not every task needs every phase — but do
not let one phase quietly do the next one's job.

| # | Phase | Reference | Run it when |
| --- | --- | --- | --- |
| 0 | Read the input | `ideate/read-input.md` | The input is a board, screenshot, brief, or PRD. Skip for a narrow text prompt. |
| 1 | Understand and map the context | `ideate/understand.md` | Always. |
| **↳** | **Branch point 1 — do we know enough?** | `ideate/understand.md` | **Always, and always visibly.** |
| — | *Research branch* | `ideate/research.md` | Only from **Stop for research first**, and only if the user asks for research help. |
| 2 | Read the signals | `ideate/understand.md` | Always. |
| 2b | Competitive research | `ideate/competitive-research.md` | **Default: skip.** See below. |
| 3 | Frame the real problem | `ideate/frame.md` | The problem is new, broad, symptom-led, or open to interpretation. Skip if already specific and agreed. |
| 4 | Understand the user situation | `ideate/understand.md` | A new problem, solution, journey, or flow. |
| 5 | Explore possible ways to solve it | `ideate/explore.md` | A new solution or meaningful redesign. |
| **↳** | **Branch point 2 — do we agree on the direction?** | `ideate/review-direction.md` | Load only when the direction needs comparison, diagnosis, or step-back logic. |
| 6 | Shape the experience | `ideate/comprehend.md` | Multiple stages, consequential decisions, or new concepts. |
| 6b | Stress-test against the principles | `../interface-principles.md` | **Compulsory** before finalising the structure, and again before the wireframe. |
| 7 | Plan content and hierarchy | `ideate/comprehend.md` + `../content-design.md` | Before any screen is drawn. |
| — | **The Brief** | below | Always. The Stage 1 sign-off gate. |
| 8 | Interactive wireframe | `ideate/wireframe.md` → `ideate/wireframe-preflight.md` | Only when the user asked for it or accepted it. |

### Branch point 1 — research

Governs everything downstream. Must be visible in the response, never silent.
Three branches: **Research not needed**, **Move ahead with assumptions**, **Stop
for research first**.

`Stop for research first` halts the stage. It produces no user story, framing,
direction, brief, or wireframe, and downstream references must not be used to
make the missing decisions look resolved.

### Competitive research — default to skip

Run it only when the user explicitly asks, or a **named** unknown could
realistically change the proposed interaction, hierarchy, recovery, or
direction. Healthcare, trust, category familiarity, or the existence of
competitors is *not* by itself a reason. Make the decision visible either way:
name the decision a scan would inform, or say why outside patterns cannot change
the direction.

> Resolves a contradiction in the source skill, where the orchestrator said
> "default to Run for healthcare" while `competitive-research.md` and
> `effort-and-speed.md` both said healthcare is explicitly not enough. Two files
> to one, and the skip-by-default reading is the one `effort-and-speed.md`
> enforces — so skip wins.

### Branch point 2 — direction review

Ask: *do we agree the direction is strong enough to structure and express?*
Make the answer explicit **before** requesting an artifact. Approval to create a
wireframe confirms the artifact, not the direction, unless the direction was
separately agreed.

On disagreement, diagnose before generating more options — the problem may be
the framing, the user understanding, directions that are too similar, a right
direction explained badly, or a structure problem rather than a direction
problem. Step back only as far as needed.

---

## The Brief

When the phases are complete, consolidate them and present for sign-off:

```markdown
# Brief: [Surface Name]

## Decisions on the record
- Research: [Research not needed | Move ahead with assumptions] — why
- Competitive research: [Run | Skip] — why
- Direction: [agreed | under review]

## Surface
[What it is, where it lives in the IA]

## User
[The working user story in short form — situation, trigger, goal,
current behavior, breakdown, what progress means]

## The design mismatch
[From frame.md — the gap between what the product currently expects or
communicates and what the user needs to understand, decide, or accomplish]

## Direction
- Product role: [Explain | Guide | Recommend | Act]
- Journey scope: [one-time task | repeated workflow | ongoing relationship]
- Chosen direction: [what it is, and why it leads]
- Alternatives considered: [what they were, why they don't lead]
- Centre of gravity: [prevention | support at the point of difficulty | recovery]

## Goal
- User goal / Business goal / Success signal

## Content inventory
[Ordered list, marked required/optional]

## Understanding map
[From comprehend.md — summarise the breaks here; full table in WIREFRAME.md]

## Priority stack
1. / 2. / 3. [Everything else is secondary]

## Flow
- Entry / Exit / Flow position
- Surfaces per stage: [page | bottom sheet | inline disclosure | dialog | system feedback]

## States
- Empty / Error / Loading / Edge cases

## Constraints
[Technical, regulatory, clinical, consistency]

## Principle check
[From interface-principles.md — which principles the solution serves, which are
in tension, which law shapes the primary action, and confirmation that nothing
violates clarity-and-safety-beat-delight]

## Basis and limits
- Provided / Observed / Inferred / Assumed (and what changes if wrong) / Unknown

## Open questions
[Anything explicitly deferred to Stage 2 or 3]
```

**The user must approve the brief before the wireframe.** Read it back, ask
"Does this capture what we're building?", and wait. A correction to the user
story means: update it, say which design decisions change, preserve the ones
that don't, and continue — do not restart.

---

## Handoff

Stage 1 writes two files plus the artifact.

**`PRODUCT.md`** — durable product context, carried across every surface. The
user story, the design mismatch, evidence labels, product role, chosen
direction, and the decisions on the record.

**`WIREFRAME.md`** — this surface only. The brief, the full understanding map,
the solution coverage table, the component candidates table, and a link to
`wireframes/<surface>.html`. This file is Stage 2's entry gate; `compose`
refuses to run without it.

Neither is saved until the user confirms.

### Exit

When both files are written, say so plainly and name the next command:

> Stage 1 is complete. `PRODUCT.md` and `WIREFRAME.md` are saved, and the
> wireframe is at `wireframes/<surface>.html`.
>
> Next: **`/dopamine compose`** — translate these zones into real Dopamine 2.0
> components with correct token resolution.

Do not run Stage 2 automatically. Recommend and let the user confirm.

---

## Completion check

- Both branch decisions are visible in the conversation with their reasons.
- The problem, user, product, and constraints were understood well enough for the decisions made.
- The absence of new research was not mistaken for the absence of user understanding, or vice versa.
- Missing information was either asked about or marked as an assumption.
- Causal claims are supported; unverified explanations remain hypotheses.
- **Stop for research first** produced no user story, framing, direction, brief, or wireframe.
- The user story is believable, editable, and aligned with the recommendation.
- The solution addresses the supported difficulty, not only the visible symptom.
- Meaningfully different directions were compared, with one named centre of gravity — and prevention, support, and recovery were compared before being combined.
- The product role and degree of user control are explicit.
- The journey covers before, during, immediately after, and ongoing where relevant.
- The user understands the right thing before each decision.
- Copy serves the user's job at that step and states limitations honestly.
- The interface-principles check ran, and its failures were resolved or named.
- The wireframe preserved solution coverage; changes were confirmed, omissions marked deferred.
- Nothing clinical — dosage, drug identity, allergen — is hidden, truncated, or carried by colour alone.
- No artifact was created that the user had not requested or accepted.
- The stage ended by naming `/dopamine compose`.

## What this stage does NOT do

- Select Dopamine components or variant props (Stage 2)
- Resolve or apply tokens (Stage 2)
- Apply brand colour or final type treatment (Stage 2)
- Make intentional departures from the system (Stage 3)
- Write production code (Stage 2)
- Connect to the Storybook MCP (Stage 2)
- Author PRDs, business rules, acceptance criteria, tickets, or estimates (product's, not ours)

The wireframe is a structural contract. Everything visual is downstream.
