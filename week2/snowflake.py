from abc import ABC


# КЛАСС MAKE_SNOWFLAKE
class MakeSnowflake:
    """
    Класс для создания базовой структуры снежинки заданного размера.
    Атрибуты:
    snowflake: Двумерный список, представляющий снежинку.
    """

    def __init__(self, size: int):
        """
        Инициализирует объект класса MakeSnowflake.
        Параметры:
        size (int): Размер снежинки (количество строк и столбцов).
        Возвращаемое значение:
        None
        """
        # Создаем матрицу размером size x size, заполненную символами '-'
        self.snowflake = [['-' for _ in range(size)] for _ in range(size)]
        # Заполняем символы '*' на главных диагоналях и средней линии
        for i in range(size):
            self.snowflake[i][i] = '*'   # Главная диагональ
            self.snowflake[i][size - i - 1] = '*'  # Побочная диагональ
            self.snowflake[i][size // 2] = '*'  # Средняя горизонтальная линия
            self.snowflake[size // 2][i] = '*'  # Средняя вертикальная линия


# АБСТРАКТНЫЙ БАЗОВЫЙ КЛАСС SNOWFLAKE
class BaseSnowflake(ABC):
    """
    Абстрактный базовый класс для всех типов снежинок.
    Методы:
    thaw(): Абстрактный метод для уменьшения размеров снежинки.
    freeze(k): Абстрактный метод для увеличения размеров снежинки.
    thicken(): Абстрактный метод для утолщения снежинки.
    show(): Абстрактный метод для отображения снежинки.
    """

    def thaw(self):
        """Уменьшение размеров снежинки."""
        pass

    def freeze(self, k: int):
        """Увеличение размеров снежинки на k слоёв."""
        pass

    def thicken(self):
        """Утолщение снежинки добавлением одного слоя."""
        pass

    def show(self):
        """Отображение текущей структуры снежинки."""
        for i in self.snowflake:
            print("".join(i))  # Выводим каждую строку снежинки


# КОНКРЕТНАЯ РЕАЛИЗАЦИЯ СНЕЖИНКИ
class Snowflake(BaseSnowflake):
    """
    Класс для управления состоянием снежинки.
    Атрибуты:
    size (int): Размер снежинки.
    snowflake (list of lists): Текущая структура снежинки.
    __steps (int): Количество шагов таяния снежинки.
    k (int): Количество добавляемых слоев.
    """

    def __init__(self, size: int):
        """
        Инициализация объекта класса Snowflake.
        Параметры:
        size (int): Начальный размер снежинки.
        Исключения:
        ValueError: Если размер не является нечётным положительным числом.
        Возвращаемое значение:
        None
        """
        if size % 2 == 0 or size < 1:
            raise ValueError("Введите целое нечётное положительное число")
        self.size = size
        # Используем класс MakeSnowflake для создания начальной структуры
        self.snowflake = MakeSnowflake(self.size).snowflake

    __steps = 0  # Статическая переменная для отслеживания шагов таяния

    def thaw(self):
        """
        Уменьшаем размер снежинки, удаляя внешние слои.
        Исключения:
        ValueError: Если снежинка уже стала слишком маленькой (< 2x2).
        Возвращаемое значение:
        None
        """
        if len(self.snowflake) > 2 and len(self.snowflake[0]) > 2:
            # Удаляем первый и последний элементы каждой строки и столбца
            self.snowflake = [row[1:-1] for row in self.snowflake[1:-1]]
            Snowflake.__steps += 1  # Увеличиваем счетчик шагов таяния
            print(f'Прошло шагов: {Snowflake.__steps}')
        else:
            raise ValueError("Снежинка растаяла :(")

    def freeze(self, k: int):
        """
        Увеличение размера снежинки на k слоев.
        Параметры:
        k (int): Количество добавляемых слоев.
        Исключения:
        ValueError: Если k не является положительным числом.
        Возвращаемое значение:
        None
        """
        if k <= 0:
            raise ValueError("Значение k должно быть положительным числом.")
        else:
            # Вычисляем новый размер снежинки
            self.size = self.size + 2 * k
            # Создаем новую снежинку большего размера
            new_snowflake = MakeSnowflake(self.size).snowflake
            self.snowflake = new_snowflake

    def thicken(self):
        """
        Утолщение снежинки добавлением одного дополнительного слоя.
        Возвращаемое значение:
        None
        """
        # Новый размер равен старому размеру плюс два
        new_size = self.size + 2
        # Создаем новую снежинку увеличенного размера
        new_snowflake = MakeSnowflake(new_size).snowflake
        self.snowflake = new_snowflake

    def show(self):
        """
        Отображает текущую структуру снежинки.
        Возвращаемое значение:
        None
        """
        return super().show()
