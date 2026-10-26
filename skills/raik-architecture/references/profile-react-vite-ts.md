# Profile: react-vite-ts

Frontend base standard for web apps.

## Layout

```
web/
  src/
    app/ or main.tsx         routing and providers
    pages/ or routes/        one folder or file per screen
    components/              shared UI; components/ui/ for the component library
    lib/                     pure helpers (formatting, dates); tested
    api/                     generated client from the backend OpenAPI
    styles/ or index.css     design tokens: the only source of color, type and spacing
  e2e/                       @playwright/test, committed
  playwright.config.ts
```

## Required

1. TypeScript strict. No untyped JavaScript.
2. One source of color, type, spacing and radii: design tokens (CSS custom properties or the Tailwind theme). No literal colors in components.
3. Every screen handles: loading (say what is happening), empty (with the next step), actionable error, limit reached. A control that cannot work is not shown. See `raik-ui`.
4. Accessibility: WCAG AA contrast checked by script, touch targets of at least 44 px, visible keyboard focus, labels on every control, no information carried by color alone, reduced motion respected.
5. Responsive: works at 360 px wide without horizontal scroll, and at 1440 px.
6. API client generated from the backend's OpenAPI; no hand-written request or response types.
7. Business rules live in the backend. A prototype may hold a temporary copy in `lib/` with tests, marked for removal when the API exists.
8. Unit tests with Vitest for `lib/` and non-trivial hooks; e2e with `@playwright/test`, one test per spec scenario.

## Flexible (default first)

- Component library: shadcn/ui (Radix primitives, accessible by default).
- Data fetching and cache: TanStack Query.
- Styling: Tailwind with tokens in the theme.
- Lint and format: Biome (or oxlint plus a formatter).
- Package manager: pnpm.
