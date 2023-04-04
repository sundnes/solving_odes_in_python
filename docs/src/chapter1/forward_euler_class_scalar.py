"""
First version of the Forward Euler class implementation,
including a class implementation of the logistic
growth model.
"""
import numpy as np


class ForwardEuler_v0:
    def __init__(self, f):
        self.f = f  # , self.U0, self.T, self.N = f, U0, T, N

    def set_initial_condition(self, u0):
        self.u0 = u0

    def solve(self, t_span, N):
        """Compute solution for t_span[0] <= t <= t_span[1],
        using N steps."""
        t0, T = t_span
        self.dt = T / N
        self.t = np.zeros(N + 1)  # N steps ~ N+1 time points
        self.u = np.zeros(N + 1)

        self.t[0] = t0
        self.u[0] = self.u0

        for n in range(N):
            self.n = n
            self.t[n + 1] = self.t[n] + self.dt
            self.u[n + 1] = self.advance()
        return self.t, self.u

    def advance(self):
        """Advance the solution one time step."""
        # Create local variables to get rid of "self." in
        # the numerical formula
        u, dt, f, n, t = self.u, self.dt, self.f, self.n, self.t

        unew = u[n] + dt * f(t[n], u[n])
        return unew


class Logistic:
    def __init__(self, alpha, R, u0):
        self.alpha, self.R, self.u0 = alpha, float(R), u0

    def __call__(self, t, u):
        return self.alpha * u * (1 - u / self.R)


if __name__ == '__main__':
    """
    Demonstrate how the class the class is used,
    by solving the logistic growth problem.
    """
    import matplotlib.pyplot as plt

    problem = Logistic(alpha=0.2, R=1.0, u0=0.1)
    solver = ForwardEuler_v0(problem)
    solver.set_initial_condition(problem.u0)

    T = 40
    t, u = solver.solve(t_span=(0, T), N=400)

    plt.plot(t, u)
    plt.title('Logistic growth, Forward Euler')
    plt.xlabel('t')
    plt.ylabel('u')
    plt.show()
