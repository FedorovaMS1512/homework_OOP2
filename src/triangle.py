import math

from src.figure import Figure


class Triangle(Figure):
    a: int
    b: int
    c: int

    def __init__(self, a, b, c):
        if not (a + b > c and a + c > b and b + c > a):
            raise ValueError("Нельзя создать треугольник")
        self.a = a
        self.b = b
        self.c = c

    @property
    def get_area(self):
        # Вычисление полупериметра
        p = (self.a + self.b + self.c) / 2

        # Вычисление площади по формуле Герона
        area = math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
        return area

    @property
    def get_perimeter(self):
        return self.a + self.b + self.c
