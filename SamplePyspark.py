from pyspark.sql import SparkSession

# Create a SparkSession
spark = SparkSession.builder \
    .appName("PySpark Example") \
    .getOrCreate()

# Define data as a list of tuples
data = [("Alice", 34), ("Bob", 45), ("Charlie", 37)]

# Create a DataFrame from the list of tuples
df = spark.createDataFrame(data, ["Name", "Age"])

# Show the DataFrame
df.show()

# Stop the SparkSession
spark.stop()
