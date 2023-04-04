from ImplicitRK import *
from AdaptiveODESolver import *
import numpy as np


class AdaptiveESDIRK(AdaptiveODESolver, ESDIRK):

    def advance(self):
        b = self.b
        e = self.e
        u = self.u
        dt = self.dt
        k = self.solve_stages()
        u_step = dt * sum(b_ * k_ for b_, k_ in zip(b, k))
        error = dt * sum(e_ * k_ for e_, k_ in zip(e, k))

        u_new = u[-1] + u_step
        error_norm = np.linalg.norm(error)
        return u_new, error_norm


class TR_BDF2_Adaptive(AdaptiveESDIRK):
    def __init__(self, f, eta=0.9):
        super().__init__(f, eta)  # calls AdaptiveODESolver.__init__
        self.stages = 3
        self.order = 2
        gamma = 1 - np.sqrt(2) / 2
        beta = np.sqrt(2) / 4
        self.gamma = gamma
        self.a = np.array([[0, 0, 0],
                           [gamma, gamma, 0],
                           [beta, beta, gamma]])
        self.c = np.array([0, 2 * gamma, 1])
        self.b = np.array([beta, beta, gamma])
        bh = np.array([(1 - beta) / 3, (3 * beta + 1) / 3, gamma / 3])
        self.e = self.b - bh


if __name__ == '__main__':
    from hodgkinhuxley import *
    import matplotlib.pyplot as plt

    model = HodgkinHuxley()

    solver = TR_BDF2_Adaptive(model)
    solver.set_initial_condition([-45, 0.31, 0.05, 0.59])

    t, u = solver.solve((0, 50), tol=0.1)

    plt.plot(t, u[:, 0], '+')
    plt.show()
