# Accessibility — Dopamine 2.0

WCAG 2.2 AA · IS 17802 · RPwD Act 2016 · GIGW 3.0

Accessibility on a healthcare app is not a quality attribute. It is
legally binding (Article 21, SC Apr 2025) and clinically necessary.
A user who cannot read a dosage label may take the wrong medicine.

This reference is non-optional in Stage 2. Every composed surface must
pass every constraint below before advancing to Stage 3.

---

## Colour and contrast

### The four ratios

| Context            | Ratio  | Applies to                                  |
| ------------------ | ------ | ------------------------------------------- |
| Body text           | ≥4.5:1 | Under 18pt regular or 14pt bold             |
| Large text          | ≥3:1   | ≥18pt regular or ≥14pt bold                 |
| UI components       | ≥3:1   | Icons (state), input borders                |
| Decorative/disabled | exempt | But disabled must still be distinguishable  |

### Three tokens that fail WCAG — handle with care

**Content/Tertiary (#868E9E)** — 3.29:1 on white. Fails body text.
Use only for icon support or large captions. For information the user
must read, escalate to Content/Secondary.

**States/Warning (#BF9514)** — 2.79:1 on white. Fails at every size.
Never put yellow text on white. Use yellow as the background with
Content/Primary on top, or shift text to Sunshine Yellow 40 (#967500).

**Branding/Coral (#ff5443)** — 3.18:1 on white. Fails body text.
OK for ≥14pt bold (button labels) and as a button background with white
text. Not for inline body copy or microcopy.

### Colour is never the only signal

Pair colour with at least one other indicator: text label, icon, weight
change, or pattern. A red border alone does not communicate "error" to
a colour-blind user.

---

## Typography

### Minimum sizes — hard floors

| Size   | Weight    | Allowed use                                    |
| ------ | --------- | ---------------------------------------------- |
| 11pt   | Bold only | Tags, badges, chips. Not sustained reading.    |
| 12pt   | Regular   | Captions only. Must use Content/Primary or /Secondary. |
| 14pt   | Regular   | Body text floor. Minimum for sustained reading. |
| 16pt   | Bold      | iOS input fields. Prevents auto-zoom on focus. |
| 24pt+  | Any       | Cabinet Grotesk threshold. Do not use Cabinet Grotesk below 24pt. |

### Text scaling — the real viewport

Many 40+ users (the largest medicine-buying cohort) set system font
scaling to 130–150% and forget. Design must work at:

- **130%** — treat as realistic default for the target demographic
- **200%** — WCAG 2.2 SC 1.4.4 conformance ceiling

### Four failure modes to prevent

1. **Fixed-height containers.** Use `min-height`, never `height`.
   Vertical padding, not totals.
2. **Truncation on critical text.** Drug names, dosages, allergens,
   and frequency NEVER truncate. Wrap to N lines, never ellipsis.
   SKU card names are the only exception.
3. **Text baked into images.** Promo banners, stamps inside JPEGs.
   Use real text overlaid on image or SVG with live `<text>`.
4. **Critical content collapsed by default.** Dosage behind
   "Details ▾" fails. Safety-critical content visible at every scale.

---

## Touch targets

| Context          | Size    | When                                        |
| ---------------- | ------- | ------------------------------------------- |
| WCAG AA floor    | 24×24   | Inline icons, dismiss ×, small chevrons     |
| Dopamine default | 48×48   | Any consumer touch point (Android + web)    |
| High-stakes      | ≥48+12dp | OTP, payment, dosage, destructive actions, allergy acknowledgment, KYC |

The spacing exception: a target <24×24 is WCAG-compliant if a 24px
circle centred on it does not intersect another target.

---

## Interactive states

> **Standing fact — state this every time the accessibility pass runs.**
>
> **Dopamine 2.0 components are mobile UI components. They do not carry
> focus-ring styling, and that is by design, not an omission.**
>
> Focus rings are a pointer-and-keyboard affordance. These components target a
> touch surface at a single 360px viewport, where there is no keyboard focus to
> ring. A Dopamine component without a visible focus ring is **correct** — do
> not raise it as a defect, do not add one with an ad-hoc CSS override, and do
> not fail a surface on it.
>
> Everything else on this page still applies in full. The remaining six states
> are still required, and hover reads as pressed on touch.

Every interactive element must have its states designed:

1. Default
2. Hover (reads as pressed on touch)
3. ~~Focus~~ — **not applicable to Dopamine components.** Mobile UI, no focus ring by design.
4. Pressed
5. Loading
6. Disabled (visually distinguishable, not just greyed text)
7. Selected

Plus Error where applicable.

If a surface ever ships outside the mobile app — a web view, a desktop
breakpoint, anything a keyboard reaches — that surface is outside Dopamine 2.0's
scope and the focus requirement returns with it. Inside the mobile app, it does
not apply.

Currently Dopamine components lack exhaustive state coverage.
When composing, the agent must verify each interactive element has the six
applicable states specified, or flag the gap. Focus is not one of them and is
never flagged.

---

## Screen reader

### Component spec = visual spec + audio spec

When specifying a component, also specify how a blind user hears it.
Example for a product card:

- Image: "Crocin Advance, 500mg paracetamol tablets, strip of 15"
- Price: "₹35.20"
- Button: "Add to cart, button. Double-tap to add Crocin Advance,
  fifteen tablets, to your cart."

### Alt text rules

- Product hero: describe product, strength, form, quantity.
  Not "Image" or "Product photo".
- Promotional banner: describe the offer.
  Not "Banner" or "Promotional offer".
- Doctor/specialist: name and specialty.
  Not "Smiling young doctor in white coat".
- User-uploaded prescription: "Uploaded prescription — tap to add
  description". Never auto-generate from OCR (privacy + safety).
- Decorative icon next to label: `alt=""` when the adjacent text
  already communicates the meaning.

---

## Forms

### Three rules for every form field

1. **Identify the field** — persistent label, not placeholder-as-label.
   Placeholder disappears on input; screen reader user loses anchor.
2. **Explain what's wrong** — "Pin code must be 6 digits", not
   "Invalid input".
3. **Suggest the fix** — "Try '110001' format".

Error messages must be programmatically associated with their field
(not floating with no association).

---

## Motion and time

| Constraint                     | Value   | Rationale                          |
| ------------------------------ | ------- | ---------------------------------- |
| Max functional motion duration | 300ms   | Chevron rotate, sheet slide, modal fade |
| Flash ceiling                  | <3/sec  | WCAG 2.3.1 — no strobing          |
| Auto-advance minimum interval  | 5s      | If carousel must auto-rotate       |
| Session expiry warning          | ≥30s    | Plus "Extend session" affordance   |

`prefers-reduced-motion: reduce` is mandatory for every animation.
Typically a crossfade or instant transition.

---

## Language

Aim for Grade 7–8 reading level on all consumer-facing copy.

| Don't                                         | Do                                         |
| --------------------------------------------- | ------------------------------------------ |
| Antihypertensive prophylaxis                  | Helps prevent high blood pressure          |
| Concurrent administration is contraindicated  | Don't take this with [other medicine]      |
| Posology: 1 tab BD AC × 5d                   | Take 1 tablet, twice a day before meals, for 5 days |

---

## The checklist (at-a-glance)

### Do

- Design every state: default, hover, pressed, disabled, loading, error
  (focus is **not applicable** — Dopamine components are mobile UI and carry no focus ring by design)
- Spec screen-reader label alongside visual label
- Use Content/Primary or /Secondary for text users must read carefully
- Pair colour with at least one other signal
- 48dp minimum tap target
- Test layouts in Hindi at 200% font scale
- Provide manual/assisted alternative to every biometric KYC check
- Aim for AAA on: dosage, allergies, expiry, OTP, payment confirmations

### Do not

- Use Content/Tertiary for body text (fails AA on white)
- Put States/Warning yellow text on white (fails every size)
- Use Coral as body-text colour at sub-18pt
- Use placeholder text as the only label
- Auto-rotate carousels on critical surfaces
- Lock users into a single biometric KYC path
- Use Cabinet Grotesk below 24pt
