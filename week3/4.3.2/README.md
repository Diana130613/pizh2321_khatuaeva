### Отчёт по лабораторной работе по предмету Объектно-ориентированное программирование
#### Хатуаева Дайана Тныбековна
#### ПИЖ-б-о-23-2(1)
#### Вариант 6
<hr>

# Цель работы
Цель данной работы заключается в ознакомлении с особенностями объектно-ориентированного программирования
в общем и его реализацией в языке *Python* на примере задания.

# Задание
***Пиццерия***
Пиццерия предлагает клиентам 
вида три пиццы: 
- Пепперони, 
- Барбекю 
- и Дары Моря, 
каждая из которых определяется тестом, соусом и начинкой. 
Требуется спроектировать и реализовать приложение для терминала, позволяющее обеспечить обслуживание посетителей. 
***Дополнительная информация*** 
В бизнес-процессе работы пиццерии в контексте задачи можно выделить 
3 сущности (объекта): 
- Терминал:  отвечает за взаимодействие с пользователем: 
1. 0 вывод меню на экран; 
2. прием команд от пользователя (выбор пиццы, подтверждение заказа, оплата и др.); 
- Заказ: содержит список заказанных пицц, умеет подсчитывать свою стоимость; 
- Пицца: содержит заявленные характеристики пиццы, а также умеет себя подготовить (замесить тесто, собрать ингредиенты и т.д.), испечь, порезать и упаковать. 
Т.к. пиццерия реализует несколько видов пиццы, которые различаются характеристиками, логично будет сделать общий класс Пицца, а в дочерних классах (например, классе ПиццаБарбекю) уточнить характеристики конкретной пиццы. 

# Выполнение лабораторной работы
В ходе выполнения лабораторной работы были созданы различные классы, реализующие все необходимые методы.
Класс ***Roman***
Описание: Класс Roman предназначен для работы с римскими числами. Внутренняя логика класса основана на обычных арабских числах (int), которые автоматически конвертируются в римский формат при необходимости (например, при выводе).

Основные ограничения
Римские числа ограничены интервалом от I до MMMCMXCIX (в арабском формате — от 1 до 3999).
Класс поддерживает: 
- операции сложения, 
- вычитания, 
- умножения
-  и деления между объектами класса Roman, а также с арабскими числами.
**Методы и функции**
Конструктор __init__(self, value)
Конструктор принимает два возможных типа значений:

int: инициализирует объект как арабское число.
str: инициализирует объект как римское число.
Если передается другой тип данных, вызывается ошибка TypeError.

```python
def __init__(self, value: Union[int, str]):
    if not isinstance(value, (int, str)):
        raise TypeError("Не могу создать римское число из {}".format(type(value)))
    
    if isinstance(value, int):
        self.__check_arabic(value)
        self._arabic = value
    elif isinstance(value, str):
        self._arabic = self.to_arabic(value)
```
Метод __add__(self, other)
Метод возвращает результат сложения двух объектов класса Roman или римского числа с арабским числом.

```python
def __add__(self, other: Union['Roman', int]) -> 'Roman':
    if not isinstance(other, (Roman, int)):
        raise TypeError("Можно складывать только объекты типа Roman или целые числа")
    if isinstance(other, Roman):
        result = self._arabic + other._arabic
    elif isinstance(other, int):
        result = self._arabic + other
    return Roman(result)
```
Метод __sub__(self, other)
Метод возвращает результат вычитания одного объекта класса Roman из другого или вычитания арабского числа из римского.

```python
def __sub__(self, other: Union['Roman', int]) -> 'Roman':
    if not isinstance(other, (Roman, int)):
        raise TypeError("Можно вычитать только объекты типа Roman или целые числа")
    if isinstance(other, Roman):
        result = self._arabic - other._arabic
    elif isinstance(other, int):
        result = self._arabic - other
    return Roman(result)
```
Метод __mul__(self, other)
Метод возвращает результат умножения римского числа на другое римское число или на арабское число.

```python
def __mul__(self, other: Union['Roman', int]) -> 'Roman':
    if not isinstance(other, (Roman, int)):
        raise TypeError("Можно умножать только объекты типа Roman или целые числа")
    if isinstance(other, Roman):
        result = self._arabic * other._arabic
    elif isinstance(other, int):
        result = self._arabic * other
    return Roman(result)
```
Метод __floordiv__(self, other)
Метод возвращает результат целочисленного деления римского числа на другое римское число или на арабское число.

```python
def __floordiv__(self, other: Union['Roman', int]) -> 'Roman':
    if not isinstance(other, (Roman, int)):
        raise TypeError("Можно делить только объекты типа Roman или целые числа")
    if isinstance(other, Roman):
        result = self._arabic // other._arabic
    elif isinstance(other, int):
        result = self._arabic // other
    return Roman(result)
```
Метод __truediv__(self, other)
Метод перенаправляет выполнение деления на метод __floordiv__, поскольку римские числа не поддерживают дробную арифметику.

```python
def __truediv__(self, other: Union['Roman', int]) -> 'Roman':
    return self.__floordiv__(other)
```
Метод __str__(self)
Метод возвращает строку, представляющую римское число.

```python
def __str__(self) -> str:
    return Roman.to_roman(self._arabic)
```
Статический метод **to_arabic(roman)**
Метод преобразует римское число в арабское.

```python
@staticmethod
def to_arabic(roman: str) -> int:
    Roman.__check_roman(roman)
    value = 0
    i = 0
    while i < len(roman):
        number = Roman.letter_to_number(roman[i])
        i += 1
        if i == len(roman):
            value += number
        else:
            next_number = Roman.letter_to_number(roman[i])
            if next_number > number:
                value += next_number - number
                i += 1
            else:
                value += number
    Roman.__check_arabic(value)
    return value
```
Статический метод **to_roman(arabic)**
Метод преобразует арабское число в римское.

```python
@staticmethod
def to_roman(arabic: int) -> str:
    Roman.__check_arabic(arabic)
    roman = ""
    n = arabic
    for i, number in enumerate(Roman.NUMBERS):
        while n >= number:
            roman += Roman.LETTERS[i]
            n -= Roman.NUMBERS[i]
    return roman
```

# Выводы
По итогу проделанной работы можно  сказать, что мы применили знания, полученные на прошлом занятии, для реализации данного кода и получили класс для управления римскими цифрами.