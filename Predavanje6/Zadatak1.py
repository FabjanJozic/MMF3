import interpolacija as inter

with open('C:\\Users\\Fabo\\Desktop\\programi\\MMF3\\Predavanje6\\V(H-H).txt','r') as read:
    linija = read.readlines()
    mod_linija = []
    for i in linija:
        col1, col2 = i.strip().split('   ')
        mod_col1 = float(col1)*0.52917721092 #pretvara u amstreme
        mod_col2 = float(col2)*315775.04 #pretvara u kelvine
        mod_i = f"{mod_col1}\t{mod_col2}\n"
        mod_linija.append(mod_i)

with open('C:\\Users\\Fabo\\Desktop\\programi\\MMF3\\Predavanje6\\V(H-H)_AK.txt','w') as write:
    write.writelines(mod_linija)

