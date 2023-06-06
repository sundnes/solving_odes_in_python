from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as plt
from pendulum import Pendulum

problem = Pendulum(L=1)
t_span = (0, 10.0)
u0 = (np.pi / 4, 0)

# optional arguments to solve_ivp:
#t_eval = np.linspace(0,10.0,1001)
#rtol = 1e-6

solution = solve_ivp(problem, t_span, u0)

plt.plot(solution.t, solution.y[0, :], label=r'$\theta$')
plt.plot(solution.t, solution.y[1, :], label=r'$\omega$')

solution = solve_ivp(problem, t_span, u0, rtol=1e-10)
plt.plot(solution.t, solution.y[0, :], ':')
plt.plot(solution.t, solution.y[1, :], ':')

plt.title(f'Pendulum problem, SciPy solve_ivp')
plt.xlabel('t')
plt.ylabel(r'Angle ($\theta$) and angular velocity ($\omega$)')
plt.legend()
plt.show()
