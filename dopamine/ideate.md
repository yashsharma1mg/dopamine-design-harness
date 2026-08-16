# Stage 1 — Ideate

Question until clarity is achieved, then produce structural wireframes.
This stage commits to *what* gets built and *why*. It makes no visual
decisions — no colour, no type treatment, no component selection. Those
belong to Stage 2.

## Entry gate

Always open. This is where every new surface starts.

## Protocol

The stage has two phases. Phase 1 (Interrogation) must complete before
Phase 2 (Wireframe) begins. Do not combine them. Do not start wireframing
while questions remain open.

---

## Phase 1 — Interrogation

Your job is to ask questions until you can write a complete brief. The user
often arrives with a vague intent ("I need a cart page", "we need an
onboarding flow"). Your job is to make it precise.

### What you need to know

Work through these dimensions. You do not need to ask them as a flat
checklist — weave them into a conversation. But every dimension must be
resolved before you move to Phase 2. If the user cannot answer one, propose
a reasonable default and get explicit approval.

#### 1. Surface identity

- What is being built? (a page, a flow of multiple pages, a modal, a
  component, a modification to an existing surface)
- Does it have a name? If not, name it together.
- Where does it live in the product's information architecture?

#### 2. User and context

- Who is the primary user? (patient, caregiver, doctor, pharmacist,
  lab technician, admin, guest)
- What is their emotional state when they arrive? (anxious about health
  results, routine refill, price-comparing, browsing, in a hurry)
- What device and context? (mobile on the go, mobile at home, desktop
  at work — this product is mobile-first but the assumption must be
  confirmed)

#### 3. Goal and success

- What is the user trying to accomplish on this surface?
- What does success look like? (order placed, lab booked, information
  understood, decision made, medication found)
- What is the business goal for this surface? (conversion, engagement,
  retention, education, compliance)
- How do we know it worked? (what action, what metric)

#### 4. Content inventory

- What content must appear on this surface? (product information, pricing,
  images, health data, status indicators, promotional content, legal text)
- What content is dynamic vs static?
- What content exists today vs needs to be created?
- Are there any content constraints? (character limits, regulatory
  requirements, mandatory disclaimers)

#### 5. Entry and exit

- How does the user arrive? (navigation, deep link, notification, search
  result, another page in the flow)
- Where do they go after? (next step in flow, back to browse, confirmation,
  external action like taking medication)
- Is this a standalone page or part of a multi-step flow?
- If it's a flow: what are all the steps, and which one is this?

#### 6. Priority hierarchy

- Of everything on this surface, what is the single most important thing?
- What is second? Third?
- What can be hidden, collapsed, or moved to a secondary view?
- Are there competing priorities? (e.g. the business wants to upsell Care
  Plan but the user wants to check out fast)

#### 7. States and edges

- What does the empty state look like? (first visit, no data, no items)
- What does the error state look like? (payment failed, out of stock,
  network error, invalid input)
- What does the loading state look like?
- Are there permission or authentication gates?
- What happens at scale? (100 items in cart, 50 lab results, long product
  names, missing images)

#### 8. Existing patterns

- Is there a current version of this surface? If so, what works and what
  doesn't?
- Are there analogous surfaces in the product that this should be
  consistent with?
- Are there competitor or reference examples the user has in mind?
- Are there hard technical constraints? (API shape, data availability,
  platform limitations)

### Interrogation rules

- **Ask 2–3 questions at a time, not 8.** Batch by theme. Start with
  surface identity and user context (they unlock everything else). Move
  to content and priority once the shape is clear. Leave states and edges
  for last.

- **Propose, don't just ask.** When you have enough signal to guess an
  answer, state your assumption and ask the user to confirm or correct.
  "I'm assuming this is mobile-first for a patient mid-refill who wants
  to add items and check out fast — does that match?" moves faster than
  "Who is the user?"

- **Name the gaps.** When the user gives a vague answer, name exactly
  what's still ambiguous. "You said 'a cart page' — I still need to know
  whether this includes the delivery address selection, or if that's a
  separate step."

- **Resolve conflicts explicitly.** If the user's answers contradict
  (e.g. "keep it simple" but also "show all the offers and savings"),
  name the tension and ask them to pick a priority.

- **Know when to stop.** You have enough when you can write the brief
  (Phase 1 output) without inventing any answers. If you're still
  guessing about the primary user action, keep asking. If you're
  debating whether a tertiary label should say "View details" or
  "See more", you've gone too far — that's Stage 2 territory.

### Phase 1 output — The Brief

When interrogation is complete, write a structured brief and present it
to the user for sign-off. Use exactly this format:

```markdown
# Brief: [Surface Name]

## Surface
[What it is, where it lives]

## User
[Who, emotional state, device/context]

## Goal
- User goal: [what they accomplish]
- Business goal: [what the org gets]
- Success signal: [observable action or metric]

## Content inventory
[Ordered list of everything on the surface, marked required/optional]

## Flow
- Entry: [how they arrive]
- Exit: [where they go]
- Flow position: [standalone | step N of M]

## Priority stack
1. [Most important element]
2. [Second]
3. [Third]
[Everything else is secondary]

## States
- Empty: [description]
- Error: [description]
- Loading: [description]
- Edge cases: [anything unusual]

## Constraints
[Technical, regulatory, consistency requirements]

## Open questions
[Anything explicitly deferred to Stage 2 or 3]
```

**The user must approve this brief before you proceed to Phase 2.**
Read it back, ask "Does this capture what we're building?", and wait for
confirmation. If they change anything, update the brief and re-confirm.

---

## Phase 2 — Wireframe

With the approved brief, produce structural wireframes. These are
layout-only, grayscale, content-zoned representations. They commit to
information architecture and spatial hierarchy. They do not commit to
visual treatment.

### Wireframe rules

- **360px mobile only.** Every wireframe is 360px wide. This is the only
  viewport. There is no desktop variant. The product is a mobile app
  and all design decisions target this single form factor.

- **Grayscale only.** Use only: white (#ffffff), light gray (#f0f0f0) for
  content zones, medium gray (#999999) for placeholder text, dark gray
  (#333333) for primary text, and black (#000000) for zone borders. No
  brand colour. No tints. The absence of colour is the point — it forces
  hierarchy through structure alone.

- **Content zones, not components.** At this stage, a "button" is a
  rectangle labelled "Primary Action: [label]". A "product card" is a
  bordered zone with placeholders for image, title, price. Do not use
  real components — that's Stage 2. The wireframe must communicate intent
  without leaning on the visual weight of real UI.

- **Real content, not lorem ipsum.** Use the actual content from the brief
  wherever possible. If the real content isn't available yet, use
  realistic placeholder content that matches the expected length and type.
  "Amoxicillin 500mg Capsule" not "Product Name Here".

- **Annotate the hierarchy.** Every zone must be labelled with:
  - What it contains (content type)
  - Its priority rank from the brief (P1, P2, P3, secondary)
  - Its interaction behaviour (tappable, scrollable, expandable, static)

- **Show the scroll.** Mark the fold line (approximately 640px from top
  on a 360px-wide mobile viewport). Content above the fold must contain
  the P1 element. Show enough of the below-fold content to indicate
  that there's more.

- **One wireframe per state.** If the brief identifies multiple meaningful
  states (empty, loaded, error), produce a separate wireframe for each.
  At minimum, produce the primary loaded state.

### Wireframe format

Produce wireframes as SVG artifacts. Each wireframe is a single SVG at
360px wide, height as needed, using simple rectangles, lines, and text.

Structure each wireframe with:
- A header annotation: surface name, state, viewport
- Zone rectangles with light gray fill and 1px dark borders
- Text labels in a monospace font at 11-12px
- Priority badges (P1, P2, P3) as small dark rectangles in zone corners
- A dashed line marking the fold
- Interaction annotations as italic text below zones

### Phase 2 output — The Wireframe Package

Deliver:
1. The approved brief (from Phase 1)
2. One or more annotated wireframes (SVG)
3. A flow diagram if the surface is multi-step (showing step sequence
   and decision points as a simple node-edge SVG)
4. A component candidates list — your initial read on which Dopamine 2.0
   components each zone might map to in Stage 2. This is advisory, not
   binding. Format:

```markdown
## Component candidates

| Wireframe zone         | Likely component(s)        | Notes                        |
| ---------------------- | -------------------------- | ---------------------------- |
| Top navigation bar     | PageHeader, Navigation     | Location context variant     |
| Product hero           | Product                    | Image carousel + title block |
| Add to cart bar        | AddToCartPill              | Sticky bottom variant        |
| Offer strip            | Offer                      | Collapsed with see-all       |
```

### Handoff to Stage 2

Save the complete output as `WIREFRAME.md` at the project root, with
the brief at the top, the wireframe SVGs referenced or embedded, and the
component candidates table at the bottom. This file is the entry gate
for Stage 2 — `compose` will refuse to proceed without it.

**The user must approve the wireframe before it is saved.** Present each
wireframe, walk through the zones and their priorities, and ask for
sign-off. If they request changes, update and re-present. Do not save
`WIREFRAME.md` until they confirm.

---

## What this stage does NOT do

- Choose colours, type treatments, or visual styling (Stage 2)
- Select specific component variants or props (Stage 2)
- Apply token values (Stage 2)
- Make intentional departures from the system (Stage 3)
- Write production code (Stage 2)
- Connect to Storybook MCP (Stage 2)

The wireframe is a structural contract. Everything visual is downstream.
