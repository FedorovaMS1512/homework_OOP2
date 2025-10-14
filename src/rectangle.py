from src.figure import Figure


class Rectangle(Figure):

    def __init__(self, a, b):
        if a <= 0 or b <= 0:
            raise ValueError("Rectangle sides can't be less than 0")
        self.a = a
        self.b = b

    @property
    def get_area(self):
        return self.a * self.b

    @property
    def get_perimeter(self):
        return (self.a + self.b) * 2
