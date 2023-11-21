

#Vrijednosti A, B, C, D, E i F su konstante. 


def met_bisekcija(function, a, b, epsilon):
    '''Metoda bisekcije ili raspolavljanja intervala [a,b] za trazenje nul-tocke funkcije u intervalu [a,b], uz ogranicenje epsilon.'''
    c =(a+b)/2
    k = 1
    while abs(c) > epsilon and k <= 500:
        if function(a)*function(c) < 0:
            a = a
            b = c
            c = (a+b)/2
        if function(a)*function(c) > 0:
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
    while abs(function(x)/deriv_function(x)) > epsilon and k <= 500:
        x -= function(x)/deriv_function(x)
        k += 1
    return x, k
    
def met_sekanta(function, x, epsilon):
    '''Metode sekante za trazenje nul-tocke funkcije u okolini tocke x uz nepoznatu derivaciju funkcije, uz ogranicenje epsilon.'''
    def deriv_function(function, x, epsilon):
        return (function(x+epsilon) - function(x-epsilon))/(2*epsilon)
    k = 1
    while abs(function(x)/deriv_function(function, x, epsilon)) > epsilon and k <= 500:
        x -= function(x)/deriv_function(function, x, epsilon)
        k +=1
    return x, k