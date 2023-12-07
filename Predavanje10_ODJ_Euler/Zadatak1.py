import numpy as np
import matplotlib.pyplot as plt

import diferencijalne_jednadzbe as dj

m = 0.2 #masa
l = 0.2484902028828339 #duljina njihala
y0 = 4 #pocetni kut
g = 9.81 #gravitacijska akceleracija
v0 = 0.0 #pocetna brzina

y0_r = y0*np.pi/180 #pocetni kut u radijanima

def analiticko(t, x, v):
    return -g*x/l

def numericko(t, x, v):
    return -g/l*np.sin(x)

T = 2*np.pi*np.sqrt(l/g) #period
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
axes.plot(dj.Euler(0.0 , y0_r, v0, numericko, 20000, t2)[0], dj.Euler(0.0 , y0_r, v0, numericko, 20000, t2)[1],
          color='orange', lw=1.1, label='$y_{E,20000}(t)$')
axes.plot(t, theta, color='purple', lw=1.1, label='$y_{a}(t)$')
axes.grid(lw=0.5)
axes.set_xlim(t1, t2)
axes.legend(loc='best')
plt.show()'''

'''fig = plt.figure(figsize=(11,5), dpi=110)
axes = fig.add_axes([0.15, 0.15, 0.75, 0.70])
plt.rcParams.update({'font.size': 9})           #type: ignore
axes.plot(dj.Euler(0.0 , y0_r, v0, numericko, 100000, t2)[0], dj.Euler(0.0 , y0_r, v0, numericko, 100000, t2)[1],
          color='blue', lw=1.5, label='Euler $N = 100000$')
axes.plot(dj.Euler(0.0 , y0_r, v0, numericko, 10000, t2)[0], dj.Euler(0.0 , y0_r, v0, numericko, 10000, t2)[1],
          color='purple', lw=1.5, label='Euler $N/10 = 10000$')
axes.plot(dj.RK4(0.0 , y0_r, v0, numericko, 100000, t2)[0], dj.RK4(0.0 , y0_r, v0, numericko, 100000, t2)[1],
          color='orange', lw=1.5, label='RK4 $N = 100000$')
axes.plot(dj.RK4(0.0 , y0_r, v0, numericko, 10000, t2)[0], dj.RK4(0.0 , y0_r, v0, numericko, 10000, t2)[1],
          color='red', lw=1.5, label='RK4 $N/10 = 10000$')
axes.grid(lw=0.5)
#axes.set_xlim(t1, t2)
axes.legend(loc='best')
plt.show()'''

t = []
theta_4 = []
theta_8 = []
theta_16 = []
theta_32 = []
for i in np.arange(0.0, 7*T+1e-5, 1e-5):
    t.append(i)
    theta_4.append(y0_r*np.cos(i*np.sqrt(g/l)))
    theta_8.append(y0_r*2*np.cos(i*np.sqrt(g/l)))
    theta_16.append(y0_r*4*np.cos(i*np.sqrt(g/l)))
    theta_32.append(y0_r*8*np.cos(i*np.sqrt(g/l)))

fig = plt.figure(figsize=(11,5), dpi=110)
axes = fig.add_axes([0.15, 0.15, 0.75, 0.70])
plt.rcParams.update({'font.size': 9})           #type: ignore
axes.plot(dj.RK4(0.0 , y0_r, v0, numericko, 1e5, 7*T)[0], dj.RK4(0.0 , y0_r, v0, numericko, 1e5, 7*T)[1],
          color='green', lw=1.3, label='RK4, $y_{0} = 4^{o}$', linestyle='--')
axes.plot(dj.RK4(0.0 , y0_r*2, v0, numericko, 1e5, 7*T)[0], dj.RK4(0.0 , y0_r*2, v0, numericko, 1e5, 7*T)[1],
          color='red', lw=1.3, label='RK4, $y_{0} = 8^{o}$', linestyle='--')
axes.plot(dj.RK4(0.0 , y0_r*4, v0, numericko, 1e5, 7*T)[0], dj.RK4(0.0 , y0_r*4, v0, numericko, 1e5, 7*T)[1],
          color='yellow', lw=1.3, label='RK4, $y_{0} = 16^{o}$', linestyle='--')
axes.plot(dj.RK4(0.0 , y0_r*8, v0, numericko, 1e5, 7*T)[0], dj.RK4(0.0 , y0_r*8, v0, numericko, 1e5, 7*T)[1],
          color='blue', lw=1.3, label='RK4, $y_{0} = 32^{o}$', linestyle='--')
axes.plot(t, theta_4, color='green', lw=1.3, label='$y_{a}, y_{0} = 4^{o}$')
axes.plot(t, theta_8, color='red', lw=1.3, label='$y_{a}, y_{0} = 8^{o}$')
axes.plot(t, theta_16, color='yellow', lw=1.3, label='$y_{a}, y_{0} = 16^{o}$')
axes.plot(t, theta_32, color='blue', lw=1.3, label='$y_{a}, y_{0} = 32^{o}$')
axes.grid(lw=0.5)
axes.legend(loc='best')
plt.show()
