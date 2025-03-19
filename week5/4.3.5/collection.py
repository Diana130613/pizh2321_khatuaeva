from money import Money
import json
from typing import List


class MoneyCollection:
    """
    Класс-контейнер для хранения объектов Money.
    """

    def __init__(self) -> None:
        """Инициализирует пустой контейнер для объектов Money."""
        self._data: List[Money] = []

    def __str__(self) -> str:
        """Представление объекта в удобном для человека виде"""
        return "\n".join(str(money) for money in self._data)

    def __getitem__(self, index: int) -> Money:
        """Позволяет получать доступ к объектам Money по индексу."""
        return self._data[index]

    def add(self, value: Money) -> None:
        """Добавляет объект Money в контейнер."""
        if not isinstance(value, Money):
            raise TypeError("Можно добавлять только объекты типа Money.")
        self._data.append(value)

    def remove(self, index: int) -> None:
        """Удаляет объект из контейнера по индексу."""
        if index < 0 or index >= len(self._data):
            raise IndexError("Индекс выходит за пределы диапазона.")
        del self._data[index]

    def save(self, filename: str) -> None:
        """Сохраняет контейнер в файл в формате JSON."""
        with open(filename, 'w') as file:
            json.dump([{"amount": money.amount, "currency": money.currency} for money in self._data], file)

    @classmethod
    def load(cls, filename: str) -> 'MoneyCollection':
        """Загружает контейнер из файла в формате JSON."""
        with open(filename, 'r') as file:
            data = json.load(file)
            collection = cls()
            for item in data:
                collection.add(Money(item["amount"], item["currency"]))
            return collection
