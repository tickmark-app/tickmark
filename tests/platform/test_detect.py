import pytest

from tickmark.platform.base import PlatformKind
from tickmark.platform.detect import current_platform, detect_platform


@pytest.mark.parametrize(
    ("sys_platform", "environ", "expected"),
    [
        ("win32", {}, PlatformKind.WINDOWS),
        ("darwin", {}, PlatformKind.MACOS),
        ("linux", {"WAYLAND_DISPLAY": "wayland-0"}, PlatformKind.WAYLAND),
        ("linux", {"XDG_SESSION_TYPE": "Wayland"}, PlatformKind.WAYLAND),
        # XWayland sets DISPLAY inside Wayland sessions; Wayland must win.
        ("linux", {"WAYLAND_DISPLAY": "wayland-0", "DISPLAY": ":0"}, PlatformKind.WAYLAND),
        ("linux", {"DISPLAY": ":0"}, PlatformKind.X11),
        ("linux", {"XDG_SESSION_TYPE": "x11"}, PlatformKind.X11),
        ("freebsd14", {"DISPLAY": ":0"}, PlatformKind.X11),
        ("linux", {}, PlatformKind.UNKNOWN),
        ("linux", {"XDG_SESSION_TYPE": "tty"}, PlatformKind.UNKNOWN),
        ("emscripten", {"DISPLAY": ":0"}, PlatformKind.UNKNOWN),
    ],
)
def test_detect_platform(
    sys_platform: str, environ: dict[str, str], expected: PlatformKind
) -> None:
    assert detect_platform(sys_platform, environ) is expected


def test_current_platform_returns_a_kind() -> None:
    assert isinstance(current_platform(), PlatformKind)
