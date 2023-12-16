import diferencijalne_jednadzbe as dj 
import matplotlib.pyplot as plt
import numpy as np
import sys

sys.getdefaultencoding()

X0_1D = [0.0, 4*np.pi/180, 0.0]
X0_3D = [4*np.pi/180, 0.0, 0.0]
V0_3D = [0.0, 0.0, 0.0]
l = 0.2484902028828339
m = 0.2
g = 9.81
N = 20000

T = 2*np.pi*np.sqrt(l/g)
t0 = 0.0
tN = 20*T

def fun_1D(vrijednosti):
    return -g/(l*m)*np.sin(vrijednosti[1])

def fun_RK4(t, x, v):
    return -g/(l*m)*np.sin(x)

def fun_3D(t, x_vri, v_vri):
    return [-g/(l*m)*np.sin(x_vri[0]), 0.0, 0.0]

X_En , V_En = dj.Euler_n(X0_1D, fun_1D, N, tN)[1], dj.Euler_n(X0_1D, fun_1D, N, tN)[2] #Eulerova metoda
X_RK, V_RK = dj.RK4(t0, X0_1D[1], X0_1D[2], fun_RK4, N, tN)[1], dj.RK4(t0, X0_1D[1], X0_1D[2], fun_RK4, N, tN)[2] #RK4 metoda
X_JUG, V_JUG = dj.JUG(t0, X0_3D, V0_3D, fun_3D, N, tN)[1][0], dj.JUG(t0, X0_3D, V0_3D, fun_3D, N, tN)[2][0] #JUG metoda

fig = plt.figure(figsize=(7,6), dpi=120)
axes = fig.add_axes([0.15, 0.15, 0.75, 0.70])
plt.rcParams.update({'font.size': 8}) #type: ignore
axes.plot(X_En, V_En, color='blue', label='Eulerova metoda', lw=0.7)
axes.plot(X_JUG, V_JUG, color='red', label='JUG metoda', lw=0.8)
axes.plot(X_RK, V_RK, color='green', label='RK4 metoda', lw=1.4)
axes.grid(lw=0.5)
axes.set_xlabel('Kut   $\u03C6$ / rad')
axes.set_ylabel('Brzina   $\u03C9$ / $\dfrac{rad}{s}$')
axes.legend(loc='best')
axes.set_title('Fazni dijagram matematičkog njihala')
plt.show()