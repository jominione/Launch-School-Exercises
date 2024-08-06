# Write a unittest assertion that will fail if value is not an instance of 
# the Numeric class exactly. value should not be an instance of one of 
# Numeric's superclasses.

# Solution:

import unittest

# Example Numeric class
class Numeric:
    pass

# Example subclass of Numeric
class SubNumeric(Numeric):
    pass

class TestExactType(unittest.TestCase):
    def test_value_is_exactly_numeric(self):
        value = 'zysf'  # Replace with the value you want to test

        # Assert that value is exactly an instance of Numeric and not a subclass
        self.assertIsInstance(value, Numeric, f"value is not exactly an "\
                      f"instance of Numeric but {type(value).__name__}")