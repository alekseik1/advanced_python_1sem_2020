# Домашнее задание по неделе 5
_Арифметических драконов лучше делать в самом конце_

Число в скобках - количество баллов.
### Теория по ООП
1. (4) Опишите в файле `basic_oop.md` своими словами следующие принципы:
  - Объект;
  - Инкапсуляция;
  - Полиморфизм;
  - Наследование;

В .md файлах можно красиво оформлять документы!
Заключите текст в две звездочки слева и две звездочки справа - и он станет **полужирным**.
Заключите текст в два нижних подчеркивания слева и два нижних подчеркивания справа - и он станет _курсивом_.
Заключите текст в кавычку \` слева и справа - и он станет `кодом`.

2. (3) Опишите в файле `solid.md` своими словами три первых принципа SOLID:
  - Single responsibility;
  - Open-close;
  - Liskov substitution.

3. (3) Посмотрите на файл `bad_solid.py`.
Какие из первых трех принципов SOLID в нем нарушены?
Опишите это в `bad_solid.md`.

### Практика по ООП в Python
4. (3) Напишите программу, которая объявляет класс `Shape`, конструктор которого принимает ширину и высоту.
После этого унаследуйте от него класс `Triangle` и `Rectangle`.
Реализуйте метод `area()`, который возвращает площадь этих фигур.

5. (3) Напишите программу с классом `Mother` от которого наследуется класс `Daughter`.
Сделайте так, чтобы результат `print(object)` был разный.
Воспользуйтесь принципами полиморфизма, наследования и инкапсуляции.

6. (4) Реализйте класс `Animal`. Внутри объявите поле для имени и возраста.
От класса `Animal` унаследуйте класс `Zebra` и `Dolphin`.
Оба класса могут вернуть описание, содержащее имя, возраст и какую-то доп.информацию, например, что это за вид животного.
Воспользуйтесь принципами полиморфизма, наследования и инкапсуляции.

### Совместная задача.
7. (10) Это задание предстоит сделать вдвоем. 
Игра "Арифметические драконы" предназначена для обучения детей арифметике.
На героя нападает дракон, который задаёт вопрос на сложение (если дракон зелёный), вычитание (красный) или умножение (черный).
  - Разбейтесь на группы по два и запишитесь в таблицу.
  - Заведите на одном из аккаунтов репозиторий, куда вы положите свой проект.
Дайте другому участнику права на редактирование репозитория и пуш коммитов.

  - Скачайте архив [arithmetic_dragons](http://cs.mipt.ru/advanced_python/extra/lab05/arithmetic_dragons.zip).
Положите коды из архива в ваш репозиторий курса в папку `w5/`, сделайте коммит в `master`.
Это будет вашей заготовкой по проекту, от нее дальше будем отталкиваться.
  - Реализуйте классы по следующей схеме и добейтесь работоспособности игры.
![Dragons UML](http://cs.mipt.ru/advanced_python/images/lab05/dragons_uml.png)

Код проекта будет только у одного участника при такой схеме работе.
Если вас это расстраивает, вы можете в конце скопировать коды к себе.

#### Hint по совместной работе в GitHub
Чтобы работать совместно, удобно работать над разными задачами в разных вектах, а затем ветки сливать.
Но перед этим стоит задуматься, в какую ветку будете сливать свою работу по завершении!
  - Создайте ветку `dragons`.
  - Договоритесь между собой, кто за что будет ответственным.
  - (опционально) Далее пусть каждый из участников создаст ветку со своим названием и делает работу в ней. По окончании работ участник открывает pull request в `dragons` и заливает свои изменения. Другой участник смотрит на эти изменения, проверяет их, а затем принимает PR.
  - В конце всех работ над проектом "Арифметические драконы" вы открываете pull request из ветки `dragons` в ветку `master`.

Предпоследний пункт необязателен: вы можете просто коммитить все в `dragons` и не паритсья с ветками.
Но рекомендуется попробовать предлагаемый подход: в более серьезных проектах от вас будут требовать новые фичи заливать именно через отдельные ветки.

Чтобы не запутаться: у вас в конце выполнения ДЗ будет два pull request.
Первый из ветки `w5` в `master` (это будут все коды, кроме драконов) и второй из ветки `dragons` в ветку `master` (это будут только коды, относящиеся к "Арифметическим драконам").
Эти два PR будут проверяться отдельно. 

Не забудьте назначить преподавателя в reviewers в обоих pull request!


## Бонус
1. Реализуйте класс тролля в "Арифметических драконах".
Тролль будет просить вычислить разложение на простые множители числа.
2. Реализуйте систему чит-кодов: для каждого противника будет код, при вводе которого в качестве ответа противник будет побежден.
В каком месте в иерархии классов лучше всего это засунуть?
Воспользуйтесь полиморфизмом, чтобы сделать для каждого типа противника разный чит-код.
