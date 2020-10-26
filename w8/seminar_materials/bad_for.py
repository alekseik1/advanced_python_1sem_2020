def all_numbers(start, final):
    current = start
    while current < final:
        yield current
        current += 1

# Context 1: a, b
# ....
# ....
# f()
#    ------->
#            Context 2:
#            коды из f()
#            ....
#            ....


# a = [x for x in range(10**10)]  # [0, ... , 10**10]
result = []
for i in all_numbers(0, 10**10):
    if i % 2 == 0:
        pass

