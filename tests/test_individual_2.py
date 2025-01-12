#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

from src.individual_2 import Money


class TestMoney(unittest.TestCase):
    """Тесты для класса Money."""

    def test_initialization(self):
        """Проверка корректной инициализации объекта Money."""
        money = Money()
        self.assertTrue(all(value == 0 for value in money.amounts.values()))

    def test_total_value(self):
        """Проверка корректного вычисления общей суммы."""
        money = Money()
        money.amounts[100] = 3
        money.amounts[0.5] = 4
        rubles, kopeks = money.total_value()
        self.assertEqual(rubles, 302)
        self.assertEqual(kopeks, 0)

    def test_add(self):
        """Проверка корректного сложения двух денежных сумм."""
        money1 = Money()
        money2 = Money()
        money1.amounts[1000] = 2
        money2.amounts[500] = 3

        result = money1.add(money2)
        self.assertEqual(result.amounts[1000], 2)
        self.assertEqual(result.amounts[500], 3)

    def test_subtraction(self):
        """Проверка корректного вычитания двух денежных сумм."""
        money1 = Money()
        money2 = Money()
        money1.amounts[1000] = 2
        money1.amounts[500] = 3
        money2.amounts[500] = 1

        result = money1.subtraction(money2)
        self.assertEqual(result.amounts[1000], 2)
        self.assertEqual(result.amounts[500], 2)

    def test_division(self):
        """Проверка корректного деления суммы на число."""
        money = Money()
        money.amounts[1000] = 2

        result = money.division(2)
        self.assertEqual(result.amounts[1000], 1)

    def test_multiplication(self):
        """Проверка корректного умножения суммы на число."""
        money = Money()
        money.amounts[500] = 4

        result = money.multiplication(1.5)
        self.assertEqual(result.amounts[500], 6)

    def test_equivalent(self):
        """Проверка равенства двух денежных сумм."""
        money1 = Money()
        money2 = Money()
        money1.amounts[100] = 5
        money2.amounts[100] = 5

        self.assertTrue(money1.equivalent(money2))

    def test_lt(self):
        """Проверка операции сравнения 'меньше'."""
        money1 = Money()
        money2 = Money()
        money1.amounts[50] = 3
        money2.amounts[100] = 1

        self.assertFalse(money1.lt(money2))

    def test_le(self):
        """Проверка операции сравнения 'больше'."""
        money1 = Money()
        money2 = Money()
        money1.amounts[500] = 3
        money2.amounts[100] = 1

        self.assertTrue(money1.le(money2))


if __name__ == "__main__":
    unittest.main()
