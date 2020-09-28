# Without arguments
# decorator(func)(2, 5)
def dec1(func):
    def wrapper(a, b):
        print('deduction')
        func(a, b)
    return wrapper


def dec2(func):
    print(2)
    return func

@dec2
def p():
    print('func')


exit(0)

def print_action(msg='summing'):
    print('called when you pass arguments to decorator announcement')
    def wrapper(func):
        print('called only when function is first time decorated')
        def wrapped_func(*args, **kwargs):
            print('summing numbers')
            return func(*args, **kwargs)
        return wrapped_func
    return wrapper


@print_action('msg')
def hello(a, b):
    print(a+b)


@dec1
def h(a, b):
    print(a-b)

@print_action('newnew')
def new(a, b):
    print('oo')


h(2, 5)
hello(5, 10)
# 'msg'(5, 10)
# decorator('msg')(func)(5, 10)



