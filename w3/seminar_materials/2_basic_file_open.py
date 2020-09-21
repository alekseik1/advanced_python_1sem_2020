f = open('text.txt', 'r')
# r - только чтение, w - запись
# b, t - байтовое и текстовое
print(f.read(3))
f.close()

# with - contextmanager
# contextmanager: __enter__() и __exit__()
with open('text.txt', 'r') as f:
    print(f.readlines())

