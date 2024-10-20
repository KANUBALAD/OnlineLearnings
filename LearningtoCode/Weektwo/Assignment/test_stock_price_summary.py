import a1
import unittest


class TestStockPriceSummary(unittest.TestCase):
    """ Test class for function a1.stock_price_summary. """

    def test_stock_price_summary_empty(self):
        """ Test with empty list """
        actual = a1.stock_price_summary([])
        expected = (0, 0)
        self.assertEqual(expected, actual)
        
    def test_stock_price_summary_single_positive(self):
        """ Test with one positive item """
        actual = a1.stock_price_summary([0.001])
        expected = (0.001, 0)
        self.assertEqual(expected, actual)
        
    def test_stock_price_summary_single_negative(self):
        """ Test with one negative item """
        actual = a1.stock_price_summary([-0.001])
        expected = (0, -0.001)
        self.assertEqual(expected, actual)
        
    def test_stock_price_summary_smallest_interesting_case(self):
        """ Test with smallest interesting case """
        actual = a1.stock_price_summary([0.001, -0.001])
        expected = (0.001, -0.001)
        self.assertEqual(expected, actual)
        
    def test_stock_price_summary_many_items(self):
        """ Test with many items """
        actual = a1.stock_price_summary([0.01, 0.03, -0.02, -0.14, 0, 0, 0.10, -0.01])
        expected = (0.14, -0.17)
        self.assertEqual(expected, actual)
        
    def test_stock_price_summary_all_zeros(self):
        """ Test with all zero values """
        actual = a1.stock_price_summary([0, 0, 0, 0])
        expected = (0, 0)
        self.assertEqual(expected, actual)
        
    def test_stock_price_summary_large_numbers(self):
        """ Test with very large numbers """
        actual = a1.stock_price_summary([1e6, -1e6])
        expected = (1e6, -1e6)
        self.assertEqual(expected, actual)
        
    def test_stock_price_summary_mixed_large_small(self):
        """ Test with mixed large and small numbers """
        actual = a1.stock_price_summary([1e6, -1e6, 0.001, -0.001])
        expected = (1e6 + 0.001, -1e6 - 0.001)
        self.assertEqual(expected, actual)
        
    def test_stock_price_summary_all_positive(self):
        """ Test with all positive values """
        actual = a1.stock_price_summary([0.01, 0.02, 0.03])
        expected = (0.06, 0)
        self.assertEqual(expected, actual)
        
    def test_stock_price_summary_all_negative(self):
        """ Test with all negative values """
        actual = a1.stock_price_summary([-0.01, -0.02, -0.03])
        expected = (0, -0.06)
        

if __name__ == '__main__':
    unittest.main(exit=False)