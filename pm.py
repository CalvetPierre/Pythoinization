import numpy as np
from scipy import constants as sc

# Initialization of global variable

global N, L, dx, tf, nt, dt, c
N = 100  # Number of cell
L = sc.au * 10e-10  # Physical size of all the cell
dx = L / N  # Size of one cell
tf = 10 * sc.minute  # Total time of the simulation
nt = 10000  # Number of iteration
dt = tf / nt  # Time step
c = 8  # Light speed

# List (L_), Ff for (F)lux at (f)rontier
global L_N, L_F, L_Ff, L_P, L_Pf, L_Xi
L_N, L_F, L_Ff, L_P, L_Pf, L_Xi = np.zeros(N), np.zeros(N), np.zeros(N), np.zeros(N), np.zeros(N), np.zeros(N)

L_N = np.ones(N) / 1000
L_N[50] += 10
