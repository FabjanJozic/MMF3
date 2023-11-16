
def int_trapezoidal(function, a, b, m):
    '''Trapezna formula za rjesavanje odredenog intervala.'''
    h = (b - a)/m  #korak integracija
    f_a = function(a)  #vrijednost funkcije u pocetnoj tocki
    f_b = function(b)  #vrijednost funkcije u krajnjoj tocki
    rez = (f_a + f_b)/2
    k = 1
    while k < m:
        rez += function(a + k*h)  #suma
        k += 1
    return rez*h


def int_Simpson(function, a, b, m):
    '''Simpsonova metoda rjesavanja odredenog integrala.'''
    h = (b - a)/m  #korak integracija
    f_a = function(a)  #vrijednost funkcije u pocetnoj tocki
    f_b = function(b)  #vrijednost funkcije u krajnjoj tocki
    rez = f_a + f_b
    k = 1
    while k < m:
        if k % 2 == 0:
            rez += 2*function(a + k*h)  #za parne k
        else:
            rez += 4*function(a + k*h)  #za neparne k
        k += 1
    return rez*h/3
