# Installation and Configuration for Kafka

In this folder, installation and configuration files for Kafka are attached. 

***Kafka 2.0.0 version works with java openjdk 8, unit tests might fail with other versions.***

##  1. Kafka Installation 

This code is made for Unix-based systems such as Linux and Mac OSX.

###  1.1 Install the Java Development Kit (JDK)
Install version 8 of OpenJDK
``` 
$ java -version 
$ sudo apt install default-jre
$ sudo apt install openjdk-8-jre-headless
$ java -version

$ javac -version
$ sudo apt install openjdk-8-jre-headless
$ sudo apt install default-jdk 
$ javac -version 
```

#### In Case Have Other Java Versions

Install the OpenJDK 8 from a PPA repository:
```
$ sudo add-apt-repository ppa:openjdk-r/ppa
```
Update the system package cache and install:
```
$ sudo apt-get update
$ sudo apt-get install openjdk-8-jdk
```
If you have more than one Java version installed on your system use the following command to switch versions:
```
    sudo update-alternatives --config java

    java -version

    openjdk version "1.8.0_72-internal"
    OpenJDK Runtime Environment (build 1.8.0_72-internal-b05)
    OpenJDK 64-Bit Server VM (build 25.72-b05, mixed mode)
```


### 1.2 Download latest version from `https://kafka.apache.org/downloads`
Download the binary pack:
```
$ wget http://mirror.olnevhost.net/pub/apache/kafka/2.2.0/kafka_2.12-2.2.0.tgz
```
Then Unpack latest version
```
tar -xzf kafka_2.12-2.2.0.tgz
cd kafka_2.12-2.2.0
```

### 1.3 Start Zookeeper
```
$ bin/zookeeper-server-start.sh config/zookeeper.properties
```

### 1.4 Start Kafka Server
```
$ bin/kafka-server-start.sh config/server.properties
```

## 2. Video Streaming 

Kafka clients up and running:
 - We use OpenCV for video rendering 
 - Flask for our “distributed” Consumer
 
 ### 2.1 Installation of Python, python-pip and OpenCV and Flask
 ```
 $ pip install kafka-python opencv-contrib-python Flask
 ```
 
 ### 2.2 Start Consumer and Start Producer
 ```
 $ python consumer/consumer.py
 
 $ python producer/producer.py 
 
OR 

 $ python ./producer/producer.py ./videos/Countdown1.mp4
 ```
 
 ### 2.3 Test
 Check video streaming at `http://0.0.0.0:5000/`
 
 
