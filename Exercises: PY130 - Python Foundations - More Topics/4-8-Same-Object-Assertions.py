# Write a test that will fail if lst and the return value of lst.process are 
# different objects.

# Solution:

import unittest

# Example list class with a process method
class CustomList(list):
    def process(self):
        # This is just an example. This method should return the same object.
        return CustomList([4, 5, 6])

class TestListProcessing(unittest.TestCase):
    def test_process_returns_same_object(self):
        lst = CustomList([1, 2, 3])  # Replace with your list instance
        
        # Call process method and assert that lst and the return value 
        # are the same object
        processed_lst = lst.process()
        self.assertIs(lst, processed_lst, "The process method did not return "\
                      "the same object.")