#!/bin/bash

javac Server.java

java Server 3000 keys/server.key keys/client.key.pub data/text.txt

rm *.class
