# Домашнее задание по неделе 13
Число в скобках - количество баллов.

_ДЗ взято с [соответствующей лабы](http://cs.mipt.ru/advanced_python/lessons/lab13.html)_.

## Сериализация
1. (2) В файле `class_to_serialize.py` допишите функции, которые будут преобразовывать класс в JSON и обратно.

## `pickle`
2. (3) [это [Упражнение 1](http://cs.mipt.ru/advanced_python/lessons/lab13.html#o1)] Попробуйте сериализовать следующие объекты:
    - I/O объекты (например, открытый файл - результат open());
    - итераторы;
    - встроенные функции (например, print или abs);
    - функции и классы (**сами классы, а не их объекты!**) из подключенных библиотек (например, `deque` из `collections`);
    - самописные функции и классы.
Что из этого можно сериализовать?
Можно ли с этими объектами после их десериализации взаимодействовать так, как это бы делалось до сериализации?
Опишите результаты либо в комментариях к коду, либо в отдельном файле `list_of_serializables.md`
3. (3) [Упражнение 2](http://cs.mipt.ru/advanced_python/lessons/lab13.html#o2).
4. (3) [это [Упражнение 3](http://cs.mipt.ru/advanced_python/lessons/lab13.html#o3)]
Вспомните упражнение 3 из девятой лабы.
Добавьте поддержку сериализации и корректной десериализации класса `TextLoader` и его итератора.
Однако учтите, что с момента создания объекта класса содержимое директории могло поменятся, и список файлов, хранимый в объекте, может быть не актуальным.
_Тем самым при десериализации необходимо заного выполнять чтение списка файлов в директории_.
Добавьте в класс методы `__getstate__` и `__setstate__` для корректной сериализации/десериализации его объектов.
