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

dx, dt = 0.2, 0.5

j = [0, 100, 200, 300, 400]
t = [dt*J for J in j]

P1 = [0.0, 20.0, 0.0, t[0], dx, dt] #pocetni uvjeti
P2 = [0.0, 20.0, 0.0, t[1], dx, dt]
P3 = [0.0, 20.0, 0.0, t[2], dx, dt]
P4 = [0.0, 20.0, 0.0, t[3], dx, dt]
P5 = [0.0, 20.0, 0.0, t[4], dx, dt]
Rub = [0.0, 0.0] #rubni uvjeti
Dif = 1e-2 #difuzijska konstanta
metoda = 'exp'

D1 = di.dif(rho, P1, Rub, Dif, metoda) #vrijednosti funkcije difuzije
D2 = di.dif(rho, P2, Rub, Dif, metoda)
D3 = di.dif(rho, P3, Rub, Dif, metoda)
D4 = di.dif(rho, P4, Rub, Dif, metoda)
D5 = di.dif(rho, P5, Rub, Dif, metoda)

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
