# Программирование на языке высокого уровня (Python).
# Задание №4.3.1. Вариант 6
#
# Выполнила: Хатуаева Д.Т.
# Группа: ПИЖ-б-о-23-2(1)
# E-mail: dana.khatuaeva@gmail.com


# добавление необходимого кода и импортирование модулей
from пицца import ПиццаБарбекю, ПиццаДарыМоря, ПиццаПепперони
from заказ import Заказ


class Терминал:
    """Класс Терминал обеспечивает взаимодействие с клиентом."""

    КОМПАНИЯ: str = "Bella pizza"
    КОМАНДА_ОТМЕНА_ЗАКАЗА: int = -1
    КОМАНДА_ПОДТВЕРЖДЕНИЕ_ЗАКАЗА: int = 0

    def __init__(self) -> None:
        """Конструктор класса.

        self.меню: список доступных пицц;
        self.заказ: список заказанных пицц;
        self.отображать_меню: определяет отображение меню
                              равен True: при создании терминала,
                              после отмены или подтверждения заказа.
        """
        # Доступные пиццы
        self.меню = [ПиццаПепперони(), ПиццаБарбекю(), ПиццаДарыМоря()]
        self.заказ = None
        self.отображать_меню = True

    def __str__(self) -> str:
        """Вернуть строковое представление класса.

        Формат вывода:

        Имя пиццерии, версия программы.
        """
        # добавление необходимого кода
        return f"{self.КОМПАНИЯ} #1"

    def показать_меню(self) -> None:
        """Показать меню.

        Показать меню следует только при наличии флага self.отображать_меню
        self.отображать_меню устанавливается в False после вывода меню.

        Формат вывода:

        Пиццерия #1
        Добро пожаловать!

        Меню:
        1. Пицца: Пепперони | Цена: 350.00 р.
           Тесто: тонкое Соус: томатный
           Начинка: пепперони, сыр моцарелла
        2. Пицца: Барбекю | Цена: 450.00 р.
           Тесто: тонкое Соус: барбекю
           Начинка: бекон, ветчина, зелень, сыр моцарелла
        3. Пицца: Дары моря | Цена: 550.00 р.
           Тесто: пышное Соус: тар-тар
           Начинка: кальмары, креветки, мидии, сыр моцарелла
        Для выбора укажите цифру через <ENTER>.
        Для отмены заказа введите -1
        Для подтверждения заказа введите 0
        """
        if not self.отображать_меню:
            return
        # добавление необходимого кода
        print(f"{self.__str__}\nДобро пожаловать!\n")
        print("Меню:")
        for index, pizza in enumerate(self.меню, start=1):
            print(f"{index}. {pizza}")
        print("\nДля выбора укажите цифру через <ENTER>.")
        print("Для отмены заказа введите -1")
        print("Для подтверждения заказа введите 0\n")

    def обработать_команду(self, пункт_меню):
        """Обработать действие пользователя.

        Аргументы:
          - пункт_меню (str): выбор пользователя.

        Возможные значения "пункт_меню":
          - -1: отменить заказ;
          -  0: подтвердить заказ; при этом осуществляется
                выставление счета, оплата, а также выполняется заказ;
                после заказ удаляется (= None)
          - 1..len(self.меню): добавление пиццы к добавить_к_заказу;
                               если заказ не создан, его нужно создать.
          - иначе: сообщить о невозможности обработать команду.

        Каждое действие подтверждается выводом на экран, например:
        1
        Пицца Пепперони добавлена!
        2
        Пицца Барбекю добавлена!
        0
        Заказ подтвержен.
        """

        try:
            пункт_меню = int(пункт_меню)
            if пункт_меню == Терминал.КОМАНДА_ОТМЕНА_ЗАКАЗА:
                # добавление необходимого кода
                if self.заказ is not None:
                    print("Заказ отменён.")
                    self.заказ = None
                else:
                    print("Ничего не было заказано.")
                self.отображать_меню = True
            elif пункт_меню == Терминал.КОМАНДА_ПОДТВЕРЖДЕНИЕ_ЗАКАЗА:
                # добавление необходимого кода
                if self.заказ is not None:
                    self.принять_оплату()  # Обработка оплаты
                    self.заказ.выполнить()  # Выполнение заказа
                    print("Ваш заказ выполнен! Приятного аппетита!")
                    self.заказ = None
                    self.отображать_меню = True
                else:
                    print("У вас ещё ничего не выбрано.")
            elif 1 <= пункт_меню <= len(self.меню):
                # добавление необходимого кода
                if self.заказ is None:
                    self.заказ = Заказ()
                self.заказ.добавить(self.меню[пункт_меню - 1])  # Добавляем пиццу в заказ
                print(f"Пицца {self.меню[пункт_меню - 1].название} добавлена!")
            else:
                # За границей меню передаем управление в обработку исключений
                raise ValueError
        except ValueError:
            print("Не могу распознать команду! Проверьте ввод.")
        except Exception:
            print("Во время работы терминала произошла ошибка...")

    def рассчитать_сдачу(self, оплата):
        """Вернуть сдачу для 'оплата'.

        Если оплата меньше стоимости заказа, возбудить исключение ValueError.
        """
        # добавление необходимого кода
        if оплата < self.заказ.сумма():
            raise ValueError("Недостаточно денег для оплаты заказа.")
        return оплата - self.заказ.сумма()

    def принять_оплату(self):
        """Обработать оплату.

        Эмулирует оплату заказа (клиент вводит сумму с клавиатуры).

        Если сумма оплаты недостаточна (определяет метод рассчитать_сдачу())
        или возникает другая ошибка - исключние передается выше.
        """
        try:
            # добавление необходимого кода
            print(f"Стоимость вашего заказа: {self.заказ.сумма():.2f} р.")
            оплата = float(input("Введите сумму оплаты: "))
            сдача = self.рассчитать_сдачу(оплата)
            if сдача > 0:
                print(f"Сдача: {сдача:.2f} р.")
        except Exception:
            print("Оплата не удалась. Заказ будет отменен.")
            raise
