# Dopamine 2.0 — AI Design Harness

An agent harness for designing mobile interfaces through the [Dopamine 2.0](https://dopamine2-0.dopamine-ds.workers.dev/) design system. Built for Claude.

Dopamine 2.0 is the internal design system for [1mg](https://www.1mg.com), a health and pharmacy product. The harness enforces a governed three-stage design workflow where each stage has an entry gate, a defined protocol, and a handoff artifact.

## The three stages

```
ideate ──→ compose ──→ polish
  │            │           │
  ▼            ▼           ▼
PRODUCT.md     Surface    DESIGN_DECISIONS.md
WIREFRAME.md   (real       (approved departures
wireframes/     components   + hard floor
 *.html         + tokens)    confirmation)
```

**Stage 1 — Ideate.** A main path with **two visible branch points**. The agent reads whatever was supplied — a prompt, a Figma or FigJam board, a screenshot, a product brief or PRD — and builds a context map with every statement labelled (provided / observed / inferred / assumed / unknown / hypothesis).

**Branch point 1 — do we know enough to solve this?** Three answers: *Research not needed*, *Move ahead with assumptions*, or *Stop for research first*. The decision must appear in the response with its reasoning; it is never taken silently. `Stop for research first` halts the stage outright — no story, framing, direction, brief, or wireframe until the gap closes.

Past that gate it reads the signals, frames the design mismatch, builds an editable user story, and explores materially different directions — naming the product role (Explain / Guide / Recommend / Act) and whether the centre of gravity is prevention, support at the point of difficulty, or recovery. **Branch point 2 — do we agree on the direction?** On disagreement it diagnoses *what* failed before generating more options, and steps back only as far as needed.

Then it shapes the journey, stress-tests it against the interface principles, plans content and hierarchy, and consolidates everything into a brief the user signs off. Only then — and only with explicit permission — does it build an interactive grayscale wireframe at 360×800. No Dopamine components, no tokens, no brand colour. Outputs: `PRODUCT.md`, `WIREFRAME.md`, `wireframes/<surface>.html`.

Throughout, `effort-and-speed.md` is the brake: use the smallest amount of work that makes the current decision well, and don't treat process depth, source count, or state count as signs of quality.

**Stage 2 — Compose.** Six phases against the live Dopamine MCP, starting with a question the protocol used to skip: **where is this being built?** `@dopamine2.0/ui` is a private React package (ESM, React 18+) that ships as a tarball, so Phase 0 confirms a host project, installs the package, wires the stylesheet once at the app root, and drops `AGENTS.md` from `get_agent_rules` so any other agent in that repo builds against the same contract. With no host project, the agent says so and offers three routes rather than quietly producing an HTML file that looks composed. The wireframe's component candidates are treated as a hypothesis, not a decision — every zone is re-resolved with `search_components` and `get_component_docs`, and composed patterns are checked first since a pattern beats assembling its parts. Every value resolves through the three-layer token hierarchy (base → semantic → component), including the Stage 1 type *roles*, which become real `--font-size-*` tokens here. Props come from the actual TypeScript contracts: inventing a prop or a union value is a defect, not a shortcut, and a zone that maps to no component is named as a system gap rather than approximated with CSS overrides. Phase 2b restores what the grayscale wireframe deliberately dropped, reading the Stage 1 `## Source language` record row by row — a gradient comes back as a gradient, a status hue as that hue, per-meaning icon tints as tints. The accessibility guidelines run in full as the gate to Stage 3.

**The deliverable is TSX importing real `@dopamine2.0/ui` components.** Hand-writing a CSS class that emulates a component is banned outright — it is a drawing of a component that drifts the moment either changes. HTML review artifacts are assembled from `preview_component` / `preview_pattern`, which return the real component's own markup. A standalone hand-written HTML file is labelled a **MOCK**, may not claim component or token fidelity, and Stage 3 refuses to polish it.

**Stage 3 — Polish.** The agent audits the composed surface for visual hierarchy, rhythm, brand presence, and signature opportunities, then proposes 3–7 specific departures from the design system grouped by risk level. The user approves each departure individually before it is applied. Accessibility constraints are a hard floor — never candidates for departure. Output: `DESIGN_DECISIONS.md`.

Stages are sequential. Each has an entry gate checked by the skill. You cannot skip to polish without a composed surface, and you cannot compose without an approved wireframe.

## Repository structure

```
.
├── README.md                                          ← you are here
├── CLAUDE.md                                          ← project-level instructions (auto-read by Claude)
└── .claude/
    └── skills/
        └── dopamine/
            ├── SKILL.md                               ← entry point, cross-stage router, system knowledge
            └── reference/
                ├── ideate.md                          ← Stage 1 router: phases, branch points, brief
                ├── ideate/
                │   ├── read-input.md                  ← Phase 0 — board, screenshot, brief, PRD
                │   ├── understand.md                  ← Phases 1-2, 4 — context map, evidence labels,
                │   │                                     branch point 1, user story
                │   ├── research.md                    ← research branch (Stop for research first only)
                │   ├── competitive-research.md        ← Phase 2b — bounded pattern scan (default: skip)
                │   ├── frame.md                       ← Phase 3 — the design mismatch
                │   ├── explore.md                     ← Phase 5 — product role, directions, surfaces
                │   ├── review-direction.md            ← branch point 2 — diagnose, step back
                │   ├── comprehend.md                  ← Phases 6-7 — user understanding map
                │   ├── wireframe.md                   ← Phase 8 — interactive grayscale wireframe
                │   └── wireframe-preflight.md         ← readiness gate before construction
                ├── interface-principles.md            ← 6 principles + 5 laws (Stages 1 and 3)
                ├── effort-and-speed.md                ← proportionality brake (always loaded)
                ├── content-design.md                  ← interface copy (Stages 1 and 2)
                ├── compose.md                         ← Stage 2 protocol (complete)
                ├── accessibility.md                   ← WCAG/IS 17802/RPwD constraints (complete)
                └── polish.md                          ← Stage 3 protocol (complete)
```

Stage 1's protocol is adapted from the `senior-designer-next` skill on the [`codex/senior-designer-next-skill-only`](https://github.com/Akshaymehta1mg/Design-skills/tree/codex/senior-designer-next-skill-only) branch of Design-skills, reconciled against Dopamine 2.0 — where the two disagreed, the design system won.

## File reference

### `CLAUDE.md`
Project-level instructions that Claude reads automatically at the start of every session. Points to the skill, summarises the three stages, and lists the project files the workflow produces (`PRODUCT.md`, `WIREFRAME.md`, `DESIGN_DECISIONS.md`).

### `SKILL.md`
The skill entry point. Contains:
- **Frontmatter** — name, keyword-rich description for auto-triggering, argument hints, allowed tools.
- **Setup protocol** — mandatory steps that run before any stage: read project context, load the stage reference file, familiarise with the codebase, check entry gates.
- **System knowledge** — compressed Dopamine 2.0 reference: three-layer token architecture, key constraints (360px viewport, 4px spacing rhythm, typography roles, radii, brand colour), the full 35-component library, and critical accessibility constraints.
- **Command router** — maps `ideate`, `compose`, and `polish` to their reference files with routing rules for exact match, fuzzy intent, and no-argument recommendations.

### `reference/ideate.md`
**Status: Complete**

The Stage 1 router. Holds the entry gate, how the agent should work, the consent gate, the response-format rules, the workflow control record, the phase table with both branch points, the brief format, the handoff, and the completion check. The phases live in `reference/ideate/`.

Three rules do most of the work. **The consent gate:** no artifact — brief, flow, research guide, wireframe — gets produced unless the user asked for it or accepted it when offered. Having enough context is not permission, and approval to build a wireframe confirms the artifact, not the direction. **The branch decisions must be visible**, both of them, with their reasoning. **The workflow control record** keeps context sufficiency, the decisions taken, and the coverage mapping on the record; a gate may be skipped only when its outcome cannot change the decision *and* the response says why.

It also resolves a contradiction inherited from the source skill, where the orchestrator said competitive research should default to *Run* for healthcare while `competitive-research.md` and `effort-and-speed.md` both said healthcare is explicitly not enough. Skip-by-default wins.

### `reference/effort-and-speed.md`
**Status: Complete**

Always loaded by Stage 1. The brake on process for its own sake: use the smallest amount of work needed to make the current decision well, produce the recommendation before expanding into artifacts, load only the references the current decision needs, and stop when more work is unlikely to change the answer. Successful internal checks stay invisible — only blockers, material assumptions, and real trade-offs get explained.

It sets two hard budgets: competitive research gets one focused search pass and at most three primary sources, and the wireframe defaults to one primary screen with no more than four essential alternate, error, or recovery states.

### `reference/interface-principles.md`
**Status: Complete**

The design-conviction layer, and the one file in the imported skill that was already written for Dopamine 2.0 and 1mg. Three layers running top-down — **principles** (what kind of experience is right), **laws** (how the experience should be designed), **visual** (how the UI gets built) — under one overriding bias:

> **Clarity and safety always beat delight.**

1mg is not a marketplace. A confused user in a healthcare space can take the wrong medicine, misread a result, miss a warning, or skip a critical preparation step. So the six principles are ranked, and higher-ranked ones win ties: **trust through explainability**, **calm over alarm**, **context aware**, **answer first**, **progressively disclose**, **participation creates ownership**. Each carries an evaluation question and a we-do/we-don't table.

The five laws translate those into design rules, each a summation of established heuristics: make the next action obvious (Fitts, Hick, Von Restorff), assume the user will make mistakes (Postel, Nielsen error prevention), consistency over creativity (Jakob, mental models), don't burden the user cognitively (Miller, Tesler), and aesthetically pleasing designs work better (aesthetic-usability, Doherty).

This layer spans stages: compulsory in Stage 1 before the structure is final and again before the wireframe, and it supplies the vocabulary for the Stage 3 polish audit — Law 5 is what "does this feel like 1mg" means concretely, and the overriding bias is the same conviction `polish.md` calls the hard floor.

### `reference/ideate/understand.md`
**Status: Complete**

Phases 1–2 and 4, and the home of branch point 1. Builds the context map (user, product, constraints, journey boundary, evidence available), labels every statement **provided / observed / inferred / assumed / unknown / hypothesis** with matching wording discipline — the material *shows* what was observed and *suggests* an inference — then summarises context sufficiency before going further.

**Branch point 1** asks whether we know who the user is, where progress breaks down, whether the direction depends on knowing *why*, and how risky it is to be wrong. The response must state which branch was chosen, why it fits, whether questions are still needed, and what remains assumption-led. The bar rises with consequence: dosage, drug identity, allergens, lab-result interpretation, prescription matching, and payment are hard to reverse, so an assumption that would pass on a browse surface fails here.

Ends with the editable user story — a design hypothesis, not a performance of empathy. It refuses to build the story at all when the user is unclear, the breakdown is unlocated, or most of the narrative would be guessed. Corrections update it, name which decisions are affected, and preserve what still holds rather than restarting.

### `reference/ideate/frame.md`
**Status: Complete**

Phase 3. Separates the **stated concern** (as the brief or ticket put it) from the **user experience** (how the person actually encounters it) from the **design mismatch** — the gap between what the product currently expects or communicates and what the user needs to understand, decide, or accomplish. The mismatch guides solution choices without being the solution. When the cause is unknown, the articulation stays at the observable level rather than inventing a motive, and the output separates the basis for the framing from what it does not yet claim.

### `reference/ideate/competitive-research.md`
**Status: Complete**

Phase 2b, and **skipped by default**. Runs only when the user asks or a *named* unknown could realistically change the interaction, hierarchy, recovery, or direction — healthcare, trust, category familiarity, or the mere existence of competitors is explicitly not enough.

When it does run it is a bounded pattern read for one moment, not a market study: one focused search pass, at most three primary sources, Mobbin MCP preferred where available. It compares through three lenses — IA, information hierarchy, and UI pattern — and extracts what is category-standard, what is helpful, what is risky, and where the whitespace is. The rule that keeps it honest: the recommendation comes first from the user, context, constraints, and product logic; competitor patterns validate, challenge, or refine that view but never become the main structure of the answer.

### `reference/ideate/explore.md`
**Status: Complete**

Phase 5. Sets the decision frame, then chooses the **product role** at each important moment — Explain, Guide, Recommend, or Act — with less autonomy wherever confidence, permission, reversibility, or consequence is weak. Picks a **journey scope** (one-time task, repeated workflow, ongoing relationship) and maps before / during / immediately after / over time.

Explores 2–4 directions that differ in behaviour, product role, or recovery model — not layout — using prevention, support at the point of difficulty, and recovery as lenses with one named as the centre of gravity. Where all three are plausible it compares them explicitly *before* combining, so a hybrid isn't chosen just because it sounds comprehensive. Compares on eight axes, recommends one, and splits the recommendation into **stable now**, **provisional now**, and **must be revisited**.

Its stage boundary defers rather than refuses — component selection is Stage 2's, deliberate departures are Stage 3's, and PRDs and engineering deliverables go back to their owners as questions.

### `reference/ideate/review-direction.md`
**Status: Complete**

Branch point 2. Not a vote on preference — a diagnosis step. When a direction is rejected or feels weak, the job is to work out *what* failed: the framing, the user story, directions that are too similar, a right direction explained badly, a structure problem rather than a direction problem, or an artifact too weak to defend a sound idea.

Then step back the smallest useful distance — to framing, to the user situation, to competitive research, to exploring directions, to shaping the experience, or just to iterating the artifact. Responding to disagreement by generating more options without understanding what failed is the specific failure this file exists to prevent.

### `reference/ideate/comprehend.md`
**Status: Complete**

Phases 6–7. Maps the experience as a sequence of changes in the user's understanding, not screens: for each stage, what they *arrive thinking*, what they *see*, what they *should understand*, what they *decide or do*, what *supports* that decision, what *concern remains*, what they *expect next*, and how the *product responds*. Classifies information as primary, supporting, conditional, reference, deferred, or removed — visual prominence follows the user's decision priority, not the product's internal importance. Then flags breaks: a decision requested before its meaning is clear, an explanation arriving after it was needed, a concern still unresolved at the point of commitment.

### `reference/ideate/wireframe.md`
**Status: Complete**

Phase 8, and only on explicit permission. Locks solution coverage first — every agreed stage, outcome, explanation, action, branch, and recovery path mapped to a screen, surface, or state and marked *mapped*, *deferred with reason*, or *unresolved*, so nothing is dropped silently. Then plans each stage across ten fields, builds the information hierarchy, and chooses the surface.

**Source inspection is a mandatory gate, and its output is an artifact.** When screenshots, screens, or a flow are supplied, every relevant frame must actually be opened, and a `## Source language` section written into `WIREFRAME.md` — surface fills (flat or gradient, both stops), the accent hue and what it signals, container geometry, icon-chip shape, whether tinting is uniform or per-meaning, imagery treatment, density, action placement, hierarchy, plus three markers that could only have come from those sources.

This is deliberately *not* an internal check. An earlier run passed preflight with no extraction at all — because "show it only if it fails" makes a check that never ran indistinguishable from one that passed. Everything downstream then invented a visual language: a gradient banner became a flat grey panel, a status blue became green, tinted icon chips became uniform grey circles, photographic thumbnails became glyphs. If the section is absent, the extraction did not happen.

The construction contract is Dopamine-aligned: 360×800 mobile only, the 4px spacing rhythm, 16px page margin, the Dopamine radii set, 48dp touch targets (≥48+12dp for OTP, payment, and dosage), Hugeicons Stroke Rounded, and text annotated by Dopamine *type role* rather than pixel size since Stage 1 has no tokens. Grayscale only — `#ffffff`, `#f0f0f0`, `#999999`, `#333333`, `#000000` — with coloured status carried by label, icon, and shape instead. Zones carry priority badges (P1/P2/P3) and interaction notes, and drug names, dosages, and allergens appear at realistic full length so truncation risk surfaces here rather than in Stage 2.

Output is an interactive clickable HTML wireframe at `wireframes/<surface>.html` — minimum critical path first, one primary screen and at most four essential states by default, with anything beyond that marked deferred in the coverage map. Motion only where it explains behaviour, `prefers-reduced-motion` respected even at this fidelity, rendered verification attempted once, and concise design notes in the delivery rather than a separate notes board.

### `reference/ideate/wireframe-preflight.md`
**Status: Complete**

A lightweight readiness gate immediately before the wireframe is created or materially revised. Confirms the context is understood, both branch decisions are explicit, the direction is agreed, the user actually permitted the artifact, coverage is mapped, the interface principles were checked, and no unresolved issue makes the interaction unsafe or structurally unsound — plus the visual-source checks when references were supplied.

It stays invisible when it passes. On failure it reports the design issue that blocks progress and the smallest next action — not the checklist. No manifest, no ledger, no user-facing artifact.

### `reference/ideate/read-input.md`
**Status: Complete**

Phase 0, for when the input isn't just a prompt. Reads a Figma or FigJam board, a screenshot, or a multi-frame visual — frames, flow arrows, sticky notes, annotations, and what's missing or contradictory — treating annotations as first-class context rather than decoration. Also reads a product brief or PRD as *design input*, classifying each statement as confirmed decision, constraint, proposal, assumption, unknown, or conflict, and returning product, policy, legal, and engineering gaps to their owners as questions instead of quietly answering them. Authoring the PRD is the one hand-off that goes sideways rather than downstream.

### `reference/ideate/research.md`
**Status: Complete**

The research branch, reachable only from `Stop for research first`. Research planning (objective, key questions, hypotheses, participants, method, what to observe, success signals) and the session script (warm-up, context, tasks, follow-ups, comprehension checks). It plans how to learn; it never invents findings or presents assumptions as participant feedback.

### `reference/content-design.md`
**Status: Complete**

Interface copy as part of the hierarchy rather than filler added after the structure is done. Shared by Stage 1 (deciding what meaning must lead, where a consequence or limitation has to be explained, what an action label promises) and Stage 2 (writing it against real components). Plain language, action-specific CTAs, and error messages that never blame the user.
### `reference/accessibility.md`
**Status: Complete**

Extracted from the Dopamine 2.0 accessibility guidelines (WCAG 2.2 AA, IS 17802, RPwD Act 2016, GIGW 3.0). Loaded as a mandatory constraint layer by Stage 2. Covers:

- **Colour and contrast** — the four ratios (4.5:1, 3:1, 3:1, exempt) and the three tokens that fail WCAG today (Content/Tertiary, States/Warning, Branding/Coral) with specific restricted-use rules and fixes.
- **Typography** — minimum size floors from 11pt bold (tags only) to 16pt bold (iOS inputs), Cabinet Grotesk ≥24pt threshold, text scaling requirements at 130% and 200%, and the four truncation failure modes.
- **Touch targets** — 24×24 floor, 48×48 default, ≥48+12dp for high-stakes actions, plus the spacing exception rule.
- **Interactive states** — the six applicable states required for every interactive element (default, hover, pressed, loading, disabled, selected). **Focus is not applicable:** Dopamine 2.0 components are mobile UI components and carry no focus-ring styling by design. The harness states this fact wherever the accessibility pass runs, so focus reads as considered-and-not-applicable rather than skipped.
- **Screen reader** — component specs must include audio spec alongside visual spec, alt text rules for five image types.
- **Forms** — three rules: persistent labels, explain what's wrong, suggest the fix.
- **Motion and time** — 300ms ceiling, no flashes ≥3/sec, prefers-reduced-motion mandatory.
- **Language** — Grade 7–8 reading level with clinical-to-plain examples.

### `reference/compose.md`
**Status: Complete**

Four phases against the live Dopamine MCP. **Resolve** — the wireframe's component candidates are a hypothesis, not a decision; `search_components` on intent, `get_component_docs` on every match, and check `list_patterns` first since a composed pattern beats assembling its parts. A zone that maps to no component is named as a system gap, never approximated with CSS overrides. **Tokenise** — every value through base → semantic → component, with the Stage 1 type *roles* resolved to real `--font-size-*` tokens. **Compose** — barrel imports, exact prop contracts, no invented props or union values, no ad-hoc restyling, icons sized to the visible glyph (roughly Figma frame × 0.6). **Verify** — coverage, tokens, the full accessibility pass, and whether the surface still serves the principles the brief recorded.

It also carries a degraded mode for when the MCP is unreachable: say so first, offer to stop, and mark every output provisional rather than inventing props.

### `reference/polish.md`
**Status: Complete**

Stage 3 protocol in three gated phases:

*Phase 1 — Audit.* The agent reads the composed surface before proposing anything, evaluating visual hierarchy against the wireframe's priority stack, rhythm and pacing, brand presence, signature opportunity, micro-interaction gaps, and copy voice. Outputs a structured assessment shared with the user.

*Phase 2 — Propose.* The agent presents 3–7 departure proposals grouped by risk level (safe, moderate, aggressive). Seven departure categories defined: spacing, typography, colour, elevation/depth, motion, layout, component, and copy — each with concrete examples and constraints noting which accessibility rules remain non-negotiable within that category. Each proposal uses a fixed format: element, system rule bent, current state, proposed state, rationale, risk, accessibility impact. Proposals must stand alone (user can approve any combination).

*Phase 3 — Apply.* Handles four response types (approved, rejected, modified, "tell me more"). Departures applied one at a time with verification. Final accessibility sweep against the full hard floor checklist. Outputs `DESIGN_DECISIONS.md` documenting every approved departure and rejected proposal.

The hard floor — accessibility constraints that are never candidates for departure — is listed at the top of the file and referenced throughout.

## Design system reference

- **Documentation:** https://dopamine2-0.dopamine-ds.workers.dev/
- **Viewport:** 360px mobile only, no desktop
- **Token architecture:** base → semantic → component (255 tokens across 7 foundation groups)
- **Components:** 35 ready (actions, navigation, forms, selection, display, feedback, cart)
- **Typography:** Cabinet Grotesk (display, ≥24pt), Figtree (all other roles)
- **Spacing:** 4px rhythm (0, 2, 4, 8, 10, 12, 16, 20, 24, 28, 32, 36, 40)
- **Brand:** coral #ff5443

## Current status

| File | Status | Notes |
| --- | --- | --- |
| `SKILL.md` | ✅ Complete | Entry point and cross-stage router |
| `reference/ideate.md` | ✅ Complete | Stage 1 router — phases, branch points, brief |
| `reference/effort-and-speed.md` | ✅ Complete | Proportionality brake — always loaded |
| `reference/interface-principles.md` | ✅ Complete | 6 principles + 5 laws — Stages 1 and 3 |
| `reference/ideate/read-input.md` | ✅ Complete | Phase 0 — board, screenshot, brief, PRD |
| `reference/ideate/understand.md` | ✅ Complete | Phases 1–2, 4 — context, evidence, branch 1, user story |
| `reference/ideate/research.md` | ✅ Complete | Research branch — Stop for research first only |
| `reference/ideate/competitive-research.md` | ✅ Complete | Phase 2b — bounded pattern scan, default skip |
| `reference/ideate/frame.md` | ✅ Complete | Phase 3 — the design mismatch |
| `reference/ideate/explore.md` | ✅ Complete | Phase 5 — product role, directions, surfaces |
| `reference/ideate/review-direction.md` | ✅ Complete | Branch 2 — diagnose disagreement, step back |
| `reference/ideate/comprehend.md` | ✅ Complete | Phases 6–7 — user understanding map |
| `reference/ideate/wireframe.md` | ✅ Complete | Phase 8 — interactive grayscale wireframe |
| `reference/ideate/wireframe-preflight.md` | ✅ Complete | Readiness gate before construction |
| `reference/content-design.md` | ✅ Complete | Interface copy — Stages 1 and 2 |
| `reference/accessibility.md` | ✅ Complete | WCAG 2.2 AA constraint layer |
| `reference/compose.md` | ✅ Complete | Stage 2 — resolve, tokenise, compose, verify |
| `reference/polish.md` | ✅ Complete | Stage 3 — audit, propose, apply |
| `CLAUDE.md` | ✅ Complete | Project-level instructions |

## What's next

1. Run Stage 1 end-to-end against a real surface and tune the gating. Eight phases plus two branch points is a lot of ceremony for a small change — `effort-and-speed.md` is the brake, but only a real run will show whether it actually holds
2. Decide whether to bring in an evaluation layer — the [ux-eval](https://github.com/Akshaymehta1mg/Design-skills) 8-gate framework is a cross-stage reviewer rather than a stage, and its touch-target check needs raising from 44px to Dopamine's 48dp before use
6. End-to-end test across all three stages against a real surface

## Structural model

The harness is structured as one skill entry point with a lean router, stage-specific knowledge loaded lazily via reference files, and project state tracked through handoff artifacts (`WIREFRAME.md`, `DESIGN_DECISIONS.md`). The base skill stays small and keyword-rich for auto-triggering; heavy instructions only load on demand.

## Tests

```bash
python3 tests/test_harness.py
```

`tests/test_harness.py` checks the invariants that actually break this harness:
every cross-reference resolves, no reference file is orphaned or undocumented,
the stage gate chain lines up end to end, the Dopamine constants (4px rhythm,
48dp targets, radii set, coral, Cabinet Grotesk ≥24pt) haven't drifted between
files, one name per concept, and the protocol rules one file states aren't
contradicted by another. It also checks that `allowed-tools` actually grants
what the protocol demands.

`tests/behavioral-scenarios.md` covers what static checks can't — whether an
agent *following* the instructions behaves correctly. Four scenarios against
fixture projects in different states: a vague prompt must halt the stage, a
well-evidenced one must proceed, the gates must reject out-of-order stages, and
a later-stage request must be handed off rather than refused.

One static check fails by design: Stage 2 is a placeholder, so
`test_stage_two_is_implemented` stays red until `compose.md` is written.
