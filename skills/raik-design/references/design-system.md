# What DESIGN.md contains

Each section states decisions with their reason. Values live in tokens; DESIGN.md names the roles and the rules.

1. **Direction**: the chosen mood in two sentences, what was rejected and why, references.
2. **Principles**: three to five rules that resolve design disputes ("numbers first", "one action per screen").
3. **Color**: tokens by role (background, surface, ink, ink-soft, border, action, on-action, danger, warning, success, focus) with hex values; data/category palette; contrast results; dark mode policy.
4. **Typography**: families and fallbacks, a short scale (5-6 sizes) with roles, weights, line heights, numeric features (tabular figures for amounts).
5. **Spacing and layout**: spacing scale, grid, breakpoints (at least 360 and 1440), maximum content width, gutters.
6. **Shape and elevation**: a short radius scale (2-3 values) and where each applies; shadows allowed or not.
7. **Components**: inventory with variants and states (default, hover, focus, active, disabled, loading, error); minimum touch target 44 px.
8. **States of a screen**: loading (with what is happening), empty (with the next step), error (what happened, what to do), limit reached, success feedback. See `raik-ui`.
9. **Motion**: durations, easing, what animates and what never does; `prefers-reduced-motion` honored.
10. **Iconography and imagery**: icon set, sizes, when icons need labels.
11. **Data visualization**: chart types allowed and for what, colors, labels, empty and negative values, accessible alternatives (a table or text).
12. **Content**: voice rules from PRODUCT.md applied to labels, buttons, errors, numbers, dates and currency formats.
13. **Accessibility**: WCAG level, focus style, keyboard paths, screen reader names, contrast checks.
14. **Changelog**: dated changes to the system and their reason.
