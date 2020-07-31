from ODESolver import RungeKutta4
import numpy as np
import matplotlib.pyplot as plt

def SIR_model(u,t):
    beta = 0.001
    nu = 1/7.0
    S, I, R = u[0], u[1], u[2]
    dS = -beta*S*I
    dI = beta*S*I - nu*I
    dR = nu*I
    return [dS,dI,dR]

S0 = 1000
I0 = 1
R0 = 0

solver= RungeKutta4(SIR_model)
solver.set_initial_condition([S0,I0,R0])
time_points = np.linspace(0, 100, 101)
u, t = solver.solve(time_points)
S = u[:,0];  I = u[:,1]; R = u[:,2]

plt.plot(t,S,t,I,t,R)
plt.show()
