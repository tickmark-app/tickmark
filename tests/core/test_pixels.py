import pytest

from tickmark.core.pixels import PixelBuffer


def make_buffer(width: int, height: int) -> PixelBuffer:
    """Each pixel encodes its own position: (x, y, x + y, 255)."""
    data = bytearray()
    for y in range(height):
        for x in range(width):
            data += bytes((x, y, x + y, 255))
    return PixelBuffer(width=width, height=height, data=bytes(data))


def test_pixel_reads_row_major_rgba() -> None:
    buffer = make_buffer(width=3, height=2)

    assert buffer.pixel(0, 0) == (0, 0, 0, 255)
    assert buffer.pixel(2, 0) == (2, 0, 2, 255)
    assert buffer.pixel(1, 1) == (1, 1, 2, 255)
    assert buffer.pixel(2, 1) == (2, 1, 3, 255)


@pytest.mark.parametrize(("x", "y"), [(-1, 0), (0, -1), (3, 0), (0, 2)])
def test_pixel_outside_image_raises(x: int, y: int) -> None:
    buffer = make_buffer(width=3, height=2)

    with pytest.raises(IndexError, match="outside"):
        buffer.pixel(x, y)


def test_wrong_data_length_is_rejected() -> None:
    with pytest.raises(ValueError, match="needs 24 bytes, got 23"):
        PixelBuffer(width=3, height=2, data=bytes(23))


def test_negative_size_is_rejected() -> None:
    with pytest.raises(ValueError, match="must not be negative"):
        PixelBuffer(width=-1, height=2, data=b"")


def test_empty_buffer_is_valid() -> None:
    assert PixelBuffer(width=0, height=0, data=b"").width == 0
