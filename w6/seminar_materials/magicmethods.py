class Computer:

    def __init__(self, proc_family, total_ram):
        self.proc_family = proc_family
        self.total_ram = total_ram

    def __gt__(self, other):
        if self.proc_family > other.proc_family:
            return True
        elif self.proc_family < other.proc_family:
            return False
        else:
            return self.total_ram > other.total_ram

    def __abs__(self):
        return 5+self.proc_family

    def __mult__(self, other):
        # a & b
        pass

    def __str__(self):
        return 'CPU family: {}\nTotal RAM: {}'.format(self.proc_family, self.total_ram)


# lt - <
# gt - >
# le - <=
# ge - >=
# ne - !=
# abs - abs()

# str - str()
# repr - later
comp1 = Computer(10, 4)
comp2 = Computer(9, 16)
# print(comp1 > comp2)
# print(comp1 < comp2)
# print(comp1 == comp2)
# print(abs(comp1))
print(comp1)

