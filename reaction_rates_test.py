import reaction_rates

# Q = m * X**3 + n * X**2 + p * X + q

# m = (alphaB * beta) * ro**2 * dt
# n = ro - (alpha + beta) * ro / (sigma * c) - alphaB * ro**2 * dt - 2 * beta * ro**2 * dt
# p = -ro * (1 + x) - Ngamma' - 1 / (sigma * c * dt) + beta * ro**2 * dt
# q = Ngamma' + ro * x + x / (sigma * c * dt)

# T, Ngamma, ro, x, dt

data = [[2.e3, 1.e0, 1.e0, 1.e-4, 1.e13], [2.e3, 1.e0, 1.e0, 1.e-1, 1.e13], [2.e3, 1.e-10, 1.e0, 1.e-4, 1.e13],
        [2.e4, 1.e-10, 1.e0, 1.e-4, 1.e13], [2.e8, 1.e-10, 1.e0, 1.e-4, 1.e13], [2.e4, 1.e0, 1.e0, 1.e-4, 1.e13],
        [2.e4, 1.e-2, 1.e-3, 1.e-4, 1.e13]]

# print(reaction_rates.Q_root(2e3, 1, 1, 1e-4, 1e13))

for i in range(7):
    print(reaction_rates.Q_root(data[i][0], data[i][1], data[i][2], data[i][3], data[i][4]))
