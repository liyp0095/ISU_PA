#!/bin/bash

javac AsymmetricKeyProducer.java

echo "generating client's key"
java AsymmetricKeyProducer keys/client.key.pub keys/client.key

echo "generating server's key"
java AsymmetricKeyProducer keys/server.key.pub keys/server.key

rm *.class
