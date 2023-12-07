import numpy as np
import matplotlib.pyplot as plt

import diferencijalne_jednadzbe as dj

m = 0.2 #masa
l = 0.02484902028828339 #duljina njihala
y0 = 4 #pocetni kut
g = 9.81 #gravitacijska akceleracija
v0 = 0.0 #pocetna brzina

y0_r = y0*np.pi/180 #pocetni kut u radijanima

def analiticko(t, x, v):
    return -g*x/l

def numericko(t, x, v):
    return -g/l*np.sin(x)

T = 2*np.pi*np.sqrt(l/g)
t1 = 1*T
t2 = 20*T

'''t = []
theta = []
for i in np.arange(t1, t2+1e-5, 1e-5):
    t.append(i)
    theta.append(y0_r*np.cos(i*np.sqrt(g/l)))

fig = plt.figure(figsize=(11,5), dpi=110)
axes = fig.add_axes([0.15, 0.15, 0.75, 0.70])
plt.rcParams.update({'font.size': 9})           #type: ignore
axes.plot(dj.Euler(0.0 , y0_r, v0, numericko, 500, t2)[0], dj.Euler(0.0 , y0_r, v0, numericko, 500, t2)[1],
          color='blue', lw=1.1, label='$y_{E,500}(t)$')
axes.plot(dj.Euler(0.0 , y0_r, v0, numericko, 1000, t2)[0], dj.Euler(0.0 , y0_r, v0, numericko, 1000, t2)[1],
          color='green', lw=1.1, label='$y_{E,1000}(t)$')
axes.plot(dj.Euler(0.0 , y0_r, v0, numericko, 5000, t2)[0], dj.Euler(0.0 , y0_r, v0, numericko, 5000, t2)[1],
          color='orange', lw=1.1, label='$y_{E,5000}(t)$')
axes.plot(t, theta, color='purple', lw=1.1, label='$y_{a}(t)$')
axes.grid(lw=0.5)
axes.set_xlim(t1, t2)
axes.legend(loc='best')
plt.show()'''

'''fig = plt.figure(figsize=(11,5), dpi=110)
axes = fig.add_axes([0.15, 0.15, 0.75, 0.70])
plt.rcParams.update({'font.size': 9})           #type: ignore
axes.plot(dj.Euler(0.0 , y0_r, v0, numericko, 10000, t2)[0], dj.Euler(0.0 , y0_r, v0, numericko, 10000, t2)[1],
          color='blue', lw=1.1, label='Euler $N = 10000$')
axes.plot(dj.Euler(0.0 , y0_r, v0, numericko, 1000, t2)[0], dj.Euler(0.0 , y0_r, v0, numericko, 1000, t2)[1],
          color='purple', lw=1.1, label='Euler $N/10 = 1000$')
axes.plot(dj.RK4(0.0 , y0_r, v0, numericko, 10000, t2)[0], dj.RK4(0.0 , y0_r, v0, numericko, 10000, t2)[1],
          color='orange', lw=1.1, label='RK4 $N = 10000$')
axes.plot(dj.RK4(0.0 , y0_r, v0, numericko, 1000, t2)[0], dj.RK4(0.0 , y0_r, v0, numericko, 1000, t2)[1],
          color='red', lw=1.1, label='RK4 $N/10 = 1000$')
axes.grid(lw=0.5)
#axes.set_xlim(t1, t2)
axes.legend(loc='best')
plt.show()'''