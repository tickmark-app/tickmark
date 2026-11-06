"""Find out which kind of desktop Tickmark is running on."""

import os
import sys
from collections.abc import Mapping

from tickmark.platform.base import PlatformKind


def detect_platform(sys_platform: str, environ: Mapping[str, str]) -> PlatformKind:
    """Classify the desktop from ``sys.platform`` and the environment.

    On Linux a Wayland session wins over X11, because ``DISPLAY`` is also set
    inside Wayland sessions for XWayland.
    """
    if sys_platform == "win32":
        return PlatformKind.WINDOWS
    if sys_platform == "darwin":
        return PlatformKind.MACOS
    if sys_platform.startswith(("linux", "freebsd", "openbsd", "netbsd")):
        session_type = environ.get("XDG_SESSION_TYPE", "").lower()
        if environ.get("WAYLAND_DISPLAY") or session_type == "wayland":
            return PlatformKind.WAYLAND
        if environ.get("DISPLAY") or session_type == "x11":
            return PlatformKind.X11
    return PlatformKind.UNKNOWN


def current_platform() -> PlatformKind:
    return detect_platform(sys.platform, os.environ)
