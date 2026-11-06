# Tickmark – rules for every Claude session

Tickmark is a free, open-source on-screen ruler for Windows, macOS and Linux,
written in Python with PySide6. Read this file and `ROADMAP.md` before you
change anything. If something you need is not written here or there, ask
instead of assuming.

## Commands

```sh
uv sync                                  # environment, always from uv.lock
uv run ruff format .                     # format
uv run ruff check .                      # lint
uv run pyright                           # types, strict mode
uv run lint-imports                      # layer rules
uv run pytest --cov                      # tests with coverage
uv run coverage report --include="src/tickmark/core/*" --fail-under=95
uv run tickmark                          # start the app
```

All of these must pass before you commit. `uv run pre-commit run --all-files`
runs the first four.

## Architecture

```
src/tickmark/
  core/      plain Python: geometry, units, calibration, colour, contrast, edges
  platform/  operating system access behind the Protocols in platform/base.py
  ui/        Qt widgets; calls core and platform, does no measuring itself
```

- `core` never imports Qt, `platform` or `ui`. `platform` never imports `ui`.
  import-linter enforces this; do not weaken the contracts in `pyproject.toml`.
- All measuring happens in **physical pixels**. Convert to Qt logical pixels
  only at the UI boundary, using the device pixel ratio of the screen involved.
- Platform features are asynchronous through callbacks, because the Wayland
  portals answer later. Callbacks are called exactly once.
- A backend states what it can do through `capabilities`. Never fail silently;
  the UI shows the user why a feature is unavailable.
- The interfaces in `platform/base.py` and the types in `core/` are shared by
  parallel work. Change them only in a dedicated pull request.

## Code rules

- No dead code, no commented-out code, no abstraction without a second user.
- Comments say *why*, never *what*.
- No `except: pass` and no swallowed errors. Log or surface every failure.
- Verify every Qt and OS API against its official documentation before using
  it. Do not write an API from memory. If you could not verify it, say so.
- Named constants for pixel values, tolerances and limits; no magic numbers.
- Every new dependency is justified in the pull request.
- No TODO comments in `main`. Open an issue instead.
- All user-visible text goes through `self.tr()` or `QCoreApplication.translate()`.
  Never build sentences by concatenating translated fragments.

## Tests

- Tests check behaviour, not implementation.
- Every bug fix starts with a test that fails without the fix.
- Use Hypothesis for geometry, units and colour maths.
- UI tests use pytest-qt and run offscreen.
- `core` coverage stays at or above 95 %.

## Commits and pull requests

- Conventional Commits: `feat:`, `fix:`, `docs:`, `test:`, `refactor:`, `ci:`, `chore:`.
- One topic per pull request, ideally under 400 changed lines.
- The pull request description states what was tested **and what was not**,
  for example "tested on Linux offscreen only; not tested on Windows or macOS".
- Never push to `main` directly. A human approves every merge.

## Working in parallel

- Each session works on one module, on its own branch, and opens one pull request.
- Touch only files in your module. Interface changes go in a separate pull request.
- End every session with a pull request whose description says what is done,
  what is open and what was not tested.

## Honesty

- Report what you actually ran and saw. Do not claim a test passed or a UI looks
  right unless you ran it or looked at a rendered image.
- The cloud environment has no real display. Behaviour on real hardware
  (HiDPI feel, hotkeys, stay-on-top, Wayland, macOS permissions) is verified by
  a human on a PC; say so instead of guessing.
