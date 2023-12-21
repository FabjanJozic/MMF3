import numpy as np

def D_exp(g_x, xt0_N, N, M):
    '''Eksplicitna metoda rjesavanje difuzijske parcijalne diferencijalne jednadzbe.
    \ng_x ------ funkcija pocetnih uvjeta za x varijablu
    \nxt0_N ---- pocetni i krajnji uvjeti polozaja pa vremena
    \nN -------- broj x koraka
    \nM -------- broj t koraka'''
    dx = (xt0_N[1]-xt0_N[0])/(N+1) #korak polozaja
    dt = (xt0_N[3]-xt0_N[2])/(M+1) #korak vremena
    alpha = dt/(dx**2)
    '''Vrijednost funkcije difuzije dobiva se rekurzivno preko vrijednosti varijable polozaja.'''
    dif_p = []*(N+1)
    dif_r = [0]*(N+1)
    for u in range(N+1):
        dif_p.append(g_x(u*dx+xt0_N[0]))
    for j in range(1, M+1): #vrijeme
        if j == 100:
            m = dif_r
        for i in range(1, N): #polozaj
            dif_r[i] = alpha*dif_p[i+1]+(1-2*alpha)*dif_p[i]+alpha*dif_p[i-1]
        dif_p = dif_r
    return dif_r

            