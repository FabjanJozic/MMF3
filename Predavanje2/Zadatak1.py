import derivacija as d
import matplotlib.pyplot as plt
import numpy as np



h =[1e-1, 1e-2, 1e-3, 1e-4, 1e-5, 1e-6]

'''
for i in h:
    for j in range(0, 11):
        print('%3d %8.5e %5.3e %8.5e' 
        %(j, d.der_2(d.e, j, i)[0], i,
        abs(d.der_2(d.e, j, i)[0] - d.e(j))))
    print('\n')
'''



x = [1., 5., 10.]
error_1 = []
error_2 = []
error_3 = []
h_log = []
for i in h:
    error_1.append(-np.log(abs(d.der_2(d.e, x[0], i)[0]- d.e(x[0]))))
    error_2.append(-np.log(abs(d.der_2(d.e, x[1], i)[0]- d.e(x[1]))))
    error_3.append(-np.log(abs(d.der_2(d.e, x[2], i)[0]- d.e(x[2]))))   
    h_log.append(-np.log(i))

fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(11, 5), dpi=120)
plt.subplots_adjust(wspace=0.4, hspace=0.2)
plt.rcParams.update({'font.size': 8})           #type: ignore
plt.axis('equal')
axes[0].set_title('x = 1')
axes[0].plot(h_log, error_1, color='blue')                                #type: ignore
axes[0].set_xlabel(' neg log(h)')                    #type: ignore
axes[0].set_ylabel('neg log(pogreška)')                    #type: ignore
axes[0].grid(lw=0.5)                                             #type: ignore
axes[0].axis('tight') 
axes[1].set_title('x = 5')                                           #type: ignore
axes[1].plot(h_log, error_2, color='red')                                #type: ignore
axes[1].set_xlabel('neg log(h)')                    #type: ignore
axes[1].set_ylabel('neg log(pogreška)')                            #type: ignore
axes[1].grid(lw=0.5)                                             #type: ignore
axes[1].axis('tight') 
axes[2].set_title('x = 10')                                           #type: ignore
axes[2].plot(h_log, error_3, color='green')                                #type: ignore
axes[2].set_xlabel('neg log(h)')                    #type: ignore
axes[2].set_ylabel('neg log(pogreška)')                             #type: ignore
axes[2].grid(lw=0.5)                                             #type: ignore
axes[2].axis('tight')                                            #type: ignore
plt.show()
