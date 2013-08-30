import unittest
from vector import Vec2D


class VectorTest(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(Vec2D(1, -4) + Vec2D(3, 2), Vec2D(4, -2))

    def test_equation(self):
        self.assertTrue(Vec2D(4, 1) == Vec2D(4, 1))
        self.assertFalse(Vec2D(0, 3) == Vec2D(-2, 3))

    def test_not_equal(self):
        self.assertTrue(Vec2D(-1, 4) != Vec2D(1, 4))
        self.assertFalse(Vec2D(1, 2) != Vec2D(1, 2))

    def test_less_than(self):
        self.assertTrue(Vec2D(-1, 4) < Vec2D(1, 5))
        self.assertFalse(Vec2D(5, 2) < Vec2D(1, 2))

    def test_hashable(self):
        self.assertTrue(hash(Vec2D(1, 2)) == hash(Vec2D(1, 2)))
        self.assertFalse(hash(Vec2D(3, 2)) == hash(Vec2D(1, 2)))
