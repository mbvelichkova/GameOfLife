import unittest
from vector import Vec2D

class VectorTest(unittest.TestCase):
    def test_multiplication(self):
        self.assertEqual(Vec2D(3, -2) * 3, Vec2D(9, -6))

    def test_addition(self):
        self.assertEqual(Vec2D(1, -4) + Vec2D(3, 2), Vec2D(4, -2))

    def test_subtraction(self):
        self.assertEqual(Vec2D(3, 8) - Vec2D(4, 3), Vec2D(-1, 5))

    def test_floordivision(self):
        self.assertEqual(Vec2D(4, 7) // 2, Vec2D(2, 3))

    def test_negation(self):
        self.assertEqual(-Vec2D(2, -4), Vec2D(-2, 4))

    def test_equation(self):
        self.assertTrue(Vec2D(4, 1) == Vec2D(4, 1))
        self.assertFalse(Vec2D(0, 3) == Vec2D(-2, 3))

    def test_not_equal(self):
        self.assertTrue(Vec2D(-1, 4) != Vec2D(1, 4))
        self.assertFalse(Vec2D(1, 2) != Vec2D(1, 2))