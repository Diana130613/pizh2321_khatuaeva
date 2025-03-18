# Программирование на языке высокого уровня (Python).
# Задание №4.3.1. Вариант 6
#
# Выполнила: Хатуаева Д.Т.
# Группа: ПИЖ-б-о-23-2(1)
# E-mail: dana.khatuaeva@gmail.com

from money import Money

if __name__ == "__main__":
    rubles = Money(700)
    print(rubles)

    # Конвертация в USD
    dollars = rubles.to_usd()
    print(dollars)

    # Конвертация в EUR
    euros = rubles.to_eur()
    print(euros)

    # Создание объекта на основании строки
    euro_from_string = Money.from_string("70 EUR")
    print(euro_from_string)

    print(euros + euro_from_string)

    # Сохранение и загрузка
    rubles.save("money.json")
    loaded_rubles = Money.load("money.json")
    assert rubles == loaded_rubles
