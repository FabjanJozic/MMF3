import nul_tocke as nt
import numpy as np
import matplotlib.pyplot as plt

def y1(t, y1_0, A, B):
    return y1_0+A*np.cos(B*t)

def y2(t, y2_0, C, D):
    return y2_0+C*np.exp(D*t)

def fun(t, y1_0, A, B, y2_0, C, D):
    return y1(t, y1_0, A, B) - y2(t, y2_0, C, D)

def deriv_fun(t, y1_0, A, B, y2_0, C, D):
    return -A*B*np.sin(B*t)-C*D*np.exp(D*t)



y1_0 = 5.0
y2_0 = 0.325
A = 1.0
B = 3.0
C = 2.0
D = 0.5

e = 1e-6 #epsilon

print(nt.met_bisekcija(fun, 1.0, 4.0, e, y1_0, A, B, y2_0, C, D), nt.met_NR(fun, deriv_fun, 1.6, e, y1_0, A, B, y2_0, C, D),
      nt.met_sekanta(fun, 1.6, e, y1_0, A, B, y2_0, C, D))

'''x = [i for i in np.arange(0.0, 5.0, 0.01)]
y = [fun(i, y1_0, A, B, y2_0, C, D) for i in x]

plt.plot(x, y)
plt.grid(True)
plt.show()'''