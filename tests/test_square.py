from src.square import Square
from src.triangle import Triangle
from src.rectangle import Rectangle
from src.circle import Circle
import pytest


@pytest.mark.parametrize(
    ('a', 'area'),
    [
     pytest.param(2, 4, id="integer"),
     pytest.param(2.2, 4.84, id="float")
     ]

)
def test_square_area(a, area):
    s = Square(a)
    assert (s.get_area == area), f"Area for square with sides {a} and should be {area}"


@pytest.mark.parametrize(
    ('a', 'perimeter'),
    [pytest.param(2, 8, id="integer"),
     pytest.param(2.2, 8.8, id="float")
    ]
)
def test_square_perimeter(a, perimeter):
    s = Square(a)
    assert (s.get_perimeter == perimeter), f"Perimeter for rectangle with sides {a} should be {perimeter}"


@pytest.mark.parametrize(
    ("a", "expected_exception", "text_exception"),
    [
        pytest.param(0, ValueError, "Square sides can't be less than 0", id="zero_side"),
        pytest.param(-2, ValueError, "Square sides can't be less than 0", id="negative_side"),
    ],
)
def test_square_invalid_side(a, expected_exception, text_exception: str):
    with pytest.raises(expected_exception, match=text_exception):
        Square(a)


class TestSquareAddArea:

    def test_square_add_area(self):

            square = Square(5)  # площадь квадрата = 25
            triangle = Triangle(3, 4, 5)  # площадь треугольника = 6
            rectangle = Rectangle(4, 6)  # площадь прямоугольника = 24
            circle = Circle(2)  # площадь круга ≈ 12.57
            another_square = Square(3)  # площадь второго квадрата = 9

            assert square.add_area(triangle) == 31
            assert square.add_area(rectangle) == 49
            assert square.add_area(circle) == 37.57
            assert square.add_area(another_square) == 34

    def test_square_add_area_invalid_object(self):

        square = Square(4)
        with pytest.raises(ValueError, match="Should be a Figure"):
            square.add_area("invalid object")


















