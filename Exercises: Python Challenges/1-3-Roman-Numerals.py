# Write some code that converts modern decimal numbers into their Roman
# number equivalents.

# The Romans were a clever bunch. They conquered most of Europe and ruled 
# it for hundreds of years. They invented concrete and straight roads and 
# even bikinis. One thing they never discovered though was the number zero. 
# This made writing and dating extensive histories of their exploits slightly 
# more challenging, but the system of numbers they came up with is still in 
# use today. For example the BBC uses Roman numerals to date their programmes.

# The Romans wrote numbers using letters - I, V, X, L, C, D, M. Notice that 
# these letters have lots of straight lines and are hence easy to hack into 
# stone tablets.

# 1  => I
# 10  => X
# 7  => VII

# There is no need to be able to convert numbers larger than about 3000. (The 
# Romans themselves didn't tend to go any higher)

# Wikipedia says: Modern Roman numerals ... are written by expressing each 
# digit separately starting with the left most digit and skipping any digit 
# with a value of zero.

# To see this in practice, consider the example of 1990. In Roman numerals, 
# 1990 is MCMXC:

# 1000=M
# 900=CM
# 90=XC

# 2008 is written as MMVIII:

# 2000=MM
# 8=VIII

# Solution:

class RomanNumeral:
    def __init__(self, number):
        self._number = number
    
    @property
    def number(self):
        return self._number
    
    def to_roman(self):
        thousand = self.number // 1000
        hundred = self.number // 100


# Examples:

import unittest

class RomanNumeralsTest(unittest.TestCase):
    @unittest.skip
    def test_1(self):
        number = RomanNumeral(1)
        self.assertEqual(number.to_roman(), "I")

    @unittest.skip
    def test_2(self):
        number = RomanNumeral(2)
        self.assertEqual(number.to_roman(), "II")

    @unittest.skip
    def test_3(self):
        number = RomanNumeral(3)
        self.assertEqual(number.to_roman(), "III")

    @unittest.skip
    def test_4(self):
        number = RomanNumeral(4)
        self.assertEqual(number.to_roman(), "IV")

    @unittest.skip
    def test_5(self):
        number = RomanNumeral(5)
        self.assertEqual(number.to_roman(), "V")

    @unittest.skip
    def test_6(self):
        number = RomanNumeral(6)
        self.assertEqual(number.to_roman(), "VI")

    @unittest.skip
    def test_9(self):
        number = RomanNumeral(9)
        self.assertEqual(number.to_roman(), "IX")

    @unittest.skip
    def test_27(self):
        number = RomanNumeral(27)
        self.assertEqual(number.to_roman(), "XXVII")

    @unittest.skip
    def test_48(self):
        number = RomanNumeral(48)
        self.assertEqual(number.to_roman(), "XLVIII")

    @unittest.skip
    def test_59(self):
        number = RomanNumeral(59)
        self.assertEqual(number.to_roman(), "LIX")

    @unittest.skip
    def test_93(self):
        number = RomanNumeral(93)
        self.assertEqual(number.to_roman(), "XCIII")

    @unittest.skip
    def test_141(self):
        number = RomanNumeral(141)
        self.assertEqual(number.to_roman(), "CXLI")

    @unittest.skip
    def test_163(self):
        number = RomanNumeral(163)
        self.assertEqual(number.to_roman(), "CLXIII")

    @unittest.skip
    def test_402(self):
        number = RomanNumeral(402)
        self.assertEqual(number.to_roman(), "CDII")

    @unittest.skip
    def test_575(self):
        number = RomanNumeral(575)
        self.assertEqual(number.to_roman(), "DLXXV")

    @unittest.skip
    def test_911(self):
        number = RomanNumeral(911)
        self.assertEqual(number.to_roman(), "CMXI")

    @unittest.skip
    def test_1024(self):
        number = RomanNumeral(1024)
        self.assertEqual(number.to_roman(), "MXXIV")

    @unittest.skip
    def test_3000(self):
        number = RomanNumeral(3000)
        self.assertEqual(number.to_roman(), "MMM")