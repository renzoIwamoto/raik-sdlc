# Screenshot review

Take screenshots of every new or changed state at each viewport, then open each one and check this list. Write down what you looked at; "looked fine" is not a review.

## Capture

With Playwright CLI:

```bash
playwright-cli open http://127.0.0.1:5173/<route>
playwright-cli resize 360 800
playwright-cli screenshot --filename <state>-mobile.png
playwright-cli resize 1440 1000
playwright-cli screenshot --filename <state>-desktop.png
```

`screenshot` captures the visible viewport by default; add `--full-page` for the whole scrollable page. Full-page shots show layout; viewport shots show what the user actually sees after an action, so take a viewport one after any action that gives feedback. Use `snapshot` to get element references for `click`, `fill` and `check`. Run `playwright-cli --help` for the full command set (checked against 0.1.22).

## Check

1. **Feedback is visible where the user is.** After closing a dialog or submitting, is the confirmation on screen, or did it render somewhere the user scrolled away from?
2. **Options make sense.** Lists of choices contain only plausible items (no impossible candidates, no duplicates).
3. **Nothing escapes its box.** Chart lines, long words, numbers and badges stay inside their containers at 360 px.
4. **Nothing hides behind fixed elements.** Bottom bars and sticky headers do not cover the last row or a primary button. (In full-page shots, fixed bars float mid-page; judge them in viewport shots.)
5. **States are distinguishable.** Disabled, selected, error and empty states read differently without relying on color alone.
6. **Text fits.** No truncation that loses meaning; numbers align; currency and signs (−, +) are where they should be.
7. **Matches the design system.** Tokens, spacing, radii and type follow `DESIGN.md`.

## Then

Fix material problems, add a test that would have caught each one when possible, and take at most one more round.
