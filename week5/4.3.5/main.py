# Программирование на языке высокого уровня (Python).
# Задание №4.3.1. Вариант 6
#
# Выполнила: Хатуаева Д.Т.
# Группа: ПИЖ-б-о-23-2(1)
# E-mail: dana.khatuaeva@gmail.com
from money import Money
from collection import MoneyCollection


if __name__ == "__main__":
    collection = MoneyCollection()

    money1 = Money(10, "RUB")
    money2 = Money(20, "USD")
    money3 = Money(30, "EUR")

    collection.add(money1)
    collection.add(money2)
    collection.add(money3)

    print("Содержимое коллекции:")
    print(collection)

    collection.save("money_collection.json")
    print("Коллекция сохранена в файл money_collection.json.")

    loaded_collection = MoneyCollection.load("money_collection.json")
    print("Загруженная коллекция:")
    print(loaded_collection)

    collection.remove(1)
    print("Содержимое после удаления второго элемента:")
    print(collection)
