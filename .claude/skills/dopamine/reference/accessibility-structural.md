# Accessibility — structural constraints (Stage 1)

WCAG 2.2 AA · IS 17802 · RPwD Act 2016 · GIGW 3.0

These are the accessibility rules that are **layout decisions, not visual
decisions**. A wireframe that fails them has already failed — no amount of
Stage 2 token work recovers it.

Load this in Stage 1 alongside `ux/wireframe-craft.md`.
Contrast, token, and font-family rules stay in `accessibility.md` (Stage 2).

## Touch target sizing

| Context | Size | When |
| --- | --- | --- |
| Floor | 24×24 | Inline icons, dismiss ×, small chevrons |
| Default | 48×48 | Any consumer touch point |
| High-stakes | ≥48 + 12dp separation | OTP, payment, dosage, destructive actions, allergy acknowledgment, KYC |

Spacing exception: a target under 24×24 passes if a 24px circle centred on
it does not intersect another target.

This is a wireframe constraint because target size determines row height,
list density, and how many items fit above the fold.

## Truncation

Drug names, dosages, allergens, and frequency **never truncate**. Wrap to
N lines. SKU card names are the only exception.

This is a wireframe constraint because wrapping changes card height and
therefore the whole vertical rhythm of a list.

## Text scaling

Design must survive 130% (realistic default for the 40+ medicine-buying
cohort) and 200% (WCAG 2.2 SC 1.4.4 ceiling).

Wireframe implications:
- No fixed-height containers. `min-height` only. Vertical padding, not totals.
- No text baked into image zones — mark text as live text in the wireframe.
- Safety-critical content is never collapsed by default. Dosage behind
  "Details ▾" fails. If the brief hides it, flag the conflict.

## State enumeration

Every interactive element needs seven states designed: default, hover,
focus, pressed, loading, disabled, selected. Plus error where applicable.

Stage 1 obligation is **enumeration, not visual design** — the stage
specification must name which states exist for each element, and the
wireframe must show any state that changes layout or content.

Dopamine components currently lack exhaustive state coverage. Flag the gap
in the wireframe notes; do not silently assume the component provides it.

## Colour is never the only signal

Any status the brief describes by colour ("red for out of stock") must
also carry a label, icon, shape, or weight change. Verify this in the
wireframe, where there is no colour to lean on.

## Surface and comprehension

- The user must understand what happens next before every action.
- Recovery paths (back, change, cancel, retry, undo) exist for every
  consequential action and appear in the wireframe.
- Plain language, Grade 7–8 reading level, in the real content used.
