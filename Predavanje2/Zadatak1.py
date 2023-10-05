import derivacija as d

h =[]
for i in range(-1, -7):
    h.append(1/10**i)

for i in h:
    for j in range(0, 11):
        print('\n%13.5e %13.5e %13.5e %d' 
        %(j, d.der_2(d.e, j, i), i,
        abs(d.der_2(d.e, j, i) - d.e(j))))

