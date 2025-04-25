from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("TestSpark").getOrCreate()

df = spark.createDataFrame([(1, "one"), (2, "two")], ["number", "word"])
df.show()

spark.stop()
