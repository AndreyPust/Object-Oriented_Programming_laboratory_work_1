#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Номиналы российских рублей могут принимать значения 1, 2, 5, 10, 50, 100, 500, 1000, 5000.
# Копейки представить как 0.01 (1 копейка), 0.05 (5 копеек), 0.1 (10 копеек), 0.5 (50 копеек).
# Создать класс Money для работы с денежными суммами. Сумма должна быть представлена полями-номиналами,
# значениями которых должно быть количество купюр данного достоинства. Реализовать сложение сумм,
# вычитание сумм, деление сумм, деление суммы на дробное число, умножение на дробное число и операции сравнения.
# Дробная часть (копейки) при выводе на экран должна быть отделена от целой части запятой (Вариант 25 (10)).


class Money:
    # Список номиналов купюр и копеек рубля
    denominations = {
        5000: "5000 руб.",
        1000: "1000 руб.",
        500: "500 руб.",
        100: "100 руб.",
        50: "50 руб.",
        10: "10 руб.",
        5: "5 руб.",
        2: "2 руб.",
        1: "1 руб.",
        0.5: "50 коп.",
        0.1: "10 коп.",
        0.05: "5 коп.",
        0.01: "1 коп.",
    }

    def __init__(self):
        """
        Метод инициализации поля для каждого номинала.
        """

        self.amounts = {denom: 0 for denom in self.denominations}

    def read(self):
        """
        Ввод количества монет или купюр какого либо номинала.
        """

        try:
            for denom in self.denominations:
                self.amounts[denom] = int(input(f"Введите количество {self.denominations[denom]}: "))
        except ValueError:
            print("Ошибка ввода. Все значения должны быть целыми числами.")

    def display(self):
        """
        Метод вывода информации о сумме.
        """

        total_rubles, total_kopeks = self.total_value()
        print(f"Сумма: {total_rubles},{int(total_kopeks):02d} руб.")

    def total_value(self):
        """
        Метод подсчета денежной суммы.
        """

        total = 0
        for denom, count in self.amounts.items():
            total += denom * count

        rubles = int(total)
        kopeks = round((total - rubles) * 100)
        return rubles, kopeks

    def add(self, other):
        """
        Метод сложения денежных сумм.
        """

        result = Money()
        for denom in self.denominations:
            result.amounts[denom] = self.amounts[denom] + other.amounts[denom]
        return result

    def subtraction(self, other):
        """
        Метод вычитания двух денежных сумм.
        """

        result = Money()
        for denom in self.denominations:
            result.amounts[denom] = self.amounts[denom] - other.amounts[denom]
        return result

    def division(self, number):
        """
        Метод деления денежной суммы на некоторое число.
        """

        result = Money()
        for denom in self.denominations:
            result.amounts[denom] = int(self.amounts[denom] / number)
        return result

    def multiplication(self, number):
        """
        Метод умножения суммы на некоторое дробное число.
        """

        result = Money()
        for denom in self.denominations:
            result.amounts[denom] = int(self.amounts[denom] * number)
        return result

    def equivalent(self, other):
        """
        Метод, сравнивающий денежные суммы, проверка равенства.
        """

        return self.total_value() == other.total_value()

    def lt(self, other):
        """
        Метод, реализующий операцию сравнения меньше.
        """

        return self.total_value() < other.total_value()

    def le(self, other):
        """
        Метод, реализующий операцию сравнения больше.
        """

        return self.total_value() > other.total_value()


if __name__ == "__main__":
    # Ввод первой суммы с клавиатуры
    print("Введите первую сумму:")
    money1 = Money()
    money1.read()

    # Ввод второй суммы с клавиатуры
    print("\nВведите вторую сумму:")
    money2 = Money()
    money2.read()

    # Вывод суммы на экран
    print("\nПервая сумма:")
    money1.display()

    print("Вторая сумма:")
    money2.display()

    # Сложение сумм
    sum_result = money1.add(money2)
    print("\nРезультат сложения:")
    sum_result.display()

    # Вычитание сумм
    sub_result = money1.subtraction(money2)
    print("\nРезультат вычитания:")
    sub_result.display()

    # Деление суммы на число
    div_result = money1.division(2)
    print("\nРезультат деления первой суммы на 2:")
    div_result.display()

    # Умножение суммы на число
    mul_result = money1.multiplication(1.5)
    print("\nРезультат умножения первой суммы на 1.5:")
    mul_result.display()

    # Сравнение сумм
    if money1.equivalent(money2):
        print("\nСуммы равны.")
    elif money1.lt(money2):
        print("\nПервая сумма меньше второй.")
    elif money1.le(money2):
        print("\nПервая сумма больше второй.")
