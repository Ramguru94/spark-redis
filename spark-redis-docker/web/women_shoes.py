import sys
from pyspark import SparkContext, SparkConf
from pyspark.sql import SQLContext

if __name__ == "__main__":

  conf = SparkConf().setAppName("redis-df").setMaster("local[*]").set("spark.redis.host", "localhost").set("spark.redis.port", "6379")
  sc = SparkContext(conf=conf)
  sqlContext = SQLContext(sc)
  df = sqlContext.read.format("com.databricks.spark.csv").option("header", "true").option("mode", "DROPMALFORMED").option("inferSchema", "true").option("delimiter", ",").load("file:///usr/spark-2.3.1/7210_1.csv")
  df_filter = df.select('id','brand','colors','dateAdded')
  df_filter.write.format("org.apache.spark.sql.redis").option("table", "women_shoesss").option("key.column", "id").save()
