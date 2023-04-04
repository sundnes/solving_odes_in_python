from forward_euler_class import *
import numpy as np


def rhs(t, u):
    return u


def exact(t):
    return np.exp(t)


solver = ForwardEuler(rhs)
solver.set_initial_condition(1.0)

T = 3.0
t_span = (0, T)
N = 30

print(f'Time step (dt)   Error (e)        e/dt')
for _ in range(10):
    t, u = solver.solve(t_span, N)
    dt = T / N
    e = abs(u[-1] - exact(T))
    print(f'{dt:<14.7f}   {e:<14.7f}   {e/dt:5.4f}')
    N = N * 2
