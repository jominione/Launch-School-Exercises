# Write a unittest assertion that will fail if value.lower does not return
# 'xyz'.

# Solution:

import unittest

class TestBool(unittest.TestCase):
    def test_value(self):
        x = 'ABC'
        self.assertEqual(x.lower(), 'xyz', f"The value {x} is did not return "\
                         f"'xyz' but {x.lower()}.")