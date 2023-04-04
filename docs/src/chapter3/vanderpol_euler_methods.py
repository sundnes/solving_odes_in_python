"""
Solve the Van der Pol model with forward and backward
Euler methods, and a reference solution with the
solve_ivp function and a low tolerance. 
With the chosen time step both methods solve the model,
but forward Euler gives spurious oscillations, and
the backward Euler solution is stable but inaccurate. 
"""

from ImplicitRK import *
import numpy as np
import matplotlib.pyplot as plt
from vanderpol import VanderPol
from scipy.integrate import solve_ivp


fig = plt.figure()
gs = fig.add_gridspec(3, hspace=0.5)
axs = gs.subplots(sharex=True, sharey=False)

mu = 10
model = VanderPol(mu=mu)
solvers = [ForwardEuler(model),BackwardEuler(model)]
solver_names = ['ForwardEuler','BackwardEuler']

T = 20
t_span = (0,T)
u0 = [1,0]
rtol = 1e-10
solution = solve_ivp(model, t_span, u0, rtol=rtol)
axs[0].plot(solution.t, solution.y[0,:])
axs[0].plot(solution.t, solution.y[1,:])
axs[0].set(title ='Reference solution')

for i, solver in enumerate(solvers):
    solver.set_initial_condition([1,0])
    N = 500
    t,u  = solver.solve(t_span=(0,20),N=N)
    axs[i+1].plot(t, u)
    axs[i+1].set(title =f'{solver_names[i]}, $\Delta t$ = {T/N:g}')

plt.show()
