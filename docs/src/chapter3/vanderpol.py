from ODESolver import *
import numpy as np
import matplotlib.pyplot as plt

class VanderPol:
    def __init__(self,mu):
        self.mu = mu

    def __call__(self,t,u):
        du1 = u[1]
        du2 = self.mu*(1-u[0]**2)*u[1]-u[0]
        return du1,du2


if __name__ == '__main__':
    model = VanderPol(mu=1)

    solver = ForwardEuler(model)
    solver.set_initial_condition([1,0])

    t_span = (0,20)
    t,u  = solver.solve(t_span=(0,20),N=1000)

    plt.plot(t,u)
    plt.show()
