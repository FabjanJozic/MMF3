import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import PillowWriter

import skripta as s

omega = 1.0
beta = 3.8
def accelerationP(t, x, v):
    return -(omega**2)*x-beta*(x**3) #za beta > 0

def accelerationN(t, x, v):
    return -(omega**2)*x+beta*(x**3) #za beta < 0

T = 2*np.pi/omega #period harmonickog oscilatora
t0, x0, v0 = 0.0, 0.5, 0.0 #pocetni uvjeti
tN = 4*T

N = 300

XP, VP = s.RK4(t0, x0, v0, accelerationP, N, tN)[1], s.RK4(t0, x0, v0, accelerationP, N, tN)[2]
XN, VN = s.RK4(t0, x0, v0, accelerationN, N, tN)[1], s.RK4(t0, x0, v0, accelerationN, N, tN)[2]

fig = plt.figure(figsize=(10,7), dpi=120)
metadata = dict(title="Fazni dijagram Duffingovog oscilatora")
writer = PillowWriter(fps=15, metadata=metadata) #type: ignore
with writer.saving(fig, "Duffing_w1_b3_8_N300.gif", 120):
    for i in range(len(XP)):
        plt.clf()              
        plt.plot(XP[:i], VP[:i], color='red', lw=1.3)
        plt.scatter(XP[i], VP[i], color='red', s=35,
                    label='\n$\u03C9$ = {}, $\u03B2$ = {}\nx0 = {}, v0 = {}\nN = {}\n'.format(
                    omega, beta, x0, v0, N))
        plt.plot(XN[:i], VN[:i], color='blue', lw=1.3)
        plt.scatter(XN[i], VN[i], color='blue', s=35,
                    label='\n$\u03C9$ = {}, $\u03B2$ = {}\nx0 = {}, v0 = {}\nN = {}\n'.format(
                    omega, -beta, x0, v0, N))
        plt.axis('equal')
        plt.grid(lw=0.4)
        plt.xlabel('Položaj  $x$ [m]')
        plt.ylabel('Brzina  $v$ [ms$^{-1}$]')
        plt.title('Fazni dijagram Duffingovog oscilatora')
        plt.legend(loc='upper right')
        writer.grab_frame()