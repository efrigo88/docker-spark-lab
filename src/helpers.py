import os
from pyspark.sql import SparkSession
import pyspark.sql.types as T

# Define schema
schema = T.StructType(
    [
        T.StructField("id", T.IntegerType(), True),
        T.StructField("name", T.StringType(), True),
        T.StructField("age", T.IntegerType(), True),
        T.StructField("city", T.StringType(), True),
    ]
)

# Create Spark session
spark = (
    SparkSession.builder.appName("TestSpark")
    .master(os.environ["THREADS"])
    .config("spark.driver.memory", os.environ["DRIVER_MEMORY"])
    .config("spark.sql.shuffle.partitions", os.environ["SHUFFLE_PARTITIONS"])
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
    .config(
        "spark.sql.catalog.spark_catalog",
        "org.apache.spark.sql.delta.catalog.DeltaCatalog",
    )
    .config("spark.jars.packages", "io.delta:delta-spark_2.12:3.2.0")
    .getOrCreate()
)
