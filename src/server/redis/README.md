# Installation Redis

## 1. Download and Install Redis

```
$ sudo apt-get install tcl
$ wget http://download.redis.io/releases/redis-5.0.5.tar.gz
$ tar xzf redis-5.0.5.tar.gz 
$ cd redis-5.0.5/
$ make
$ make test 
```

## 2. Run Redis
```
$ ./src/redis-server redis.conf

$ python redis-test/producer.py
$ python redis-test/consumer.py
```
Then video is at http://localhost:9000

## 3. Configuration of Redis 

Please refer to ***redis-voyager5.conf*** and ***redis-voyager6.conf***

