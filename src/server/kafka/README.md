# Installation and Configuration for Kafka (Binary Version)

In this folder, installation and configuration files for Kafka are attached. 

***Kafka 2.0.0 version works with java openjdk 8, unit tests might fail with other versions.***

To compile Kafka 2.0.0, you need:
- Scala version 2.12.8.
- Java Openjdk 8
- Gradle 5.0 

Where our ***~/.bashrc *** as follows:
```
# original PATH
export PATH=/home/wenhui/bin:/home/wenhui/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/sbin:/snap/bin

# add gradle 
export GRADLE_HOME=/opt/gradle/gradle-5.0
export PATH=${GRADLE_HOME}/bin:${PATH}


# Adding for Zookeeper and Kafka 
# export PATH=$PATH:/opt/gradle/gradle-5.0/bin
# export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
export PATH=$JAVA_HOME/bin:$PATH

# set JAVA_TOOL_OPTIONS to resolve error of IBM SDK
# for zookeeper
export JAVA_TOOL_OPTIONS="-Dcom.ibm.jsse2.overrideDefaultTLS=true"

```

```
gradle --version 
Picked up JAVA_TOOL_OPTIONS: -Dcom.ibm.jsse2.overrideDefaultTLS=true

------------------------------------------------------------
Gradle 5.0
------------------------------------------------------------

Build time:   2018-11-26 11:48:43 UTC
Revision:     7fc6e5abf2fc5fe0824aec8a0f5462664dbcd987

Kotlin DSL:   1.0.4
Kotlin:       1.3.10
Groovy:       2.5.4
Ant:          Apache Ant(TM) version 1.9.13 compiled on July 10 2018
JVM:          1.8.0_212 (Oracle Corporation 25.212-b03)
OS:           Linux 4.8.0-58-lowlatency amd64

```

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
// kafka 2.0.0 works with openjdk8, scala 12
$ wget https://archive.apache.org/dist/kafka/2.0.0/kafka_2.11-2.0.0.tgz
```
Then Unpack latest version
```
tar -xzf kafka_2.12-2.0.0.tgz
cd kafka_2.12-2.0.0
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
 
 
