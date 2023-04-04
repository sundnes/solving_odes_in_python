"""
Class implementation of the SIR model. The model is mostly
the same as the one in SIR_class_v1.py, but immunity is
lost after a while. The loss of immunity is modeled as
a slow leak of people from the R category back to S.
"""
from ODESolver import RungeKutta4
import numpy as np
import matplotlib.pyplot as plt

class SIR:
    def __init__(self, beta, nu, gamma):
        self.beta = beta
        self.nu = nu
        self.gamma = gamma

    def __call__(self,u,t):
        S, I, R = u[0], u[1], u[2]
        dS = -self.beta*S*I + self.gamma*R
        dI = self.beta*S*I - self.nu*I
        dR = self.nu*I - self.gamma*R
        return [dS,dI,dR]



S0 = 1000
I0 = 1
R0 = 0

model = SIR(beta=0.001, nu=1/7.0, gamma = 1.0/50)
solver= RungeKutta4(model)
solver.set_initial_condition([S0,I0,R0])
time_points = np.linspace(0, 100, 101)
u, t = solver.solve(time_points)
S = u[:,0];  I = u[:,1]; R = u[:,2]

plt.plot(t,S,t,I,t,R)
plt.show()
