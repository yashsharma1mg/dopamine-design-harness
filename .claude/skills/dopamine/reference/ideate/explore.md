# Stage 1 · Phase 4 — Explore possible ways to solve it


## Purpose

This step exists to compare meaningful ways the product could help the user. A stronger solution changes the user's ability to make progress. It does not only rearrange screens or rename actions.

Use this reference after the workflow has:

- understood the problem;
- mapped the context;
- checked whether research is still needed;
- framed the real problem;
- built enough user understanding to compare directions responsibly.

If research is still blocking the direction, do not use this file to fake certainty. Return to the research branch or, if the user explicitly wants progress in parallel, keep the work provisional and reversible.

Gate on the branch-1 decision:

- **Research not needed:** compare directions and recommend one using the workflow below.
- **Move ahead with assumptions:** recommend only within the supported scope. Keep assumptions visible, limit product autonomy, preserve user control, and prefer choices that can be changed, undone, or recovered from.
- **Stop for research first:** do not recommend a final direction and do not produce a flow, wireframe, or screen. State the competing hypotheses and the design decision that better understanding must resolve. If the user asks for early ideas anyway, present them as hypotheses to investigate, never as the recommendation.

Before using this file, say why it is responsible to move ahead:

- what is stable enough to solve now;
- what is still assumption-led;
- whether the recommendation is stable or provisional.

## Boundary

This file is for solution direction, not final interface making and not product or engineering definition.

It may define:

- how the product should help;
- what role the product should play;
- what the user should understand and control;
- how the journey should change;
- what prevention, support, or recovery the experience should include;
- which high-level surfaces or interaction models the direction depends on.

**Hand off downstream, do not do here:**

- Dopamine component selection, variant props, and token resolution → **Stage 2, `compose.md`**. The component candidates table at the end of Stage 1 is advisory only.
- Final visual treatment, intentional departures, motion polish → **Stage 3, `polish.md`**.

**Hand off sideways, do not do at all:**

- Product requirements, business rules, acceptance criteria, roadmap decisions.
- Technical specifications, APIs, engineering tickets, or estimates.

When the direction depends on policy, ops, product, or technical decisions, surface the dependency instead of silently deciding it.

Nothing here refuses design-system work — it defers it. Stage 2 exists to implement Dopamine 2.0 against this direction and Stage 3 exists to depart from it deliberately. Name the stage that owns the request; never say it is out of scope.

When the user explicitly asks for solution directions, options, or recommendation as the deliverable, stop after producing the direction output. Do not continue into detailed flow design, hierarchy planning, surface mapping, or wireframes unless the user explicitly asks for the next step.

## 1. Set the decision frame

Carry forward:

- the working user story;
- the framed UX problem;
- the user's desired progress;
- the product's desired outcome;
- known constraints and capabilities;
- assumptions that could change the direction.

State what the solution must achieve and what it must avoid.

Before exploring directions, ask:

- Does the direction depend on a cause we have not actually established?
- If that assumption is wrong, what breaks?
- Can the direction be reviewed, changed, undone, or recovered from?
- Does trust, privacy, policy, safety, or consequence require a lower-risk direction first?

If the answer makes the frame unstable, step back. Do not invent precision and continue anyway.

## 2. Decide what role the product should play

Choose the role the product should play at the important moments in the journey:

- **Explain:** help the user understand information, status, consequences, or limitations.
- **Guide:** structure the process while keeping the user as the decision-maker.
- **Recommend:** suggest a direction with reasons and visible limits.
- **Act:** do something on the user's behalf within a clear scope and control boundary.

The role may change across the journey, but every change should be intentional. Define:

- what the product knows;
- what it infers;
- what it recommends;
- what it is allowed to do;
- what requires user confirmation or consent;
- how the user can change, pause, undo, or recover.

Use less product autonomy when confidence, permission, or reversibility is weak.

## 3. Choose the journey scope

Decide what kind of journey this problem needs:

- a one-time task;
- a repeated workflow;
- an ongoing relationship;
- or a connected mix of these.

Map the relevant horizon:

- **Before:** what triggers the need and how the user enters;
- **During:** what the user needs to understand, decide, and do;
- **Immediately after:** what changed, what happens next, and what control remains;
- **Over time:** what may continue, return, or need follow-up.

Do not design an ongoing system for a temporary need. Do not stop at transaction completion if the user's outcome continues beyond it.

## 4. Explore distinct directions

Create a small set of directions that differ in behavior, product role, or recovery model, not only in layout.

Each direction should define:

- the central idea;
- how the journey changes;
- the product role;
- the degree of user control;
- what it needs from the product or operation;
- the main advantage;
- the main trade-off or risk;
- when this direction would be the wrong choice.

Use prevention, support at the point of difficulty, and recovery as lenses where relevant. They may combine, but one should be the center of gravity.

Do not explore endless minor variations. Usually 2 to 4 directions are enough.

## 5. Compare directions

Compare directions against:

- fit with the user story;
- ability to resolve the real problem;
- clarity and effort for the user;
- trust, consent, and reversibility;
- fit with product capabilities and constraints;
- effect on the full journey, not only one screen;
- operational and implementation complexity;
- durability as conditions change.

Do not treat all directions as equal if one clearly leads. Say which one leads and why.

When prevention, support at the point of difficulty, and recovery are all plausible, compare them explicitly before combining them. Do not jump to a hybrid only because it sounds comprehensive.

## 6. Recommend one direction

Recommend one direction and explain:

- why it leads;
- why the others do not lead;
- what useful parts of the other directions should still be kept;
- what assumption boundaries still matter;
- what must remain provisional if research is still in progress.

If the user explicitly asked to proceed while research runs in parallel, mark the recommendation as provisional and keep the direction limited to reversible choices.

Split the recommendation when needed:

- **Stable now:** what is strong enough to design with confidence.
- **Provisional now:** what depends on assumptions that are acceptable for working progress.
- **Must be revisited:** what should change if research, ops, or policy answers come back differently.

## 7. Describe the experience architecture

For the recommended direction, define:

- entry points and triggers;
- major stages in the journey;
- what the user needs to understand at each stage;
- where the important decisions happen;
- what the system does and communicates;
- alternate and recovery paths;
- completion and post-completion behavior;
- ongoing behavior when relevant;
- dependencies and unresolved questions.

This is still architecture, not a full flow or wireframe.

When the direction depends on lab, ops, policy, or system behavior, surface those dependencies before describing detailed experience promises.

## 8. Choose high-level surfaces intentionally

At the direction level, classify the important interactions as:

- page;
- bottom sheet;
- inline disclosure;
- dialog;
- system feedback.

Base this on:

- continuity with the current context;
- depth of task;
- amount of information required;
- decision weight and consequence;
- reversibility and interruption;
- need to compare with parent context.

Do not decide surfaces from habit.

## 9. Narrate the recommendation

Explain the recommendation like a designer would:

1. What the user needs at this moment.
2. What the product should do to help.
3. What the user will understand and control.
4. Why this direction fits better than the alternatives.
5. What is deliberately deferred, removed, or left manual.
6. What trade-off the direction accepts.

## Output structure

```markdown
## Recommended Direction

**Design problem**
...

**User progress to unlock**
...

**Decision frame**
...

**Product role**
...

**Journey scope**
...

**Directions considered**
| Direction | Core idea | User fit | Control and trust | Complexity | Main trade-off |
| --- | --- | --- | --- | --- | --- |
| ... | ... | ... | ... | ... | ... |

**Chosen direction**
...

**Why it leads**
...

**What remains provisional or dependent**
- ...

**Experience architecture**
- Before:
- During:
- Immediately after:
- Over time:

**High-level surface decisions**
- ...

**Recovery and support implications**
- ...

**Open questions**
- ...

**Recommended next level of detail**
...
```

## Quality check

- The direction follows from the framed problem and user story.
- The step did not proceed when missing research still blocked the core direction.
- The answer stated why it was responsible to move ahead or why the work remained provisional.
- The compared directions are meaningfully different.
- The chosen direction is clear and justified.
- Product role and user control are explicit.
- Trade-offs are concrete.
- Prevention, support, and recovery were considered when relevant.
- Prevention, support, and recovery were compared explicitly before being combined.
- Dependencies are surfaced instead of silently decided.
- The recommendation stops before final UI, product requirements, or engineering specification.
