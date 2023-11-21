
def Thomas(lower_diag, main_diag, upper_diag, solutions):
    '''Thomasova metoda za pronalazenje rjesenja linearnog sustava jednadzbi iz trodijagonalne matrice.'''
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
    for i in range(1, n - 1):
        c_trenutno[i] = c[i]/(b[i] - a[i - 1]*c_trenutno[i - 1])
        d_trenutno[i] = (d[i] - a[i - 1]*d_trenutno[i - 1])/(b[i] -a[i - 1]*c_trenutno[i - 1])
    d_trenutno[n - 1] = (d[n - 1] - a[n - 2]*d_trenutno[n - 2])/(b[n - 1] - a[n - 2]*c_trenutno[n - 2])
    rez[n - 1] = d_trenutno[n - 1]
    for j in range(n - 2, -1, -1):
        rez[j] = d_trenutno[j] - c_trenutno[j]*rez[j + 1]
    return rez


def Gauss_Jordan(matrix):
    '''Gauss-Jordanova metoda eliminacije za pretvaranje matrice u gornju dijagonalnu matricu.'''
    matrica = matrix
    m = len(matrica)
    n = len(matrica[0])
    for i in range(min(m, n)):
        if matrica[i][i] == 0:
            for j in range(i + 1, m):
                if matrica[j][i] != 0:
                    matrica[i], matrica[j] = matrica[j], matrica[i]
                    break
                else:
                    continue
            for j in range(i + 1, m):
                N = matrica[j][i]/matrica[i][i]
                for k in range(i, n):
                    matrica[j][k] -= N*matrica[i][k]
    return matrica
