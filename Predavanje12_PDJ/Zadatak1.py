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

dx, dt = 0.2, 0.5

P1 = [0.0, 20.0, 0.0, t[0], dx, dt] #pocetni uvjeti
P2 = [0.0, 20.0, 0.0, t[1], dx, dt]
P3 = [0.0, 20.0, 0.0, t[2], dx, dt]
P4 = [0.0, 20.0, 0.0, t[3], dx, dt]
P5 = [0.0, 20.0, 0.0, t[4], dx, dt]

Dif = 1e-2 #difuzijska konstanta

D1 = di.D_exp(rho, P1, Dif) #vrijednosti funkcije difuzije
D2 = di.D_exp(rho, P2, Dif)
D3 = di.D_exp(rho, P3, Dif)
D4 = di.D_exp(rho, P4, Dif)
D5 = di.D_exp(rho, P5, Dif)

X = [x/dx for x in np.arange(0.0, 20.0+dx, dx)]

fig = plt.figure(figsize=(7,5), dpi=120)
axes = fig.add_axes([0.10, 0.10, 0.85, 0.85])
plt.rcParams.update({'font.size': 8}) #type:ignore
axes.plot(X, D1, label='t = {}$\u0394$t'.format(j[0]), lw=1.4, color='purple')
axes.plot(X, D2, label='t = {}$\u0394$t'.format(j[1]), lw=1.4, color='blue')
axes.plot(X, D3, label='t = {}$\u0394$t'.format(j[2]), lw=1.4, color='cyan')
axes.plot(X, D4, label='t = {}$\u0394$t'.format(j[3]), lw=1.4, color='green')
axes.plot(X, D5, label='t = {}$\u0394$t'.format(j[4]), lw=1.4, color='orange')
axes.grid(lw=0.5)
axes.set_xlabel('x / $\u0394$x')
axes.set_ylabel('$\u03C1(x,t)$ / kgm$^{-1}$')
axes.legend(loc='best')
axes.set_title('Difuzija')
plt.show()
