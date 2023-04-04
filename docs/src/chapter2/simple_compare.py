import numpy as np
import matplotlib.pyplot as plt
from ODESolver import ForwardEuler, ExplicitMidpoint, RungeKutta4

def f(t,u):
    return u

t_span = (0,3) 
N = 6

fe = ForwardEuler(f)
fe.set_initial_condition(u0=1)
t1, u1 = fe.solve(t_span,N)
plt.plot(t1, u1, label='Forward Euler')

em = ExplicitMidpoint(f)
em.set_initial_condition(u0=1)
t2, u2 = em.solve(t_span,N)
plt.plot(t2, u2, label='Explicit Midpoint')

rk4 = RungeKutta4(f)
rk4.set_initial_condition(u0=1)
t3, u3 = rk4.solve(t_span,N)
plt.plot(t3, u3, label='Runge-Kutta 4')

#plot the exact solution in the same plot
time_exact = np.linspace(0,3,301) 
plt.plot(time_exact,np.exp(time_exact),label='Exact')
plt.title('RK solvers for exponential growth, $\Delta t = 0.5$')
plt.xlabel('$t$')
plt.ylabel('$u(t)$')
plt.legend()
plt.show()