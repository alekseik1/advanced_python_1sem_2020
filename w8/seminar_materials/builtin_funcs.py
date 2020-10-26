import math
# Объекты, по которым можно проитерироваться, называются iterable

# filter, map, zip
# 1. filter(func1, iterable)
def is_even(s):
    return s % 2 == 0


print('Even numbers')
print(list(filter(is_even, [1, 2, 3, 4, 5, 6])))
for i in filter(is_even, [1, 2, 3, 4, 5, 6]):
    print(i)

# lambda
print(list(filter(lambda x: x % 2 == 0, range(100))))
# lambda arg1, arg2, arg3: return_value

# 2. map(func, iterable)
print('Squares')
print(list(map(lambda x: x**2, range(100))))

# 3. zip(iter1, iter2)
print(list(zip([0, 2, 4, 6, 8], [1, 3, 5, 7])))

# 4. enumerate(iter)
# (position, element)
# ['a', 'b', 'c'] -> [(0, 'a'), (1, 'b'), (2, 'c')]

