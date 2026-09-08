---
name: user-story
description: Build a narrated, editable account of the user's context, behavior, difficulty, and desired progress before defining the experience.
---

# User Story

## Purpose

A user story is the working narrative that connects context to design. It explains how a person reaches the experience, what they are trying to do, what they do today, where they become stuck, and what would help them progress.

Treat it as an editable design hypothesis, not permission to fill a vague prompt with a plausible narrative.

## Entry condition

Build the story only after the main workflow selects **Move forward** or **Move carefully**. The central sequence needs enough support to identify:

- the relevant user and situation;
- what they are trying to achieve;
- what they currently do;
- where progress breaks down.

New research is not required when supplied material or established product understanding supports this sequence. The absence of a research document is not the absence of user understanding.

Select **Learn first** instead when most of the central sequence would be assumed, several plausible stories would lead to different solutions, or the assumptions would carry meaningful consequence. Return the gaps to the main workflow rather than creating the story.

## Build the narrative

Cover the parts that materially affect the design:

1. **Situation:** What is happening around the user when the need appears?
2. **Trigger:** What causes them to enter the product or journey now?
3. **Goal:** What outcome are they trying to reach in their own terms?
4. **Current behavior:** How do they handle the need today, inside or outside the product?
5. **Breakdown:** Where does progress slow, stop, or become uncertain?
6. **Understanding:** What do they already know, and what are they trying to make sense of?
7. **Emotional context:** What creates urgency, hesitation, effort, or loss of confidence?
8. **Desired progress:** What would make them feel able to continue?
9. **Afterward:** What do they expect to happen once the immediate task is complete?

Do not add personal details that do not affect the design. Do not turn demographic assumptions into motivations or behaviors. If emotional context is unknown, omit it rather than adding a plausible feeling.

## Separate confidence levels

Mark the basis of the story using the same language as the main workflow:

- **Provided:** supplied directly by the user or source material.
- **Observed:** visible in an artifact, flow, behavior, or data.
- **Inferred:** an interpretation supported by what is provided or observed; say that the material suggests it.
- **Assumed:** needed to move carefully without support; state what design decision would change if it is wrong.
- **Unknown:** not answered by the available material.
- **Hypothesis:** a possible explanation to examine, not part of the story as fact.

Do not use phrases such as “users want,” “users are confused,” or “the reason is” unless the available support justifies the claim.

## Present it for correction

Write the story as a short connected narration, followed by the assumptions and gaps. Explicitly invite the user to correct what is inaccurate, remove what does not belong, and add missing context.

Do not require confirmation when the story is sufficient for responsible progress. Continue with clearly marked assumptions in **Move carefully** unless a missing answer could change the problem, product role, journey architecture, or safety of the direction.

A correction invitation is not a substitute for asking a blocking question. Do not create a mostly assumed story and rely on the user to repair it later.

## Correction loop

When the user changes the story:

1. Incorporate the correction without defending the earlier inference.
2. Restate only the changed part and the revised complete meaning.
3. Identify affected design decisions.
4. Update the problem framing, solution direction, flow, or hierarchy where necessary.
5. Preserve unaffected work.
6. Keep unresolved assumptions visible.

The story remains editable throughout the design process. Later design decisions may reveal a missing or contradictory part of the narrative; return to it when needed.

## Output structure

```markdown
## Working User Story

**Narrative**
...

**What is provided or observed**
- ...

**What is inferred**
- ...

**What is assumed**
- ...

**What is unknown or still a hypothesis**
- ...

**Design consequence**
...

**Correction invitation**
...
```

## Quality check

- The narrative starts in the user's context, not on a product screen.
- The entry condition was met before the story was created.
- The user has a clear goal and a believable reason to act.
- The breakdown is specific enough to design for.
- Emotional context is connected to behavior rather than added for tone.
- The desired progress is expressed as a user outcome, not a feature.
- Assumptions are easy for the user to find and correct.
- Central user context is not carried mainly by assumptions.
- Claims are worded according to their level of support.
- The story supports the problem framing and solution without predetermining them.
