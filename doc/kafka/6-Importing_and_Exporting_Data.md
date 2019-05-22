# 6. Importing and Exporting Data 

## 6.1 Create a simple text file to work with that has 2 lines
```
$ echo -e "foo\nbar" > test.txt
```

## 6.2 Setup connector in standalone mode
 - pass in connection properties config
 - then file connection config
 - then file sync config (serialization)
 - all configs here ship w/ Kafka and act as templates

```
$ bin/connect-standalone.sh config/connect-standalone.properties config/connect-file-source.properties config/connect-file-sink.properties
```
Once the above connector starts running, it will read test.txt
and write to test.sink.txt

## 6.3 Check result by reading the contents of the file
```
$ cat test.sink.txt
foo
bar
```

## 6.4 To see the data in the consumer run the following
```
$ bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic connect-test --from-beginning
```
In a separate terminal window, add some lines to the file
```
$ echo "Another line" >> test.txt
```
