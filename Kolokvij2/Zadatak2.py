import numpy as np
import matplotlib.pyplot as plt
import skripta as s 

C = 500e-6
omega = 2*np.pi
V0 = 5.0

def change(t, x, v):
    return -C*V0*(omega**2)*np.sin(omega*t)

def change_5(t, x, v):
    return -5*C*V0*(omega**2)*np.sin(omega*t)

t0, tN = 0.0, 2*(2*np.pi/omega)
q0, I0 = 0.0, C*V0*omega

N = 2000

T, q, I = s.JUG(t0, q0, I0, change, N, tN)[0], s.JUG(t0, q0, I0, change, N, tN)[1], s.JUG(t0, q0, I0, change, N, tN)[2]
T_5, q_5, I_5 = s.JUG(t0, 5*q0, 5*I0, change_5, N, tN)[0], s.JUG(t0, 5*q0, 5*I0, change_5, N, tN)[1], s.JUG(t0, 5*q0, 5*I0, change_5, N, tN)[2]

fig = plt.figure(figsize=(9,6), dpi=120)
axes = fig.add_axes([0.10, 0.10, 0.85, 0.85])
plt.rcParams.update({'font.size': 8}) #type:ignore
axes.plot(T, q, label='naboj $q(t)$, 1*q', lw=1.4, color='red')
axes.plot(T, I, label='struja $I(t)$, 1*q', lw=1.4, color='blue')
axes.plot(T_5, q_5, label='naboj $q(t)$, 5*q', lw=1.4, color='red', linestyle='-.')
axes.plot(T_5, I_5, label='struja $I(t)$, 5*q', lw=1.4, color='blue', linestyle='-.')
axes.grid(lw=0.5)
axes.set_xlabel('vrijeme')
axes.set_ylabel('napon i struja')
#axes.set_ylabel('$frac{I(t)}{I_{max}}$ , $frac{q(t)}{q_{max}}$')
axes.legend(loc='best')
axes.set_title('Struja i napon')
plt.show()