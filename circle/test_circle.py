import math
import unittest

from circle import Circle


class TestCircle(unittest.TestCase):
    def test_can_create_circle(self):
        cases = [1.0, 3.0, 4.0, 10000.0]

        for radius in cases:
            circle = Circle(1, 2, radius)
            self.assertEqual(repr(circle), f"Circle(x=1, y=2, radius={radius})")
            self.assertEqual(circle.radius, radius)

    def test_raises_if_radius_is_invalid(self):
        cases = [0, -1, -1000]

        for radius in cases:
            self.assertRaises(ValueError, Circle, 1, 2, radius)

    def test_can_calculate_square(self):
        cases = [
            [1, math.pi],
            [3, 9 * math.pi],
            [4, 16 * math.pi],
            [10000, 100_000_000 * math.pi],
        ]

        for case in cases:
            radius, square = case
            circle = Circle(1, 2, radius)
            self.assertAlmostEqual(circle.square(), square, 7)

    def test_can_patch(self):
        cases = [
            [(1, 2, 9), (2, 4, None), (2, 4, 9)],
            [(1, 2, 9), (None, None, None), (1, 2, 9)],
            [(1, 2, 9), (None, None, 3), (1, 2, 3)],
        ]

        for case in cases:
            sides, patch, expected = case

            circle = Circle(*sides)
            patched = circle.patch(*patch)
            self.assertIsNot(circle, patched)
            self.assertEqual(patched.x, expected[0])
            self.assertEqual(patched.y, expected[1])
            self.assertEqual(patched.radius, expected[2])

    def test_point_inside(self):
        cases = [
            [(1, 2, 1), (1, 2), True],
            [(1, 2, 1), (1, 3), True],
            [(1, 2, 1), (1, 3), True],
            [(1, 2, 1), (1, 3.1), False],
        ]
        for case in cases:
            sides, (x, y), expected = case
            self.assertEqual(expected, Circle(*sides).point_inside(x, y))

    def test_point_on_circle(self):
        cases = [
            [(1, 2, 1), (1, 2), False],
            [(1, 2, 1), (1, 3), True],
            [(1, 2, 1), (1, 3), True],
            [(1, 2, 1), (1, 3.00000001), True],
        ]
        for case in cases:
            sides, (x, y), expected = case
            self.assertEqual(expected, Circle(*sides).point_on_circle(x, y))
