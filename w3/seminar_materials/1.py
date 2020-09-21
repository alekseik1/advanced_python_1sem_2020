# Открыть файл
f = open('text.txt', 'r')
# f.seek(0) -- вернуть каретку в начало файла
# Считать все строки
x = f.readlines()   # type: list[str]
print(x[0].strip())
print(x[1].lstrip())    # Пустая
print(x[2].rstrip())
# Пусто
print(f.readlines())
# \t - табуляция, \r - вернуть картеки
# Закрывать файл обязательно
f.close()
