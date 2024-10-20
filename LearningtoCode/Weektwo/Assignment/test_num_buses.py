import a1
import unittest


class TestNumBuses(unittest.TestCase):
    """ Test class for function a1.num_buses. """
    
    def test_num_buses_zero(self):
        """ Test num_buses with 0 passengers """
        actual = a1.num_buses(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_num_buses_one(self):
        """ Test num_buses with 1 passenger """
        actual = a1.num_buses(1)
        expected = 1
        self.assertEqual(expected, actual)

    def test_num_buses_exact_capacity(self):
        """ Test num_buses with exactly 40 passengers """
        actual = a1.num_buses(40)
        expected = 1
        self.assertEqual(expected, actual)

    def test_num_buses_double_capacity(self):
        """ Test num_buses with exactly 80 passengers """
        actual = a1.num_buses(80)
        expected = 2
        self.assertEqual(expected, actual)

    def test_num_buses_one_over_capacity(self):
        """ Test num_buses with 81 passengers """
        actual = a1.num_buses(81)
        print(f"the actual is {actual}")
        expected = 2
        self.assertEqual(expected, actual)

    def test_num_buses_large_number(self):
        """ Test num_buses with 155 passengers """
        actual = a1.num_buses(155)
        expected = 4
        self.assertEqual(expected, actual)

    def test_num_buses_odd_number(self):
        """ Test num_buses with 75 passengers """
        actual = a1.num_buses(75)
        expected = 2
        self.assertEqual(expected, actual)

    def test_num_buses_large_even_number(self):
        """ Test num_buses with a large even number of passengers """
        actual = a1.num_buses(1000)
        expected = 20
        self.assertEqual(expected, actual)

    def test_num_buses_large_odd_number(self):
        """ Test num_buses with a large odd number of passengers """
        actual = a1.num_buses(1001)
        expected = 21
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main(exit=False)