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

cs = CubicSpline(r, V)

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

yS = cs(x)
yP_S = []
for i in range(len(x)):
    yP_S.append(yP[i] - yS[i])

comb = list(zip(r, yL, yP, dyP, yS, yP_S))
with open('C:\\Users\\Fabo\\OneDrive\\Desktop\\programi\\MMF3\\Predavanje7\\V(H-H)_inter.txt','w') as write:
    for val1, val2, val3, val4, val5, val6 in comb:
        l = "\n%+18.10e %+18.10e %+18.10e %+18.10e %+18.10e %+18.10e" %(val1, val2, val3, val4, val5, val6)
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
axes.legend(['$(r_{i}, V_{i})$', 'Lagrange', 'Neville', 'CubicSpline'], loc='best')
plt.show()