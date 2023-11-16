import integral as cal
import numpy as np


m = 3.37e-26#kg
T = 300#K
dv = 50#m/s
k = 1.38064852e-23#J/K

v = np.sqrt((8*k*T)/(np.pi*m))#m/s

K = m/(2*k*T) #eksponencijalna konstanta

def p(x):
    return (K/np.pi)**(3/2)*4*np.pi*(x**2)*np.exp(-K*(x**2))

o = [10, 50, 100, 1000, 2000]


print("\n%20s %20s %20s" %('broj koraka','trapezoidna formula', 'Simpsonova metoda'))
for i in range(len(o)):
    print("\n%20d %20.10lf %20.10lf" %(o[i], cal.int_trapezoidal(p, v - dv, v + dv, o[i]), cal.int_Simpson(p, v - dv, v + dv, o[i])))
print("\n")