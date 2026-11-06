"""Screen pixels without Qt.

Platform backends convert whatever their system returns into a
``PixelBuffer``, so colour picking and edge detection in ``tickmark.core``
work the same on every operating system and can be tested with plain bytes.
"""

from dataclasses import dataclass

BYTES_PER_PIXEL = 4
"""Pixels are stored as RGBA, 8 bits per channel."""

type Rgba = tuple[int, int, int, int]


@dataclass(frozen=True, slots=True)
class PixelBuffer:
    """A row-major RGBA8888 image in physical pixels, without row padding."""

    width: int
    height: int
    data: bytes

    def __post_init__(self) -> None:
        if self.width < 0 or self.height < 0:
            msg = f"PixelBuffer size must not be negative, got {self.width}x{self.height}"
            raise ValueError(msg)
        expected = self.width * self.height * BYTES_PER_PIXEL
        if len(self.data) != expected:
            msg = (
                f"PixelBuffer of {self.width}x{self.height} needs {expected} bytes, "
                f"got {len(self.data)}"
            )
            raise ValueError(msg)

    def pixel(self, x: int, y: int) -> Rgba:
        """Return the RGBA value at ``(x, y)``; raise ``IndexError`` outside the image."""
        if not (0 <= x < self.width and 0 <= y < self.height):
            msg = f"Pixel ({x}, {y}) is outside the {self.width}x{self.height} image"
            raise IndexError(msg)
        offset = (y * self.width + x) * BYTES_PER_PIXEL
        red, green, blue, alpha = self.data[offset : offset + BYTES_PER_PIXEL]
        return (red, green, blue, alpha)
