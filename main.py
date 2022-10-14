import numpy as np
import matplotlib.pyplot as plt

N = 10
A = np.ones(N)
plt.plot(A)
plt.show()



import numpy as np
import matplotlib.pyplot as plt

from scipy import constants as sc

# Initialization system in 1D

N = 100 # Nombre de cellules
L = sc.au*10e-10 # Taille physique de l'ensemble des cellules
dx = L/N # Taille d'une cellule
tf = 10*sc.minute # Temps total de la simulation
nt = 10000 # Nombre d'itérations
dt=tf/nt # Pas de temps

c = 8

# Courant Condition
print(3*c*dt/dx)
if 3*c*dt/dx >= 1:
    print("Courant condition not respected !")
    
# List (L_), Ff for (F)lux at (f)rontier
L_N, L_F, L_Ff, L_P, L_Pf, L_Xi = np.zeros(N), np.zeros(N), np.zeros(N), np.zeros(N), np.zeros(N), np.zeros(N)

# Definition of function to iterate throughout the simulation
# Change function name for explicite/implicite ?

def Updt_N():
    global L_N, L_Ff
    for i in range(N-1):
        L_N[i] += dt/dx * (L_Ff[i] - L_Ff[i+1])
        
    L_N[N-1] += dt/dx * (L_Ff[N-1] - L_Ff[0])

    
def Updt_P():
    global L_N, L_P, L_Xi
    L_P = L_Xi * L_N
    
    
def Updt_F():
    global L_F, L_Pf
    for i in range(N-1):
        L_F[i] += c**2 * dt/dx * (L_Pf[i] - L_Pf[i+1])
        
    L_F[N-1] += c**2 * dt/dx * (L_Pf[N-1] - L_Pf[0])

    
def GLF_Pf():
    global L_F, L_P, L_Pf
    for i in range(N):
        L_Pf[i] = 0.5 * (L_P[i-1] + L_P[i]) - c/2 * (L_F[i] - L_F[i-1])

        
def GLF_Ff():
    global L_N, L_F, L_Ff
    for i in range(N):
        L_Ff[i] = 0.5 * (L_F[i-1] + L_F[i]) - c/2 * (L_N[i] - L_N[i-1])

        
def Updt_Xi():
    global L_N, L_F, L_Xi
    f = L_F / (c * L_N)
    #print("Ici c'est :", L_N)
    L_Xi = (3 + 4 * f**2) / (5 + 2 * np.sqrt(4 - 3 * f**2))
    
t = 0
# List (L_), Ff for (F)lux at (f)rontier
#L_N, L_F, L_Ff, L_P, L_Pf, L_Xi = np.zeros(N), np.zeros(N), np.zeros(N), np.zeros(N), np.zeros(N), np.zeros(N)
global L_N
L_N = np.ones(N) / 1000
L_N[50] += 10

while t < tf :
    t += dt
    
    GLF_Ff()
    Updt_N()
    Updt_Xi()
    Updt_P()
    GLF_Pf()
    Updt_F()
    
    # Stockage / Plot
    print(t/tf)
    plt.plot(L_N)
    plt.ylim(0, 10)
    plt.show()
    #print("\n L_Ff", L_Ff)
    #print("\n L_N",L_N)
    #print("\n L_Xi",L_Xi)
    #print("\n L_P",L_P)
    #print("\n L_Pf",L_Pf)
    #print("\n L_F",L_F)

    
print("\n Fini !")


