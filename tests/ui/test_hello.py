from PySide6.QtCore import QEvent
from PySide6.QtWidgets import QApplication
from pytestqt.qtbot import QtBot

from tickmark.platform.base import PlatformKind
from tickmark.ui.hello import HelloWindow


def test_shows_detected_desktop(qtbot: QtBot) -> None:
    window = HelloWindow(PlatformKind.WAYLAND)
    qtbot.addWidget(window)

    assert window.platform_label.text() == "Desktop: wayland"


def test_shows_scale_factor(qtbot: QtBot) -> None:
    window = HelloWindow(PlatformKind.X11)
    qtbot.addWidget(window)
    window.show()
    qtbot.waitExposed(window)

    expected = f"Screen scale: {window.devicePixelRatioF():g}"
    assert window.scale_label.text() == expected


def test_scale_label_follows_screen_changes(qtbot: QtBot) -> None:
    window = HelloWindow(PlatformKind.X11)
    qtbot.addWidget(window)
    window.scale_label.setText("stale")

    QApplication.sendEvent(window, QEvent(QEvent.Type.DevicePixelRatioChange))

    assert window.scale_label.text().startswith("Screen scale: ")
