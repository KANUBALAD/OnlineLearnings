import a1
import unittest


class TestNumBuses(unittest.TestCase):
    """ Test class for function a1.num_buses. """
    def test_num_buses_1(self):
        """ Test num_buses with with 0"""
        actual = a1.num_buses(0)
        expected = 0
        self.assertEqual(expected, actual)


    def test_num_buses_1(self):
        """ Test num_buses with with 1"""
        actual = a1.num_buses(1)
        expected = 1
        self.assertEqual(expected, actual)


    def test_num_buses_2(self):
        """ Test num_buses with with even number 40"""
        actual = a1.num_buses(40)
        expected = 1
        self.assertEqual(expected, actual)

    def test_num_buses_3(self):
        """ Test num_buses with with even number 80"""
        actual = a1.num_buses(80)
        expected = 2
        self.assertEqual(expected, actual)

    def test_num_buses_3(self):
        """ Test num_buses with with odd number 81"""
        actual = a1.num_buses(81)
        expected = 3
        self.assertEqual(expected, actual)


    def test_num_buses_3(self):
        """ Test num_buses with with odd number 155"""
        actual = a1.num_buses(155)
        expected = 4
        self.assertEqual(expected, actual)


    # Add your test methods for a1.num_buses here.


if __name__ == '__main__':
    unittest.main(exit=False)