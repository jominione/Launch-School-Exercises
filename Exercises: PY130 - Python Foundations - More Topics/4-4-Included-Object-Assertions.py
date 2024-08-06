# Write a unittest assertion that will fail if the 'xyz' is not in the lst.

# Solution:

import unittest

class TestSuite(unittest.TestCase):
    def test_list(self):
        lst = ['abc', 'def', 'ghi']
        self.assertIn('xyz', lst)