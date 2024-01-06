import numpy as np

def D_exp(g_x, xt0_N, D):
    '''Eksplicitna metoda rjesavanje difuzijske parcijalne
    diferencijalne jednadzbe.
    \ng_x ------ funkcija pocetnih uvjeta za x varijablu
    \nxt0_N ---- vektor pocetnih uvjeta
    \nD -------- konstanta difuzije'''
    dx = xt0_N[4] #korak polozaja
    dt = xt0_N[5] #korak vremena
    N = int(xt0_N[1]/dx) #broj tocaka u prostoru
    M = int(xt0_N[3]) #broj tocaka u vremenu
    alpha = D*dt/(dx**2)
    '''Vrijednost funkcije difuzije dobiva se rekurzivno preko
    vrijednosti varijable polozaja.'''
    dif_p = np.zeros(N+1)
    dif_r = np.zeros(N+1)
    for u in range(len(dif_p)):
        dif_p[u] = g_x(xt0_N[0]+u*dx)
    for j in range(M+1): #vrijeme
        for i in range(1, N): #polozaj
            dif_r[i] = alpha*dif_p[i+1]+(1-2*alpha)*dif_p[i]+alpha*dif_p[i-1]
        dif_p = np.copy(dif_r)
    return dif_r

            