import numpy as np


def gauleg(x_1, x_2, n):
    '''Metoda Gauss-Legendrove kvadrature za odredivanje nultocki x i njihovih statistickih
    tezina w. Granice integracije su x1 i x2, a duljina lista x i w je n.'''
    x = [0]*n #nul-tocke
    w = [0]*n #tezine nul-tocaka
    epsilon = 1e-6 #minimalna vrijednost za nul-tocku
    m = int((n+1)/2) #brojac
    x_m = (x_1+x_2)/2 #sredina intervala
    x_l = (x_2-x_1)/2 #pola intervala
    for i in range(1, m+1):
        z = np.cos(np.pi*(i-0.25)/(n+0.5)) #pocetna vrijednost nul-tocke
        while True:
            '''/do while/ petlja koja na kraju provjerava je li uvjet zadovoljen'.
            Racunjanje Legendrovih polinoma s pocetnim polimomima L1 i L2'''
            L1 = 1.0
            L2 = 0.0
            for j in range(1, n+1):
                L3 = L2
                L2 = L1
                L1 = ((2*j-1)*z*L2-(j-1)*L3)/j
            dL = n*(z*L1-L2)/(z**2-1) #derivacija Legendrovog polinoma
            z_0 = z
            z = z_0-L1/dL
            if abs(z-z_0) < epsilon:
                break
        x[i-1] = x_m-x_l*z #racunanje nul-tocki
        x[n-i] = x_m+x_l*z
        w[i-1] = 2*x_l/((1-z**2)*dL**2) #racunanje tezina
        w[n-i] = w[i-1] #iskoristavanje simetricnosti
    return x, w


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


def int_gauleg(function, a, b, m):
    '''Metoda rjesavanja odredenog integrala koristeci Gauss-Legendrovu kvadraturu.'''
    x, w = gauleg(a, b, m)[0], gauleg(a, b, m)[1] #nul-tocke i tezine nul-tocki
    rez = 0.0
    for i in range(len(x)):
        rez += function(x[i])*w[i] #suma
    return rez    