import sys



def lagrange(X, Y, x, m):
    '''Langrangeova interpolacija polinoma.'''
    rez = 0.0
    for i in range(0, m + 1):
        L = 1.0
        for j in range(0, m + 1):
            if j != i:
                L *= (x - X[j])/(X[i] - X[j])
        rez += Y[i]*L
    return rez


def polint(X, Y, NP, x):
	# polint radi polinomnu interpolaciju na temelju Nevilleva algoritma
    # ulaz: NP parova podataka (X,Y) i argument x
    # izlaz: vrijednost polinoma yN u tocki x i greska procjene dy
	ns=1
	C=[0]
	D=[0]
	Xa=[0]
	Ya=[0]
	for i in range(NP):
		Xa.append(X[i])
		Ya.append(Y[i])
	# trazimo najblizeg susjeda (ns) od x
	mdx=abs(x - Xa[1]) # udaljenost tocke x od 1. cvora
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