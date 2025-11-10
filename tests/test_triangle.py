from src.triangle import Triangle
from src.rectangle import Rectangle
from src.square import Square
from src.circle import Circle
import pytest


@pytest.mark.parametrize(
    ("a", "b", "c", "area"),
    [
        pytest.param(4, 6, 8, 11.62, id="integer"),
        pytest.param(4.2, 5.3, 6.4, 11.07, id="float"),
    ],
)
def test_triangle_area(a, b, c, area):
    t = Triangle(a, b, c)
    assert (t.get_area == area), f"Area for triangle with sides {a}, {b}, {c} should be {area}"


@pytest.mark.parametrize(
    ("a", "b", "c", "perimeter"),
    [
        pytest.param(2, 4, 5, 11, id="integer"),
        pytest.param(2.5, 4.5, 6.5, 13.5, id="float"),
    ],
)
def test_triangle_perimeter(a, b, c, perimeter):
    t = Triangle(a, b, c)
    assert (t.get_perimeter == perimeter), f"Area for triangle with sides {a}, {b}, {c} should be {perimeter}"


@pytest.mark.parametrize(
    ("a", "b", "c", "expected_exception", "text_exception"),
    [
        pytest.param(-2, 4, 5, ValueError, "Triangle sides can't be less than 0", id='negative_side'),
        pytest.param(0, 0, 0, ValueError, "Triangle sides can't be less than 0", id='zero_sides'),
        pytest.param(1, 1, 3, ValueError, "Нельзя создать треугольник", id='invalid_triangle')
    ]
)
def test_triangle_invalid_sides(a, b, c, expected_exception, text_exception: str):
    with pytest.raises(expected_exception, match=text_exception):
        Triangle(a, b, c)


class TestTriangleAddArea:

    def test_triangle_add_area(self):
        triangle = Triangle(3, 4, 5)   # площадь треугольника = 6
        rectangle = Rectangle(4, 6)      # площадь прямоугольника = 24
        square = Square(5)                     # площадь квадрата = 25
        circle = Circle(2)                     # площадь круга ≈ 12.566
        another_triangle = Triangle(6, 8, 10)  # площадь второго треугольника = 24

        assert triangle.add_area(rectangle) == 30
        assert triangle.add_area(square) == 31
        assert triangle.add_area(another_triangle) == 30
        assert triangle.add_area(circle) == 18.57

    def test_triangle_add_area_invalid_object(self):

        triangle = Triangle(4, 6, 8)
        with pytest.raises(ValueError, match="Should be a Figure"):
            triangle.add_area("invalid object")

