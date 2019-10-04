#!/bin/sh

javac WebSearch.java

echo "============== Task 1 ================"
echo "intranet 1 :"
java WebSearch intranet1 breadth
java WebSearch intranet1 depth
echo "intranet 5 :"
java WebSearch intranet5 breadth
java WebSearch intranet5 depth
echo "intranet 7 :"
java WebSearch intranet7 breadth
java WebSearch intranet7 depth

echo "============== Task 2a ==============="
echo "intranet 1 :"
java WebSearch intranet1 best
echo "intranet 5 :"
java WebSearch intranet5 best
echo "intranet 7 :"
java WebSearch intranet7 best

echo "============== Task 2b ==============="
echo "intranet 1 :"
java WebSearch intranet1 beam
echo "intranet 5 :"
java WebSearch intranet5 beam
echo "intranet 7 :"
java WebSearch intranet7 beam

rm *.class
