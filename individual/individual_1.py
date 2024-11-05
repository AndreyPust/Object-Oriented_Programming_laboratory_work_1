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

    def read(self):
        # Ввод значений с клавиатуры
        try:
            self.first = float(input("Введите цену товара (положительное дробное число): "))
            if self.first <= 0:
                raise ValueError("Цена должна быть положительным числом")

            self.second = int(input("Введите количество товара (положительное целое число): "))
            if self.second <= 0:
                raise ValueError("Количество должно быть положительным целым числом")
        except ValueError as e:
            print(f"Ошибка ввода: {e}")
            return False
        return True

    def display(self):
        # Вывод информации о товаре
        print(f"Цена товара: {self.first}, Количество: {self.second}")

    def cost(self):
        # Метод для вычисления стоимости товара
        return self.first * self.second


def make_pair(first, second):
    # Функция для создания объекта Pair
    try:
        return Pair(first, second)
    except ValueError as e:
        print(f"Ошибка создания объекта: {e}")
        return None


# Пример использования:
if __name__ == "__main__":
    # Создание объекта через функцию make_pair
    pair = make_pair(19.99, 5)

    if pair:
        pair.display()  # Вывод данных
        print(f"Общая стоимость: {pair.cost()}")  # Расчет стоимости

    # Ввод данных с клавиатуры
    new_pair = Pair(1, 1)  # создаем новый объект
    if new_pair.read():
        new_pair.display()  # Вывод данных
        print(f"Общая стоимость: {new_pair.cost()}")  # Расчет стоимости
