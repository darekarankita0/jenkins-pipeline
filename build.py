# build.py

from pyspark.sql import SparkSession

def calculate_sum(spark, numbers):
    df = spark.createDataFrame(numbers, ["number"])
    return df.groupBy().sum().collect()[0][0]

if __name__ == "__main__":
    spark = SparkSession.builder \
        .appName("SumCalculator") \
        .getOrCreate()

    numbers = [(1,), (2,), (3,), (4,), (5,)]
    total_sum = calculate_sum(spark, numbers)
    print("Total sum:", total_sum)

    spark.stop()
