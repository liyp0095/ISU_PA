#/bin/python
#-*- coding:utf8 -*-

'''
* Three dimensional transformation matrix M = vn(T) - (n*v)I_4
* where, v is view point, n(T) is transform of n, n is viewplan vector, I_4 is identity matrix.
* Yuepei Li
* 2019-09-11 14:51:18
'''

import numpy as np
import argparse
import time

def ParserAdd(parser):
    parser.add_argument("--assignment", help="give the answers of assignment",
                    action="store_true")
    parser.add_argument("--console", help="give the answers of assignment",
                    action="store_true")


def projectionMatrix(n, v):
    return np.dot(v, n.T) - np.dot(v.T, n)*np.identity(4)


def answerAssignment():
    vertices = np.array([[0, 0, 0, 1], [1, 0, 0, 1], [0, 1, 0, 1], [1, 1, 1, 1]]).T
    print("1. (4 pts)Perspective projection onto the viewplane −x + 3y + 2z − 4 = 0 from the viewpoint (2, −1, 1).")
    n = np.array([[-1, 3, 2, -4]]).T
    v = np.array([[2, -1, 1, 1]]).T
    print("Matrix = ")
    start_time = time.time()
    m = projectionMatrix(n, v)
    print(m)
    print("Apply to vertices: ")
    print(np.dot(m, vertices))
    print("--- %s seconds ---" % (time.time() - start_time))

    print("2. (4 pts) Perspective projection onto the viewplane 5x−3z+2 = 0 from the viewpoint (1,4,−1).")
    n = np.array([[5, 0, -3, 2]])
    n = n.T
    v = np.array([[1, 4, -1, 1]])
    v = v.T
    print("Matrix = ")
    start_time = time.time()
    m = projectionMatrix(n, v)
    print(m)
    print("Apply to vertices: ")
    print(np.dot(m, vertices))
    print("--- %s seconds ---" % (time.time() - start_time))

    print("3. (4 pts) Parallel projection onto the viewplane 2y + 3z + 4 = 0 in the direction of the vector (1, −2, 3).")
    n = np.array([[0, 2, 3, 4]])
    n = n.T
    v = np.array([[1, -2, 3, 0]])
    v = v.T
    print("Matrix = ")
    start_time = time.time()
    m = projectionMatrix(n, v)
    print(m)
    print("Apply to vertices: ")
    print(np.dot(m, vertices))
    print("--- %s seconds ---" % (time.time() - start_time))

    print("4. (4 pts) Parallel projection onto the viewplane 7x − 8y + 5 = 0 in the direction of the vector (0, 4, 9).")
    n = np.array([[7, -8, 0, 5]])
    n = n.T
    v = np.array([[0, 4, 9, 0]])
    v = v.T
    print("Matrix = ")
    start_time = time.time()
    m = projectionMatrix(n, v)
    print(m)
    print("Apply to vertices: ")
    print(np.dot(m, vertices))
    print("--- %s seconds ---" % (time.time() - start_time))


def goConsole():
    vertices = np.array([[0, 0, 0, 1], [1, 0, 0, 1], [0, 1, 0, 1], [1, 1, 1, 1]]).T
    reply = "yes"
    while reply == "yes":
        viewplan = input("View plane (4 numbers split by spaces): ")
        n = np.array([[float(vp) for vp in viewplan.strip().split(" ")]]).T
        viewpoint = input("View point (4 numbers split by spaces): ")
        v = np.array([[float(vp) for vp in viewpoint.strip().split(" ")]]).T
        print("Matrix = ")
        start_time = time.time()
        m = projectionMatrix(n, v)
        print(m)
        print("Apply to vertices: ")
        print(np.dot(m, vertices))
        print("--- %s seconds ---" % (time.time() - start_time))
        reply = "no"
        reply = input("Continue ... (yes/[no]): ")


def main():
    parser = argparse.ArgumentParser()
    ParserAdd(parser)
    args = parser.parse_args()

    if args.assignment:
        answerAssignment()

    if args.console:
        goConsole()


if __name__ == "__main__":
    main()
