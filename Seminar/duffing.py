import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import PillowWriter

import skripta as s

omega0 = 1.0 #svojstvena frekvencija
beta = 1.0 #faktor nelinearnosti
delta = 0.1 #gusenje
omega = 1.0 #vanjska frekvencija
gama = 0.2 #vanjska amplituda
def accelerationP(t, x, v):
    return -(omega0**2)*x-delta*v-beta*(x**3)+gama*np.cos(omega*t) #za beta > 0

def accelerationN(t, x, v):
    return -(omega0**2)*x-delta*v+beta*(x**3)+gama*np.cos(omega*t) #za beta < 0

T = 2*np.pi/omega0 #period harmonickog oscilatora
t0, x0, v0 = 0.0, 0.0, 0.0 #pocetni uvjeti
tN = 14*T

N = 1500

XP, VP = s.RK4(t0, x0, v0, accelerationP, N, tN)[1], s.RK4(t0, x0, v0, accelerationP, N, tN)[2]
XN, VN = s.RK4(t0, x0, v0, accelerationN, N, tN)[1], s.RK4(t0, x0, v0, accelerationN, N, tN)[2]

fig = plt.figure(figsize=(10,7), dpi=120)
metadata = dict(title="Fazni dijagram Duffingovog oscilatora")
writer = PillowWriter(fps=15, metadata=metadata) #type: ignore
with writer.saving(fig, "Duffing_pobudeno.gif", 120):
    for i in range(len(XP)):
        plt.clf()              
        plt.plot(XP[:i], VP[:i], color='red', lw=1.3)
        plt.scatter(XP[i], VP[i], color='red', s=35,
                    label='\n$\u03C9$0 = {}, $\u03B2$ = {}\nx0 = {}, v0 = {}\n$\u03C9$ = {}, $\u03B4$ = {}, $\u03B3$ = {}\nN = {}\n'.format(
                    omega0, beta, x0, v0, omega, delta, gama, N))
        plt.plot(XN[:i], VN[:i], color='blue', lw=1.3)
        plt.scatter(XN[i], VN[i], color='blue', s=35,
                    label='\n$\u03C9$0 = {}, $\u03B2$ = {}\nx0 = {}, v0 = {}\n$\u03C9$ = {}, $\u03B4$ = {}, $\u03B3$ = {}\nN = {}\n'.format(
                    omega0, -beta, x0, v0, omega, delta, gama, N))
        plt.axis('equal')
        plt.grid(lw=0.4)
        plt.xlabel('Položaj  $x$ [m]')
        plt.ylabel('Brzina  $v$ [ms$^{-1}$]')
        plt.title('Fazni dijagram Duffingovog oscilatora')
        plt.legend(loc='upper right')
        writer.grab_frame()