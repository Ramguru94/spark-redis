FROM ubuntu:xenial

RUN apt-get update && curl http://mirrors.fibergrid.in/apache/spark/spark-2.3.2/spark-2.3.2-bin-hadoop2.7.tgz | tar -xz -C /usr/local/ && cd /usr/local && ln -s spark-2.3.2-bin-hadoop2.7 spark
RUN apt-get update && sudo apt-get install -y openjdk-8-jdk


