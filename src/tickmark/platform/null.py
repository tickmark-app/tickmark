"""A backend that can do nothing.

Used on unknown systems and in tests. Every request completes immediately with
the "not available" result, so the UI exercises its fallback paths.
"""

from collections.abc import Callable
from dataclasses import dataclass, field

from tickmark.core.geometry import Point, Rect
from tickmark.core.pixels import PixelBuffer
from tickmark.platform.base import Capability, PlatformKind


class NullCursorSource:
    def cursor_position(self) -> Point | None:
        return None


class NullScreenGrabber:
    def capture(self, region: Rect, on_done: Callable[[PixelBuffer | None], None]) -> None:
        on_done(None)


class NullHotkeyService:
    def register(
        self,
        action: str,
        shortcut: str,
        on_triggered: Callable[[], None],
        on_result: Callable[[bool], None],
    ) -> None:
        on_result(False)

    def unregister(self, action: str) -> None:
        pass


@dataclass(frozen=True)
class NullBackend:
    kind: PlatformKind = PlatformKind.UNKNOWN
    capabilities: frozenset[Capability] = frozenset()
    cursor: NullCursorSource = field(default_factory=NullCursorSource)
    screen: NullScreenGrabber = field(default_factory=NullScreenGrabber)
    hotkeys: NullHotkeyService = field(default_factory=NullHotkeyService)
