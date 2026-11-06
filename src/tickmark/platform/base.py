"""Interfaces between the UI and the operating system.

Screen capture and hotkey registration report their result through a callback
rather than a return value. Windows, macOS and X11 answer immediately, but the
Wayland portals answer later over D-Bus, often after asking the user. One
callback-based interface covers both without a second code path in the UI.

All coordinates are physical pixels on the virtual desktop.
"""

from collections.abc import Callable
from enum import Enum, auto
from typing import Protocol

from tickmark.core.geometry import Point, Rect
from tickmark.core.pixels import PixelBuffer


class PlatformKind(Enum):
    WINDOWS = "windows"
    MACOS = "macos"
    X11 = "x11"
    WAYLAND = "wayland"
    UNKNOWN = "unknown"


class Capability(Enum):
    """Things a backend may or may not be able to do on the current system."""

    GLOBAL_CURSOR_POSITION = auto()
    """Read the cursor position anywhere on screen, not only over Tickmark's windows."""

    SCREEN_CAPTURE = auto()
    """Read screen pixels, possibly after the user grants permission."""

    GLOBAL_HOTKEYS = auto()
    """Bind shortcuts that work while another application has focus."""

    STAY_ON_TOP = auto()
    """Keep a window above all other windows."""

    FREE_WINDOW_POSITIONING = auto()
    """Place a window at an exact position on the desktop."""

    CURSOR_WARP = auto()
    """Move the cursor programmatically, e.g. with the arrow keys."""


class CursorSource(Protocol):
    def cursor_position(self) -> Point | None:
        """Return the cursor position, or ``None`` when the system does not reveal it."""
        ...


class ScreenGrabber(Protocol):
    def capture(self, region: Rect, on_done: Callable[[PixelBuffer | None], None]) -> None:
        """Capture ``region`` and call ``on_done`` exactly once.

        ``on_done`` receives ``None`` when capturing failed or the user declined.
        """
        ...


class HotkeyService(Protocol):
    def register(
        self,
        action: str,
        shortcut: str,
        on_triggered: Callable[[], None],
        on_result: Callable[[bool], None],
    ) -> None:
        """Ask the system to bind ``shortcut`` to ``action``.

        ``shortcut`` uses Qt's portable key sequence text, for example ``"Alt+F1"``.
        ``on_result`` is called exactly once with whether the binding is active.
        Registering an action again replaces its previous binding.
        """
        ...

    def unregister(self, action: str) -> None:
        """Remove the binding for ``action``; unknown actions are ignored."""
        ...


class PlatformBackend(Protocol):
    @property
    def kind(self) -> PlatformKind: ...

    @property
    def capabilities(self) -> frozenset[Capability]: ...

    @property
    def cursor(self) -> CursorSource: ...

    @property
    def screen(self) -> ScreenGrabber: ...

    @property
    def hotkeys(self) -> HotkeyService: ...
