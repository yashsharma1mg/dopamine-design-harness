---
name: solution
description: Explore, compare, and recommend a product experience direction after the user story and design problem are understood.
---

# Design the Solution

## Purpose

Choose how the product should help the user, then shape the experience around that choice. Review solution quality before designing screens. A stronger solution changes the user's ability to make progress; it does not only rearrange interface elements.

## Entry condition and allowed output

Use this reference only after the main workflow checks user understanding, existing support, cause dependence, consequence, and reversibility.

- **Move forward:** compare directions and recommend a solution using the normal workflow in this file.
- **Move carefully:** recommend only within the supported scope. Keep assumptions visible, limit product autonomy, preserve user control, and prefer choices that can be changed, undone, or recovered from.
- **Learn first:** do not recommend a final direction or produce a flow, wireframe, or screen. State the competing hypotheses and the design decision that better understanding must resolve.

The absence of newly conducted research does not block solution work when existing understanding is sufficient. Missing core user context or an unknown cause does block it when different answers would change the direction or when the consequence of being wrong is meaningful.

If the user explicitly asks for early ideas during **Learn first**, present them only as hypotheses to investigate, not as the recommended solution.

## Pre-UI boundary

This reference defines the experience direction, not the finished interface or the product and engineering specification.

It may define user behavior, information needs, stages, states, controls, surface choices, recovery, and experience dependencies. It must stop before:

- final visual design or design-system implementation;
- a high-fidelity UI prototype;
- product requirements, business rules, acceptance criteria, or roadmap decisions;
- engineering tickets, architecture, APIs, technical specifications, or estimates.

When the solution depends on a product, policy, operational, or technical decision, record the dependency and the question for its owner. Do not silently make that decision or turn it into another team's deliverable.

## 1. Set the decision frame

Carry forward:

- the working user story;
- the underlying design problem;
- the desired user and product outcomes;
- known capabilities and constraints;
- assumptions that could change the direction.

State what the solution must achieve and what it must avoid. If the frame is not stable enough to compare directions, return to the missing context rather than inventing precision.

Before exploring directions, ask:

- Does the direction depend on an unverified explanation of user behavior?
- What happens to the user if the assumption is wrong?
- Can the decision be reviewed, changed, undone, or recovered from?
- Does its reach, autonomy, trust, privacy, policy, or safety require stronger support?
- Can a safer, more reversible direction make responsible progress while learning continues?

## 2. Decide the product role

Choose the role the product plays at each important moment:

- **Explain:** help the user understand information, status, or consequences.
- **Guide:** structure the process while the user remains the decision-maker.
- **Recommend:** propose a direction with reasons, limits, and alternatives.
- **Act:** take action within explicit permission, scope, and controls.

The role may change across the journey, but each change must be intentional. Define:

- what the product knows;
- what it infers;
- what it proposes;
- what it may do;
- what requires user review or consent;
- how the user can change, pause, undo, or recover;
- how the product explains its reasoning and limitations.

Use less product autonomy when confidence, permission, reversibility, or consequence is unclear.

## 3. Choose the journey scope

Decide whether the problem needs:

- a one-time task;
- a repeated workflow;
- an ongoing product relationship;
- or a connected set of these.

Map the relevant time horizon:

- **Before:** trigger, current behavior, expectation, and entry point.
- **During:** understanding, decisions, actions, feedback, and recovery.
- **Immediately after:** confirmation, status, next step, and retained control.
- **Over time:** progress, reminders, changes, learning, or return behavior.

Do not make an ongoing system when the need is truly temporary. Do not end at transaction completion when the user's outcome continues beyond it.

## 4. Explore distinct directions

Create a small set of directions that differ in behavior or product role, not only in layout. For each direction, define:

- the central idea;
- how the journey changes;
- the product role;
- the degree of user control;
- what it requires from the product or operation;
- the main advantage;
- the main risk or trade-off;
- what would make the direction inappropriate.

Include prevention, support at the point of difficulty, and recovery as lenses when relevant. These lenses may be combined, but one should be the center of gravity.

## 5. Compare and choose

Compare directions against:

- fit with the user story;
- ability to resolve the underlying problem;
- clarity and effort for the user;
- product capability and constraint fit;
- safety, trust, consent, and reversibility;
- effect on the complete journey;
- implementation and operational complexity;
- durability as user needs or product conditions change.

Recommend one direction. Explain why it leads, why the alternatives do not lead, and which useful parts of them should remain.

In **Move carefully**, also explain the boundary of the recommendation, the assumption being carried, the decision it affects, and how the design reduces the consequence of that assumption being wrong.

## 6. Describe the experience architecture

For the recommended direction, define:

- entry points and triggers;
- stages in the journey;
- decisions and information required at each stage;
- system behavior and feedback;
- alternate, error, and recovery paths;
- completion and post-completion experience;
- ongoing states when relevant;
- dependencies and unresolved questions.

Route to `user-understanding.md` before finalizing the order of information and decisions.

## 7. Choose interaction surfaces intentionally

Classify each important interaction as a page, bottom sheet, inline disclosure, dialog, or system feedback.

- **Page:** a distinct destination, sustained task, or deep information space.
- **Bottom sheet:** a temporary contextual task that preserves the parent context and can be dismissed without losing progress.
- **Inline disclosure:** supporting information or a lightweight choice that belongs directly within the current content.
- **Dialog:** a focused interruption that requires immediate acknowledgement or a bounded decision.
- **System feedback:** a status or result communicated without creating a new task surface.

Decide using:

- continuity with the current context;
- depth and duration of the task;
- amount of information required;
- decision weight and consequence;
- reversibility and interruption;
- need to compare with the parent content;
- navigation expectations;
- accessibility and device constraints.

Do not use a bottom sheet as a default for every secondary action. Do not create a new page merely because a state needs to be shown.

## 8. Narrate the recommendation

Explain the recommendation in design language:

1. The user's need at the moment.
2. The experience principle guiding the decision.
3. What the product does.
4. What the user understands and controls.
5. Why the sequence and hierarchy work.
6. What is deliberately deferred, removed, or left manual.
7. The trade-off being accepted.

## Output structure

```markdown
## Recommended Direction

**Response mode**
...

**Design problem**
...

**Basis and limits**
...

**Product role**
...

**Journey scope**
...

**Directions considered**
| Direction | User fit | Product fit | Control and trust | Complexity | Main trade-off |
| --- | --- | --- | --- | --- | --- |
| ... | ... | ... | ... | ... | ... |

**Chosen direction and rationale**
...

**Experience architecture**
- Before:
- During:
- Immediately after:
- Over time:

**Important surface decisions**
- ...

**Edge and recovery paths**
- ...

**Trade-offs and dependencies**
- ...

**Open questions**
- ...

**Recommended next level of detail**
...

**UI handoff boundary**
- Decisions resolved by this UX direction:
- Decisions left for UI design:
- Questions left for product, policy, operations, or engineering:
```

## Quality check

- The recommendation follows from the user story and design problem.
- The main workflow's understanding and consequence gate was passed before a recommendation was made.
- The response mode matches the available support and the consequence of being wrong.
- The product role and degree of user control are explicit.
- The chosen direction was compared with meaningfully different alternatives.
- The solution covers the relevant time horizon.
- The experience uses product capabilities without hiding uncertainty or limitations.
- Information, actions, and surfaces have a reason tied to the user's stage.
- Risks and trade-offs are concrete.
- Unverified explanations remain assumptions or hypotheses rather than causal claims.
- **Learn first** did not produce a final recommendation or design artifact.
- The recommendation stops before final UI, product requirements, and engineering specifications.
- Dependencies are surfaced as questions rather than completed on behalf of another function.
- The narration explains the reasoning instead of presenting screens as the solution.
