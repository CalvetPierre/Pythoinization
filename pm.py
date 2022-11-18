import numpy as np
from scipy import constants as sc


# Initialization of global variable
def init():
    global N, L, dx, tf, nt, dt, c
    N = 100  # Number of cell
    L = sc.au  # Physical size of all the cell
    dx = L / N  # Size of one cell
    tf = 10 * sc.minute  # Total time of the simulation
    nt = 1000  # Number of iteration
    dt = tf / nt  # Time step
    c = sc.c  # Light speed
    # sc.parsec


    # List (L_), Ff for (F)lux at (f)frontier
    global L_N, L_F, L_Ff, L_P, L_Pf, L_Xi
    L_N, L_F, L_Ff, L_P, L_Pf, L_Xi = np.zeros(N), np.zeros(N), np.zeros(N), np.zeros(N), np.zeros(N), np.zeros(N)

    L_N = np.ones(N) / 1000

    # List that will be used to save the last value of given list
    global L_N1, L_F1, L_Ff1, L_P1, L_Pf1, L_Xi1
    L_N1, L_F1, L_Ff1, L_P1, L_Pf1, L_Xi1 = np.zeros(N), np.zeros(N), np.zeros(N), np.zeros(N), np.zeros(N), np.zeros(N)

    L_N1 = np.ones(N) / 1000

    global T, L_x
    T = 2e4
    L_x = np.ones(N) * 0.0012
