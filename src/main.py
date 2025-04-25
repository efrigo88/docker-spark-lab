from .helpers import spark, schema

# Read JSON file
df = (
    spark.read.option("multiLine", "true")
    .schema(schema)
    .json("./data/input/sample_data.json")
)

# Save as Delta table
DELTA_PATH = "./data/output/delta_table"
df.write.format("delta").mode("overwrite").save(DELTA_PATH)

# Read back from Delta and show
delta_df = spark.read.format("delta").load(DELTA_PATH)
print("Data from Delta table:")
delta_df.show()

spark.stop()
