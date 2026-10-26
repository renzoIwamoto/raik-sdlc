# Screen states

Design each state that can occur. "Can it happen?" decides, not "is it likely?".

| State | Must show | Avoid |
|---|---|---|
| Loading | What is happening ("Reading your emails...") and, for long work, progress or the current phase. Keep layout stable (skeletons in the final shape) | A bare spinner for more than a second; layout jumps |
| Empty, first use | Why it is empty and the one next step (a button or link) | A blank area; "No data" |
| Empty, filtered | That filters hide the results, and a way to clear them | Looking identical to first use |
| Partial | What loaded and what did not, with a retry for the missing part | Hiding the partial data |
| Error | What happened in user terms, whether data is safe, and what to do (retry, contact, wait) | Raw API messages, codes, blame |
| Limit reached | Which limit, what still works, and what changes it | Silent failure |
| Offline or reconnecting | That the app is offline and what will happen when it returns; keep the last data visible | Clearing the screen |
| Success | Confirmation where the user is looking, with undo when the action is destructive or broad | A toast that appears off-screen or vanishes before it is read |
| Permission or access revoked | What lost access and how to restore it, prominently | Burying it in settings |

## Controls

For each control: default, hover, focus (visible), active, disabled (only if the reason is shown or obvious; otherwise hide it), loading (when it triggers work), error (inline, next to the field, with how to fix it).

## Numbers and data

Format with the locale's rules (currency symbol, decimal separator, negative sign before the symbol), align figures, never mix currencies in one total, show what a zero or negative value means.
