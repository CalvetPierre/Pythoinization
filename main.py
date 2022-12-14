import matplotlib.pyplot as plt
import numpy as np
from imageio.plugins import pillow

import pm
import func
from matplotlib.animation import FuncAnimation
from matplotlib.animation import PillowWriter

pm.init()

# Courant Condition
print("Courant value :", 3 * pm.c * pm.dt / pm.dx)
if 3 * pm.c * pm.dt / pm.dx >= 1:
    print("Courant condition not respected !")
    print("STOP HERE")

t = 0
# Method Explicit (meth = "exp") or Implicit (meth = "imp")
meth = "exp"

# To count nb of step
i = 0

# Storage of N values
N_temp = []
while t < pm.tf/10:
    i += 1
    t += pm.dt
    pm.L_N[50] += 10000
    func.GLF()
    func.updt_N(meth)
    func.updt_Xi()
    func.updt_P()
    func.updt_F(meth)

    # Stock / Plot
    plt.figure(4)
    plt.plot(pm.L_N)
    plt.ylim(0, 10)

    plt.figure(5)
    plt.plot(pm.L_x)
    plt.ylim(0, 1.2)

    # Storage of N each 20 time step

    if i % 10 == 0:
        N_temp.append(pm.L_N.tolist())
        print(t / pm.tf)

plt.show()

# print(np.shape(N_temp))
# print(N_temp[1])
# print(len(N_temp))
plt.figure(1)
for i in range(len(N_temp)):
    plt.plot(N_temp[i])
plt.show()

fig = plt.figure(3)

axis = plt.axes(xlim=(0, 100),
                ylim=(0, 6))

# initializing a line variable
line, = axis.plot([], [], lw=3)


# data which the line will
# contain (x, y)
def init():
    line.set_data([], [])
    return line,


def animate(i):
    x = np.linspace(0, 99, 100)

    # plots a sine graph
    y = np.array(N_temp[i])
    line.set_data(x, y)
    # TODO plot speed of the front wave
    # See : https://www.geeksforgeeks.org/matplotlib-animate-multiple-lines/
    # line.set_data(np.array([50+i*pm.c*pm.dt/pm.dx]*2), np.array([0, 4]))
    # here doesn't work logically

    return line,


# Following comment is to store animation in a gif

anim = FuncAnimation(fig, animate,
                     init_func=init,
                     frames=200,
                     interval=20,
                     blit=True)

writer = PillowWriter(fps=30)
anim.save('animation.gif', writer=writer)


print("\n End !")
