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


def Euler(t0, x0, v0, function, N, tN):
    '''
    Eulerova metoda za numericko rjesavanje obicnih diferencijalnih jednadzbi
    prvog reda.
    \nt0 --- pocetni trenutak
    \nx0 --- pocetni polozaj
    \nv0 --- pocetna brzina
    \nN  --- broj iteracija
    \ntN --- krajnji trenutak
    '''
    h = (tN-t0)/N #vremenski korak
    T = [t0] #pocetni trenutak
    X = [x0] #pocetni polozaj
    V = [v0] #pocetna brzina
    A = [function(t0, x0, v0)] #pocetna akceleracija
    while T[-1] <= tN:
        T.append(T[-1]+h)
        X.append(X[-1]+V[-1]*h)
        V.append(V[-1]+A[-1]*h)
        A.append(function(T[-1], X[-1], V[-1]))
    return T, X, V, A


def RK2(t0, x0, v0, function, N, tN):
    '''
    Prediktor-korektor metoda za numericko rjesavanje obicnih diferencijalnih
    jednadzbi prvog reda, Runge-Kutta 2 metoda.
    \nt0 --- pocetni trenutak
    \nx0 --- pocetni polozaj
    \nv0 --- pocetna brzina
    \nN  --- broj iteracija
    \ntN --- krajnji trenutak
    '''
    h = (tN-t0)/N #vremenski korak
    T = [t0] #pocetni trenutak
    X = [x0] #pocetni polozaj
    V = [v0] #pocetna brzina
    A = [function(t0, x0, v0)] #pocetna akceleracija
    while T[-1] <= tN:
        t = T[-1]
        x = X[-1]
        v = V[-1]
        k1v = function(t, x, v)
        k1x = v
        k2v = function(t+h, x+h*k1x, v+h*k1v)
        k2x = v+h*k1v
        T.append(T[-1]+h)
        X.append(x+(k1x+k2x)*h/2)
        V.append(v+(k1v+k2v)*h/2)
        A.append(function(T[-1], X[-1], V[-1]))
    return T, X, V, A


def RK4(t0, x0, v0, function, N, tN):
    '''
    Runge-Kutta 4 metoda za numericko rjesavanje obicnih diferencijalnih
    jednadzbi prvog reda.
    \nt0 --- pocetni trenutak
    \nx0 --- pocetni polozaj
    \nv0 --- pocetna brzina
    \nN  --- broj iteracija
    \ntN --- krajnji trenutak
    '''
    h = (tN-t0)/N #vremenski korak
    T = [t0] #pocetni trenutak
    X = [x0] #pocetni polozaj
    V = [v0] #pocetna brzina
    A = [function(t0, x0, v0)] #pocetna akceleracija
    while T[-1] <= tN:
        t = T[-1]
        x = X[-1]
        v = V[-1]
        k1v = function(t, x, v)
        k1x = v
        k2v = function(t+h/2, x+h/2*k1x, v+h/2*k1v)
        k2x = v+h/2*k1v
        k3v = function(t+h/2, x+h/2*k2x, v+h/2*k2v)
        k3x = v+h/2*k2v
        k4v = function(t+h, x+h*k3x, v+h*k3v)
        k4x = v+h*k3v
        T.append(t+h)
        X.append(x+(k1x+2*k2x+2*k3x+k4x)*h/6)
        V.append(v+(k1v+2*k2v+2*k3v+k4v)*h/6)
        A.append(function(T[-1], X[-1], V[-1]))
    return T, X, V, A


def Euler_n(X0, function, N, xN):
    '''
    Eulerova metoda za rjesavanje obicnih diferencijalnih jednadzbi n-tog
    reda za jednodimenzionalni problem.
    \n
    \nX0 ---------- vektor pocetnih uvjeta
    \nfunction ---- funkcija derivacije n-tog reda
    \nN ----------- broj intervala
    \nxN ---------- krajnja vrijednost
    '''
    n = len(X0) #red diferencijalne jednadzbe
    h = (xN-X0[0])/N #korak
    X = np.zeros((n+1, N+1)) #matrica rjesenja
    X[:-1, 0] = X0 #dodavanje pocetnih uvjeta
    X[-1, 0] = function(X0) #dodavanje vrijednosti derivacije n-tog reda
    for i in range(N):
        X[0, i+1] = (i+1)*h
        X[1:-1, i+1] = X[1:-1, i]+h*X[2:, i]
        X[-1, i+1] = function(X[:-1, i])
    return X


def JUG(t0, X0, V0, acceleration, N, tN):
    '''Metoda aproksimiranog jednolikog ubrzanog gibanja za rjesavanje obicnih
    diferencijalnih jednadzbi gibanja u prostoru.'''
    h = (tN-t0)/N #korak u vremenu
    X = np.zeros(N+1) #matrica polozaja
    V = np.zeros(N+1) #matrica brzina
    A = np.zeros(N+1) #matrica akceleracija
    T = np.zeros(N+1) #vrijeme
    X[0] = X0 #pocetni uvjeti polozaja
    V[0] = V0 #pocetni uvjeti brzina
    A[0] = acceleration(t0, X0, V0) #pocetni uvjeti akceleracija
    T[0] = t0 #pocetni uvjet vremena
    for j in range(N):
            A[j+1] = acceleration(T[j], X[j], V[j])
            V[j+1] = V[j]+h*A[j]
            X[j+1] = X[j]+h*V[j]+0.5*(h**2)*A[j]
            T[j+1] = (j+1)*h
    return T, X, V, A


def Thomas(lower_diag, main_diag, upper_diag, solutions):
    '''Thomasova metoda za pronalazenje rjesenja linearnog sustava jednadzbi
    iz trodijagonalne matrice.'''
    a = lower_diag
    b = main_diag
    c = upper_diag
    d = solutions
    n = len(d)
    c_trenutno = [0]*n
    d_trenutno = [0]*n
    rez = [0]*n
    c_trenutno[0] = c[0]/b[0]
    d_trenutno[0] = d[0]/b[0]
    for i in range(1, n-1):
        c_trenutno[i] = c[i]/(b[i]-a[i-1]*c_trenutno[i-1])
        d_trenutno[i] = (d[i]-a[i-1]*d_trenutno[i-1])/(b[i]-a[i-1]*c_trenutno[i-1])
    d_trenutno[n-1] = (d[n-1]-a[n-2]*d_trenutno[n-2])/(b[n-1]-a[n-2]*c_trenutno[n-2])
    rez[n-1] = d_trenutno[n-1]
    for j in range(n-2, -1, -1):
        rez[j] = d_trenutno[j]-c_trenutno[j]*rez[j+1]
    return rez


def dif(g_x, xt0_N, R, D, met):
    '''Eksplicitna i implicitna metoda rjesavanje difuzijske parcijalne
    diferencijalne jednadzbe u 1D.
    \ng_x ------ funkcija pocetnih uvjeta za x varijablu
    \nxt0_N ---- vektor pocetnih uvjeta - [x0, xN, t0, tN, dx, dt]
    \nR -------- vektor rubnih uvjeta - [x<, x>]
    \nD -------- konstanta difuzije
    \nmet ------ metoda rjesavanja - "exp" / "imp"'''
    dx = xt0_N[4] #korak polozaja
    dt = xt0_N[5] #korak vremena
    N = int((xt0_N[1]-xt0_N[0])/dx) #broj tocaka u prostoru
    M = int((xt0_N[3]-xt0_N[2])/dt) #broj tocaka u vremenu
    dL = R[0] #lijevi rubni uvjet
    dD = R[1] #desni rubni uvjet
    alpha = D*dt/(dx**2)
    dif_p = np.zeros(N+1)
    dif_r = np.zeros(N+1)
    for u in range(len(dif_p)):
        dif_p[u] = g_x(xt0_N[0]+u*dx)
    if met == 'exp': #eksplicitna metoda
        for j in range(M+1): #vrijeme
            for i in range(1, N): #polozaj
                dif_r[i] = alpha*dif_p[i+1]+(1-2*alpha)*dif_p[i]+alpha*dif_p[i-1]
            dif_r[0], dif_r[-1] = dL, dD
            dif_p = np.copy(dif_r)
    elif met == 'imp': #implicitna metoda
        down = [-alpha]*N
        mid = [1+2*alpha]*(N+1)
        up = [-alpha]*N
        for j in range(M+1): #vrijeme
            dif_r = Thomas(down, mid, up, dif_p)
            dif_r[0], dif_r[-1] = dL, dD
            dif_p = np.copy(dif_r)
    else:
        print('Invalid method input.')
    return dif_r