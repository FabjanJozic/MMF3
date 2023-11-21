import nul_tocke as nt
import numpy as np
import matplotlib.pyplot as plt


y1_0 = 5
A = 1
B = 3
y2_0 = 0.325
C = 2
D = 0.5

def y1(t):
    return y1_0+A*np.cos(B*t)

def y2(t):
    return y2_0+C*np.exp(D*t)

def fun(t):
    return y1(t) - y2(t)

def deriv_fun(t):
    return -A*B*np.sin(B*t)-C*D*np.exp(D*t)



y1_0 = 5.0
y2_0 = 0.325
A = 1.0
B = 3.0
C = 2.0
D = 0.5

e = 1e-6 #epsilon

print(nt.met_bisekcija(fun, 0.0, 2.8, e), nt.met_NR(fun, deriv_fun, 1.6, e),
      nt.met_sekanta(fun, 1.6, e))

x = [i for i in np.arange(0.0, 5.0, 0.01)]
y = [fun(i) for i in x]

plt.plot(x, y)
plt.grid(True)
plt.show()