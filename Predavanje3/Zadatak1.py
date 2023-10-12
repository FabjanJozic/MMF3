import nul_tocke as nt
import numpy as np

def y1(t, y1_0, A, B):
    return y1_0+A*np.cos(B*t)

def y2(t, y2_0, C, D):
    return y2_0+C*np.exp(D*t)

def fun(t, y1_0, A, B, y2_0, C, D):
    return y1(t, y1_0, A, B) - y2(t, y2_0, C, D)


y1_0 = 5.0
y2_0 = 0.325
A = 1.0
B = 3.0
C = 2.0
D = 0.5

e = 1e-6 #epsilon

