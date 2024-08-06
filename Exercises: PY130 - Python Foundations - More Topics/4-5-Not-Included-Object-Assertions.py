# Write a test that will fail if 'xyz' is one of the elements in the list
# lst.

# Solution:

import unittest

class TestListNotContains(unittest.TestCase):
    def test_does_not_contain_xyz(self):
        lst = ['abc', 'def', 'xyz']  # Replace with the list you want to test

        # Assert that 'xyz' is not in the list
        self.assertNotIn('xyz', lst, f"'xyz' should not be in the list {lst}")