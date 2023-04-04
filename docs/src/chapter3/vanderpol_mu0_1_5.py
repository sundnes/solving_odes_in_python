from ImplicitRK import *
import numpy as np
import matplotlib.pyplot as plt
from vanderpol import VanderPol


fig = plt.figure()
gs = fig.add_gridspec(3, hspace=0.5)
axs = gs.subplots(sharex=True, sharey=False)
#fig, axs = plt.subplots(3, sharex=True, sharey=False)
for i, mu in enumerate([0, 1, 5]):
    model = VanderPol(mu=mu)

    solver = Radau3(model)
    solver.set_initial_condition([1, 0])

    t_span = (0, 20)
    t, u = solver.solve(t_span=(0, 20), N=100)
    axs[i].plot(t, u)
    axs[i].set(title=f'$\\mu={mu}$')
plt.show()
