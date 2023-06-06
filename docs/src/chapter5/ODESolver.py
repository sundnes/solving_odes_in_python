"""
Version 2 of the ODESolver class hierarchy. This class works for systems
of ODEs and for a single (scalar) ODE.
"""

import numpy as np


class ODESolver:
    def __init__(self, f):
        # Wrap user's f in a new function that always
        # converts list/tuple to array (or let array be array)
        self.model = f
        self.f = lambda t, u: np.asarray(f(t, u), float)

    def set_initial_condition(self, u0):
        if np.isscalar(u0):              # scalar ODE
            self.neq = 1                 # no of equations
            u0 = float(u0)
        else:                            # system of ODEs
            u0 = np.asarray(u0)
            self.neq = u0.size           # no of equations
        self.u0 = u0

    def solve(self, t_span, N):
        """Compute solution for
        t_span[0] <= t <= t_span[1],
        using N steps.
        Returns the solution and the 
        time points as arrays. 
        """
        t0, T = t_span
        self.dt = (T - t0) / N
        self.t = np.zeros(N + 1)  # N steps ~ N+1 time points
        if self.neq == 1:
            self.u = np.zeros(N + 1)
        else:
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
        raise NotImplementedError("Advance method is not implemented in the base class")



class ForwardEuler(ODESolver):
    def advance(self):
        u, f, n, t = self.u, self.f, self.n, self.t
        dt = self.dt
        return u[n] + dt * f(t[n], u[n])

class Heun(ODESolver):
    def advance(self):
        u, f, n, t = self.u, self.f, self.n, self.t
        dt = self.dt
        k1 = f(t[n], u[n])
        k2 = f(t[n] + dt, u[n] + dt * k1)
        return u[n] + dt / 2 * (k1 + k2)

class ExplicitMidpoint(ODESolver):
    def advance(self):
        u, f, n, t = self.u, self.f, self.n, self.t
        dt = self.dt
        dt2 = dt / 2.0
        k1 = f(t[n], u[n])
        k2 = f(t[n] + dt2, u[n] + dt2 * k1)
        return u[n] + dt * k2

class RungeKutta4(ODESolver):
    def advance(self):
        u, f, n, t = self.u, self.f, self.n, self.t
        dt = self.dt
        dt2 = dt / 2.0
        k1 = f(t[n], u[n],)
        k2 = f(t[n] + dt2, u[n] + dt2 * k1, )
        k3 = f(t[n] + dt2, u[n] + dt2 * k2, )
        k4 = f(t[n] + dt, u[n] + dt * k3, )
        return u[n] + (dt / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)

def test_exact_numerical_solution():
    """
    Test the different methods for a problem
    where the analytical solution is known and linear.
    All the methods should be exact to machine precision
    for this choice.
    """
    registered_solver_classes = [ForwardEuler,
    Heun, ExplicitMidpoint, RungeKutta4]

    a = 0.2
    b = 3

    def f(t, u):
        return a  

    def u_exact(t):
        """Exact u(t) corresponding to f above."""
        return a * t + b

    u0 = u_exact(0)
    T = 8
    N = 10
    tol = 1E-15
    t_span = (0, T)
    for solver_class in registered_solver_classes:
        solver = solver_class(f)
        solver.set_initial_condition(u0)
        t, u = solver.solve(t_span, N)
        u_e = u_exact(t)
        max_error = (u_e - u).max()
        msg = f'{solver.__class__.__name__} failed with max_error={max_error}'
        assert max_error < tol, msg


if __name__ == '__main__':
    test_exact_numerical_solution()
