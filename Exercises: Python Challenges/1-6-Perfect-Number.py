# The Greek mathematician Nicomachus devised a classification scheme for
# natural numbers (1, 2, 3, ...), identifying each as belonging uniquely to
# the categories of abundant, perfect, or deficient based on a comparison
# between the number and the sum of its positive divisors (the numbers that)
# can be evely divided into the target number with no remainder, excluding 
# the number itself). For instance, the positive divisors of 15 are 1, 3, and
# 5. This sum is known as the Aliquot sum.

# * Perfect numbers have an Aliquot sum that is equal to the original number.
# * Abundant numbers have an Aliquot sum that is greater than the original
#   number.
# * Deficient numbers have an Aliquot sumt hat is less than the original
#   number.

# Examples:

# * 6 is a perfect number since its divisors 1, 2, and 3, and 1 + 2 + 3 = 6.
# * 28 is a perfect number since its divisors are 1, 2, 4, 7, and 14 and 1 + 2
#   + 4 + 7 + 14 = 28.
# * 15 is a deficient number since its divisors are 1, 3, and 5 and 1 + 3 
#   + 5 = 9 which is less than 15.
# * 24 is an abundant number since its divisors are 1, 2, 3, 4, 6, 8, and 12
#   and 1 + 2 + 3 + 4 + 6 + 8 + 12 = 36 which is greater than 24.
# * Prime numbers 7, 13, etc. are always deficient since their only divisor is
#   1.

# Write a program that can tell whether a number is perfect, abundant, or
# deficient.

# Solution:

class PerfectNumber:
        
    @classmethod
    def classify(cls, number):
        if number < 1:
            raise ValueError("Input must be a positive integer")
        
        divisors = [num for num in range(1, number) if \
                    number % num == 0]
        
        if sum(divisors) == number:
            return 'perfect'
        elif sum(divisors) > number:
            return 'abundant'
        else:
            return 'deficient'

# Examples:

import unittest

class PerfectNumberTest(unittest.TestCase):

    def test_initialize_perfect_number(self):
        try:
            PerfectNumber.classify(-1)
            self.fail("Expected exception not raised")
        except ValueError as e:
            self.assertEqual(str(e), "Input must be a positive integer")

    def test_classify_deficient(self):
        result = PerfectNumber.classify(13)
        self.assertEqual(result, "deficient")

    def test_classify_perfect(self):
        result = PerfectNumber.classify(28)
        self.assertEqual(result, "perfect")

    def test_classify_abundant(self):
        result = PerfectNumber.classify(12)
        self.assertEqual(result, "abundant")

if __name__ == "__main__":
    unittest.main()