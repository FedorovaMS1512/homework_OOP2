from src.circle import Circle
from src.triangle import Triangle
from src.rectangle import Rectangle
from src.square import Square
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


class TestCircleAddArea:
    def test_circle_add_area(self):

        circle = Circle(2)                     # площадь круга ≈ 12.57
        triangle = Triangle(3, 4, 5)  # площадь треугольника = 6
        rectangle = Rectangle(4, 6)      # площадь прямоугольника = 24
        square = Square(5)                     # площадь квадрата = 25
        another_circle = Circle(3)             # площадь второго круга ≈ 28.27

        assert circle.add_area(triangle) == 18.57
        assert circle.add_area(rectangle) == 36.57
        assert circle.add_area(square) == 37.57
        assert circle.add_area(another_circle) == 40.84

    def test_circle_add_area_invalid_object(self):

        circle = Circle(4)
        with pytest.raises(ValueError, match="Should be a Figure"):
            circle.add_area("invalid object")
