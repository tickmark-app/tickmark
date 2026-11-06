# Tickmark

**A free, open-source on-screen ruler for Windows, macOS and Linux.**

Tickmark aims to combine a classic floating ruler, smart edge-snapping
measurement and floating guides in one tool, free for personal and commercial
use, without accounts, licence keys or telemetry.

> **Status: pre-alpha.** The project foundation is in place; the ruler itself
> is not usable yet. See the [roadmap](ROADMAP.md) for what is planned.

## Planned highlights

- Horizontal, vertical and combined rulers that stay sharp on HiDPI screens
  and on multiple monitors with different scaling
- Real and scaled pixels, plus mm, cm and inches after a one-time calibration
- Point-to-point measuring with distance and angle
- Magnifier with colour picker (HEX, RGB, HSL, OKLCH) and colour history
- Edge snapping, spacing and bounding-box measurement
- Floating guides, a freeze mode for menus and Wayland, WCAG contrast checks
- Fully keyboard-operable, translatable into any language

## Development

Tickmark is written in Python with [PySide6](https://doc.qt.io/qtforpython-6/)
and uses [uv](https://docs.astral.sh/uv/) for everything.

```sh
uv sync                     # install Python, dependencies and dev tools
uv run tickmark             # start the app
uv run pytest               # run the tests
uv run pre-commit install   # run all checks before every commit
```

Read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request.

## License

Tickmark is released under the [MIT License](LICENSE). It uses Qt through
PySide6, which is licensed under the LGPLv3.
