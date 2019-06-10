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

## 4. Redis Cluster Version

```
// On Voyager 4 
$ ./src/redis-server ../redis-cluster-master.conf

// On Voyager 5 
$ ./src/redis-server ../redis-cluster-slave.conf

// One Voyager 6
$ $ ./src/redis-server ../redis-cluster-slave.conf

// Then on any node start cluster version
./redis-cli --cluster create 10.10.0.14:6379 10.10.0.15:6381 10.10.0.16:6381

// Then test 
$ ./src/redis-benchmark -t set,get -h 10.10.0.14 -p 6379 -c 1020 -n 100000 -d 117000 
```
