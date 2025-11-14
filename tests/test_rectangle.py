from src.rectangle import Rectangle
from src.circle import Circle
from src.triangle import Triangle
from src.square import Square
import pytest


@pytest.mark.parametrize(
    ("a", "b", "area"),
    [pytest.param(2, 4, 8, id="integer"), pytest.param(2.1, 4.1, 8.61, id="float")],
)
def test_rectangle_area(a, b, area):
    r = Rectangle(a, b)
    assert (
        r.get_area == area
    ), f"Area for rectangle with sides {a} and {b} should be {area}"


@pytest.mark.parametrize(
    ("a", "b", "perimeter"),
    [pytest.param(2, 4, 12, id="integer"), pytest.param(2.2, 4.2, 12.8, id="float")],
)
def test_rectangle_perimeter(a, b, perimeter):
    r = Rectangle(a, b)
    assert (
        r.get_perimeter == perimeter
    ), f"Perimeter for rectangle with sides {a} and {b} should be {perimeter}"


@pytest.mark.parametrize(
    ("a", "b", "expected_exception", "text_exception"),
    [
        pytest.param(
            0, 0, ValueError, "Rectangle sides can't be less than 0", id="zero_sides"
        ),
        pytest.param(
            -2,
            -4,
            ValueError,
            "Rectangle sides can't be less than 0",
            id="negative_side",
        ),
    ],
)
def test_rectangle_invalid_sides(a, b, expected_exception, text_exception: str):
    with pytest.raises(expected_exception, match=text_exception):
        Rectangle(a, b)


class TestRectangleAddArea:

    @pytest.mark.parametrize(
        "rectangle, some_figure, expected_area",
        [
            (Rectangle(4, 6), Circle(2), 36.57),
            (Rectangle(4, 6), Triangle(3, 4, 5), 30),
            (Rectangle(4, 6), Square(5), 49),
            (Rectangle(4, 6), Rectangle(3, 5), 39),
        ],
    )
    def test_rectangle_add_area(self, rectangle, some_figure, expected_area):
        assert rectangle.add_area(some_figure) == expected_area

    def test_rectangle_add_area_invalid_object(self):

        rectangle = Rectangle(4, 6)
        with pytest.raises(ValueError, match="Should be a Figure"):
            rectangle.add_area("invalid object")
