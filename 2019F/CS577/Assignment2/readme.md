## Programming Problem

**5.(24 pts)**  Implement the three-dimensional projection procedure with the viewpoint and viewplane as input, and the computed projection matrix as output. In addition, output the projected images of a number of input data points. All the inputs and outputs should be in homogeneous coordinates.

Your code and run time results should be zipped in a file named Firstname_Lastname_HW1_Prob5.zip.

Determine the projection matrix for each of the following transformation, and apply the matrix to the tetrahedron with vertices (0, 0, 0), (1, 0, 0), (0, 1, 0), and (1, 1, 1).

1. (4 pts)Perspective projection onto the viewplane −x + 3y + 2z − 4 = 0 from the viewpoint (2, −1, 1).
2. (4 pts) Perspective projection onto the viewplane 5x−3z+2 = 0 from the viewpoint (1,4,−1).
3. (4 pts) Parallel projection onto the viewplane 2y + 3z + 4 = 0 in the direction of the vector (1, −2, 3).
4. (4 pts) Parallel projection onto the viewplane 7x − 8y + 5 = 0 in the direction of the vector (0, 4, 9).


## How to run?

### Platform

python3.7 and packages ( argparse, numpy)

### Results

```sh
(python37) ➜ Assignment2 git:(master) ✗ python ProjectionProblem.py --assignment

```

```sh
1. (4 pts)Perspective projection onto the viewplane −x + 3y + 2z − 4 = 0 from the viewpoint (2, −1, 1).
Matrix =
[[ 5.  6.  4. -8.]
 [ 1.  4. -2.  4.]
 [-1.  3.  9. -4.]
 [-1.  3.  2.  3.]]
2. (4 pts) Perspective projection onto the viewplane 5x−3z+2 = 0 from the viewpoint (1,4,−1).
Matrix =
[[ -5.   0.  -3.   2.]
 [ 20. -10. -12.   8.]
 [ -5.   0.  -7.  -2.]
 [  5.   0.  -3.  -8.]]
3. (4 pts) Parallel projection onto the viewplane 2y + 3z + 4 = 0 in the direction of the vector (1, −2, 3).
Matrix =
[[-5.  2.  3.  4.]
 [ 0. -9. -6. -8.]
 [ 0.  6.  4. 12.]
 [ 0.  0.  0. -5.]]
4. (4 pts) Parallel projection onto the viewplane 7x − 8y + 5 = 0 in the direction of the vector (0, 4, 9).
Matrix =
[[ 32.   0.   0.   0.]
 [ 28.   0.   0.  20.]
 [ 63. -72.  32.  45.]
 [  0.   0.   0.  32.]]
 ```

 ```sh
 python ProjectionProblem.py --console
 ```

 ```sh
 View plane (4 numbers split by spaces): 0 2 3 4
View point (4 numbers split by spaces): 1 -2 3 0
Matrix =
[[-5.  2.  3.  4.]
 [-0. -9. -6. -8.]
 [ 0.  6.  4. 12.]
 [ 0.  0.  0. -5.]]
Continue ... (yes/[no]):
```
