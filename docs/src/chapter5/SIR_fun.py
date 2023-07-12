from ODESolver import RungeKutta4
import numpy as np
import matplotlib.pyplot as plt


def SIR_model(t, u):
    beta = 0.001
    nu = 1 / 7.0
    S, I, R = u[0], u[1], u[2]
    dS = -beta * S * I
    dI = beta * S * I - nu * I
    dR = nu * I
    return [dS, dI, dR]


S0 = 1000
I0 = 1
R0 = 0

solver = RungeKutta4(SIR_model)
solver.set_initial_condition([S0, I0, R0])
t_span = (0, 100)
t, u = solver.solve(t_span, N=101)
S = u[:, 0]
I = u[:, 1]
R = u[:, 2]

plt.plot(t, S, t, I, t, R)
plt.show()
