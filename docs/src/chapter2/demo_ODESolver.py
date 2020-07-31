"""
Simple demo to illustrate the usage of the ODESolver class hhierarchy
and show the difference in accuracy between the methods.
"""
import numpy as np
import matplotlib.pyplot as plt
from ODESolver_scalar import ForwardEuler, ExplicitMidpoint, RungeKutta4

def f(u, t):
    return u

time_points = np.linspace(0, 3, 11)

fe = ForwardEuler(f)
fe.set_initial_condition(U0=1)
u1, t1 = fe.solve(time_points)
plt.plot(t1, u1, label='Forward Euler')

em = ExplicitMidpoint(f)
em.set_initial_condition(U0=1)
u2, t2 = em.solve(time_points)
plt.plot(t2, u2, label='Explicit Midpoint')

rk4 = RungeKutta4(f)
rk4.set_initial_condition(U0=1)
u3, t3 = rk4.solve(time_points)
plt.plot(t3, u3, label='RungeKutta 4')

#plot the exact solution in the same plot
time_exact = np.linspace(0,3,301) #more points to improve the plot
plt.plot(time_exact,np.exp(time_exact),label='Exact')

plt.legend()
plt.show()
