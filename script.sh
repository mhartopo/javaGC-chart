#!/bin/bash

echo "-Xms512m -Xmx512m"
java -Xms512m -Xmx512m -XX:+UseParallelGC -XX:+PrintGCTimeStamps -Xloggc:log1.txt GCTest 10000 10000 100 4
sleep 10
java -Xms512m -Xmx512m -XX:+UseG1GC -XX:+PrintGCTimeStamps -Xloggc:log2.txt GCTest 10000 10000 100 4
sleep 10
java -Xms512m -Xmx512m -XX:+UseConcMarkSweepGC -XX:+PrintGCTimeStamps -Xloggc:log3.txt GCTest 10000 10000 100 4
sleep 10

echo "-Xms768m -Xmx768m"
java -Xms768m -Xmx768m -XX:+UseParallelGC -XX:+PrintGCTimeStamps -Xloggc:log4.txt GCTest 10000 10000 100 4
sleep 10
java -Xms768m -Xmx768m -XX:+UseG1GC -XX:+PrintGCTimeStamps -Xloggc:log5.txt GCTest 10000 10000 100 4
sleep 10
java -Xms768m -Xmx768m -XX:+UseConcMarkSweepGC -XX:+PrintGCTimeStamps -Xloggc:log6.txt GCTest 10000 10000 100 4
sleep 10

echo "-Xms1024m -Xmx1024m"
java -Xms1024m -Xmx1024m -XX:+UseParallelGC -XX:+PrintGCTimeStamps -Xloggc:log7.txt GCTest 10000 10000 100 4
sleep 10
java -Xms1024m -Xmx1024m -XX:+UseG1GC -XX:+PrintGCTimeStamps -Xloggc:log8.txt GCTest 10000 10000 100 4
sleep 10
java -Xms1024m -Xmx1024m -XX:+UseConcMarkSweepGC -XX:+PrintGCTimeStamps -Xloggc:log9.txt GCTest 10000 10000 100 4
sleep 10