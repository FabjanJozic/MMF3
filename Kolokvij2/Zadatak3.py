import numpy as np
import matplotlib.pyplot as plt
import skripta as s 

D = 1.0
x0, xN, t0 = 0.0, 1.0, 0.0
rub = [0.0, 0.0]
dx, dt = 0.1, 0.005
tN = [0.0, dt*6, dt*8]

def rho(x):
    if x <= 1/5:
        return -x
    elif x > 1/5 and x <= 8/10:
        return x-2/5
    else:
        return 1-x

P0 = [x0, xN, t0, tN[0], dx, dt] 
P6 = [x0, xN, t0, tN[1], dx, dt]
P8 = [x0, xN, t0, tN[2], dx, dt]

P0e = [x0, xN, t0, tN[0], dx, dt*10] 
P6e = [x0, xN, t0, tN[1], dx, dt*10]
P8e = [x0, xN, t0, tN[2], dx, dt*10]

X = [x for x in np.arange(x0, xN+dx, dx)]

D0 = s.dif(rho, P0, rub, D, 'imp')
D6 = s.dif(rho, P6, rub, D, 'imp')
D8 = s.dif(rho, P8, rub, D, 'imp')

D0e = s.dif(rho, P0e, rub, D, 'exp')
D6e = s.dif(rho, P6e, rub, D, 'exp')
D8e = s.dif(rho, P8e, rub, D, 'exp')

fig = plt.figure(figsize=(7,5), dpi=120)
axes = fig.add_axes([0.10, 0.10, 0.85, 0.85])
plt.rcParams.update({'font.size': 8}) #type:ignore
axes.plot(X, D0, label='implicitna, t = {}$\u0394$t'.format(0), lw=1.4, color='purple')
axes.plot(X, D6, label='implicitna, t = {}$\u0394$t'.format(6), lw=1.4, color='blue')
axes.plot(X, D8, label='implicitna, t = {}$\u0394$t'.format(8), lw=1.4, color='cyan')
axes.plot(X, D0e, label='eksplicitna, t = {}$\u0394$t'.format(0), lw=1.4, color='purple', linestyle='--')
axes.plot(X, D6e, label='eksplicitna, t = {}$\u0394$t'.format(6), lw=1.4, color='blue', linestyle='--')
axes.plot(X, D8e, label='eksplicitna, t = {}$\u0394$t'.format(8), lw=1.4, color='cyan', linestyle='--')
axes.grid(lw=0.5)
axes.set_xlabel('x / m')
axes.set_ylabel('$\u03C1(x,t)$ / kgm$^{-1}$')
axes.legend(loc='best')
axes.set_title('Difuzija')
plt.show()