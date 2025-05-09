# Программирование на языке высокого уровня (Python).
# Задание №4.3.1. Вариант 6
#
# Выполнила: Хатуаева Д.Т.
# Группа: ПИЖ-б-о-23-2(1)
# E-mail: dana.khatuaeva@gmail.com

from typing import Union


class Roman:
    """Класс Roman реализует работу с римскими числами.

    Алгоритм: http://math.hws.edu/eck/cs124/javanotes7/c8/ex3-ans.html.

    Внутри класс работает с обычными арабскими числами (int),
    которые преобразуются в римские при необходимости (например, при выводе).

    Ключевой атрибут: self._arabic (арабское число).

    Ограничения: число должно быть в пределах [1; 3999].
    """

    # Константы класса
    ARABIC_MIN = 1
    ARABIC_MAX = 3999
    ROMAN_MIN = "I"
    ROMAN_MAX = "MMMCMXCIX"

    LETTERS = ["M", "CM", "D", "CD", "C", "XC", "L",
               "XL", "X", "IX", "V", "IV", "I"]
    NUMBERS = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

    def __init__(self, value: Union[int, str]):
        """Инициализация класса.

        Параметры:
            value (str): римское число, например, X.
                или
            value (int): арабское число, например, 5.
                или
            value (другой тип):  возбудить исключение TypeError.
        """
        if not isinstance(value, (int, str)):
            raise TypeError("Не могу создать римское число из {0}".
                            format(type(value)))

        if isinstance(value, int):
            self.__check_arabic(value)
            self._arabic = value
        elif isinstance(value, str):
            self._arabic = self.to_arabic(value)

    def __add__(self, other: Union['Roman', int]) -> 'Roman':
        """Создать новый объект как сумму 'self' и 'other'.

        Параметры:
            other (Roman): ...
                или
            other (int): арабское число, добавить к self.
                или
            other (другой тип):  возбудить исключение TypeError.
        """
        # мой код ниже
        if not isinstance(other, (Roman, int)):
            raise TypeError("Складываются только объекты Roman или целые числа")
        if isinstance(other, Roman):
            result = self._arabic + other._arabic
        elif isinstance(other, int):
            result = self._arabic + other
        return Roman(result)

    def __sub__(self, other: Union['Roman', int]) -> 'Roman':
        """Создать новый объект как разность self и other.

        Параметры:
            other (Roman): ...
                или
            other (int): арабское число, отнять от self.
                или
            other (другой тип):  возбудить исключение TypeError.
        """
        # мой код ниже
        if not isinstance(other, (Roman, int)):
            raise TypeError("Можно вычитать только объекты типа Roman или целые числа")
        if isinstance(other, Roman):
            result = self._arabic - other._arabic
        elif isinstance(other, int):
            result = self._arabic - other
        return Roman(result)

    def __mul__(self, other: Union['Roman', int]) -> 'Roman':
        """Создать новый объект как произведение self и other.

        Параметры:
            other (Roman): ...
                или
            other (int): арабское число, добавить к self.
                или
            other (другой тип):  возбудить исключение TypeError.
        """
        # мой код ниже
        if not isinstance(other, (Roman, int)):
            raise TypeError("Можно умножать только объекты типа Roman или целые числа")
        if isinstance(other, Roman):
            result = self._arabic * other._arabic
        elif isinstance(other, int):
            result = self._arabic * other
        return Roman(result)

    def __floordiv__(self, other: Union['Roman', int]) -> 'Roman':
        """Создать новый объект как частное self и other.

        Параметры:
            other (Roman): ...
                или
            other (int): арабское число, добавить к self.
                или
            other (другой тип):  возбудить исключение TypeError.
        """
        # мой код ниже
        if not isinstance(other, (Roman, int)):
            raise TypeError("Можно умножать только объекты типа Roman или целые числа")
        if isinstance(other, Roman):
            result = self._arabic // other._arabic
        elif isinstance(other, int):
            result = self._arabic // other
        return Roman(result)

    def __truediv__(self, other: Union['Roman', int]) -> 'Roman':
        """Создать новый объект как частное self и other.

        Параметры:
            other (Roman): ...
                или
            other (int): арабское число, добавить к self.
                или
            other (другой тип):  возбудить исключение TypeError.
        """
        # Любое деление для римского числа считается делением нацело,
        # поэтому необходимо передать "работу" реализованному методу
        # целочисленного деления
        return self.__floordiv__(other)

    def __str__(self) -> str:
        """Вернуть строковое представление класса."""
        return Roman.to_roman(self._arabic)

    @staticmethod
    def __check_arabic(value: int):
        """Возбудить исключение ValueError, если 'value' не принадлежит
        [ARABIC_MIN; ARABIC_MIN]."""
        # мой код ниже
        if not (Roman.ARABIC_MIN <= value <= Roman.ARABIC_MAX):
            raise ValueError("Значение value выбивается из диапазона")

    @staticmethod
    def __check_roman(value: str):
        """Возбудить исключение ValueError, если 'value' содержит
        недопустимые символы (не входящие в LETTERS)."""
        # мой код ниже
        for char in value:
            if char.upper() not in Roman.LETTERS:
                raise ValueError("Value содержит недопустимые символы")

    @property
    def arabic(self) -> int:
        """Вернуть арабское представление числа."""
        # мой код ниже
        return self._arabic

    @staticmethod
    def to_arabic(roman: str) -> int:
        """Преобразовать римское число 'roman' в арабское.

        Параметры:
            roman (str): римское число, например, "X".

        Возвращает:
            int: арабское число.
        """
        def letter_to_number(letter: str) -> int:
            """Вернуть арабское значение римской цифры 'letter'.

            Регистр не учитывается."""
            # мой код ниже
            letter = letter.upper()  # Приводим букву к верхнему регистру
            if letter == 'I':
                return 1
            elif letter == 'V':
                return 5
            elif letter == 'X':
                return 10
            elif letter == 'L':
                return 50
            elif letter == 'C':
                return 100
            elif letter == 'D':
                return 500
            elif letter == 'M':
                return 1000
            else:
                raise ValueError(f"Недопустимая римская цифра: '{letter}'")

        Roman.__check_roman(roman)

        i = 0  # Позиция в строке roman
        value = 0  # Преобразованное число

        while i < len(roman):

            number = letter_to_number(roman[i])

            i += 1

            if i == len(roman):
                # В строке roman больше не осталось символов, добавляем number
                value += number
            else:
                # Если символы остались, необходимо посмотреть на следующий.
                # Если следующий символ "больше", считаем их за одну цифру.
                # Это необходимо, например, для того,
                # чтобы IV преобразовать в 4, а не 15.
                next_number = letter_to_number(roman[i])
                if next_number > number:
                    # Комбинируем цифры и перемещаем i к следующей
                    value += next_number - number
                    i += 1
                else:
                    # Просто добавляем следующую цифру
                    value += number

        Roman.__check_arabic(value)
        return value

    @staticmethod
    def to_roman(arabic: int) -> str:
        """Преобразовать арабское число 'arabic' в римское.

        Параметры:
            arabic (int): арабское число, например, 5.

        Возвращает:
            str: римское число.
        """
        Roman.__check_arabic(arabic)

        roman = ""
        # n - часть arabic, которую осталось преобразовать
        n = arabic

        for i, number in enumerate(Roman.NUMBERS):
            while n >= number:
                roman += Roman.LETTERS[i]
                n -= Roman.NUMBERS[i]

        return roman
