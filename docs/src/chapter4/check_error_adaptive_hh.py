"""
The code solves the Hodgkin-Huxley model with the
RKF45, Euler-Heun, and TR-BDF2 adaptive RK solvers.
The global error is estimated by comparing to a
reference solution computed by solve_ivp.
The tolerance, global error and number of steps
are printed to the terminal.
"""

from AdaptiveImplicitRK import *
from hodgkinhuxley import *
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

import numpy as np


def rhs(t, u):
    return u


def exact(t):
    return np.exp(t)


solvers = {'TR-BDF2': [TR_BDF2_Adaptive, 2],
           'RKF45': [RKF45, 4],
           'EulerHeun': [EulerHeun, 1],
           }


model = HodgkinHuxley()
u0 = [-45, 0.31, 0.05, 0.59]
t_span = (0, 50)

ref_sol = solve_ivp(model, t_span, u0, rtol=1e-10, atol=1e-12)
t_ref, u_ref = ref_sol.t, ref_sol.y

for solver_name, (solver_class, order) in solvers.items():
    solver = solver_class(model)
    solver.set_initial_condition(u0)

    print(f'{solver_name} order = {order}')
    print(f'Tolerance  Global error  Number of steps')
    for tol in [1.0, 0.1, 0.01]:
        t, u = solver.solve(t_span, tol)
        steps = len(t)
        e = abs(u[-1, 0] - u_ref[0, -1])
        print(f'{tol:<8.3f}   {e:<12.7f}  {steps}')
