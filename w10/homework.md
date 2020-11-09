# Домашнее задание по неделе 10
Число в скобках - количество баллов.
_ДЗ частично взято с [соответствующей лабы](http://cs.mipt.ru/advanced_python/lessons/lab10.html)_

## Threading, GIL
1. (2) Опишите в файле `threading_explained.md`, в чем разница между потоком и процессом.

2. (2) Опишите в файле `gil.md`, что такое GIL и почему `multiprocessing` свободен от него.

3. (3) Напишите программу, которая будет по заданному списку хостов пинговать их 
(т.е. вызывать `ping`, [подробнее](https://ru.wikipedia.org/wiki/Ping)). Используйте `threading`.

4. (3) Напишите программу, которая будет вычислять скалярное произведение двух векторов с использованием **потоков**.
5. (2) Возьмите какой-нибудь большой вектор (так, чтобы программа из п.4 работала от 1 до 20 секунд при одном потоке).
Замерьте время выполнения и постройте график (вы можете провести усреднение по 3 запускам, чтобы убрать шумы).
Помогли ли потоки ускорить программу?

## Multiprocessing
6. (2) Опишите в файле `multiprocessing_explained.md`, как работает модуль `multiprocessing` и как он делит память между процессами.

7. (2) Опишите в файле `synchronization_primitives.md`, что такое примитивы синхронизации.
Там же опишите, что такое мьютекс (Mutex) и как работает `multiprocessing.Lock()`.

8. (3) Перепишите программу из п.4 с использованием `multiprocessing` и постройте такие же графики, как в п.5.
Ускорилась ли теперь программа?
_На данном этапе необязательно сохранять результат подсчета и выдавать его. Главное, чтобы были расчеты_.

9. (3) Организуйте передачу результатов подсчета между процессорами с помощью `Queue` и с помощью `Pipe`.
Добейтесь того, чтобы на выходе Ваша программа могла вывести скалярное произведение.

## Pool
10. (3) Перепишите скалярное произведение векторов через `Pool` 
(подсказка: используйте `pool.map` и передавайте ему `zip` из двух векторов).
