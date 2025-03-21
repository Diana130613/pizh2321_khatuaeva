# Программирование на языке высокого уровня (Python).
# Задание №4.3.1. Вариант 6
#
# Выполнила: Хатуаева Д.Т.
# Группа: ПИЖ-б-о-23-2(1)
# E-mail: dana.khatuaeva@gmail.com


class Пицца:
    """Класс Пицца содержит общие атрибуты для пиццы.

    Дочерние классы будут их конкретизировать.
    """

    def __init__(self):
        """Конструктор класса.

        Инициализирует атрибуты пиццы (значения по умолчанию).
        """
        self.название = "Заготовка"
        self.тесто = "тонкое"  # тонкое или пышное
        self.соус = "кетчуп"   # или другой
        self.начинка = []      # список начинок (по умолчанию - нет)

        self.цена = 0

    def __str__(self):
        """Вернуть информацию о пицце: название, тесто, соус, начинка.

        Формат вывода:

        Пицца: Пепперони | Цена: 350.00 р.
        Тесто: тонкое Соус: томатный
        Начинка: пепперони, сыр моцарелла
        """
        # добавление необходимого кода
        Название = (f"Пицца: {self.название} | Цена: {self.цена: .2f} р.")
        Тесто = (f"Тесто: {self.тесто}")
        Соус = (f"Соус: {self.соус}")
        Начинка = (f"Начинка: {self.начинка}")
        return "\n".join([Название, Тесто, Соус, Начинка])

    def подготовить(self):
        """Сообщить о процессе подготовки.

        Формат вывода:

        Начинаю готовить пиццу Пепперони
          - замешиваю тонкое тесто...
          - добавляю соус: томатный...
          - и, конечно: пепперони, сыр моцарелла...
        """
        название = f"Начинаю готовить пиццу {self.название}"
        тесто = f"  - замешиваю {self.тесто} тесто..."
        соус = f"  - добавляю соус: {self.соус}..."
        начинка = f"  - и, конечно: {', '.join(self.начинка)}..."
        # Собираем все строки вместе
        return "\n".join([название, тесто, соус, начинка])

    def испечь(self):
        """Сообщить о процессе запекания пиццы.

        Формат вывода: произвольное сообщение.
        """
        # добавление необходимого кода
        print("Идёт процесс запекания пиццы")

    def нарезать(self):
        """Сообщить о процессе нарезки.

        Формат вывода: произвольное сообщение.
        """
        # добавление необходимого кода
        print("Идёт процесс нарезки")

    def упаковать(self):
        """Сообщить о процессе упаковки.

        Формат вывода: произвольное сообщение.
        """
        # добавление необходимого кода
        print("Идёт процесс упаковки")


class ПиццаПепперони(Пицца):
    """Класс ПиццаПепперони дополняет класс Пицца."""

    def __init__(self):
        super().__init__()
        # добавление необходимого кода
        self.название = "Пепперони"
        self.начинка = ['пепперони', 'сыр моцарелла']
        self.соус = "томатный"
        self.цена = 350.00  # Цена в рублях


class ПиццаБарбекю(Пицца):
    """Класс ПиццаБарбекю дополняет класс Пицца."""

    def __init__(self):
        # добавление необходимого кода
        super().__init__()
        self.название = "Барбекю"
        self.соус = "барбекю"
        self.начинка = ["бекон", "ветчина", "зелень", "сыр моцарелла"]
        self.цена = 450.00  # Цена в рублях


class ПиццаДарыМоря(Пицца):
    """Класс ПиццаДарыМоря дополняет класс Пицца."""

    def __init__(self):
        # добавление необходимого кода
        super().__init__()
        self.название = "Дары моря"
        self.начинка = ["кальмары", "креветки", "мидии", "сыр моцарелла"]
        self.цена = 550.00  # Цена в рублях
