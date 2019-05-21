# 4. Setup a Multi-Broker Cluster


## 4.1 Create config files for each new broker
```
$ cp config/server.properties config/server-1.properties
$ cp config/server.properties config/server-2.properties
```

## 4.2 Update the following properties in the new files
```
config/server-1.properties:
    broker.id=1
    listeners=PLAINTEXT://:9093
    log.dir=/tmp/kafka-logs-1

config/server-2.properties:
    broker.id=2
    listeners=PLAINTEXT://:9094
    log.dir=/tmp/kafka-logs-2
```

## 4.3 Start the two new nodes in separate termial windows
Note : You should already have Zookeeper running

```
$ bin/kafka-server-start.sh config/server-1.properties &
...
$ bin/kafka-server-start.sh config/server-2.properties &
...
```

## 4.4 Create new topic replicated to all 3 nodes
```
$ bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 3 --partitions 1 --topic my-replicated-topic
```


## 4.5 See stats about our new topic
```
$ bin/kafka-topics.sh --describe --zookeeper localhost:2181 --topic my-replicated-topic
```
```
Topic:my-replicated-topic	PartitionCount:1	ReplicationFactor:3	Configs:
	Topic: my-replicated-topic	Partition: 0	Leader: 1	Replicas: 1,2,0	Isr: 1,2,0
```
## 4.6 Compare this to our 'test' topic
```
$ bin/kafka-topics.sh --describe --zookeeper localhost:2181 --topic test
```
```
Topic:test	PartitionCount:1	ReplicationFactor:1	Configs:
	Topic: test	Partition: 0	Leader: 0	Replicas: 0	Isr: 0
```
