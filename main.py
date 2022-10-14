import matplotlib.pyplot as plt
import pm
import func

pm.init()

# Courant Condition
print("Courant value :", 3 * pm.c * pm.dt / pm.dx)
if 3 * pm.c * pm.dt / pm.dx >= 1:
    print("Courant condition not respected !")

t = 0
while t < pm.tf:
    t += pm.dt

    func.GLF_Ff()
    func.updt_N()
    func.updt_Xi()
    func.updt_P()
    func.GLF_Pf()
    func.updt_F()

    # Stock / Plot
    print(t / pm.tf)
    plt.plot(pm.L_N)
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
