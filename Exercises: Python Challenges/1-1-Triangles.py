# Write a program to determine whether a triangle is equilateral, isosceles,
# or scalene.

# An equilateral triangle has all three sides the same length.

# An isosceles triangle has exactly two sides of the same length.

# A scalene triangle has all sides of different lengths.

# Note: For a shape to be a triangle at all, all sides must be of length > 0,
# and the sum of the lengths of any two sides must greater than the length
# of the third side.

# Solution:

class Triangle:

    def __init__(self, side1, side2, side3):
        self.sides = [side1, side2, side3]
        if not self._is_valid():
            raise ValueError("Invalid triangle lengths")

    @property
    def kind(self):

        if len(set(self.sides)) == 1:
            return "equilateral"
        elif len(set(self.sides)) == 2:
            return "isosceles"
        else:
            return "scalene"
    
    def _is_valid(self):
        return (
            all(side > 0 for side in self.sides)
            and self.sides[0] + self.sides[1] > self.sides[2]
            and self.sides[0] + self.sides[2] > self.sides[1]
            and self.sides[1] + self.sides[2] > self.sides[0]
        )

# Examples:

import unittest

class TestTriangle(unittest.TestCase):
    @unittest.skip
    def test_equilateral_equal_sides(self):
        triangle = Triangle(2, 2, 2)
        self.assertEqual(triangle.kind, "equilateral")

    @unittest.skip
    def test_larger_equilateral_equal_sides(self):
        triangle = Triangle(10, 10, 10)
        self.assertEqual(triangle.kind, "equilateral")

    @unittest.skip
    def test_isosceles_last_two_sides_equal(self):
        triangle = Triangle(3, 4, 4)
        self.assertEqual(triangle.kind, "isosceles")

    @unittest.skip
    def test_isosceles_first_last_sides_equal(self):
        triangle = Triangle(4, 3, 4)
        self.assertEqual(triangle.kind, "isosceles")

    @unittest.skip
    def test_isosceles_first_two_sides_equal(self):
        triangle = Triangle(4, 4, 3)
        self.assertEqual(triangle.kind, "isosceles")

    @unittest.skip
    def test_isosceles_exactly_two_sides_equal(self):
        triangle = Triangle(10, 10, 2)
        self.assertEqual(triangle.kind, "isosceles")

    @unittest.skip
    def test_scalene_no_equal_sides(self):
        triangle = Triangle(3, 4, 5)
        self.assertEqual(triangle.kind, "scalene")

    @unittest.skip
    def test_scalene_larger_no_equal_sides(self):
        triangle = Triangle(10, 11, 12)
        self.assertEqual(triangle.kind, "scalene")

    @unittest.skip
    def test_scalene_no_equal_sides_descending(self):
        triangle = Triangle(5, 4, 2)
        self.assertEqual(triangle.kind, "scalene")

    @unittest.skip
    def test_small_triangles_are_legal(self):
        triangle = Triangle(0.4, 0.6, 0.3)
        self.assertEqual(triangle.kind, "scalene")

    @unittest.skip
    def test_no_size_is_illegal(self):
        with self.assertRaises(ValueError):
            Triangle(0, 0, 0)

    @unittest.skip
    def test_negative_size_is_illegal(self):
        with self.assertRaises(ValueError):
            Triangle(3, 4, -5)

    @unittest.skip
    def test_size_inequality_is_illegal(self):
        with self.assertRaises(ValueError):
            Triangle(1, 1, 3)

    @unittest.skip
    def test_size_inequality_is_illegal_2(self):
        with self.assertRaises(ValueError):
            Triangle(7, 3, 2)

    @unittest.skip
    def test_size_inequality_is_illegal_3(self):
        with self.assertRaises(ValueError):
            Triangle(10, 1, 3)

    @unittest.skip
    def test_size_inequality_is_illegal_4(self):
        with self.assertRaises(ValueError):
            Triangle(1, 1, 2)