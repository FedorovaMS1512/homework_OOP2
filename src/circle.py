import math

from src.figure import Figure


class Circle(Figure):
    r: int

    def __init__(self, r):
        if r <= 0:
            raise ValueError("Radius can't be less than 0")
        self.r = r

    @property
    def get_area(self):
        area = math.pi * (self.r**2)
        return area

    @property
    def get_perimeter(self):
        perimeter = 2 * math.pi * self.r
        return perimeter
