#!/bin/bash

set -x
set -m 

rm redis.txt
rm uncorrected_redis.txt

#for j in {7843200,8843200,9843200,11500000,12500000,13500000,14500000,15500000,16500000,17500000,18500000}
#for j in {117000,1843200,2843200,3843200,4147200,4843200,5843200,6843200,7843200,8843200,9843200,11500000}
for j in {117000..117000..1}
do
	for i in {1..512..1}
	do
		/usr/local/go/bin/go run main.go $i $j
		mv redis.txt redis_size_$i.txt
		rm uncorrected_redis.txt
	done
done		 
