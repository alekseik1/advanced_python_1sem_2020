def print_coroutine():
    x = "start"
    while True:
        '''
        Обратите внимание, что yield здесь используется двояко:
        1) Когда вызывается coroutine.send(<something>) - тогда yield возвращает (как функция) то, 
        что передали в send(). Из корутины при этом выхода не происходит!
        2) Когда вызывается изнутри самой корутины - тогда yield отдает управление и выходит из 
        корутины, отдавая значение, указанное справа от yield. При этом происходит выход из корутины.
        '''
        x = yield 'Возвращаю через yield: {}'.format(x)
        print("Печатаю через print(): ", x)

coroutine = print_coroutine()
print(next(coroutine))
for i in range(10):
    print(coroutine.send(i))
