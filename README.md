# spark-redis

This Project contains Dockerfile that creates a docker container with Apache Spark and Redis server in it. This will execute a spark-submit with the Spark-Redis Dependency solving jar file, which is compiled using Maven. This Spark sumit job will load the CSV file and filters the needed columns into the Redis Server Datastore.

### Spark Redis Connection:

Connection between spark and Redis server through Pyspark is achieved like below code,

```
conf = SparkConf().setAppName("redis-df").setMaster("local[*]").set("spark.redis.host", "localhost").set("spark.redis.port", "6379")
```

Here we will specify the Spark job app name, redis host ip and port to establish connection.

We reformat the CSV file formate into Json format by setting delimiter, set header used in the csv file to be true and read the CSV file like below sippet

```
sqlContext.read.format("com.databricks.spark.csv").option("header", "true").option("mode", "DROPMALFORMED").option("inferSchema", "true").option("delimiter", ",").load("file:///usr/spark-2.3.1/7210_1.csv"
```

We can filter the needed columns for our operations like the snippet given below, where we filter out only id, brand, color and dataAdded from the CSV file.

```
df.select('id','brand','colors','dateAdded')
```

Then we push this data into Redis server using the below snippet by mentioning the table name under which the data needs to be mapped

```
df_filter.write.format("org.apache.spark.sql.redis").option("table", "women_shoesss").option("key.column", "id").save()
```


### Querying inside Redis Server

Once we push the data, we can log into redis server using the cli,
```
redis-cli
```

Then we can use the below command to list out all the data stored under the key column, 'id'
```
keys "women_shoess:*"
```
which outputs like,
```
127.0.0.1:6379> keys "women_shoess:*"
  1) "women_shoess:AVpfnXovLJeJML43Ag1J"
  2) "women_shoess:AVpfey1xLJeJML4399Ad"
  3) "women_shoess:AVpe68MAilAPnD_xQ6P3"
  4) "women_shoess:AVpe8K4ZLJeJML43yySO"
  5) "women_shoess:AVpgL6xyilAPnD_xou1V"
  6) "women_shoess:AVpgj1abilAPnD_xuJSy"
  7) "women_shoess:AVpe_6lhLJeJML430H_G"
  8) "women_shoess:AVpflFRpilAPnD_xeXa2"
  9) "women_shoess:AVpfmdXZ1cnluZ0-nxgT"
 10) "women_shoess:AVpe5xbWilAPnD_xQeml"
 ```
 
 We can get information specific to a particular id by specifying the id like below snippet,
 ```
 127.0.0.1:6379> hgetall "women_shoess:AVpg-PWgilAPnD_xznmH"
 ```
 which outputs like the product information like,
 ```
 127.0.0.1:6379> hgetall "women_shoess:AVpg-PWgilAPnD_xznmH"
1) "id"
2) "AVpg-PWgilAPnD_xznmH"
3) "dateAdded"
4) "2016-03-29 21:51:09.0"
5) "brand"
6) "Gucci"
 ```
 Another example
 ```
 127.0.0.1:6379> hgetall "women_shoesss:AVpe-0U9ilAPnD_xSTyK"
1) "id"
2) "AVpe-0U9ilAPnD_xSTyK"
3) "brand"
4) "Pikolinos"
5) "dateAdded"
6) "2016-02-26 19:06:57.0"
7) "colors"
8) "Black"
```
### Docker Compose

We can launch the container using the docker compose like,
```
docker-compose up -d
```
and shut down the contaier using
```
docker-compose down
```

