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

o = [10, 50, 100]


print("\n%20s %25s %25s %25s" %('broj koraka','trapezoidna formula', 'Simpsonova metoda', 'Gauss-Legendrova kvadratura'))
for i in range(len(o)):
    print("\n%20d %25.10lf %25.10lf %25.10lf" %(o[i], cal.int_trapezoidal(p, v-dv, v+dv, o[i]),
                                       cal.int_Simpson(p, v - dv, v + dv, o[i]), cal.int_gauleg(p, v-dv, v+dv, o[i]))),
print("\n")