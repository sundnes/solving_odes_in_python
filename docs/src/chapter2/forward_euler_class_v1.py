"""
First version of the Forward Euler class implementation,
including a class implementation of the logistic
growth model.
"""
import numpy as np
import matplotlib.pyplot as plt

class ForwardEuler_v1:
    def __init__(self, f, U0, T, N):
        self.f, self.U0, self.T, self.N = f, U0, T, N
        self.dt = T/float(N)
        self.u = np.zeros(self.N+1)
        self.t = np.zeros(self.N+1)

    def solve(self):
        """Compute solution for 0 <= t <= T."""
        self.u[0] = float(self.U0)
        self.t[0] = float(0)

        for n in range(self.N):
            self.n = n
            self.t[n+1] = self.t[n] + self.dt
            self.u[n+1] = self.advance()
        return self.u, self.t

    def advance(self):
        """Advance the solution one time step."""
        # Create local variables to get rid of "self." in
        # the numerical formula
        u, dt, f, n, t = self.u, self.dt, self.f, self.n, self.t

        unew = u[n] + dt*f(u[n], t[n])
        return unew



if __name__ == '__main__':
    """
    Demonstrate how the class the class is used,
    by solving the logistic growth problem.
    """

    class Logistic:
        def __init__(self, alpha, R, U0):
            self.alpha, self.R, self.U0 = alpha, float(R), U0

        def __call__(self, u, t):
            return self.alpha*u*(1 - u/self.R)

    problem = Logistic(0.2, 1, 0.1)
    method = ForwardEuler_v1(problem,problem.U0,40,401)
    u, t = method.solve()
    plt.plot(t,u)
    plt.show()
