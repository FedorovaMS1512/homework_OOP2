from src.figure import Figure


class Square(Figure):

    def __init__(self, a):
        if a <= 0:
            raise ValueError("Square sides can't be less than 0")
        self.a = a

    @property
    def get_area(self):
        return round((self.a**2), 2)

    @property
    def get_perimeter(self):
        return round((self.a * 4), 2)
