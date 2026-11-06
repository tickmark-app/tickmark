"""Integer geometry in physical pixels.

Tickmark measures in physical (device) pixels. Conversion to Qt's logical,
device-independent pixels happens only at the UI boundary, so every value in
this module is exactly what the screen shows.
"""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Point:
    """A position on the virtual desktop, in physical pixels."""

    x: int
    y: int


@dataclass(frozen=True, slots=True)
class Rect:
    """An axis-aligned rectangle in physical pixels.

    The rectangle is half-open: it contains ``left <= x < right`` and
    ``top <= y < bottom``, so a 10 px wide rectangle covers exactly 10 pixels.
    """

    x: int
    y: int
    width: int
    height: int

    def __post_init__(self) -> None:
        if self.width < 0 or self.height < 0:
            msg = f"Rect size must not be negative, got {self.width}x{self.height}"
            raise ValueError(msg)

    @property
    def left(self) -> int:
        return self.x

    @property
    def top(self) -> int:
        return self.y

    @property
    def right(self) -> int:
        return self.x + self.width

    @property
    def bottom(self) -> int:
        return self.y + self.height

    def contains(self, point: Point) -> bool:
        return self.left <= point.x < self.right and self.top <= point.y < self.bottom
