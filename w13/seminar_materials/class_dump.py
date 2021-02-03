import pickle


class MyClass:
    def __init__(self, a, b):
        self.a, self.b = a, b

# {'a': <value_a>, 'b': <value_b>}
# 1. Сам класс как таковой, без инициализации
# Если сериализуем объект класса:
# 2. Словарь из значений полей
# 3. (1) + (2) --> в вывод

a = MyClass(2, 'a')
print('__dict__ is', a.__dict__)
dump = pickle.dumps(a)
print('dumped version:', dump)
b = pickle.loads(dump)
print('loaded version:', b)
print(b.__dict__)

