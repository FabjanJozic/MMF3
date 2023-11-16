import numpy as np
import matplotlib.pyplot as plt


def L_i(X, Y, x, m):
    '''Langrangeova interpolacija polinoma.'''
    rez = 0.0
    for i in range(0, m + 1):
        L = 1.0
        for j in range(0, m + 1):
            if j != i:
                L *= (x - X[j])/(X[i] - X[j])
        rez += Y[i]*L
    return rez



T = [1, 2, 3, 4, 5]
X = [-2*t - 4*t**2 + t**3 for t in T]

m_1 = 2
m_2 = 3

t = []
x_1 = []
x_2 = []

for o in np.arange(1.0, 5.001, 0.001):
    t.append(o)
    x_1.append(L_i(T, X, o, m_1))
    x_2.append(L_i(T, X, o, m_2))


fig = plt.figure(figsize=(13,6), dpi=90)
axes = fig.add_axes([0.15, 0.15, 0.75, 0.70])
plt.rcParams.update({'font.size': 10})           #type: ignore
axes.scatter(T, X, c='orange', edgecolor='red')
axes.plot(t, x_1, color='green', lw=0.9)
axes.plot(t, x_2, color='blue', lw=0.9)
axes.set_xlabel('$t$  [s]')
axes.set_ylabel('$x$  [cm]')
axes.grid(lw=0.5)
axes.legend(['točke', 'fit  $P_{2}$(t)', 'fit  $P_{3}$(t)'], loc='best')
plt.show()
