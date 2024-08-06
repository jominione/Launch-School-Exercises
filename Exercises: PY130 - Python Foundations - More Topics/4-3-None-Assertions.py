# Write a unittest assertion that will fail if value is not None.

# Solution:

import unittest

class TestSuite(unittest.TestCase):
    def test_none(self):
        x = 132
        self.assertIsNone(x)