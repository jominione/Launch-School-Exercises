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
        thousands = (self.number // 1000) * 1000
        hundreds = ((self.number - thousands) // 100) * 100
        tens = ((self.number - thousands - hundreds) // 10) * 10
        ones = self.number - thousands - hundreds - tens
        roman_numeral = ''
        match thousands:
            case 1000:
                roman_numeral += 'M'
            case 2000:
                roman_numeral += 'MM'
            case 3000:
                roman_numeral += 'MMM'
        match hundreds:
            case 100:
                roman_numeral += 'C'
            case 200:
                roman_numeral += 'CC'
            case 300:
                roman_numeral += 'CCC'
            case 400:
                roman_numeral += 'CD'
            case 500:
                roman_numeral += 'D'
            case 600:
                roman_numeral += 'DC'
            case 700:
                roman_numeral += 'DCC'
            case 800:
                roman_numeral += 'DCCC'
            case 900:
                roman_numeral += 'CM'
        match tens:
            case 10:
                roman_numeral += 'X'
            case 20:
                roman_numeral += 'XX'
            case 30:
                roman_numeral += 'XXX'
            case 40:
                roman_numeral += 'XL'
            case 50:
                roman_numeral += 'L'
            case 60:
                roman_numeral += 'LX'
            case 70:
                roman_numeral += 'LXX'
            case 80:
                roman_numeral += 'LXXX'
            case 90:
                roman_numeral += 'XC'
        match ones:
            case 1:
                roman_numeral += 'I'
            case 2:
                roman_numeral += 'II'
            case 3:
                roman_numeral += 'III'
            case 4:
                roman_numeral += 'IV'
            case 5:
                roman_numeral += 'V'
            case 6:
                roman_numeral += 'VI'
            case 7:
                roman_numeral += 'VII'
            case 8:
                roman_numeral += 'VIII'
            case 9:
                roman_numeral += 'IX'
        
        return roman_numeral

# Examples:

import unittest

class RomanNumeralsTest(unittest.TestCase):

    def test_1(self):
        number = RomanNumeral(1)
        self.assertEqual(number.to_roman(), "I")

    def test_2(self):
        number = RomanNumeral(2)
        self.assertEqual(number.to_roman(), "II")

    def test_3(self):
        number = RomanNumeral(3)
        self.assertEqual(number.to_roman(), "III")

    def test_4(self):
        number = RomanNumeral(4)
        self.assertEqual(number.to_roman(), "IV")

    def test_5(self):
        number = RomanNumeral(5)
        self.assertEqual(number.to_roman(), "V")

    def test_6(self):
        number = RomanNumeral(6)
        self.assertEqual(number.to_roman(), "VI")

    def test_9(self):
        number = RomanNumeral(9)
        self.assertEqual(number.to_roman(), "IX")

    def test_27(self):
        number = RomanNumeral(27)
        self.assertEqual(number.to_roman(), "XXVII")

    def test_48(self):
        number = RomanNumeral(48)
        self.assertEqual(number.to_roman(), "XLVIII")

    def test_59(self):
        number = RomanNumeral(59)
        self.assertEqual(number.to_roman(), "LIX")

    def test_93(self):
        number = RomanNumeral(93)
        self.assertEqual(number.to_roman(), "XCIII")

    def test_141(self):
        number = RomanNumeral(141)
        self.assertEqual(number.to_roman(), "CXLI")

    def test_163(self):
        number = RomanNumeral(163)
        self.assertEqual(number.to_roman(), "CLXIII")

    def test_402(self):
        number = RomanNumeral(402)
        self.assertEqual(number.to_roman(), "CDII")

    def test_575(self):
        number = RomanNumeral(575)
        self.assertEqual(number.to_roman(), "DLXXV")

    def test_911(self):
        number = RomanNumeral(911)
        self.assertEqual(number.to_roman(), "CMXI")

    def test_1024(self):
        number = RomanNumeral(1024)
        self.assertEqual(number.to_roman(), "MXXIV")

    def test_3000(self):
        number = RomanNumeral(3000)
        self.assertEqual(number.to_roman(), "MMM")