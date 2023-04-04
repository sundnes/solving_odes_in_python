from ODESolver import *
from scipy.optimize import root


class ImplicitRK(ODESolver):
    def solve_stages(self):
        u, f, n, t = self.u, self.f, self.n, self.t
        neq = self.neq
        s = self.stages
        k0 = f(t[n], u[n])
        k0 = np.hstack([k0 for i in range(s)])

        sol = root(self.stage_eq, k0)

        return np.split(sol.x, s)

    def stage_eq(self, k_all):
        a, c = self.a, self.c
        s, neq = self.stages, self.neq

        u, f, n, t = self.u, self.f, self.n, self.t
        dt = self.dt

        res = np.zeros_like(k_all)
        k = np.split(k_all, s)
        for i in range(s):
            fi = f(t[n] + c[i] * dt, u[n] + dt *
                   sum([a[i, j] * k[j] for j in range(s)]))
            res[i * neq:(i + 1) * neq] = k[i] - fi

        return res

    def advance(self):
        b = self.b
        u, n, t = self.u, self.n, self.t
        dt = self.dt
        k = self.solve_stages()

        return u[n] + dt * sum(b_ * k_ for b_, k_ in zip(b, k))


class BackwardEuler(ImplicitRK):
    def __init__(self, f):
        super().__init__(f)
        self.stages = 1
        self.a = np.array([[1]])
        self.c = np.array([1])
        self.b = np.array([1])


class ImpMidpoint(ImplicitRK):
    def __init__(self, f):
        super().__init__(f)
        self.stages = 1
        self.a = np.array([[1 / 2]])
        self.c = np.array([1 / 2])
        self.b = np.array([1])


class Radau2(ImplicitRK):
    def __init__(self, f):
        super().__init__(f)
        self.stages = 2
        self.a = np.array([[5 / 12, -1 / 12], [3 / 4, 1 / 4]])
        self.c = np.array([1 / 3, 1])
        self.b = np.array([3 / 4, 1 / 4])


class Radau3(ImplicitRK):
    def __init__(self, f):
        super().__init__(f)
        self.stages = 3
        sq6 = np.sqrt(6)
        self.a = np.array([[(88 - 7 * sq6) / 360,
                            (296 - 169 * sq6) / 1800,
                            (-2 + 3 * sq6) / (225)],
                           [(296 + 169 * sq6) / 1800,
                            (88 + 7 * sq6) / 360,
                            (-2 - 3 * sq6) / (225)],
                           [(16 - sq6) / 36, (16 + sq6) / 36, 1 / 9]])
        self.c = np.array([(4 - sq6) / 10, (4 + sq6) / 10, 1])
        self.b = np.array([(16 - sq6) / 36, (16 + sq6) / 36, 1 / 9])


class SDIRK(ImplicitRK):
    def stage_eq(self, k, c_i, k_sum):
        u, f, n, t = self.u, self.f, self.n, self.t
        dt = self.dt
        gamma = self.gamma

        return k - f(t[n] + c_i * dt, u[n] + dt * (k_sum + gamma * k))

    def solve_stages(self):
        u, f, n, t = self.u, self.f, self.n, self.t
        a, c = self.a, self.c
        s = self.stages

        k = f(t[n], u[n])  # initial guess for first stage
        k_sum = np.zeros_like(k)
        k_all = []
        for i in range(s):
            k_sum = sum(a_ * k_ for a_, k_ in zip(a[i, :i], k_all))
            k = root(self.stage_eq, k, args=(c[i], k_sum)).x
            k_all.append(k)

        return k_all


class SDIRK2(SDIRK):
    def __init__(self, f):
        super().__init__(f)
        self.stages = 2
        gamma = (2 - np.sqrt(2)) / 2
        self.gamma = gamma
        self.a = np.array([[gamma, 0],
                           [1 - gamma, gamma]])
        self.c = np.array([gamma, 1])
        self.b = np.array([1 - gamma, gamma])


class ESDIRK(SDIRK):
    def solve_stages(self):
        u, f, n, t = self.u, self.f, self.n, self.t
        a, c = self.a, self.c
        s = self.stages

        k = f(t[n], u[n])  # initial guess for first stage
        k_sum = np.zeros_like(k)
        k_all = [k]
        for i in range(1, s):
            k_sum = sum(a_ * k_ for a_, k_ in zip(a[i, :i], k_all))
            k = root(self.stage_eq, k, args=(c[i], k_sum)).x
            k_all.append(k)

        return k_all


class TR_BDF2(ESDIRK):
    def __init__(self, f):
        super().__init__(f)
        self.stages = 3
        gamma = 1 - np.sqrt(2) / 2
        beta = np.sqrt(2) / 4
        self.gamma = gamma
        self.a = np.array([[0, 0, 0],
                           [gamma, gamma, 0],
                           [beta, beta, gamma]])
        self.c = np.array([0, 2 * gamma, 1])
        self.b = np.array([beta, beta, gamma])


if __name__ == "__main__":
    registered_solver_classes.extend(
        [BackwardEuler, ImpMidpoint, Radau2, Radau3, SDIRK2, TR_BDF2])
    test_exact_numerical_solution()
