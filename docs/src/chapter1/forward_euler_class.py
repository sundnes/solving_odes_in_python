"""
Forward Euler class implementation for systems of ODEs.
"""

import numpy as np


class ForwardEuler:
    def __init__(self, f):
        self.f = lambda t, u: np.asarray(f(t, u), float)

    def set_initial_condition(self, u0):
        self.u0 = np.asarray(u0)
        self.neq = self.u0.size

    def solve(self, t_span, N):
        """Compute solution for
        t_span[0] <= t <= t_span[1],
        using N steps."""
        t0, T = t_span
        self.dt = (T - t0) / N
        self.t = np.zeros(N + 1)
        self.u = np.zeros((N + 1, self.neq))

        msg = "Please set initial condition before calling solve"
        assert hasattr(self, "u0"), msg

        self.t[0] = t0
        self.u[0] = self.u0

        for n in range(N):
            self.n = n
            self.t[n + 1] = self.t[n] + self.dt
            self.u[n + 1] = self.advance()
        return self.t, self.u

    def advance(self):
        """Advance the solution one time step."""
        u, dt, f, n, t = self.u, self.dt, self.f, self.n, self.t
        return  u[n] + dt * f(t[n], u[n])

class Logistic:
    def __init__(self, alpha, R):
        self.alpha, self.R = alpha, R

    def __call__(self, t, u):
        return self.alpha * u * (1 - u / self.R)


if __name__ == '__main__':
    """
    Demonstrate how the class is used,
    by solving the logistic growth problem.
    To test the class for a system of ODEs,
    run pendulum.py
    """
    import matplotlib.pyplot as plt

    problem = Logistic(alpha=0.2, R=1.0)
    solver = ForwardEuler(problem)
    u0 = 0.1
    solver.set_initial_condition(u0)

    T = 40
    t, u = solver.solve(t_span=(0, T), N=400)

    plt.plot(t, u)
    plt.title('Logistic growth, Forward Euler')
    plt.xlabel('t')
    plt.ylabel('u')
    plt.show()
