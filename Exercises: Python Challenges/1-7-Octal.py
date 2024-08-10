# Implement octal to decial conversion. Given an octal input string, your
# program should produce a decimal output. Treat invalid input as octal 0.
# Note that the only valid digits in an octal number are 0, 1, 2, 3, 4, 5,
# 6, and 7.

# Note: Implement the conversion yourself. Don't use any built-in or library
# methods that perform the necessary conversions for you. In this exercise,
# the code necessary to perform the conversion is what we're looking for.

# About Octal (Base-8)

# Decimal is a base-10 system. A number 233 in base 10 notation can be 
# understood as a linear combination of powers of 10:

# * The rightmost digit gets multiplied by 10^0 = 1
# * The next digit gets multiplied by 10^1 = 10
# * The digit after that gets multiplied by 10^2 = 100
# * The digit after that gets multiplied by 10^3 = 1000
# * ...
# * The n_th_digit gets multiplied by 10^(n-1).
# * All of these values are then summed.

# Thus:

#   233 # decimal
# = 2*10^2 + 3*10^1 + 3*10^0
# = 2*100  + 3*10   + 3*1

# Octal numbers are similar, but they use a base-8 system. A number 233 in
# base 8 can be understood as a linear combination of powers of 8:

# * The rightmost digit gets multiplied by 8^0 = 1
# * The next digit gets multiplied by 8^1 = 8
# * The digit after that gets multiplied by 8^2 = 64
# * The digit after that gets multiplied by 8^3 = 512
# * ...
# * The n_th_digit gets multiplied by 8^(n-1).
# * All of these values are then summed.

# Thus:

#   233 # octal
# = 2*8^2 + 3*8^1 + 3*8^0
# = 2*64  + 3*8   + 3*1
# = 128   + 24    + 3
# = 155

# Solution:

class Octal:
    VALID_DIGITS = {'0', '1', '2', '3', '4', '5', '6', '7'}

    def __init__(self, number):
        self.number = str(number)

    def to_decimal(self):
        if self._is_valid():
            digits = tuple(zip([int(char) for char in self.number], range(len(self.number)-1, -1, -1)))
            return sum([digit * (8**index) for digit, index in digits])
        else:
            return 0

    def _is_valid(self):
        return (self.number.isnumeric()
                and (all(char in Octal.VALID_DIGITS for char in self.number)))

# Examples:

import unittest

class OctalTest(unittest.TestCase):

    def test_octal_1_is_decimal_1(self):
        self.assertEqual(1, Octal("1").to_decimal())

    def test_octal_10_is_decimal_8(self):
        self.assertEqual(8, Octal("10").to_decimal())

    def test_octal_17_is_decimal_15(self):
        self.assertEqual(15, Octal("17").to_decimal())

    def test_octal_11_is_decimal_9(self):
        self.assertEqual(9, Octal("11").to_decimal())

    def test_octal_130_is_decimal_88(self):
        self.assertEqual(88, Octal("130").to_decimal())

    def test_octal_2047_is_decimal_1063(self):
        self.assertEqual(1063, Octal("2047").to_decimal())

    def test_octal_7777_is_decimal_4095(self):
        self.assertEqual(4095, Octal("7777").to_decimal())

    def test_octal_1234567_is_decimal_342391(self):
        self.assertEqual(342391, Octal("1234567").to_decimal())

    def test_invalid_octal_is_decimal_0(self):
        self.assertEqual(0, Octal("carrot").to_decimal())

    def test_8_is_seen_as_invalid_and_returns_0(self):
        self.assertEqual(0, Octal("8").to_decimal())

    def test_9_is_seen_as_invalid_and_returns_0(self):
        self.assertEqual(0, Octal("9").to_decimal())

    def test_6789_is_seen_as_invalid_and_returns_0(self):
        self.assertEqual(0, Octal("6789").to_decimal())

    def test_abc1z_is_seen_as_invalid_and_returns_0(self):
        self.assertEqual(0, Octal("abc1z").to_decimal())

    def test_valid_octal_formatted_string_011_is_decimal_9(self):
        self.assertEqual(9, Octal("011").to_decimal())

    def test_234abc_is_seen_as_invalid_and_returns_0(self):
        self.assertEqual(0, Octal("234abc").to_decimal())

if __name__ == "__main__":
    unittest.main()