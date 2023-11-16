import linear_algebra_methods as li
import numpy as np


A = np.array([[2, 6, 0, 0, 0, 0, 0],
            [1, 4, 5, 0, 0, 0, 0],
            [0, 2, 6, 4, 0, 0, 0],
            [0, 0, 3, 8, 3, 0, 0],
            [0, 0, 0, 5, 6, 2, 0],
            [0, 0, 0, 0, 5, 4, 1],
            [0, 0, 0, 0, 0, 6, 2]])

B = np.array([0, 1, 2, 3, 2, 1, 0])

upp = np.array([6, 5, 4, 3, 2, 1])
mid = np.array([2, 4, 6, 8, 6, 4, 2])
low = np.array([1, 2, 3, 4, 5, 6])

X = li.Thomas(low, mid, upp, B)

for i in X:
    print(i*14)