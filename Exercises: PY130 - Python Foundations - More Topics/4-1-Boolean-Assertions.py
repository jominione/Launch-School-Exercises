# Write a unittest assertion that will fail if value % 2 != 0 is False.

# Solution:

import unittest

class TestBool(unittest.TestCase):
    def test_odd(self):
        x = 4
        self.assertTrue(x % 2 != 0, f"The value {x} is not odd.")