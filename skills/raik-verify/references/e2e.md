# End-to-end tests

Patterns for committed `@playwright/test` suites.

## Layout

```
<web-app>/
  playwright.config.ts
  e2e/
    <capability>.spec.ts     one file per spec capability
```

One `test()` per spec scenario, named after it, so a failing test points at the requirement it protects.

## Config: two viewports as projects

```ts
import { defineConfig, devices } from '@playwright/test'

export default defineConfig({
  testDir: './e2e',
  use: { baseURL: 'http://127.0.0.1:5173', reducedMotion: 'reduce' },
  webServer: { command: 'pnpm dev --host 127.0.0.1 --port 5173 --strictPort', url: 'http://127.0.0.1:5173', reuseExistingServer: !process.env.CI },
  projects: [
    { name: 'mobile', use: { ...devices['Pixel 5'], viewport: { width: 360, height: 800 } } },
    { name: 'desktop', use: { viewport: { width: 1440, height: 1000 } } },
  ],
})
```

`webServer` starts and stops the dev server, which avoids orphan processes.

## Guards in every test

```ts
import { test as base, expect } from '@playwright/test'

export const test = base.extend({
  page: async ({ page }, use) => {
    const errors: string[] = []
    page.on('pageerror', (e) => errors.push(e.message))
    page.on('console', (m) => { if (m.type() === 'error') errors.push(m.text()) })
    await use(page)
    expect(errors, 'no console errors').toEqual([])
    const fits = await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth)
    expect(fits, 'no horizontal scroll').toBe(true)
  },
})
```

## Forcing states the fixtures never reach

Intercept the request or module that supplies data and append or replace what you need. Never edit shared fixtures for one test.

```ts
await page.route('**/api/transactions*', async (route) => {
  const response = await route.fetch()
  const body = await response.json()
  body.items.push({ kind: 'refund', cents: 300000, categoryId: null })
  await route.fulfill({ response, json: body })
})
```

In a prototype without an API, the same works on a source module served by the dev server: fetch it, append code, fulfill.

## Assert what the user perceives

- Feedback must be **in the viewport**, not only in the DOM:
  ```ts
  const box = await page.getByRole('status').boundingBox()
  expect(box && box.y >= 0 && box.y + box.height <= page.viewportSize()!.height).toBe(true)
  ```
- Prefer roles and visible text (`getByRole`, `getByText`) over CSS selectors.
- Assert concrete values from the scenario ("+S/ 40.00"), not just presence.

## Regression

Run the whole suite, not only the new file. A change that breaks an earlier scenario is not done.
