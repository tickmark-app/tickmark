# Roadmap

Tickmark combines a classic floating ruler, smart edge-snapping measurement and
floating guides in one free tool for Windows, macOS and Linux.

The bar for 1.0: everything the popular commercial screen rulers do for
day-to-day work, without their gaps – sharp on HiDPI and mixed-DPI monitors,
usable on every operating system, free for commercial use.

## 0.1 – Foundation and first ruler

- [x] Project foundation: tooling, CI on three systems, layer rules, interfaces
- [ ] Single ruler, horizontal and vertical, sharp at 100–200 % scaling
- [ ] Live cursor position in physical and scaled pixels
- [ ] Point-to-point measuring with Space, cancel with Esc
- [ ] Magnifier with colour picker and copy to clipboard
- [ ] Tray icon, show/hide hotkey
- [ ] English and German, translation pipeline in place

## 0.5 – Feature parity with classic screen rulers

- [ ] Combined horizontal and vertical ruler, multiple instances
- [ ] Calibration to mm, cm and inches
- [ ] Angle and distance from the origin, golden ratio marks
- [ ] Transparency, colours, fonts, large-number mode
- [ ] Docking to screen edges, "bring ruler here", reset position
- [ ] Rotation, including 180° (origin at the bottom or right)
- [ ] Settings window, settings stored as a readable file
- [ ] Portable build without admin rights, signed Windows builds
- [ ] "Coming from PixelRuler" page with familiar shortcuts

## 1.0 – Beyond the classics

- [ ] Edge snapping with adjustable tolerance
- [ ] Spacing mode: distance to the nearest edges in all directions
- [ ] Bounding-box measurement, several measurements held on screen
- [ ] Floating guides that show distances between them
- [ ] Copy measurements as px, rem or CSS
- [ ] WCAG contrast check between two picked colours
- [ ] Freeze mode: measure on a screenshot (the main mode on Wayland)
- [ ] Packages: winget, Scoop, Flathub, AppImage, Homebrew tap, PyPI
- [ ] At least five languages, including one right-to-left language

## 1.x – Later

- [ ] Colour-blindness simulation in the magnifier
- [ ] Screenshot with measurements drawn in
- [ ] Frames with aspect ratio and grid, device templates
- [ ] Integrations with design tools

## Platform strategy

| | Windows | macOS | Linux X11 | Linux Wayland |
| --- | --- | --- | --- | --- |
| Floating ruler | yes | yes | yes | through XWayland |
| Global cursor position | yes | yes | yes | no (freeze mode instead) |
| Screen capture | yes | after "Screen Recording" permission | yes | screenshot portal |
| Global hotkeys | yes | yes | yes | GlobalShortcuts portal |

macOS builds are ad-hoc signed but not notarized, so users approve the app once
in System Settings. Windows builds are signed through the SignPath Foundation
once the first release exists.

## Out of scope

- Telemetry, accounts or any paid features
- A browser extension or web version
