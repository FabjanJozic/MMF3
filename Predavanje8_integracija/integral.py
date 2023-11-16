
def int_trapezoidal(function, a, b, m):
    '''Trapezna formula za rjesavanje odredenog intervala.'''
    h = (b - a)/m  #korak integracija
    f_a = 0.5*function(a)  #vrijednost funkcije u pocetnoj tocki
    f_b = 0.5*function(b)  #vrijednost funkcije u krajnjoj tocki
    rez = f_a
    k = 1
    while k < m:
        rez += function(a + k*h)  #suma
        k += 1
    rez += f_b
    return rez*h


def int_Simpson(function, a, b, m):
    '''Simpsonova metoda rjesavanja odredenog integrala.'''
    h = (b - a)/m  #korak integracija
    f_a = function(a)  #vrijednost funkcije u pocetnoj tocki
    f_b = function(b)  #vrijednost funkcije u krajnjoj tocki
    rez = f_a
    k = 1
    while k < m:
        if k % 2 == 0:
            rez += 2*function(a + k*h)  #za parne vrijednosti funkcije
        else:
            rez += 4*function(a + k*h)  #za neparne vrijednosti funkcije
        k += 1
    rez += f_b
    return rez*h/3


def kvadrat(x):
    return 2

print(int_trapezoidal(kvadrat, 0, 2, 200))
print(int_Simpson(kvadrat, 0, 2, 200))