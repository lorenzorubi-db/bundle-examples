from pyspark.sql import functions as F

df = spark.read.format("cloudFiles") \
    .option("cloudFiles.format", "csv") \
    .load("/Volumes/main/raw/incoming")