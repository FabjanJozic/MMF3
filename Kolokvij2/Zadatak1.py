import numpy as np 
import skripta as s 

x0, xN = -0.2, 3.0
a, b = 2.0, 1.0

def gustoca(x):
    return a*np.exp(x)+b*(x**5)

N = [50, 100, 200, 500]

for i in range(len(N)):
    print("\n%8d %15.12lf" %(N[i], s.int_gauleg(gustoca, x0, xN, N[i])))