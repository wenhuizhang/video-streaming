# ~/.bashrc: executed by bash(1) for non-login shells.
# see /usr/share/doc/bash/examples/startup-files (in the package bash-doc)
# for examples

# Add go
export GOROOT=/usr/local/go
export GOPATH=$HOME/go
export PATH=$GOPATH/bin:$GOROOT/bin:$PATH

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



