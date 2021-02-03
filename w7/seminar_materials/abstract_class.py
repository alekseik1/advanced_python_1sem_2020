from abc import abstractmethod, ABC
"""
>>> import datetime
>>> datetime.date

>>> from datetime import date
>>> date
>>> datetime.date # error

>>> import datetime.submodule1
>>> datetime.submodule1.func_a()

>>> from datetime import submodule1
>>> submodule1.func_a()

>>> from datetime.submodule1 import func_a
>>> func_a()
"""

class A(ABC):

    @abstractmethod
    def redefine_me(self):
        pass


class B(A):
    def redefine_me(self):
        print(1)


b = B()
b.redefine_me()
a = A()
a.redefine_me()
# a.redefine_me()

