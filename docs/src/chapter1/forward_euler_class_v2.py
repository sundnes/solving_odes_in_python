"""
Alternative version of the Forward Euler class,
applied to solve the samelogistic growth problem
as the ForwardEuler_v1 class.
"""
import numpy as np
import matplotlib.pyplot as plt

class ForwardEuler_v2:
    def __init__(self, f):
        self.f = f

    def set_initial_condition(self,U0):
        self.U0 = float(U0)

    def solve(self, time_points):
        """Compute solution for array of time points"""
        self.t = np.asarray(time_points)
        N = len(self.t)
        self.u = np.zeros(N)
        self.u[0] = self.U0

        # Time loop
        for n in range(N-1):
            self.n = n
            self.u[n+1] = self.advance()
        return self.u, self.t

    def advance(self):
        """Advance the solution one time step."""
        # Create local variables to get rid of "self." in
        # the numerical formula
        u, f, n, t = self.u, self.f, self.n, self.t
        #dt is not necessarily constant:
        dt = t[n+1]-t[n]
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
    time = np.linspace(0,40,401)

    method = ForwardEuler_v2(problem)
    method.set_initial_condition(problem.U0)
    u, t = method.solve(time)
    plt.plot(t,u)
    plt.show()
