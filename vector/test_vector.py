import unittest
from vector import Vector3D


class TestVector3D(unittest.TestCase):

    def test_can_sum(self):
        v1 = Vector3D(1, 2, 3)
        v2 = Vector3D(4, 5, 6)
        self.assertEqual(v1 + v2, Vector3D(5, 7, 9))
        self.assertEqual(v1 + 1, Vector3D(2, 3, 4))
        self.assertEqual(1 + v1, Vector3D(2, 3, 4))

    def test_can_subtract(self):
        v1 = Vector3D(1, 2, 3)
        v2 = Vector3D(4, 5, 6)
        self.assertEqual(v2 - v1, Vector3D(3, 3, 3))
        self.assertEqual(v1 - 1, Vector3D(0, 1, 2))

        self.assertRaises(TypeError, lambda: 1 - v1)

    def test_can_multiply(self):
        v1 = Vector3D(1, 2, 3)
        v2 = Vector3D(4, 6, 6)
        self.assertEqual(v2 * v1, Vector3D(4, 12, 18))
        self.assertEqual(v2 * 2, Vector3D(8, 12, 12))

    def test_can_divide(self):
        v1 = Vector3D(1, 2, 3)
        v2 = Vector3D(4, 6, 6)
        self.assertEqual(v2 / v1, Vector3D(4, 3, 2))
        self.assertEqual(v2 / 2, Vector3D(2, 3, 3))

    def test_can_unpack(self):
        vector = Vector3D(7, 8, 9)
        x, y, z = vector

        self.assertEqual(x, 7)

        self.assertEqual(y, 8)
        self.assertEqual(z, 9)
