from ODESolver import RungeKutta4
import numpy as np
import matplotlib.pyplot as plt

class SEIR:
    def __init__(self, beta, mu, nu, gamma):
        self.beta = beta
        self.mu = mu
        self.nu = nu
        self.gamma = gamma

    def __call__(self, t, u):
        S, E, I, R = u
        N = S + I + R + E
        dS = -self.beta * S * I / N + self.gamma * R
        dE = self.beta * S * I / N - self.mu * E
        dI = self.mu * E - self.nu * I
        dR = self.nu * I - self.gamma * R
        return [dS, dE, dI, dR]


S0 = 1000
E0 = 0
I0 = 1
R0 = 0
model = SEIR(beta=1.0, mu=1.0 / 5, nu=1.0 / 7, gamma=1.0 / 50)

solver = RungeKutta4(model)
solver.set_initial_condition([S0, E0, I0, R0])
t_span = (0, 100)
t, u = solver.solve(t_span, N=101)

S = u[:, 0]
E = u[:, 1]
I = u[:, 2]
R = u[:, 3]

plt.plot(t, S, t, E, t, I, t, R)
plt.show()
