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
    [
     pytest.param(2, 4, 12, id="integer"),
     pytest.param(2.2, 4.2, 12.8, id="float")
     ],
)
def test_rectangle_perimeter(a, b, perimeter):
    r = Rectangle(a, b)
    assert (r.get_perimeter == perimeter), f"Perimeter for rectangle with sides {a} and {b} should be {perimeter}"


@pytest.mark.parametrize(
    ("a", "b", "expected_exception", "text_exception"),
    [
        pytest.param(0, 0, ValueError, "Rectangle sides can't be less than 0", id="zero_sides"),
        pytest.param(-2, -4, ValueError, "Rectangle sides can't be less than 0", id="negative_side"),
    ],
)
def test_rectangle_invalid_sides(a, b, expected_exception, text_exception: str):
    with pytest.raises(expected_exception, match=text_exception):
        Rectangle(a, b)


class TestCircleAddArea:

    def test_circle_add_area(self):

        circle = Circle(2)                     # площадь круга ≈ 12.57
        triangle = Triangle(3, 4, 5)  # площадь треугольника = 6
        rectangle = Rectangle(4, 6)       # площадь прямоугольника = 24
        square = Square(5)                     # площадь квадрата = 25
        another_circle = Circle(3)             # площадь второго круга ≈ 28.27

        assert circle.add_area(triangle) == 18.57
        assert circle.add_area(rectangle) == 36.57
        assert circle.add_area(square) == 37.57
        assert circle.add_area(another_circle) == 40.84

    def test_rectangle_add_area_invalid_object(self):

        rectangle = Rectangle(4, 6)
        with pytest.raises(ValueError, match="Should be a Figure"):
            rectangle.add_area("invalid object")
