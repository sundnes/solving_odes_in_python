from ImplicitRK import *
import numpy as np
import matplotlib.pyplot as plt
from vanderpol import VanderPol
from scipy.integrate import solve_ivp


fig = plt.figure(figsize=(6.4,8.4))
gs = fig.add_gridspec(6, hspace=0.5)
axs = gs.subplots(sharex=True, sharey=False)

mu = 10
model = VanderPol(mu=mu)
solvers = [BackwardEuler(model), SDIRK2(model),TR_BDF2(model),Radau2(model),Radau3(model)]
solver_names = ['BackwardEuler','SDIRK2','TR2_BDF2','Radau2','Radau3']

T = 20
t_span = (0,T)
u0 = [1,0]
rtol=1e-10
solution = solve_ivp(model, t_span, u0,rtol=rtol)
axs[0].plot(solution.t, solution.y[0,:])
axs[0].plot(solution.t, solution.y[1,:])
axs[0].set(title ='Reference solution')

for i, solver in enumerate(solvers):
    solver.set_initial_condition([1,0])
    N = 200
    t,u  = solver.solve(t_span=(0,20),N=N)
    axs[i+1].plot(t, u)
    axs[i+1].set(title =f'{solver_names[i]}, $\Delta t$ = {T/N:g}')
plt.show()
