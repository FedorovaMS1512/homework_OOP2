from src.square import Square
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


