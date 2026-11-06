"""A placeholder window that proves the toolchain works end to end.

It shows the detected desktop and the screen's scale factor, which is the
first thing to check on a new machine. It is replaced by the ruler in 0.1.
"""

from PySide6.QtCore import QEvent
from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget

from tickmark.platform.base import PlatformKind


class HelloWindow(QWidget):
    def __init__(self, platform_kind: PlatformKind, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.setWindowTitle("Tickmark")

        self.platform_label = QLabel(self.tr("Desktop: {0}").format(platform_kind.value))
        self.scale_label = QLabel()

        layout = QVBoxLayout(self)
        layout.addWidget(QLabel(self.tr("Hello, Tickmark")))
        layout.addWidget(self.platform_label)
        layout.addWidget(self.scale_label)

        self.update_scale_label()

    def event(self, event: QEvent) -> bool:
        # Sent when the window moves to a screen with a different scale factor.
        if event.type() == QEvent.Type.DevicePixelRatioChange:
            self.update_scale_label()
        return super().event(event)

    def update_scale_label(self) -> None:
        ratio = self.devicePixelRatioF()
        self.scale_label.setText(self.tr("Screen scale: {0:g}").format(ratio))
