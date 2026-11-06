"""Application entry point."""

import sys
from collections.abc import Sequence

from PySide6.QtWidgets import QApplication

from tickmark import __version__
from tickmark.platform.detect import current_platform
from tickmark.ui.hello import HelloWindow


def main(argv: Sequence[str] | None = None) -> int:  # pragma: no cover - runs the event loop
    app = QApplication(list(argv) if argv is not None else sys.argv)
    app.setApplicationName("Tickmark")
    app.setOrganizationName("tickmark-app")
    app.setApplicationVersion(__version__)

    window = HelloWindow(current_platform())
    window.show()
    return app.exec()
