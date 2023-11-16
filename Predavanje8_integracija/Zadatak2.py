import integral as cal
import numpy as np


m = 3.37e-26#kg
T = 300#K
k = 1.38064852e-23#J/K

K = m/(2*k*T) #eksponencijalna konstanta

def p(x):
    return (K/np.pi)**(3/2)*4*np.pi*(x**2)*np.exp(-K*(x**2))

h = 0.1
v = [1e3, 5e3, 1e4, 5e4]

print("\n%22s %22s %22s %22s" %('broj koraka', 'maksimalna brzina','trapezoidna formula', 'Simpsonova metoda'))
for i in range(len(v)):
    print("\n%22.1e %22.1e %22.17lf %22.17lf" %(v[i]/h, v[i], cal.int_trapezoidal(p, 0., v[i], v[i]/h), cal.int_Simpson(p, 0., v[i], v[i]/h)))
print("\n")