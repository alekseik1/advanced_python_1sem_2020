class AbstractFigure:
    # MyCamelCaseExample -- camel case
    # my_camel_case_example -- snake case

    # Method
    def __init__(self, area, length):
        # Field
        self.area = area
        self.length = length

    def print_self(self):
        print('Area is:', self.area)
        print('Length:', self.length)


fig1 = AbstractFigure(2, 5)
fig1.print_self()


fig2 = AbstractFigure(9, 10)
fig2.print_self()
# print(fig1.area)

