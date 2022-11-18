# Definition of function to iterate throughout the simulation
# Change function name for explicit/implicit ?
import pm
import numpy as np
import reaction_rates


def GLF():
    pm.L_Pf1 = pm.L_Pf
    pm.L_Ff1 = pm.L_Ff
    for i in range(pm.N):
        pm.L_Pf[i] = 0.5 * (pm.L_P[i - 1] + pm.L_P[i]) - pm.c / 2 * (pm.L_F[i] - pm.L_F[i - 1])
        pm.L_Ff[i] = 0.5 * (pm.L_F[i - 1] + pm.L_F[i]) - pm.c / 2 * (pm.L_N[i] - pm.L_N[i - 1])


def updt_N(meth):
    if meth == "exp":  # TODO
        pm.L_N[pm.N - 1] += pm.dt / pm.dx * (pm.L_Ff1[pm.N - 1] - pm.L_Ff1[0])
        pm.L_N[pm.N - 1] = reaction_rates.updt_Ngamma(pm.T, pm.L_N[pm.N - 1], 3, pm.L_x[pm.N - 1], pm.dt)
        pm.L_x[pm.N - 1] = reaction_rates.Q_root(pm.T, pm.L_N[pm.N - 1], 3, pm.L_x[pm.N - 1], pm.dt)
        # print(pm.L_x[40])
        # + reaction_rates.updt_Ngamma(T,pm.L_N[pm.N - 1], ro, x, pm.dt)
        for i in range(pm.N - 1):
            pm.L_N[i] += pm.dt / pm.dx * (pm.L_Ff1[i] - pm.L_Ff1[i + 1])
            pm.L_N[i] = reaction_rates.updt_Ngamma(pm.T, pm.L_N[i], 300, pm.L_x[pm.N - 1], pm.dt)
            pm.L_x[i] = reaction_rates.Q_root(pm.T, pm.L_N[i], 300, pm.L_x[i], pm.dt)




    '''
    if meth == "imp":
        print(1)
        pm.L_N[pm.N - 1] += pm.dt / pm.dx * (pm.L_Ff[pm.N - 1] - pm.L_Ff[0]) * 1
        for i in range(pm.N - 1):
            pm.L_N[i] += pm.dt / pm.dx * (pm.L_Ff[i] - pm.L_Ff[i + 1])'''


def updt_P():
    pm.L_P = pm.L_Xi * pm.L_N * pm.c ** 2


def updt_F(meth):
    if meth == "exp":
        # pm.L_F1 = pm.L_F 1
        pm.L_F[pm.N - 1] += pm.dt / pm.dx * (pm.L_Pf1[pm.N - 1] - pm.L_Pf1[0])
        for i in range(pm.N - 1):
            pm.L_F[i] += pm.dt / pm.dx * (pm.L_Pf1[i] - pm.L_Pf1[i + 1])

    '''
    if meth == "imp":
        print(2)
         # pm.L_F1 = pm.L_F
        pm.L_F[pm.N - 1] += pm.dt / pm.dx * (pm.L_Pf[pm.N - 1] - pm.L_Pf[0])
        for i in range(pm.N - 1):
            pm.L_F[i] += pm.dt / pm.dx * (pm.L_Pf[i] - pm.L_Pf[i + 1]) '''


def updt_Xi():
    f = pm.L_F / (pm.c * pm.L_N)
    pm.L_Xi = (3 + 4 * f ** 2) / (5 + 2 * np.sqrt(4 - 3 * f ** 2))
