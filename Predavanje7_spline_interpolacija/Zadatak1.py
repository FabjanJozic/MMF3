import interpolacija as inter
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline



with open('C:\\Users\\Fabo\\OneDrive\\Desktop\\programi\\MMF3\\Predavanje6\\V(H-H)_AK.txt','r') as read:
    linija = read.readlines()
    r = []
    V = []
    mod_linija2 = []
    for i in range(len(linija)):
        col1, col2 = linija[i].strip().split()
        mod_col1 = float(col1)
        mod_col2 = float(col2)
        r.append(mod_col1)
        V.append(mod_col2)
    read.close()

a = 2.81
b = 9.81
c = (b - a)/70
x = []
yL = []
yP = []
dyP = []
for j in np.arange(a, b + c, c):
    x.append(j)
    yL.append(inter.lagrange(r, V, len(r) - 1, j))
    yP.append(inter.polint(r, V, len(r), j)[0])
    dyP.append(abs(inter.polint(r, V, len(r), j)[1]))

def der_V(r):
    '''Funkcija derivacije potencijala V na vecim udaljenostima r.'''
    C = 45064e-6
    return C*6*(r**(-7))

V_der = (yL[1] - yL[0])/(x[1] - x[0])

cs = CubicSpline(r, V, bc_type=((1, V_der), (1, der_V(x[-1]))))

yS = cs(x)
yP_S = []
for i in range(len(x)):
    yP_S.append(yP[i] - yS[i])

with open('C:\\Users\\Fabo\\OneDrive\\Desktop\\programi\\MMF3\\Predavanje7\\V(H-H)_inter.txt','w') as write:
    write.write("\n%18s %18s %18s %18s %18s %18s" %('r = x', 'yL', 'yP', 'dyP', 'yS', 'yP - yS'))
    write.write('\n')
    for u in range(len(x)):
        l = "\n%+18.10e %+18.10e %+18.10e %+18.10e %+18.10e %+18.10e" %(x[u], yL[u], yP[u], dyP[u], yS[u], yP_S[u])
        write.write(l)
    write.close()

fig = plt.figure(figsize=(10,5), dpi=120)
axes = fig.add_axes([0.15, 0.15, 0.80, 0.75])
plt.rcParams.update({'font.size': 8})           #type: ignore
axes.scatter(r, V, c='white', edgecolor='black', s=75)
axes.scatter(x, yL, c='red', edgecolor='red', s=50)
axes.scatter(x, yP, c='blue', edgecolor='blue', s=25)
axes.scatter(x, yS, c='yellow', edgecolor='yellow', s=10)
axes.set_xlabel('$r$ / $\AA$')
axes.set_ylabel('$V$ / $K$')
axes.set_xlim(1., 10.)
axes.set_ylim(-10., 10.)
axes.set_title('V - r   graf')
axes.legend(['$(r_{i}, V_{i})$', 'Lagrange', 'Neville', 'CubicSpline'], loc='best')
plt.show()