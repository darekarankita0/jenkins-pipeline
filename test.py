# test.py

import unittest
from pyspark.sql import SparkSession
from build import calculate_sum

class TestSumCalculator(unittest.TestCase):
    def setUp(self):
        self.spark = SparkSession.builder \
            .appName("TestSumCalculator") \
            .master("local[*]") \
            .getOrCreate()

    def tearDown(self):
        self.spark.stop()

    def test_calculate_sum(self):
        numbers = [(1,), (2,), (3,), (4,), (5,)]
        expected_sum = sum(num[0] for num in numbers)
        result_sum = calculate_sum(self.spark, numbers)
        self.assertEqual(result_sum, expected_sum)

if __name__ == '__main__':
    unittest.main()
