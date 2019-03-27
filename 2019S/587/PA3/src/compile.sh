#!/bin/bash

cd Manager

javac *java

cd ../Agent

javac *java



export JAVA_HOME=$(dirname $(dirname `which java`))

gcc -fPIC -I"$JAVA_HOME/include" -I"$JAVA_HOME/include/linux" -shared -o libCmdAgentC.so CmdAgentC.c


#rmiregistry &

#java -Djava.library.path=. Agent 20
