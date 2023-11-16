

#Vrijednosti A, B, C, D, E i F su konstante. 


def met_bisekcija(function, a, b, epsilon, A, B, C, D, E, F):
    '''Metoda bisekcije ili raspolavljanja intervala [a,b] za trazenje nul-tocke funkcije u intervalu [a,b], uz ogranicenje epsilon.'''
    c =(a+b)/2
    k = 1
    while abs(c) > epsilon and k <= 500:
        if function(a, A, B, C, D, E, F)*function(c, A, B, C, D, E, F) < 0:
            a = a
            b = c
            c = (a+b)/2
        if function(a, A, B, C, D, E, F)*function(c, A, B, C, D, E, F) > 0:
            a = c
            b = b
            c = (a+b)/2
        else:
            break
        k +=1
    return c, k

def met_NR(function, deriv_function, x, epsilon, A, B, C, D, E, F):
    '''Newton-Raphsonova metoda za trazenje nul-tocke funkcije u okolini tocke x uz poznavanje derivacije funkcije, uz ogranicenje epsilon.'''
    k = 1
    while abs(function(x, A, B ,C, D, E, F)/deriv_function(x, A, B, C, D, E, F)) > epsilon and k <= 500:
        x -= function(x, A, B, C, D, E, F)/deriv_function(x, A, B, C, D, E, F)
        k += 1
    return x, k
    
def met_sekanta(function, x, epsilon, A, B, C, D, E, F):
    '''Metode sekante za trazenje nul-tocke funkcije u okolini tocke x uz nepoznatu derivaciju funkcije, uz ogranicenje epsilon.'''
    def deriv_function(function, x, epsilon, A, B, C, D, E, F):
        return (function(x+epsilon, A , B, C, D, E, F) - function(x-epsilon, A, B, C, D, E, F))/(2*epsilon)
    k = 1
    while abs(function(x, A, B, C, D, E, F)/deriv_function(function, x, epsilon, A, B, C, D, E, F)) > epsilon and k <= 500:
        x -= function(x, A, B, C, D, E, F)/deriv_function(function, x, epsilon, A, B, C, D, E, F)
        k +=1
    return x, k