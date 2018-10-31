# !/bin/bash 
/etc/init.d/redis-server restart
gzip -d /usr/spark-2.3.1/7210_1.csv.gz
spark-submit --jars /usr/spark-2.3.1/spark-redis/spark-redis-with-dependencies.jar /usr/spark-2.3.1/women_shoes.py
