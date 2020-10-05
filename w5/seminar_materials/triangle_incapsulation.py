class AbstractFigure:

    _area = -1
    _perimeter = -1

    def __init__(self, area, length):
        self._area = area
        self._length = length

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
        if self._perimeter == -1:
            self._perimeter = self.side1 + self.side2 + self.side3
        return self._perimeter

    def get_area(self):
        if self._area == -1:
            p = self.get_perimeter()/2
            self._area = (p*(p - self.side1)*(p - self.side2)*(p - self.side3))**0.5
        return self._area


tr1 = Triangle(2, 5, 6)
tr2.print_self()
# Want to see error here
# tr1.side1
tr1.print_self()

# Private -- self only; starts with __
# Protected -- self and children; starts with _
# Public -- anyone; starts with neither __ nor _

