class PrintCoroutine:
    __item = 'start'

    def send(self, item):
        self.__item = item
        return self.__next__()
    
    def __next__(self):
        print('Печатаю через print(): ', self.__item)
        return 'Возвращаю через yield: {}'.format(self.__item)


coroutine = PrintCoroutine()
print(next(coroutine))
for i in range(10):
    # Обратите внимание, что на первой строке немного не такой вывод
    # Попробуйте прикинуть последовательность вызовов в генераторе и в классе
    print(coroutine.send(i))

