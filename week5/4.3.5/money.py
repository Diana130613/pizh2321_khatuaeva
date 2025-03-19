import json
from typing import Union


class Money:
    """
    Класс для работы с денежными суммами.
    """

    def __init__(self, amount: float, currency: str = "RUB"):
        """
        Инициализирует объект с заданной суммой и валютой (по умолчанию RUB).

        amount: Количество денег.
        currency: Валюта (по умолчанию "RUB").
        """
        self.amount = amount
        self.currency = currency.upper()

    def __str__(self) -> str:
        """Возвращает строку в удобном для человека виде."""
        return f"{self.amount:.2f} {self.currency}"

    def __add__(self, other: 'Money') -> 'Money':
        """
        Сложение двух денежных единиц одной валюты.

        other: Другой объект Money.
        return: Новый объект Money с результатом сложения.
        """
        if not isinstance(other, Money):
            raise TypeError("Можно складывать только объекты типа Money.")
        if self.currency != other.currency:
            raise ValueError("Валюты должны совпадать.")
        return Money(self.amount + other.amount, self.currency)

    def __sub__(self, other: 'Money') -> 'Money':
        """
        Вычитание двух денежных единиц одной валюты.

        other: Другой объект Money.
        return: Новый объект Money с результатом вычитания.
        """
        if not isinstance(other, Money):
            raise TypeError("Можно вычитать только объекты типа Money.")
        if self.currency != other.currency:
            raise ValueError("Валюты должны совпадать.")
        return Money(self.amount - other.amount, self.currency)

    def __mul__(self, multiplier: Union[int, float]) -> 'Money':
        """
        Умножение суммы на множитель.

        multiplier: Множитель.
        return: Новый объект Money с результатом умножения.
        """
        if not isinstance(multiplier, (int, float)):
            raise TypeError("Множитель должен быть числом.")
        return Money(self.amount * multiplier, self.currency)

    def __eq__(self, other: object) -> bool:
        """
        Проверяет равенство двух денежных единиц.

        other: Другой объект Money.
        return: True, если суммы и валюты совпадают, иначе False.
        """
        if not isinstance(other, Money):
            return NotImplemented
        return self.amount == other.amount and self.currency == other.currency

    @classmethod
    def from_string(cls, str_value: str) -> 'Money':
        """
        Создает объект на основе строки.

        str_value: Строка с суммой и валютой.
        return: Объект Money.
        """
        parts = str_value.split()
        if len(parts) != 2:
            raise ValueError("Должно быть два элемента: сумма и валюта.")
        try:
            amount = float(parts[0])
            currency = parts[1].upper()
            return cls(amount, currency)
        except ValueError as e:
            raise ValueError("Ошибка преобразования строки.") from e

    def save(self, filename: str) -> None:
        """
        Сохраняет объект в файл в формате JSON.

        filename: Имя файла для сохранения.
        """
        with open(filename, 'w') as file:
            json.dump({"amount": self.amount, "currency": self.currency}, file)

    @classmethod
    def load(cls, filename: str):
        """
        Загружает объект из файла в формате JSON.

        filename: Имя файла для загрузки.
        return: Объект Money.
        """
        with open(filename, 'r') as file:
            data = json.load(file)
            return cls(data["amount"], data["currency"])

    def to_rub(self) -> 'Money':
        """
        Конвертирует сумму в рубли.

        return: Новый объект Money с суммой в рублях.
        """
        if self.currency == "RUB":
            return self
        elif self.currency == "USD":
            # Курс USD к RUB
            return Money(self.amount * 81.75, "RUB")
        elif self.currency == "EUR":
            # Примерный курс EUR к RUB
            return Money(self.amount * 89.50, "RUB")
        else:
            raise ValueError("Конвертация в RUB не поддерживается.")

    def to_usd(self) -> 'Money':
        """
        Конвертирует сумму в доллары.

        return: Новый объект Money с суммой в долларах.
        """
        if self.currency == "USD":
            return self
        elif self.currency == "RUB":
            # Курс RUB к USD
            return Money(self.amount * 0.012, "USD")
        elif self.currency == "EUR":
            # Курс EUR к USD
            return Money(self.amount * 1.09, "USD")
        else:
            raise ValueError("Конвертация в USD не поддерживается.")

    def to_eur(self) -> 'Money':
        """
        Конвертирует сумму в евро.

        return: Новый объект Money с суммой в евро.
        """
        if self.currency == "EUR":
            return self
        elif self.currency == "RUB":
            # Курс RUB к EUR
            return Money(self.amount * 0.011, "EUR")
        elif self.currency == "USD":
            # Курс USD к EUR
            return Money(self.amount * 0.91, "EUR")
        else:
            raise ValueError("Конвертация в EUR не поддерживается.")
