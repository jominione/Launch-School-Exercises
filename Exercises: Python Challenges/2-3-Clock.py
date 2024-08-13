# Create a clock that is independent of date.

# You should be able to add minutes to and subtract mintues from the time
# represented by a given Clock object. Note that you should not mutate Clock
# objects when adding and subtracting minutes -- create a new Clock object.

# Two clock objects that represent the same time should be equal to each other.

# You may not use any built-in date or time functionality; just use arithmetic
# operations.

# Solution:

class Clock:

    def __init__(self, hours, minutes):
        self._hours = hours
        self._minutes = minutes

    @classmethod
    def at(cls, hours, minutes=0):
        cls._hours = hours
        self._minutes = minutes
        result = f'{self._hours:02}:{self._minutes:02}'
        return result

    def __eq__(self, other):
        if (self.at(self._hours, self._minutes) == 
           other.at(other._hours, other._minutes)):
            return True
        else:
            False

    def __str__(self):

        return f'{self.at(self._hours, self._minutes)}'

    def __add__(self, number):
        
        
        hours, minutes = self._minutes_to_time(number)

        return self.at(self._hours + hours,
                       self._minutes + minutes)

    def __sub__(self):

        return self.at(self._hours - minutes_to_time(number)[0],
                       self._minutes - minutes_to_time(number)[1])

 
    def _minutes_to_time(self, number):
        minutes_excluding_days = number % (24 * 60)
        hours = minutes_excluding_days // 60
        minutes = minutes_excluding_days % 60
        result = (hours, minutes)
        return result


print(minutes_to_time(3061))

# Examples:

import unittest

class ClockTest(unittest.TestCase):
    @unittest.skip
    def test_on_the_hour(self):
        self.assertEqual('08:00', str(Clock.at(8)))
        self.assertEqual('09:00', str(Clock.at(9)))
    @unittest.skip
    def test_past_the_hour(self):
        self.assertEqual('11:09', str(Clock.at(11, 9)))
    @unittest.skip
    def test_add_a_few_minutes(self):
        clock = Clock.at(10) + 3
        self.assertEqual('10:03', str(clock))
    @unittest.skip
    def test_adding_does_not_mutate(self):
        old_clock = Clock.at(10)
        new_clock = old_clock + 3
        self.assertIsNot(new_clock, old_clock)
    @unittest.skip
    def test_subtract_fifty_minutes(self):
        clock = Clock.at(0) - 50
        self.assertEqual('23:10', str(clock))
    @unittest.skip
    def test_subtracting_does_not_mutate(self):
        old_clock = Clock.at(10)
        new_clock = old_clock - 50
        self.assertIsNot(new_clock, old_clock)
    @unittest.skip
    def test_add_over_an_hour(self):
        clock = Clock.at(10) + 61
        self.assertEqual('11:01', str(clock))
    @unittest.skip
    def test_wrap_around_at_midnight(self):
        clock = Clock.at(23, 30) + 60
        self.assertEqual('00:30', str(clock))
    @unittest.skip
    def test_add_more_than_a_day(self):
        clock = Clock.at(10) + 3061
        self.assertEqual('13:01', str(clock))
    @unittest.skip
    def test_subtract_a_few_minutes(self):
        clock = Clock.at(10, 30) - 5
        self.assertEqual('10:25', str(clock))
    @unittest.skip
    def test_subtract_minutes(self):
        clock = Clock.at(10) - 90
        self.assertEqual('08:30', str(clock))
    @unittest.skip
    def test_wrap_around_at_negative_midnight(self):
        clock = Clock.at(0, 30) - 60
        self.assertEqual('23:30', str(clock))
    @unittest.skip
    def test_subtract_more_than_a_day(self):
        clock = Clock.at(10) - 3061
        self.assertEqual('06:59', str(clock))
    @unittest.skip
    def test_equivalent_clocks(self):
        clock1 = Clock.at(15, 37)
        clock2 = Clock.at(15, 37)
        self.assertEqual(clock1, clock2)
    @unittest.skip
    def test_non_equivalent_clocks(self):
        clock1 = Clock.at(15, 37)
        clock2 = Clock.at(15, 36)
        clock3 = Clock.at(14, 37)
        self.assertNotEqual(clock1, clock2)
        self.assertNotEqual(clock1, clock3)
    @unittest.skip
    def test_wrap_around_backwards(self):
        clock1 = Clock.at(0, 30) - 60
        clock2 = Clock.at(23, 30)
        self.assertEqual(clock1, clock2)

if __name__ == '__main__':
    unittest.main()