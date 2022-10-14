# Definition of function to iterate throughout the simulation
# Change function name for explicit/implicit ?
import pm
import numpy as np


def updt_N():
    pm.L_N1 = pm.L_N
    pm.L_N[pm.N - 1] += pm.dt / pm.dx * (pm.L_Ff1[pm.N - 1] - pm.L_Ff1[0])
    for i in range(pm.N - 1):
        pm.L_N[i] += pm.dt / pm.dx * (pm.L_Ff1[i] - pm.L_Ff1[i + 1])


def updt_P():
    pm.L_P1 = pm.L_P
    pm.L_P = pm.L_Xi * pm.L_N


def updt_F():
    pm.L_F1 = pm.L_F
    pm.L_F[pm.N - 1] += pm.c ** 2 * pm.dt / pm.dx * (pm.L_Pf1[pm.N - 1] - pm.L_Pf1[0])
    for i in range(pm.N - 1):
        pm.L_F[i] += pm.c ** 2 * pm.dt / pm.dx * (pm.L_Pf1[i] - pm.L_Pf1[i + 1])


def GLF_Pf():
    pm.L_Pf1 = pm.L_Pf
    for i in range(pm.N):
        pm.L_Pf[i] = 0.5 * (pm.L_P1[i - 1] + pm.L_P1[i]) - pm.c / 2 * (pm.L_F1[i] - pm.L_F1[i - 1])


def GLF_Ff():
    pm.L_Ff1 = pm.L_Ff
    for i in range(pm.N):
        pm.L_Ff[i] = 0.5 * (pm.L_F1[i - 1] + pm.L_F1[i]) - pm.c / 2 * (pm.L_N1[i] - pm.L_N1[i - 1])


def updt_Xi():
    pm.L_Xi1 = pm.L_Xi
    f = pm.L_F / (pm.c * pm.L_N)
    pm.L_Xi = (3 + 4 * f ** 2) / (5 + 2 * np.sqrt(4 - 3 * f ** 2))
