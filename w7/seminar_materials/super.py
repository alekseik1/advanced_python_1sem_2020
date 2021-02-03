class A:
    def print(self):
        print(1)
        print(type(self))


class B(A):

    def __init__(self, a):
        super().__init__()
        self.a = a

    def print(self):
        super().print()
        print('I\'m second')


b = B()
b.print()

"""
Java:
class MyClass {
    public void myFunc() {
        this.print();
    }
}
"""

