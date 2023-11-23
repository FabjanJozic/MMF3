import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline
import sys

def polint(X, Y, NP, x):
	# polint radi polinomnu interpolaciju na temelju Nevilleva algoritma
    # ulaz: NP parova podataka (X,Y) i argument x
    # izlaz: vrijednost polinoma yN u tocki x i greska procjene dy
	ns = 1
	C = [0]
	D = [0]
	Xa = [0]
	Ya = [0]
	for i in range(NP):
		Xa.append(X[i])
		Ya.append(Y[i])
	# trazimo najblizeg susjeda (ns) od x
	mdx = abs(x - Xa[1]) # udaljenost tocke x od 1. cvora
	for i in range(1, NP + 1):
		dx = abs(x - Xa[i])
		if (dx < mdx): # udaljenost od ostalih cvorova
			ns = i
			mdx = dx # minimala udaljenost
		# pocetne vrijednosti (nulti stupac)
		C.append(Ya[i])
		D.append(Ya[i])
	yN = Ya[ns] # prva aproksimacija (prvi stupac)
	ns = ns - 1
	for m in range(1, NP):         # za svaki stupac
		for i in range(1, NP - m + 1): # za svaki redak
			bCx = Xa[i] - x         # brojnik u C: razlika x-eva
			bDx = Xa[i + m] - x       # brojnik u D: razlika x-eva
			CD = C[i + 1] - D[i]       # razlika iz prethodnog stupca
			# stop ako postoje zaokruzeno-isti xi
			odnos = bCx - bDx
			if (odnos == 0.0): sys.exit("STOP: dijeljenje s 0!")
			odnos = CD/odnos
			D[i] = bDx*odnos  # koeficijenti C i D
			C[i] = bCx*odnos
		''' Nakon svakog izracuna stupaca C-ova i D-ova slijedi odluka:
		koju korekciju dy = (C ili D) dodati (oduzeti) aproksimaciji y.
		Biramo sto ravniju (kracu) putanju kroz tablicu   (efikasnije).
		Parcijalne aproksimacije ostaju centrirane obzirom na x-->P(x). 
		Pri tom naravno treba paziti gdje smo (umanjiti ns po potrebi).
		Korekcije dy se smanjuju pa zadnja predstavlja gresku procjene. '''
		if (2*ns < (NP - m)):
			dy = C[ns+1]
		else:
			dy = D[ns]
			ns = ns - 1
		yN += dy
	return yN, dy

X = [x for x in np.arange(0, 3 + 3/13, 3/13)] #pocetne x vrijednosti
Y = [] #pocetne y vrijednosti
for j in range(len(X)):
    k = 0
    Y_j = 1
    while k <= 5:
        Y_j *= X[j] - k
        k += 1
    Y.append(Y_j)

der_L = (Y[1] - Y[0])/(X[0] - X[1]) #numericki iznos derivacija lijeve strane funkcije
der_R = (Y[-1] - Y[-2])/(X[-1] - X[-2]) #numericki iznos derivacije desne strane funkcije

#cs = CubicSpline(X, Y, bc_type=((1, der_L), (1, der_R)))
cs = CubicSpline(X, Y, bc_type='natural')

X_g = [] #x vrijednosti za graf
Y_g_N = [] #y vrijednosti za graf za Nevilleov algoritam
error = [] #pogreske y vrijednosti dobivene Nevilleovim algoritmom
Y_g_s = [] #y vrijednosti za graf za kubicni spline
for i in np.arange(0, 3 + 3/81, 3/81):
    X_g.append(i)
    Y_g_N.append(polint(X, Y, len(X), i)[0])
    error.append(abs(polint(X, Y, len(X), i)[1]))
Y_g_s = cs(X_g)

fig = plt.figure(figsize=(10,5), dpi=120)
axes = fig.add_axes([0.15, 0.15, 0.80, 0.75])
plt.rcParams.update({'font.size': 8})           #type: ignore
axes.scatter(X, Y, c='yellow', edgecolor='black', s=60, label='$(x_{i}, y_{i})$')
axes.plot(X_g, Y_g_s, color='red', label='CubicSpline')
axes.plot(X_g, Y_g_N, color='blue', label='Neville')
axes.errorbar(X_g, Y_g_N, error, capsize=2, fmt='o', markersize=3, color='blue', linewidth=0.5, label='Neville - error')
axes.set_xlabel('$x$ / m')
axes.set_ylabel('$y$ / m$^{5}$')
axes.set_xlim(-0.5, 3.5)
axes.legend()
axes.grid()
plt.show()

'''print("%25s %25s %25s %25s" %('X', 'Y - CubicSpline', 'Y - Neville', 'Neville error'))
for e in range(len(X_g)):
    print("%25.8e %25.8e %25.8e %25.8e" %(X_g[e], Y_g_s[e], Y_g_N[e], error[e]))'''