# Write a program that manages robot factory settings.

# When robots come off the factory floor, they have no name. The first time
# you boot them up, a random name is generated, such as RX837 or BC811.

# Every once in a while, we need to reset a robot to its factory settings,
# which means that their name gets wiped. The next time you ask, it will 
# respond with a new random name.

# The names must be random; they should not follow a predictable sequence.
# Random names means there is a risk of collisions. Your solution should not 
# allow using the same name twice.

# Solution:

import re
import random

class Robot:

    def __init__(self):
        self._name = self._generate_name()

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name
    
    def _generate_name(self):
        alphabet = [chr(i) + chr(j) for i in range(65, 91) 
                                    for j in range(65, 91)]
        number = [str(num1) + str(num2) + str(num3) for num1 in range(10)
                                                    for num2 in range(10)
                                                    for num3 in range(10)]
        
        names = [alphabet[letters] + number[numbers] 
                                    for letters in range(len(alphabet))
                                    for numbers in range(len(number))]
        
        return random.sample(names, 1)[0]

    def reset(self):
        self.name = self._generate_name()

robot1 = Robot().name
robot2 = Robot().name
print(robot1)
print(robot2)

# Examples:

import unittest


class RobotTest(unittest.TestCase):
    DIFFERENT_ROBOT_NAME_SEED = 1234
    SAME_INITIAL_ROBOT_NAME_SEED = 1000

    NAME_REGEXP = re.compile(r"^[A-Z]{2}\d{3}$")

    def test_has_name(self):
        self.assertTrue(self.NAME_REGEXP.match(Robot().name))

    def test_name_sticks(self):
        robot = Robot()
        self.assertEqual(robot.name, robot.name)

    def test_different_robots_have_different_names(self):
        random.seed(RobotTest.DIFFERENT_ROBOT_NAME_SEED)
        self.assertNotEqual(Robot().name, Robot().name)

    def test_reset_name(self):
        random.seed(RobotTest.DIFFERENT_ROBOT_NAME_SEED)
        robot = Robot()
        name1 = robot.name
        robot.reset()
        name2 = robot.name
        self.assertNotEqual(name1, name2)
        self.assertTrue(self.NAME_REGEXP.match(name2))

    def test_different_name_when_chosen_name_is_taken(self):
        random.seed(RobotTest.SAME_INITIAL_ROBOT_NAME_SEED)
        name1 = Robot().name
        random.seed(RobotTest.SAME_INITIAL_ROBOT_NAME_SEED)
        name2 = Robot().name
        self.assertNotEqual(name1, name2)

if __name__ == "__main__":
    unittest.main()