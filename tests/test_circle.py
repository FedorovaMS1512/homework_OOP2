from src.circle import Circle
import pytest


@pytest.mark.parametrize(
    ("radius", "area"),
    [
        pytest.param(5, 78.54, id="integer"),
        pytest.param(6.2, 120.76, id="float"),
    ],
)
def test_circle_area(radius, area):
    c = Circle(radius)
    assert c.get_area == area, f"Area for circle with radius {radius} should be {area}"


@pytest.mark.parametrize(
    ("radius", "perimeter"),
    [
       pytest.param(5, 31.42, id="integer"),
       pytest.param(6.2, 38.96, id="float")],
)
def test_rectangle_perimeter(radius, perimeter):
    c = Circle(radius)
    assert (c.get_perimeter == perimeter), f"Perimeter for circle with radius {radius} should be {perimeter}"


@pytest.mark.parametrize(
    ("radius", "expected_exception", "text_exception"),
    [
        pytest.param(0, ValueError, "Radius can't be less than 0", id="zero_sides"),
        pytest.param(-2, ValueError, "Radius can't be less than 0", id="negative_side"),
    ],
)
def test_circle_invalid_sides(radius, expected_exception, text_exception: str):
    with pytest.raises(expected_exception, match=text_exception):
        Circle(radius)



