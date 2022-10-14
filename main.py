import numpy as np
import matplotlib.pyplot as plt
from scipy import constants as sc
import func
from pm import *

# Courant Condition
print("Courant value :", 3 * c * dt / dx)
if 3 * c * dt / dx >= 1:
    print("Courant condition not respected !")

t = 0
while t < tf:
    t += dt

    func.GLF_Ff()
    func.updt_N()
    func.updt_Xi()
    func.updt_P()
    func.GLF_Pf()
    func.updt_F()

    # Stock / Plot
    print(t / tf)
    plt.plot(L_N)
    plt.ylim(0, 10)
    if t % 0.01:
        plt.show()
    # print("\n L_Ff", L_Ff)
    # print("\n L_N",L_N)
    # print("\n L_Xi",L_Xi)
    # print("\n L_P",L_P)
    # print("\n L_Pf",L_Pf)
    # print("\n L_F",L_F)

print("\n End !")
