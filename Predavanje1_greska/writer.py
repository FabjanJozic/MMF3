import Zadatak1 as zad
import numpy as np
import os.path


limit1 = 1e-10
limit2 = 1e-15


with open('C:\\Users\\Fabo\\Desktop\\programi\\MMF3\\Predavanje1\\tablica1.txt','w') as f:
    f.writelines("%19s %19s %19s %19s %19s %19s %19s %19s %19s" %('vrijednost x', 'exp(-x) red', 'broj iteracija', 'exp(-x) rekurzivna',
                                                                  'broj iteracija', 'exp(-x) inverz', 'broj iteracija', 'exp(-x)', 'epsilon'))
    f.write('\n')
    for i in range(0, 11):
        i *= 10
        f.writelines("\n%+19d %+19.8e %+19d %+19.8e %+19d %+19.8e %+19d %+19.8e %+19.8e" %(i, zad.exp_red(i, limit1)[0],
                                                                zad.exp_red(i, limit1)[1], zad.exp_rek(i, limit1)[0], zad.exp_rek(i, limit1)[1],
                                                                zad.exp_rec(i, limit1)[0], zad.exp_rec(i, limit1)[1], np.exp(-i), limit1))
    f.write('\n')
    for i in range(0, 11):
        i *= 10
        f.writelines("\n%+19d %+19.8e %+19d %+19.8e %+19d %+19.8e %+19d %+19.8e %+19.8e" %(i, zad.exp_red(i, limit2)[0],
                                                                zad.exp_red(i, limit2)[1], zad.exp_rek(i, limit2)[0], zad.exp_rek(i, limit2)[1],
                                                                zad.exp_rec(i, limit2)[0], zad.exp_rec(i, limit2)[1], np.exp(-i), limit2))   
    f.close()

'''with open('tablica1.txt', 'r') as fp1, \
    open('C:\\Users\\Fabo\\Desktop\\programi\\MMF3\\Predavanje1\\tablica1.txt', 'w') as fp2:
        results = fp1.read()
        fp2.write(results)'''