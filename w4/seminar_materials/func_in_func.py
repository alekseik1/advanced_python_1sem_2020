def func1(a, b, f2):
    print('Inside func1')
    print(a)
    print(b)
    return f2


def func2():
    print('Inside func2')
    return -7


print(func1(1, 2, func2)())
