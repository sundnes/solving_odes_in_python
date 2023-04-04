from ODESolver import *
from scipy.optimize import root

class BackwardEuler(ODESolver):

    def stage_eq(self,k):
        u, f, n, t = self.u, self.f, self.n, self.t
        dt = self.dt
        return k - f(t[n]+dt,u[n]+dt*k)

    def solve_stage(self):
        u, f, n, t = self.u, self.f, self.n, self.t
        k0 = f(t[n],u[n])
        sol = root(self.stage_eq,k0)
        return sol.x

    def advance(self):
        u, f, n, t = self.u, self.f, self.n, self.t
        dt = self.dt
        k1 = self.solve_stage()
        return u[n]+dt*k1


class CrankNicolson(BackwardEuler):
    def advance(self):
        u, f, n, t = self.u, self.f, self.n, self.t
        dt = self.dt
        k1 = f(t[n],u[n])
        k2 = self.solve_stage()
        return u[n]+dt/2*(k1+k2)
    

if __name__ == "__main__":
    registered_solver_classes.extend([BackwardEuler,CrankNicolson])
    test_exact_numerical_solution()