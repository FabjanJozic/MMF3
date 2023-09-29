import numpy as np
import math

def exp_rek(x): #b
    "Vrijednost eksponencijalne funkcije negativnog eksponenta dobivena redom."
    result = 1.0
    e = 10**(-10)
    k = 1
    mem = 1.0
    while abs(mem) > e:
        mem *= -x/k
        result += mem
        k += 1
    return result

def exp_red(x): #a
    "Vrijednost eksponencijalne funkcije negativnog eksponenta dobivena rekurzivnom formulom."
    result = 1.0
    e = 10**(-10)
    k = 1
    mem = 1.0
    while abs(mem) > e:
        mem = ((-1)**k)*(x**k)/math.factorial(k)
        result += mem
        k += 1    
    return result

def exp_rec(x): #c
    "Vrijednost eksponencijalne funkcije negativnog eksponenta dobivena reciprociranjem standardne eksponencijalne funkcije iz a."
    result = 1.0
    e = 10**(-10)
    k = 1
    mem = 1.0
    while abs(mem) > e:
        mem = (x**k)/math.factorial(k)
        result += mem
        k += 1
    return 1/result

for i in range(0, 10):
    i *= 10
    print("%13.5e %13.5e %13.5e %d" %(exp_red(i), exp_rek(i), exp_rec(i), i))

print('\n%13.5e %13.5e %13.5e %d' %(exp_red(20), exp_rek(20), exp_rec(20), 20))