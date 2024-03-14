# test.py

import unittest
from build import calculate_sum

class TestSumCalculator(unittest.TestCase):
    def test_calculate_sum(self):
        numbers = [1, 2, 3, 4, 5]
        expected_sum = sum(numbers)
        result_sum = calculate_sum(numbers)
        self.assertEqual(result_sum, expected_sum)

if __name__ == '__main__':
    unittest.main()
