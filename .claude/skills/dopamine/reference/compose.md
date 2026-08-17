# Stage 2 — Compose

> This reference will be completed when Stage 1 is finalised.
> Gate: requires approved WIREFRAME.md from Stage 1.
> MCP connection to Storybook enters here.

## What this stage does

Translates wireframe zones into real Dopamine 2.0 components with
correct token resolution, variant selection, and prop configuration.
The Storybook MCP is used to discover component APIs, validate prop
combinations, and confirm visual output.

## Mandatory references loaded by this stage

1. `reference/accessibility.md` — every composed surface must pass
   every constraint before advancing to Stage 3. This is non-optional.
   Accessibility on a healthcare app is legally binding and clinically
   necessary.

2. The Dopamine 2.0 Storybook documentation site for component APIs,
   token values, and variant specifications.

## Key constraints (preview)

- Components never reference base tokens. Semantic tokens are the API.
- The three failing tokens (Content/Tertiary, States/Warning, Coral)
  have restricted usage rules from the accessibility guidelines.
- Drug names, dosages, allergens, and frequency NEVER truncate.
- Every interactive element needs all seven states designed.
- Screen-reader labels must be specified alongside visual labels.
- 48dp minimum touch targets; ≥48+12dp for high-stakes actions.
- `prefers-reduced-motion: reduce` on every animation.
- 360px mobile viewport only. No desktop.

## Full protocol — to be written
