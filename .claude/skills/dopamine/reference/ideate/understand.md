# Stage 1 · Phases 1–2 — Understand, map, and decide whether to research

Four jobs in order: understand the ask, map the context, take **branch point 1**
(do we know enough to solve this?), and read the signals. Branch point 1 governs
everything downstream — it must appear in the response, never be taken silently.

## 1. Understand the problem

Inspect all material the user provided before interpreting it. If the input is a
board, screenshot, brief, or PRD, `read-input.md` runs first.

At this step, identify only:

- what is going wrong right now;
- what should improve;
- what kind of design help is being asked for;
- what is clearly stated versus still vague.

Do not solve, narrate, or explain causes yet. The job is to understand the ask,
not to interpret it fully.

## 2. Map the context

Build the surrounding context map:

- **User:** situation, goal, prior understanding, current behavior, hesitation, capability constraints.
- **Product:** where the experience lives, the current journey, existing information, capabilities, dependencies, and product intent.
- **Constraints:** business, policy, legal, technical, operational, content, accessibility, and time constraints.
- **Journey boundary:** what happens before the experience, during it, immediately after it, and later if the relationship continues.
- **Evidence available:** flows, screens, research, complaints, data, operational knowledge, prior learnings.

This product is mobile-first at 360px and healthcare-regulated. Clinical
consequence, regulatory constraint, and accessibility are first-class entries in
the constraint list, not footnotes.

### Label every important statement

- **Provided** — supplied directly by the user or source material.
- **Observed** — visible in an artifact, flow, behavior, or data.
- **Inferred** — an interpretation supported by what is provided or observed.
- **Assumed** — needed to move forward without support; say what changes if it is wrong.
- **Unknown** — not answered by the available material.
- **Hypothesis** — a possible explanation that still needs examining.

Match the wording to the support: the material **shows** what was provided or
observed, and **suggests** an inference. An unsupported explanation is named an
assumption or a hypothesis. Say what is unknown when the cause is not
established. Do not write "users want", "users are confused", or "the reason is"
unless the support justifies it.

### Summarise context sufficiency

For a meaningful redesign, summarise before continuing: user, goal, journey
boundary, evidence, constraints, consequence of being wrong, assumptions, and
unknowns. Keep it brief, but do not omit a category silently.

If core context is missing in a way that could change the framing, the journey
in scope, or the class of solution, pause here and ask — do not wait until after
solutioning starts. Use the exact heading:

**Answer me few questions**

---

## 3. Branch point 1 — Do we know enough to solve this?

**This checkpoint must be visible in the response** before framing, user story,
solution directions, flows, or wireframes. Never decide it silently.

Ask:

- Do we know who the relevant user is and what they are trying to achieve?
- Do we know where progress breaks down?
- Do we know why, or does the direction depend on knowing why?
- Is the current support strong enough to move responsibly?
- How risky is it to be wrong here?

### The three branches

- **Research not needed** — continue to step 4.
- **Stop for research first** — research is needed and it blocks the direction. Guide the research and stop deeper solutioning.
- **Move ahead with assumptions** — research is still needed, but the user explicitly wants progress in parallel. Keep assumptions visible and limit the work to reversible decisions.

### Before leaving this step, the response must

- state which branch was chosen;
- explain why that branch fits this problem;
- say whether targeted questions are still needed before proceeding;
- if moving ahead, say what is stable enough to use now and what remains assumption-led.

Use plain designer language:

- *We don't need fresh research for the first pass because…*
- *We can move ahead, but only with assumptions, because…*
- *We shouldn't solve yet because we still need to learn…*

Never jump from a vague problem statement straight into user story, framing,
direction, or wireframing without showing this decision. If the problem is still
too vague, ask the targeted questions here under **Answer me few questions**
rather than pretending the branch is already clear.

**Raise the bar in this product.** Dosage, drug identity, allergens, lab-result
interpretation, prescription matching, and payment are high-consequence and hard
to reverse. An assumption that would pass on a browse surface does not pass here.

### The research branch

When research is needed:

1. Name what is unclear.
2. Explain why it matters.
3. Define what must be learned.
4. Choose the lightest suitable method.
5. Guide the research if the user wants help — load `research.md` only then.
6. Wait for the learning to come back.
7. Re-enter the workflow at the most relevant phase.

Offer guidance; never invent findings.

---

## 4. Read the signals

Interpret only the evidence already available. Pull out repeated breakdowns,
strong versus weak signals, contradictions, and likely design implications.

Do not invent new evidence. Do not overstate unsupported causes. When moving
into framing, briefly say what feels stable enough to use now.

---

## 5. Understand the user situation

Run this only after the branch is **Research not needed** or **Move ahead with
assumptions**, and only once the workflow has enough support to continue
responsibly.



### Purpose

This step builds the working user story for design. It connects the user's context to the problem so the solution is grounded in an actual situation, not only in a business symptom or screen issue.

Treat the story as an editable design hypothesis, not a fact and not a performance of empathy.

### When to use this step

Use this reference only when the workflow has enough support to continue into user understanding.

Do not build the story when:

- the relevant user is still unclear;
- the point of breakdown is still unclear;
- most of the narrative would be guessed;
- different plausible stories would lead to different directions;
- research is still blocking the core decision.

In that case, return to the research branch instead of writing a confident-sounding story.

### What this step is allowed to do

This step may define:

- the user's situation when the need appears;
- what triggers the journey;
- what the user is trying to achieve;
- what they currently do;
- where progress slows, stops, or becomes uncertain;
- what they already know or do not know;
- what creates urgency, hesitation, mistrust, or effort;
- what progress would mean to them;
- what they expect after the immediate task is complete.

This step must not:

- invent motivations without support;
- turn demographic assumptions into behavior;
- add emotional detail only for tone;
- solve the problem inside the story;
- present unsupported claims as truth.

### Build the story

Cover only the parts that materially affect the design:

1. **Situation:** what is happening around the user when this need appears?
2. **Trigger:** why are they entering the journey now?
3. **Goal:** what are they trying to achieve in their own terms?
4. **Current behavior:** how do they handle this today, inside or outside the product?
5. **Breakdown:** where does progress slow, stop, or become uncertain?
6. **Understanding:** what do they know, and what are they trying to make sense of?
7. **Decision pressure:** what creates urgency, hesitation, mistrust, or effort?
8. **Desired progress:** what would make them feel able to continue?
9. **Afterward:** what do they expect once the immediate task is complete?

If emotional context is unknown, omit it rather than adding a plausible feeling.

### Separate confidence levels

Mark the basis of the story using the same language as the main workflow:

- **Provided:** supplied directly by the user or source material.
- **Observed:** visible in an artifact, flow, behavior, or data.
- **Inferred:** supported interpretation of what is provided or observed.
- **Assumed:** needed for provisional or careful progress; state what decision would change if it is wrong.
- **Unknown:** not answered by the current material.
- **Hypothesis:** a possible explanation to examine, not a story fact.

Do not use phrases such as "users want," "users are confused," or "the reason is" unless the support justifies them.

### Present it for correction

Write the story as a short connected narration, then separate:

- what is solid;
- what is inferred;
- what is assumed;
- what is still unknown.

Invite correction directly. The user should be able to remove, correct, or add context without having to undo the whole work.

When the user explicitly asks for the user story, user situation, or narrative as the deliverable, stop after producing this output. Do not continue into solution direction, flow design, hierarchy, or wireframes unless the user explicitly asks for the next step.

Do not ask for confirmation when the story is already sufficient for responsible progress. Continue with clearly marked assumptions unless the gap would change the framing, direction, or safety of the design.

### What to do when the story is challenged

If the user disagrees with the story:

1. update the changed part without defending the earlier version;
2. restate the revised meaning;
3. identify which design decisions are affected;
4. update only those parts of the work;
5. preserve what still holds.

The user story remains editable throughout the workflow.

### Output structure

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

**Why this matters for the design**
...

**Correction invitation**
...
```

### Quality check

- The story starts in the user's context, not on a product screen.
- The user has a clear goal and believable reason to act.
- The breakdown is specific enough to design for.
- Decision pressure is tied to the behavior, not added for drama.
- Desired progress is expressed as a user outcome, not a feature.
- Assumptions are easy to find and correct.
- Central parts of the story are not carried mainly by assumptions.
- The story supports the framing and solution without predetermining them.
