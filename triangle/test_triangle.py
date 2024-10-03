import unittest

from triangle import Triangle


class TestTriangle(unittest.TestCase):
    def test_can_create_triangle(self):
        cases = [
            (2, 5, 4),
            (7, 6, 8),
            (60000, 30000, 50000),
        ]
        for sides in cases:
            t = Triangle(*sides)
            self.assertEqual(t.a, sides[0])
            self.assertEqual(t.b, sides[1])
            self.assertEqual(t.c, sides[2])

    def test_raises_if_sides_are_invalid(self):
        cases = [
            [(0, 0, 0), ValueError],
            [(1, 2, 0), ValueError],
            [(1, 0, 2), ValueError],
            [(0, 1, 2), ValueError],
            [(-1, 1, 2), ValueError],
            [(1, -1, 2), ValueError],
            [(1, 1, -1), ValueError],
            [(1, 3, 4), ValueError],
        ]
        for case in cases:
            sides, error = case
            self.assertRaises(error, Triangle, *sides)

    def test_can_calculate_square_with_correct_sides(self):
        cases = [
            [(2.0, 5.0, 4.0), 3.7996710],
            [(7.0, 6.0, 8.0), 20.333163],
            [(60000.0, 30000.0, 50000.0), 748331477.3547883],
        ]

        for case in cases:
            sides, square = case
            t = Triangle(*sides)
            repr_str = f"Triangle(a={sides[0]}, b={sides[1]}, c={sides[2]})"
            self.assertEqual(repr(t), repr_str)
            self.assertEqual(t.a, sides[0])
            self.assertEqual(t.b, sides[1])
            self.assertEqual(t.c, sides[2])
            self.assertAlmostEqual(t.square(), square, 6)

    def test_can_check_if_triangle_is_right(self):
        cases = [
            ([1, 2, 2], 7, False),
            ([3, 4, 5], 7, True),
            ([4, 3, 5], 7, True),
            ([5.00000001, 3.0, 4.0], 6, True),  # This should be right triangle with 6 places
        ]

        for case in cases:
            sides, places, ok = case
            t = Triangle(*sides)
            self.assertEqual(t.is_right(places), ok)

    def test_with_sides_updates_triangle(self):
        cases = [
            [(2, 5, 4), (3, None, None), (3, 5, 4), None],
            [(2, 5, 4), (1, None, None), (), ValueError],
        ]
        for case in cases:
            sides, patches, result, error = case
            base = Triangle(*sides)
            if error is not None:
                self.assertRaises(ValueError, base.with_sides, *patches)
                return

            patched = base.with_sides(*patches)
            self.assertEqual(patched.a, float(result[0]))
            self.assertEqual(patched.b, float(result[1]))
            self.assertEqual(patched.c, float(result[2]))
