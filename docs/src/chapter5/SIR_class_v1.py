"""
Class implementation of the SIR model. The model is exactly the
same as the function implementation in SIR_fun.py, but the
class implementation is more convenient for varying parameters.
"""


from ODESolver import RungeKutta4
import numpy as np
import matplotlib.pyplot as plt


class SIR:
    def __init__(self, beta, nu):
        self.beta = beta
        self.nu = nu

    def __call__(self, t, u):
        S, I, R = u[0], u[1], u[2]
        dS = -self.beta * S * I
        dI = self.beta * S * I - self.nu * I
        dR = self.nu * I
        return [dS, dI, dR]


S0 = 1000
I0 = 1
R0 = 0

model = SIR(beta=0.001, nu=1 / 7.0)
solver = RungeKutta4(model)
solver.set_initial_condition([S0, I0, R0])
t_span = (0, 100)
t, u = solver.solve(t_span, N=101)
S = u[:, 0]
I = u[:, 1]
R = u[:, 2]

plt.plot(t, S, t, I, t, R)
plt.legend(['S', 'I', 'R'])
plt.xlabel('Time (days)')
plt.ylabel('Number of people')
plt.savefig('SIR_simple.pdf')
plt.show()
