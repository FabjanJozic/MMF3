
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

def f(x):
    return x**2 + 5

x = [i for i in range(1, 5 + 1)]

e = 1e-6 #pomak oko x za derivaciju
def df(f, x, e): #centralna derivacija funkcije f(x)
    return (f(x + e) - f(x - e))/(2*e)

fun_der = []
for i in range(len(x)):
    fun_der.append(df(f, x[i], e))
print(fun_der)

a = [1, 2, 3, 4] #donja dijagolana
b = [1, 1, 1, 1, 1] #glavna dijagonala
c = [4, 3, 2, 1] #dornja dijagonala
fun = [f(i) for i in x] #vrijednosti funkcije

print(Thomas(a, b, c, fun))
