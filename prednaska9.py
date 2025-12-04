"""
from muj_modul import fibonacci
import unittest

class TestStringMethods(unittest.TestCase):
    def test_fibonacci(self):
        vysledek = fibonacci(2)
        self.assertEqual(vysledek, [1, 1, 2])

        self.assertEqual(fibonacci(10), [1, 1, 2, 3, 5, 8])

    def test_secti(self):
        self.assertEqual(1 + 1, 2)
"""

from muj_modul import fibonacci

def test_fibonacci():
    assert fibonacci(2) == [1, 1, 2]

    assert fibonacci(10) == [1, 1, 2, 3, 5, 8]


if __name__ == "__main__":
    pass