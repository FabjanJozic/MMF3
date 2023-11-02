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
for j in np.arange(a, b + c, c):
    x.append(j)
    yL.append(inter.lagrange(r, V, j, len(r) - 1))
    with open('C:\\Users\\Fabo\\OneDrive\\Desktop\\programi\\MMF3\\Predavanje6\\V(H-H)_inter.txt','w') as write2:
        


'''fig = plt.figure(figsize=(13,6), dpi=90)
axes = fig.add_axes([0.15, 0.15, 0.75, 0.70])
axes.scatter(x, yL, color='red')
axes.set_xlim(a, b)
axes.grid(lw=0.5)
plt.show()'''

        


