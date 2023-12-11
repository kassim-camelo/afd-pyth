import unittest
from main import calculator

class TestCalculator(unittest.TestCase):
    def test_calc(self):
        self.assertEqual(calculator("1 + 1"), 2)
        self.assertEqual(calculator("2 * 3"), 6)
        self.assertEqual(calculator("4 - 5"), -1)
        self.assertEqual(calculator("6 / 2"), 3)
        self.assertEqual(calculator("(1 + 2) * 3"), 9)
        self.assertEqual(calculator("2 * (3 + 4)"), 14)
        self.assertEqual(calculator("(2 + 3) * (4 - 1)"), 15)
        self.assertEqual(calculator("((2 + 3) * 4) - 5"), 15)
        self.assertEqual(calculator("2 * (3 + (4 - 5))"), 4)
        self.assertEqual(calculator("(2 + 3) * (4 - (5 + 6))"), -35)
        self.assertEqual(calculator("((2 + 3) * 4) - (5 + 6)"), 9)
        self.assertEqual(calculator("2 * ((3 + 4) - 5)"), 4)
        self.assertEqual(calculator("(2 + (3 * 4)) - 5"), 9)
        self.assertEqual(calculator("2 * (3 + (4 / 2))"), 10)
        self.assertEqual(calculator("(2 + 3) * (4 / (5 - 2))"), 6.6667)
        self.assertEqual(calculator("((2 + 3) * 4) / 5"), 4)
        self.assertEqual(calculator("2 * ((3 + 4) / 2)"), 7)
        self.assertEqual(calculator("(2 + (3 * 4)) / 5"), 2.8)
        self.assertEqual(calculator("2 * (3 + (4 * 2))"), 22.0)
        self.assertEqual(calculator("(2 + 3) * (4 * (5 - 2))"), 60.0)
        self.assertEqual(calculator("((2 + 3) * 4) * 5"), 100)
        self.assertEqual(calculator("2 * ((3 + 4) * 2)"), 28)
        self.assertEqual(calculator("(2 + (3 / 4)) - 5"), -2.25)
        self.assertEqual(calculator("2 * (3 + (4 / 2))"), 10)
        self.assertEqual(calculator("(2 + 3) / (4 / (5 - 2))"), 3.75)
        self.assertEqual(calculator("((2 + 3) / 4) - 5"), -3.75)
        self.assertEqual(calculator("2 / ((3 + 4) - 5)"), 1)
        self.assertEqual(calculator("(2 + (3 / 4)) / 5"), 0.55)
        with self.assertRaises(Exception):
            calculator("1 + 2 +")

if __name__ == '__main__':
    unittest.main()