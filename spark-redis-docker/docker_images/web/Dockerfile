FROM gettyimages/spark

RUN apt-get update && apt-get install -y software-properties-common && apt install -y make gcc libc6-dev tcl wget maven git

RUN apt-get update && apt-get install -y redis-server


ADD start.sh /usr/spark-2.3.1/start.sh
ADD women_shoes.py /usr/spark-2.3.1/women_shoes.py
ADD 7210_1.csv.gz /usr/spark-2.3.1/7210_1.csv.gz

RUN cd /usr/spark-2.3.1 && git clone https://github.com/RedisLabs/spark-redis.git && cd spark-redis && mvn clean package -DskipTests && mv /usr/spark-2.3.1/spark-redis/target/*with-dependencies.jar spark-redis-with-dependencies.jar
RUN sh /usr/spark-2.3.1/start.sh
