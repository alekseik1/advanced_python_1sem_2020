class AbstractFigure:

    area = 0
    length = 0

    def __init__(self, area, length):
        self.area = area
        self.length = length

    def get_area(self):
        raise NotImplementedError()

    def get_perimeter(self):
        raise NotImplementedError()

    def print_self(self):
        print('Area is:', self.get_area())
        print('Perimeter is:', self.get_perimeter())


class Triangle(AbstractFigure):

    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def get_perimeter(self):
        return self.side1 + self.side2 + self.side3

    def get_area(self):
        p = self.get_perimeter()/2
        return (p*(p - self.side1)*(p - self.side2)*(p - self.side3))**0.5


tr1 = Triangle(2, 5, 6)
tr1.print_self()

# abstract1 = AbstractFigure(2, 5)
# abstract1.print_self()

