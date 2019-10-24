# CS577 Assignment 6, Yuepei Li

## Platform

```
python 3.7 + ubuntu
```

## How to run

```shell
python main.py

# show some test case
python Derivative.py
```

## Result

```shell
➜  Assignment6 git:(master) ✗ python main.py      
================= Bisection ==================
  phi     x       y
1.5467  0.029   1.2029
1.9457  -0.3612 0.9179
4.3375  -0.3612 -0.9179
4.7365  0.029   -1.2029

================== Vertices ==================
  phi     x       y
0       3.0     0.0
1.0119  1.0756  1.7199
1.7321  -0.1697 1.043
3.1416  -1.0    0.0
4.5511  -0.1697 -1.043
5.2713  1.0756  -1.7199
6.2832  3.0     -0.0
```

```sh
➜  Assignment6 git:(master) ✗ python Derivative.py
======== angTest =========
ang =  0.5

p =  2.7386856000373703
p' =  -1.0142887562826677
p'' =  -1.7808813497621379
p'' =  1.4872986156163983

k =  0.5795126751821017
k' =  0.02901362264037771
```

## Problem

- [ ] No verify if k' k'' equals zero
- [ ] Could add graphics.
- [ ] Not general solution for the question.
