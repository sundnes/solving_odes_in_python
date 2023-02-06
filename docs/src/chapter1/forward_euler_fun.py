"""
Implementation of the ForwardEuler method as a function.
"""
import numpy as np
import matplotlib.pyplot as plt


def ForwardEuler(f, U0, T, N):
    """Solve u'=f(u,t), u(0)=U0, with n steps until t=T."""
    import numpy as np
    t = np.zeros(N+1)
    u = np.zeros(N+1)  # u[n] is the solution at time t[n]

    u[0] = U0
    t[0] = 0
    dt = T/N

    for n in range(N):
        t[n+1] = t[n] + dt
        u[n+1] = u[n] + dt*f(u[n], t[n])

    return u, t

#demo: solve u' = u, u(0) = 1
def f(u, t):
    return u

U0 = 1
T = 3
N = 30
u, t = ForwardEuler(f, U0, T, N)
plt.plot(t,u)
plt.show()
