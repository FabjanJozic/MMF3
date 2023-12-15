import diferencijalne_jednadzbe as dj
import matplotlib.pyplot as plt 

X0 = [0.0, 0.0, 0.0] #pocetni uvjeti
m = 4.7 #masa
F = 5.2 #sila
k = 400
def idi(Y): #funkcija alceleracije
    return F/m
N = 6000
tN = 3.2 #krajnje vrijeme gibanja

t, x, v, a = dj.Euler_n(X0, idi, N, tN)[0], dj.Euler_n(X0, idi, N, tN)[1], dj.Euler_n(X0, idi, N, tN)[2], dj.Euler_n(X0, idi, N, tN)[3]

fig = plt.figure(figsize=(11,5), dpi=110)
axes = fig.add_axes([0.15, 0.15, 0.75, 0.70])
plt.rcParams.update({'font.size': 9})           #type: ignore
axes.plot(t, x, color='blue', label='put')
axes.plot(t, v, color='green', label='brzina')
axes.plot(t, a, color='red', label='akceleracija')
axes.grid(lw=0.5)
axes.legend(loc='best')
plt.show()

