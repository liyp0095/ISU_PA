#!/bin/sh

C_FILE=$1
C_PARA="rrwwrwwr"
C_FILE_NAME=${C_FILE%.*}

OUT_FILE=$C_FILE_NAME.out
gcc $C_FILE -o $OUT_FILE
#rm ${C_FILE_NAME}_output.txt
./$OUT_FILE $C_PARA # > output_${C_FILE_NAME}.txt
rm $OUT_FILE
