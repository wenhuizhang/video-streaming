#!/bin/bash

set -x
set -m 

rm redis.txt
rm uncorrected_redis.txt


for i in {1..522..1}
do
	go run main.go $i
	mv redis.txt redis_$i.txt
	rm uncorrected_redis.txt
done

		 
