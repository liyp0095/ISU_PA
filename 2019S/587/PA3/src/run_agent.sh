#!/bin/bash

cd Agent
java -Djava.library.path=. Agent $1
