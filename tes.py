# Define schema for the DataFrame
schema = StructType([
    StructField("sp_sub_category_id", IntegerType(), True),
    StructField("omni_subcat_id", IntegerType(), True),
    StructField("omni_subcat_name", StringType(), True),
    StructField("r2_d2_path", StringType(), True)
])

# Create DataFrame
df = spark.createDataFrame(rows, schema)
