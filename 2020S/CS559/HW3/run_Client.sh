#!/bin/bash

javac Client.java

java Client 127.0.0.1 3000 keys/client.key keys/server.key.pub

rm *.class
