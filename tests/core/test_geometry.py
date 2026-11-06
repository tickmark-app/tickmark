import pytest
from hypothesis import given
from hypothesis import strategies as st

from tickmark.core.geometry import Point, Rect

coordinates = st.integers(min_value=-10_000, max_value=10_000)
lengths = st.integers(min_value=0, max_value=10_000)


def test_edges_follow_from_origin_and_size() -> None:
    rect = Rect(x=10, y=20, width=30, height=40)

    assert (rect.left, rect.top, rect.right, rect.bottom) == (10, 20, 40, 60)


def test_rect_is_half_open() -> None:
    rect = Rect(x=0, y=0, width=10, height=10)

    assert rect.contains(Point(0, 0))
    assert rect.contains(Point(9, 9))
    assert not rect.contains(Point(10, 9))
    assert not rect.contains(Point(9, 10))


def test_empty_rect_contains_nothing() -> None:
    assert not Rect(x=5, y=5, width=0, height=0).contains(Point(5, 5))


@pytest.mark.parametrize(("width", "height"), [(-1, 0), (0, -1), (-5, -5)])
def test_negative_size_is_rejected(width: int, height: int) -> None:
    with pytest.raises(ValueError, match="must not be negative"):
        Rect(x=0, y=0, width=width, height=height)


@given(
    rect=st.builds(Rect, x=coordinates, y=coordinates, width=lengths, height=lengths),
    point=st.builds(Point, x=coordinates, y=coordinates),
)
def test_contains_matches_bounds(rect: Rect, point: Point) -> None:
    inside = rect.x <= point.x < rect.x + rect.width and rect.y <= point.y < rect.y + rect.height

    assert rect.contains(point) is inside


@given(x=coordinates, y=coordinates, width=st.integers(0, 500), height=st.integers(0, 500))
def test_width_counts_exactly_the_covered_pixels(x: int, y: int, width: int, height: int) -> None:
    rect = Rect(x=x, y=y, width=width, height=height)

    covered = sum(rect.contains(Point(px, rect.top)) for px in range(x - 1, x + width + 1))

    assert covered == (width if height > 0 else 0)
