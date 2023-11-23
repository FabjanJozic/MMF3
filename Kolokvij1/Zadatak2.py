import numpy as np

def met_bisekcija(function, a, b, epsilon):
    '''Metoda bisekcije ili raspolavljanja intervala [a,b] za trazenje nul-tocke funkcije u intervalu [a,b], uz ogranicenje epsilon.'''
    c =(a+b)/2
    k = 1
    while abs(c) > epsilon and k <= 600:
        if function(a)*function(c) < 0:
            a = a
            b = c
            c = (a+b)/2
        elif function(a)*function(c) > 0:
            a = c
            b = b
            c = (a+b)/2
        else:
            break
        k +=1
    return c, k

def met_NR(function, deriv_function, x, epsilon):
    '''Newton-Raphsonova metoda za trazenje nul-tocke funkcije u okolini tocke x uz poznavanje derivacije funkcije, uz ogranicenje epsilon.'''
    k = 1
    while abs(function(x)/deriv_function(x)) > epsilon and k <= 600:
        x -= function(x)/deriv_function(x)
        k += 1
    return x, k

m = 3.37e-26 #masa cestice
T = 300 #temperatura
k = 1.38064852e-23 #Boltzmannova konstanta
f_MB = 1.3e-3 #vrijednost funkcije razdiobe
e = 1e-8 # numericka preciznost
K = m/(2*k*T) #konstanta redukcije

def f(v): #funkcija raspodjele
    return ((K/np.pi)**(3/2))*4*np.pi*(v**2)*np.exp(-K*(v**2))

def df(v): #analiticka derivacija funkcije raspodjele
    return ((K/np.pi)**(3/2))*8*np.pi*v**np.exp(-K*(v**2))*(1 + K*(v**2))

a = [-1e-3, 4e6] #lijeve tocke intervala
b = [2.5e-3, 1e7] #desne tocke intervala
c = [] #potencijalne nul-tocke
for u in range(len(a)):
    c.append((a[u] + b[u])/2)

print(met_bisekcija(f, a[0], b[0], e), met_bisekcija(f, a[1], b[1], e))
print(met_NR(f, df, c[0], e), met_NR(f, df, c[1], e))