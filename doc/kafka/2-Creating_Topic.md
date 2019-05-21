# 2. Create a Topic

## 2.1 Run built-in script to create new topic named "test" with 1 partition on 1 node
```
$ bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic test
```

## 2.2 See the topic
```
$ bin/kafka-topics.sh --list --zookeeper localhost:2181
```
