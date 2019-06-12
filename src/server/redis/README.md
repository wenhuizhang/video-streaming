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

### 4.1 Test

```
// On Voyager 4 
$ ./src/redis-server ../redis-cluster-master.conf

// On Voyager 5 
$ ./src/redis-server ../redis-cluster-slave.conf

// One Voyager 6
$ $ ./src/redis-server ../redis-cluster-slave.conf

// Then on any node start cluster version
./redis-cli --cluster create 10.10.0.14:6379 10.10.0.15:6379 10.10.0.16:6379

// Then test 
$ ./src/redis-benchmark -t set,get -h 10.10.0.14 -p 6379 -c 1020 -n 100000 -d 117000 
```

### 4.2 Clean Slate

For each node:
```
wenhui@voyager6:~/video-streaming/src/server/redis/redis-5.0.5/src$ ./redis-cli -h 10.10.0.15
10.10.0.15:6379> CLUSTER NODES
ded225b0b464100816582d85175c274055932201 10.10.0.16:6379@16379 master - 0 1560290490597 3 connected 10923-16383
8eb0814f4c60ff8dadde009002cf21b525a01485 10.10.0.15:6379@16379 myself,master - 0 1560290288000 2 connected 5461-10922
8ace6924bde0a96e5e044a210d437cdac1b1c519 10.10.0.14:6379@16379 master - 0 1560290489595 1 connected 0-5460
10.10.0.15:6379> FLUSHALL
OK
10.10.0.15:6379> CLUSTER RESET
OK


wenhui@voyager6:~/video-streaming/src/server/redis/redis-5.0.5/src$ ./redis-cli -h 10.10.0.14


wenhui@voyager6:~/video-streaming/src/server/redis/redis-5.0.5/src$ ./redis-cli -h 10.10.0.16
```

### 4.3 Start Node

```
wenhui@voyager6:~/video-streaming/src/server/redis/redis-5.0.5/src$ ./redis-cli --cluster create 10.10.0.14:6379 10.10.0.15:6379 10.10.0.16:6379
>>> Performing hash slots allocation on 3 nodes...
Master[0] -> Slots 0 - 5460
Master[1] -> Slots 5461 - 10922
Master[2] -> Slots 10923 - 16383
M: 8ace6924bde0a96e5e044a210d437cdac1b1c519 10.10.0.14:6379
   slots:[0-5460] (5461 slots) master
M: 8eb0814f4c60ff8dadde009002cf21b525a01485 10.10.0.15:6379
   slots:[5461-10922] (5462 slots) master
M: ded225b0b464100816582d85175c274055932201 10.10.0.16:6379
   slots:[10923-16383] (5461 slots) master
Can I set the above configuration? (type 'yes' to accept): yes
>>> Nodes configuration updated
>>> Assign a different config epoch to each node
>>> Sending CLUSTER MEET messages to join the cluster
Waiting for the cluster to join
..
>>> Performing Cluster Check (using node 10.10.0.14:6379)
M: 8ace6924bde0a96e5e044a210d437cdac1b1c519 10.10.0.14:6379
   slots:[0-5460] (5461 slots) master
M: 8eb0814f4c60ff8dadde009002cf21b525a01485 10.10.0.15:6379
   slots:[5461-10922] (5462 slots) master
M: ded225b0b464100816582d85175c274055932201 10.10.0.16:6379
   slots:[10923-16383] (5461 slots) master
[OK] All nodes agree about slots configuration.
>>> Check for open slots...
>>> Check slots coverage...
[OK] All 16384 slots covered.

```
