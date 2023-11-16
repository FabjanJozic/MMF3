import linear_algebra_methods as li
import numpy as np

upp = np.array([-2, -2, -2])
mid = np.array([4, 6, 6, 8])
low = np.array([-2, -2, -2])

sol = np.array([5, 0, 0, 0])

X = li.Thomas(low, mid, upp, sol)
for i in X:
    print(i*94)