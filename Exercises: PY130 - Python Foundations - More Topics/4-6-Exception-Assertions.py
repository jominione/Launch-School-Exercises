# Write a unittest assertion that will fail unless employee.hire raises a 
# NoExperienceError exception.

# Solution:

import unittest

class NoExperienceError(Exception):
    pass

# Example Employee class
class Employee:
    def hire(self):
        # Code that raises NoExperienceError if conditions are met
        raise NoExperienceError("No experience provided")

class TestEmployeeHiring(unittest.TestCase):
    def test_hire_raises_no_experience_error(self):
        employee = Employee()

        # Assert that hiring raises a NoExperienceError
        with self.assertRaises(NoExperienceError) as context:
            employee.hire()
        
        # Optionally check the exception message
        self.assertEqual(str(context.exception), "No experience provided")