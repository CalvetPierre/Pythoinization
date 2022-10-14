# Definition of function to iterate throughout the simulation
# Change function name for explicit/implicit ?
from pm import *


def updt_N():
    L_N[N - 1] += dt / dx * (L_Ff[N - 1] - L_Ff[0])
    for i in range(N - 1):
        L_N[i] += dt / dx * (L_Ff[i] - L_Ff[i + 1])


def updt_P():
    L_P = L_Xi * L_N


def updt_F():
    L_F[N - 1] += c ** 2 * dt / dx * (L_Pf[N - 1] - L_Pf[0])
    for i in range(N - 1):
        L_F[i] += c ** 2 * dt / dx * (L_Pf[i] - L_Pf[i + 1])


def GLF_Pf():
    for i in range(N):
        L_Pf[i] = 0.5 * (L_P[i - 1] + L_P[i]) - c / 2 * (L_F[i] - L_F[i - 1])


def GLF_Ff():
    for i in range(N):
        L_Ff[i] = 0.5 * (L_F[i - 1] + L_F[i]) - c / 2 * (L_N[i] - L_N[i - 1])


def updt_Xi():
    f = L_F / (c * L_N)
    L_Xi = (3 + 4 * f ** 2) / (5 + 2 * np.sqrt(4 - 3 * f ** 2))
