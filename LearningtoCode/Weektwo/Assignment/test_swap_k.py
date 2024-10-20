import unittest
from a1 import swap_k

class TestSwapK(unittest.TestCase):
    """ Test class for function swap_k. """

    def test_swap_k_empty(self):
        """ Test with an empty list """
        nums = []
        swap_k(nums, 0)
        self.assertEqual(nums, [])

    def test_swap_k_zero(self):
        """ Test with k = 0 """
        nums = [1, 2, 3, 4]
        swap_k(nums, 0)
        self.assertEqual(nums, [1, 2, 3, 4])

    def test_swap_k_small_list(self):
        """ Test with a small list """
        nums = [1, 2, 3, 4]
        swap_k(nums, 2)
        self.assertEqual(nums, [3, 4, 1, 2])

    def test_swap_k_large_list(self):
        """ Test with a larger list """
        nums = [1, 2, 3, 4, 5, 6, 7, 8]
        swap_k(nums, 3)
        self.assertEqual(nums, [6, 7, 8, 4, 5, 1, 2, 3])

    def test_swap_k_half_list(self):
        """ Test with k equal to half the list length """
        nums = [1, 2, 3, 4, 5, 6]
        swap_k(nums, 3)
        self.assertEqual(nums, [4, 5, 6, 1, 2, 3])

    def test_swap_k_one(self):
        """ Test with k = 1 """
        nums = [1, 2, 3, 4, 5, 6]
        swap_k(nums, 1)
        self.assertEqual(nums, [6, 2, 3, 4, 5, 1])

if __name__ == '__main__':
    unittest.main(exit=False)