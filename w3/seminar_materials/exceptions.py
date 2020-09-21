import json


class MyExceptionHello(Exception):
    pass


def b():
    try:
        # json.loads('')
        raise MyExceptionHello("hell")
        print('never executed')
    except MyExceptionHello as e:
        print("Hello, it's error!")
def a():
    b()


a()

