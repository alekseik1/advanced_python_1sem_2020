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


@print_action()
def h1():
    print('asdasd')

hello(2, 5)
hello(2, 5)
hello(2, 5)
# -> decorator('msg')(func)(2, 5)
# log

