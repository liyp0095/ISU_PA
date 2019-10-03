## Platform

elementory OS + gcc

```
(base) ➜  Assignment2 git:(master) ✗ uname -a
Linux PC 4.15.0-62-generic #69-Ubuntu SMP Wed Sep 4 20:55:53 UTC 2019 x86_64 x86_64 x86_64 GNU/Linux
```
```
gcc (Ubuntu 7.4.0-1ubuntu1~18.04.1) 7.4.0
Copyright (C) 2017 Free Software Foundation, Inc.
```

## How to run

```shell
sh run.sh RPRW.c
```

## Result

```shell
(base) ➜  Assignment2 git:(master) ✗ sh run.sh RPRW.c
Process 0 (reader) arrives.
Process 0 starts reading.
Process 1 (reader) arrives.
Process 1 starts reading.
Process 0 ends reading.
Process 0 (reader) leaves.
Process 2 (writer) arrives.
Process 1 ends reading.
Process 1 (reader) leaves.
Process 2 starts writing.
Process 3 (writer) arrives.
Process 4 (reader) arrives.
Process 2 ends writing.
Process 2 (writer) leaves.
Process 4 starts reading.
Process 5 (writer) arrives.
Process 6 (writer) arrives.
Process 4 ends reading.
Process 4 (reader) leaves.
Process 3 starts writing.
Process 7 (reader) arrives.
Process 3 ends writing.
Process 3 (writer) leaves.
Process 7 starts reading.
Process 7 ends reading.
Process 7 (reader) leaves.
Process 5 starts writing.
Process 5 ends writing.
Process 5 (writer) leaves.
Process 6 starts writing.
Process 6 ends writing.
Process 6 (writer) leaves.
All Done!
```

## Question

- works well in my linux computer, but incorrect in [pyrite]( (http://web.cs.iastate.edu/~smkautz/cs227f12/labs/lab1/page15.html).
- ```sem_destory``` not works
- ```wait(NULL);``` not works
