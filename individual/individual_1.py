#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Поле «first» – дробное положительное число, цена товара;
# поле «second» – целое положительное число, количество единиц товара.
# Реализовать метод «cost()» — вычисление стоимости товара (Вариант 25(5)).

class Pair:
    def __init__(self, first, second):
        """
        Метод инициализации, проверяет аргументы на корректность.
        """

        if not isinstance(first, (int, float)) or first <= 0:
            raise ValueError("Цена товара должна быть положительным дробным числом!")
        if not isinstance(second, int) or second <= 0:
            raise ValueError("Количество товара должно быть положительным целым числом!")

        self.first = float(first)  # Цена товара
        self.second = int(second)  # Количество товара

    def get_first(self):
        return self.first

    def get_second(self):
        return self.second


class PairInput:
    @staticmethod
    def read():
        """
        Метод, позволяющий производить ввод значений с клавиатуры.
        """

        try:
            first = float(input("Введите цену товара (положительное дробное число): "))
            if first <= 0:
                raise ValueError("Цена товара должна быть положительным числом!")

            second = int(input("Введите количество товара (положительное целое число): "))
            if second <= 0:
                raise ValueError("Количество товара должно быть положительным целым числом!")

            return Pair(first, second)  # Возвращаем объект Pair с введенными данными
        except ValueError as e:
            print(f"Ошибка ввода: {e}")
            return None


class PairDisplay:
    @staticmethod
    def display(any_pair):
        """
        Метод, позволяющий выводить информацию о товаре (количество, стоимость).
        """

        if isinstance(any_pair, Pair):
            print(f"Цена товара: {any_pair.get_first()}, Количество: {any_pair.get_second()}")
        else:
            print("Невозможно вывести данные, объект пары некорректен.")


class PairCostCalculator:
    @staticmethod
    def cost(any_pair):
        """
        Метод, вычисляющий стоимость всего товара.
        """

        if isinstance(any_pair, Pair):
            return any_pair.get_first() * any_pair.get_second()
        else:
            raise ValueError("Некорректный объект пары для вычисления стоимости!")


def make_pair(first, second):
    """
    Функция для создания объекта Pair с проверкой на корректность данных
    """

    try:
        return Pair(first, second)
    except ValueError as e:
        print(f"Ошибка создания объекта: {e}")
        return None


# Пример использования
if __name__ == "__main__":
    # Создание объекта через функцию make_pair
    pair = make_pair(9.99, 5)

    if pair:
        PairDisplay.display(pair)  # Вывод данных
        print(f"Общая стоимость : {PairCostCalculator.cost(pair)}")  # Расчет стоимости всего товара

    # Способ с вводом данных с клавиатуры
    new_pair = PairInput.read()  # Ввод данных и создание новой пары
    if new_pair:
        PairDisplay.display(new_pair)  # Вывод данных
        print(f"Общая стоимость : {PairCostCalculator.cost(new_pair)}")  # Расчет стоимости всего товара
