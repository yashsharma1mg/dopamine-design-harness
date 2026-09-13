# Stage 1 · Research branch

Reachable only from a **Stop for research first** decision at branch point 1,
and only when the user asks for research help. Guide the research; never
invent findings or present assumptions as participant feedback.

---


## What this step is for

Use research to answer an uncertainty that materially affects a design decision. This may happen before a direction can be chosen or when an existing direction needs validation. Keep the work proportionate to the consequence of being wrong.

Research is not a required ceremony. Existing flows, artifacts, product knowledge, analytics, previous research, complaints, operational knowledge, constraints, or direct observation may already provide enough user understanding.

## Decide whether research is needed

Do not recommend new research when:

- the relevant user, situation, behavior, and breakdown are sufficiently understood;
- the issue is observable and bounded;
- the decision does not depend on an unknown motivation or cause;
- the consequence is limited and the choice is easy to change or recover from;
- additional research would not change the direction.

Recommend learning first when:

- core user context or current behavior is unknown;
- several plausible causes would lead to different product roles, journeys, or solutions;
- the decision depends on unsupported beliefs about motivation, comprehension, or behavior;
- the decision has meaningful consequences for control, trust, privacy, policy, safety, access, or money;
- existing material and responsible owners cannot answer the blocking question.

This distinction follows the main workflow:

- **Research not needed:** no new research is needed for the current decision.
- **Move ahead with assumptions:** continue within a supported, reversible scope and identify what should be checked later.
- **Stop for research first:** answer the blocking question before recommending the solution.

## Offer a research guide

When the user asks for research help and the available understanding is insufficient, first explain:

- what is already understood;
- what still needs to be learned;
- why those gaps could change the design direction;
- how a focused research guide could help.

Structure this explanation using bold section titles so it is easy to scan:

- **What we know**
- **What is missing**
- **Why research is needed**
- **What we need to learn**
- **Suggested research approach**
- **What I can do next**

Then ask whether the user wants the guide. Do not create it automatically merely because research may be useful.

The offer should be direct:

> I can create a research guide covering what the research needs to uncover, the assumptions to examine, suitable participants and methods, session questions or tasks, what to observe, how to organise the findings, and which design decisions the findings should inform. Would you like me to create it?

When the next step needs user approval, introduce it with the exact heading: **Shall I proceed with**

If the user agrees, ask only for setup information that materially affects the guide:

1. the product or design decision the research should inform;
2. the users, customers, staff, records, or existing material the team can access;
3. research, complaints, behavioral information, or operational knowledge already available;
4. time, access, privacy, policy, or operational constraints.

If an answer is unavailable, mark it as an assumption and keep the guide within that limit.

## Recommend the smallest useful learning activity

In **Stop for research first**, do not automatically create a full research plan. First return:

```markdown
## Lightweight Learning Recommendation

**Question to answer**
...

**Why it changes the design**
...

**Lightest suitable method**
...

**Who or what to learn from**
...

**Decision this unlocks**
...
```

Create the full plan below only when the user asks for research planning or when that level of detail is the requested output.

## Research guide output

When the user accepts the offer, return:

```markdown
# Research Guide

## Decision the Research Will Support
...

## Current Understanding
...

## What We Still Need to Learn
...

## Assumptions to Examine
...

## Recommended Participants or Sources
...

## Recommended Method
...

## Session Structure
...

## Interview Questions or Tasks
...

## What to Observe
...

## How to Organise the Findings
...

## How Findings Will Affect the Design
...

## Open Questions and Constraints
...
```

## What the output looks like

```markdown
# Research Plan

## Research Objective
...

## Key Questions
- ...

## Hypotheses
- ...

## Participants
...

## Method
...

## Tasks or Stimuli
- ...

## What to Observe
- ...

## Success Signals
- ...

## Risks
- ...

## Timeline
...

## Output
...
```

## Picking the right method

- **Existing-material review** when prior research, support conversations, complaints, product decisions, or operational knowledge may already answer the question.
- **Analytics review** when behavioral data can locate or compare what happens in the journey.
- **Interviews or observation** when the decision depends on context, current behavior, motivation, or mental models.
- **Concept or comprehension study** when the team needs to understand how people interpret a proposed direction or consequential information.
- **Usability study** when the question is whether people can understand and complete a screen or flow.
- **Survey** only when the question is narrow, the response options are already understood, and scale is necessary.

## Ground rules

- Tie the plan to the product decision it needs to inform. Research without a decision to feed is just curiosity.
- Do not treat the lack of a new study as a lack of user understanding.
- Do not over-research low-consequence, reversible changes.
- Increase the strength of support as consequence and irreversibility increase.
- Keep observations, inferences, assumptions, unknowns, and hypotheses separate in the plan and its findings.
- Do not use research to delay a decision that existing understanding already supports.
- Do not invent participant feedback, findings, quotes, patterns, or validation.
- Do not imply that planning research is the same as conducting it.
- The guide may help the user run and organise research, but the agent does not claim to recruit or interview participants itself.

## Completion check

- The research need is tied to a material design decision.
- Existing sources were considered before proposing new work.
- The method is the lightest one capable of answering the question responsibly.
- The scope reflects the consequence of being wrong.
- The expected result can change or confirm a specific design decision.
- A full plan was not produced when a lightweight recommendation was sufficient.
- A research guide was created only after the user accepted the offer or explicitly requested one.
- The output plans learning without fabricating findings.

---


## What this step is for

Use this reference after the user explicitly requests a script or accepts the offer to create a research guide. Write the questions, tasks, and moderator notes that help the user or research team run the session. A good script feels like a natural conversation, not an interrogation.

Before writing, confirm the decision the research should inform, who or what the team can learn from, what is already known, and which constraints affect the session. Ask only for missing information that would materially change the script.

## What the output looks like

```markdown
# Research Script

## Session Goal
...

## Moderator Intro
...

## Warm-Up Questions
1. ...
2. ...

## Context Questions
1. ...
2. ...

## Task Prompts
1. ...
2. ...

## Follow-Up Questions
1. ...
2. ...

## Comprehension Checks
1. ...
2. ...

## Closing Questions
1. ...
2. ...

## Notes for Moderator
- ...
```

## Ground rules

- Don't lead the witness. Ask open questions that don't hint at the "right" answer.
- Ask about past behavior before asking for opinions.
- Keep tasks realistic. Frame them the way the user would actually encounter them, not how the product team thinks about them.
- Don't explain the UI before asking someone to use it. That defeats the purpose.
- When reviewing flow clarity, ask participants to identify their next action without prompting them toward it.
- Treat the script as a guide for the user or research team to conduct; do not imply that the agent has recruited or interviewed participants.
- Never add invented findings, quotes, expected answers, or claims of validation to the script or its follow-up.
