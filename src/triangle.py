import math

from src.figure import Figure


class Triangle(Figure):

    def __init__(self, a, b, c):
        if not (a + b > c and a + c > b and b + c > a):
            raise ValueError("Нельзя создать треугольник")
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Triangle sides can't be less than 0")
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
