---
name: modes
description: Evidence tagging and response-mode selection. Loaded first in Stage 1, before any other UX reference.
---

# Evidence and Mode

Absorbed from the senior-designer skill. This replaces flat interrogation.
Load this before any other file in `reference/ux/`.

## Invocation is consent

The user ran `/dopamine ideate`. That is an explicit request for Stage 1
output. Do not re-ask permission to produce a brief, a direction, a flow,
or a wireframe — the stage gates in this harness already handle approval.

The only thing you still stop for is the two **stage gates** in
`ideate.md` (direction sign-off, wireframe sign-off).

## Tag every material statement

Mark each statement in the context map as one of:

| Tag | Meaning |
| --- | --- |
| Provided | Supplied directly by the user or source material |
| Observed | Visible in an artifact, flow, behaviour, or data |
| Inferred | An interpretation the material supports — phrase it as suggestion |
| Assumed | Needed to move forward without support — state what changes if wrong |
| Unknown | Not answered by available material |
| Hypothesis | A possible explanation still to be examined |

Untagged assertion is the failure mode. A brief that reads as fact but
is 60% assumption produces a wireframe nobody can argue with and everybody
disagrees with later.

## Build the context map

Cover these. Tag each line.

- **Problem** — current behaviour, point of difficulty, consequence, desired change.
- **User** — situation, goal, prior understanding, behaviour, motivation, hesitation, capability constraints.
- **Product** — where it lives in the IA, existing journey, available information, capabilities, dependencies, product intent.
- **Constraints** — business, policy, legal, technical, operational, content, accessibility, time.
- **Journey boundary** — before, during, immediately after, and later if the relationship continues.

The eight dimensions from the previous version of this stage are now a
completeness checklist for the map above, not a script: surface identity,
user and context, goal and success, content inventory, entry and exit,
priority hierarchy, states and edges, existing patterns.

## Choose a mode

Before asking anything, decide whether the answer could change a material
design decision. Question count is not rigor.

**Move forward** — user and breakdown are understood, the decision is
bounded, existing support is sufficient. Produce the reasoning and the
output. State material assumptions. Do not request research that would
not change the direction.

**Move carefully** — the main direction is stable but a gap affects detail
or confidence. Produce only the supported scope, keep important choices
reversible, name the assumption and the decision it affects, identify what
to check later.

**Learn first** — core user context or cause is unknown, plausible answers
lead to different directions, or the consequence requires stronger support.
State what is known and missing, explain why it matters, ask 2–4 focused
questions, and **stop**. Do not produce a user story, problem articulation,
solution direction, flow, or wireframe in this mode.

Require stronger support as consequence, irreversibility, autonomy, trust,
privacy, policy, or safety increases. On a pharmacy surface, dosage,
allergy, payment, prescription upload, and substitution are high-consequence
by default — assume Move carefully at minimum unless told otherwise.

## Asking rules

- Ask only questions whose answers could change framing, direction, flow,
  hierarchy, or safety.
- Batch 2–4, by theme. Explain which decision depends on each answer.
- Propose, don't just ask. State your assumption and invite correction.
- Name the gap precisely when an answer is vague.
- Name conflicts explicitly and make the user pick a priority.
- Do not repeat information already supplied. Do not ask preference
  questions that belong to Stage 2 or Stage 3.

New research is not required when the issue is clear, bounded, supported
by existing understanding, and the decision does not depend on an unknown
cause. Absence of new research is not absence of user understanding.

If a blocking question cannot be answered from existing material, name the
smallest useful learning activity — the question, the lightest method, who
to examine, and the decision it unlocks. Load `research-plan.md` and
`research-script.md` only if the user asks for a guide.
