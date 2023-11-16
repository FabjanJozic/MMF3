import interpolacija as inter
import numpy as np
import matplotlib.pyplot as plt



with open('C:\\Users\\Fabo\\OneDrive\\Desktop\\programi\\MMF3\\Predavanje6\\V(H-H).txt','r') as read1:
    linija1 = read1.readlines()
    mod_linija1 = []
    for i in range(2, len(linija1)):
        col1, col2 = linija1[i].strip().split()
        mod_col1 = float(col1)*0.52917721092 #pretvara u angstrome
        mod_col2 = float(col2)*315775.04 #pretvara u kelvine
        mod_i = f"{mod_col1}\t{mod_col2}\n"
        mod_linija1.append(mod_i)
    read1.close()

with open('C:\\Users\\Fabo\\OneDrive\\Desktop\\programi\\MMF3\\Predavanje6\\V(H-H)_AK.txt','w') as write1:
    write1.writelines(mod_linija1)

with open('C:\\Users\\Fabo\\OneDrive\\Desktop\\programi\\MMF3\\Predavanje6\\V(H-H)_AK.txt','r') as read2:
    linija2 = read2.readlines()
    r = []
    V = []
    mod_linija2 = []
    for i in range(len(linija2)):
        col1, col2 = linija2[i].strip().split()
        mod_col1 = float(col1)
        mod_col2 = float(col2)
        r.append(mod_col1)
        V.append(mod_col2)
    read2.close()

a = 2.81
b = 9.81
c = (b - a)/70
x = []
yL = []
yP = []
dyP = []
for j in np.arange(a, b + c, c):
    x.append(j)
    yL.append(inter.lagrange(r, V, j, len(r) - 1))
    yP.append(inter.polint(r, V, len(r), j)[0])
    dyP.append(abs(inter.polint(r, V, len(r), j)[1]))

comb = list(zip(r, yL, yP, dyP))
with open('C:\\Users\\Fabo\\OneDrive\\Desktop\\programi\\MMF3\\Predavanje6\\V(H-H)_inter.txt','w') as write2:
    for val1, val2, val3, val4 in comb:
        linija = f"{val1}\t{val2}\t{val3}\t{val4}\n"
        write2.write(linija)
    write2.close()

fig = plt.figure(figsize=(10,5), dpi=120)
axes = fig.add_axes([0.15, 0.15, 0.80, 0.75])
plt.rcParams.update({'font.size': 8})           #type: ignore
axes.scatter(r, V, c='white', edgecolor='black', s=60)
axes.scatter(x, yL, c='red', edgecolor='red', s=35)
axes.errorbar(x, yP, dyP, capsize=2, fmt='o', markersize=3, color='blue', linewidth=0.5)
axes.set_xlabel('$r$ / $\AA$')
axes.set_ylabel('$V$ / $K$')
axes.set_xlim(1., 10.)
axes.set_ylim(-10., 10.)
axes.legend(['$(r_{i}, V_{i})$', 'Lagrange', 'Neville'], loc='best')
plt.show()

        


