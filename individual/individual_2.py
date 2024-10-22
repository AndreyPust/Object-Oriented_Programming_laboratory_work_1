#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Номиналы российских рублей могут принимать значения 1, 2, 5, 10, 50, 100, 500, 1000, 5000.
# Копейки представить как 0.01 (1 копейка), 0.05 (5 копеек), 0.1 (10 копеек), 0.5 (50 копеек).
# Создать класс Money для работы с денежными суммами. Сумма должна быть представлена полями-номиналами,
# значениями которых должно быть количество купюр данного достоинства. Реализовать сложение сумм,
# вычитание сумм, деление сумм, деление суммы на дробное число, умножение на дробное число и операции сравнения.
# Дробная часть (копейки) при выводе на экран должны быть отделена от целой части запятой (Вариант 25 (10)).

class Money:
    # Список номиналов рублевых купюр и копеек
    denominations = {
        5000: '5000 руб.',
        1000: '1000 руб.',
        500: '500 руб.',
        100: '100 руб.',
        50: '50 руб.',
        10: '10 руб.',
        5: '5 руб.',
        2: '2 руб.',
        1: '1 руб.',
        0.5: '50 коп.',
        0.1: '10 коп.',
        0.05: '5 коп.',
        0.01: '1 коп.'
    }

    def __init__(self):
        # Инициализация поля для каждого номинала
        self.amounts = {denom: 0 for denom in self.denominations}

    def read(self):
        # Ввод количества купюр и монет с клавиатуры
        try:
            for denom in self.denominations:
                self.amounts[denom] = int(input(f"Введите количество {self.denominations[denom]}: "))
        except ValueError:
            print("Ошибка ввода. Все значения должны быть целыми числами.")

    def display(self):
        # Выводим информацию о сумме
        total_rubles, total_kopeks = self.total_value()
        print(f"Сумма: {total_rubles},{int(total_kopeks):02d} руб.")

    def total_value(self):
        # Рассчитываем общую сумму денег в рублях и копейках
        total = 0
        for denom, count in self.amounts.items():
            total += denom * count

        rubles = int(total)
        kopeks = round((total - rubles) * 100)
        return rubles, kopeks

    def __add__(self, other):
        # Сложение двух денежных сумм
        result = Money()
        for denom in self.denominations:
            result.amounts[denom] = self.amounts[denom] + other.amounts[denom]
        return result

    def __sub__(self, other):
        # Вычитание двух денежных сумм
        result = Money()
        for denom in self.denominations:
            result.amounts[denom] = self.amounts[denom] - other.amounts[denom]
        return result

    def __truediv__(self, number):
        # Деление суммы на дробное число
        result = Money()
        for denom in self.denominations:
            result.amounts[denom] = int(self.amounts[denom] / number)
        return result

    def __mul__(self, number):
        # Умножение суммы на дробное число
        result = Money()
        for denom in self.denominations:
            result.amounts[denom] = int(self.amounts[denom] * number)
        return result

    def __eq__(self, other):
        # Операция сравнения "равно"
        return self.total_value() == other.total_value()

    def __lt__(self, other):
        # Операция сравнения "меньше"
        return self.total_value() < other.total_value()

    def __le__(self, other):
        # Операция сравнения "меньше или равно"
        return self.total_value() <= other.total_value()


if __name__ == "__main__":
    # Демонстрация работы класса Money

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
    sum_result = money1 + money2
    print("\nРезультат сложения:")
    sum_result.display()

    # Вычитание сумм
    sub_result = money1 - money2
    print("\nРезультат вычитания:")
    sub_result.display()

    # Деление суммы на число
    div_result = money1 / 2
    print("\nРезультат деления первой суммы на 2:")
    div_result.display()

    # Умножение суммы на число
    mul_result = money1 * 1.5
    print("\nРезультат умножения первой суммы на 1.5:")
    mul_result.display()

    # Сравнение сумм
    if money1 == money2:
        print("\nСуммы равны.")
    elif money1 < money2:
        print("\nПервая сумма меньше второй.")
    else:
        print("\nПервая сумма больше второй.")
