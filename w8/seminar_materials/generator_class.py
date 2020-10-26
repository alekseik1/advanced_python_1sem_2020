class MyIterable:

    def __iter__(self):
        yield 1
        yield 2

for i in MyIterable():
    print(i)

