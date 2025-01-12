#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from unittest.mock import patch

from src.individual_1 import Pair, make_pair


class TestPair(unittest.TestCase):
    """Тесты для класса Pair и связанных с ним функций."""

    def test_initialization_valid(self):
        """Проверка корректной инициализации объекта Pair."""
        pair = Pair(10.5, 3)
        self.assertEqual(pair.first, 10.5)
        self.assertEqual(pair.second, 3)

    def test_initialization_invalid_price(self):
        """Проверка выброса исключения при некорректной цене товара."""
        with self.assertRaises(ValueError):
            Pair(-5.0, 3)
        with self.assertRaises(ValueError):
            Pair(0, 3)
        with self.assertRaises(ValueError):
            Pair("abc", 3)

    def test_initialization_invalid_quantity(self):
        """Проверка выброса исключения при некорректном количестве товара."""
        with self.assertRaises(ValueError):
            Pair(10.5, -3)
        with self.assertRaises(ValueError):
            Pair(10.5, 0)
        with self.assertRaises(ValueError):
            Pair(10.5, "abc")

    def test_cost_calculation(self):
        """Проверка корректного расчёта стоимости товара."""
        pair = Pair(10.0, 5)
        self.assertEqual(pair.cost(), 50.0)

    @patch("builtins.input", side_effect=["19.99", "5"])
    def test_read_valid(self, mock_input):
        """Проверка успешного чтения данных с клавиатуры."""
        pair = Pair(1, 1)  # Создаём временный объект
        result = pair.read()
        self.assertTrue(result)
        self.assertEqual(pair.first, 19.99)
        self.assertEqual(pair.second, 5)

    @patch("builtins.input", side_effect=["-10", "5"])
    def test_read_invalid_price(self, mock_input):
        """Проверка обработки некорректного ввода цены с клавиатуры."""
        pair = Pair(1, 1)  # Создаём временный объект
        result = pair.read()
        self.assertFalse(result)

    @patch("builtins.input", side_effect=["19.99", "-5"])
    def test_read_invalid_quantity(self, mock_input):
        """Проверка обработки некорректного ввода количества с клавиатуры."""
        pair = Pair(1, 1)  # Создаём временный объект
        result = pair.read()
        self.assertFalse(result)

    def test_make_pair_valid(self):
        """Проверка успешного создания объекта Pair через функцию make_pair."""
        pair = make_pair(20.0, 2)
        self.assertIsNotNone(pair)
        self.assertEqual(pair.first, 20.0)
        self.assertEqual(pair.second, 2)

    def test_make_pair_invalid_price(self):
        """Проверка обработки некорректной цены при создании объекта через make_pair."""
        pair = make_pair(-20.0, 2)
        self.assertIsNone(pair)

    def test_make_pair_invalid_quantity(self):
        """Проверка обработки некорректного количества при создании объекта через make_pair."""
        pair = make_pair(20.0, -2)
        self.assertIsNone(pair)


if __name__ == "__main__":
    unittest.main()
