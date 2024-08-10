# Write a program that will take a string of digits and return all the possible
# consecutive number series of a specified length in that string.

# For example, the string "012345" has the following 3-digit series:

# * 012
# * 123
# * 234

# Likewise, here are the 4-digit series:

# * 0123
# * 1234

# Finally, if you ask for a 6-digit series from a 5-digit string, you should
# throw an error.

# Solution:
from functools import reduce

class Series:
    def __init__(self, digits):
        self.digits = [int(digit) for digit in list(digits)]
        
    def slices(self, n):
        series = []
        if len(self.digits) < n:
            raise ValueError()
        else:
            for index in range(0,len(self.digits)+1-n):
                series.append(self.digits[index:index+n])
        return series

# Examples:

import unittest

class SeriesTest(unittest.TestCase):

    def test_simple_slices_of_one(self):
        series = Series("01234")
        self.assertEqual([[0], [1], [2], [3], [4]], series.slices(1))


    def test_simple_slices_of_one_again(self):
        series = Series("92834")
        self.assertEqual([[9], [2], [8], [3], [4]], series.slices(1))


    def test_simple_slices_of_two(self):
        series = Series("01234")
        self.assertEqual([[0, 1], [1, 2], [2, 3], [3, 4]], series.slices(2))


    def test_other_slices_of_two(self):
        series = Series("98273463")
        expected = [[9, 8], [8, 2], [2, 7], [7, 3], [3, 4], [4, 6], [6, 3]]
        self.assertEqual(expected, series.slices(2))


    def test_simple_slices_of_two_again(self):
        series = Series("37103")
        self.assertEqual([[3, 7], [7, 1], [1, 0], [0, 3]], series.slices(2))


    def test_simple_slices_of_three(self):
        series = Series("01234")
        self.assertEqual([[0, 1, 2], [1, 2, 3], [2, 3, 4]], series.slices(3))


    def test_simple_slices_of_three_again(self):
        series = Series("31001")
        self.assertEqual([[3, 1, 0], [1, 0, 0], [0, 0, 1]], series.slices(3))


    def test_other_slices_of_three(self):
        series = Series("982347")
        expected = [[9, 8, 2], [8, 2, 3], [2, 3, 4], [3, 4, 7]]
        self.assertEqual(expected, series.slices(3))


    def test_simple_slices_of_four(self):
        series = Series("01234")
        self.assertEqual([[0, 1, 2, 3], [1, 2, 3, 4]], series.slices(4))


    def test_simple_slices_of_four_again(self):
        series = Series("91274")
        self.assertEqual([[9, 1, 2, 7], [1, 2, 7, 4]], series.slices(4))


    def test_simple_slices_of_five(self):
        series = Series("01234")
        self.assertEqual([[0, 1, 2, 3, 4]], series.slices(5))


    def test_simple_slices_of_five_again(self):
        series = Series("81228")
        self.assertEqual([[8, 1, 2, 2, 8]], series.slices(5))


    def test_simple_slice_that_blows_up(self):
        series = Series("01234")
        with self.assertRaises(ValueError):
            series.slices(6)


    def test_more_complicated_slice_that_blows_up(self):
        slice_string = "01032987583"
        series = Series(slice_string)
        with self.assertRaises(ValueError):
            series.slices(len(slice_string) + 1)

if __name__ == "__main__":
    unittest.main()