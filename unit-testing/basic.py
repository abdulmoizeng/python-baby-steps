# This one is an implementation for `unittest` : A built in test runner

import unittest


def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def wrong_subtraction(a, b):
    return a - b - 1


def wrong_addition(a, b):
    return a + 1 + b


class TestAddition(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(addition(2, 4), 6, "2 + 4 should result in 6")

    def test_subtraction(self):
        self.assertEqual(subtraction(6, 3), 3, "6 - 3 should result in 3")

    def test_wrong_addition(self):
        self.assertEqual(wrong_addition(2, 4), 6, "6 should be the result : Test Failed")

    def test_wrong_subtraction(self):
        self.assertEqual(wrong_subtraction(6, 3), 3, "3 Should be the result : Test Failed")


if __name__ == '__main__':
    unittest.main()