import matplotlib.pyplot as plt
import pm
import func

pm.init()

# Courant Condition
print("Courant value :", 3 * pm.c * pm.dt / pm.dx)
if 3 * pm.c * pm.dt / pm.dx >= 1:
    print("Courant condition not respected !")

t = 0
# Method Explicit (meth = "exp") or Implicit (meth = "imp")
meth = "exp"
while t < pm.tf:
    t += pm.dt

    func.GLF()
    func.updt_N(meth)
    func.updt_Xi()
    func.updt_P()
    func.updt_F(meth)

    # Stock / Plot
    print(t / pm.tf)
    plt.plot(pm.L_N)
    plt.ylim(0, 10)

plt.show()

print("\n End !")
