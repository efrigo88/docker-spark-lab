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

spark = (
    SparkSession.builder.appName("TestSpark")
    .master("local[4]")
    .config("spark.driver.memory", "8g")
    .config("spark.sql.shuffle.partitions", "4")
    .getOrCreate()
)

# Read JSON file with schema and multiLine option
df = (
    spark.read.option("multiLine", "true")
    .schema(schema)
    .json("sample_data.json")
)

# Show the data
print("Sample Data:")
df.show()

spark.stop()
