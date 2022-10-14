# Definition of function to iterate throughout the simulation
# Change function name for explicit/implicit ?
import pm
import numpy as np


def updt_N():
    # pm.L_N1 = pm.L_N
    pm.L_N[pm.N - 1] += pm.dt / pm.dx * (pm.L_Ff[pm.N - 1] - pm.L_Ff[0])
    for i in range(pm.N - 1):
        pm.L_N[i] += pm.dt / pm.dx * (pm.L_Ff[i] - pm.L_Ff[i + 1])


def updt_P():
    # pm.L_P1 = pm.L_P
    pm.L_P = pm.L_Xi * pm.L_N * pm.c**2


def updt_F():
    # pm.L_F1 = pm.L_F
    pm.L_F[pm.N - 1] += pm.dt / pm.dx * (pm.L_Pf[pm.N - 1] - pm.L_Pf[0])
    for i in range(pm.N - 1):
        pm.L_F[i] += pm.dt / pm.dx * (pm.L_Pf[i] - pm.L_Pf[i + 1])


def GLF_Pf():
    # pm.L_Pf1 = pm.L_Pf
    for i in range(pm.N):
        pm.L_Pf[i] = 0.5 * (pm.L_P[i - 1] + pm.L_P[i]) - pm.c / 2 * (pm.L_F[i] - pm.L_F[i - 1])


def GLF_Ff():
    # pm.L_Ff1 = pm.L_Ff
    for i in range(pm.N):
        pm.L_Ff[i] = 0.5 * (pm.L_F[i - 1] + pm.L_F[i]) - pm.c / 2 * (pm.L_N[i] - pm.L_N[i - 1])


def updt_Xi():
    # pm.L_Xi1 = pm.L_Xi
    f = pm.L_F / (pm.c * pm.L_N)
    pm.L_Xi = (3 + 4 * f ** 2) / (5 + 2 * np.sqrt(4 - 3 * f ** 2))
