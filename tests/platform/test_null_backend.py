from tickmark.core.geometry import Rect
from tickmark.core.pixels import PixelBuffer
from tickmark.platform.base import PlatformBackend, PlatformKind
from tickmark.platform.null import NullBackend


def test_null_backend_satisfies_the_backend_interface() -> None:
    backend: PlatformBackend = NullBackend()  # checked by pyright

    assert backend.kind is PlatformKind.UNKNOWN
    assert backend.capabilities == frozenset()


def test_cursor_position_is_unknown() -> None:
    assert NullBackend().cursor.cursor_position() is None


def test_capture_reports_failure_exactly_once() -> None:
    results: list[PixelBuffer | None] = []

    NullBackend().screen.capture(Rect(0, 0, 10, 10), results.append)

    assert results == [None]


def test_hotkey_registration_reports_failure_exactly_once() -> None:
    results: list[bool] = []
    triggered: list[None] = []

    hotkeys = NullBackend().hotkeys
    hotkeys.register("toggle-ruler", "Alt+F1", lambda: triggered.append(None), results.append)
    hotkeys.unregister("toggle-ruler")

    assert results == [False]
    assert triggered == []


def test_backend_can_report_a_known_kind() -> None:
    assert NullBackend(kind=PlatformKind.WAYLAND).kind is PlatformKind.WAYLAND
