def generate_even():
    start = 0
    while True:
        yield start
        print('Yield is done')
        start += 2
        if start == 6:
            break

def empty_generator():
    yield 1

initialized_generator = generate_even()

# Dangerous
# for i in initialized_generator:
#     print(i)

# next(initialized_generator)

gen = empty_generator()
for i in gen:
    print(i)

for j in gen:
    print('never here')

