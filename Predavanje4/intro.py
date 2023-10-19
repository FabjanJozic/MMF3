import numpy as np

A = np.array([[4, -2, 1],
             [3, 6, -4],
             [2, 1, 8]])

B1 = np.array([12, -25, 32])
B2 = np.array([4, -10, 22])
B3 = np.array([20, -30, 40])

X1 = np.linalg.solve(A, B1)
X2 = np.linalg.solve(A, B2)
X3 = np.linalg.solve(A, B3)

print(X1, X2, X3)