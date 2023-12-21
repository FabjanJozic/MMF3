import numpy as np 
import matplotlib.pyplot as plt 
import difuzija as di
import sys

sys.getdefaultencoding()


def rho(x):
    if x >= 2.0 and x <= 5.0:
        return 5.5
    else:
        return 0.0

j = [0, 100, 200, 300, 400]
t = [0.5*J for J in j]

P1 = [0.0, 20.0, 0.0, t[0]] #pocetni uvjeti
P2 = [0.0, 20.0, 0.0, t[1]]
P3 = [0.0, 20.0, 0.0, t[2]]
P4 = [0.0, 20.0, 0.0, t[3]]
P5 = [0.0, 20.0, 0.0, t[4]]

N = 100

D1 = di.D_exp(rho, P1, N, j[0]) #vrijednosti funkcije difuzije
D2 = di.D_exp(rho, P2, N, j[1])
D3 = di.D_exp(rho, P3, N, j[2])
D4 = di.D_exp(rho, P4, N, j[3])
D5 = di.D_exp(rho, P5, N, j[4])

X = [x/(20.0/N) for x in np.arange(0.0, 20.0 + 20.0/N, 20.0/N)]

fig = plt.figure(figsize=(9,6), dpi=120)
axes = fig.add_axes([0.15, 0.15, 0.75, 0.70])
plt.rcParams.update({'font.size': 8}) #type: ignore
axes.plot(X, D1, label='t = {}$\u0394$x'.format(j[0]), lw=0.8, color='lightblue')
#axes.plot(X, D2, label='t = {}$\u0394$x'.format(j[1]), lw=0.8, color='blue')
#axes.plot(X, D3, label='t = {}$\u0394$x'.format(j[2]), lw=0.8, color='cyan')
#axes.plot(X, D4, label='t = {}$\u0394$x'.format(j[3]), lw=0.8, color='green')
#axes.plot(X, D5, label='t = {}$\u0394$x'.format(j[4]), lw=0.8, color='orange')
axes.grid(lw=0.5)
axes.set_xlabel('x / $\u0394$x')
axes.set_ylabel('$\u03C1(x,t)$ / kgm$^{-1}$')
axes.legend(loc='best')
axes.set_title('Fazni dijagram matematičkog njihala')
plt.show()

