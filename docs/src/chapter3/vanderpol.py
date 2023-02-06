from ODESolver import *
from ImplicitEuler import *
import numpy as np
import matplotlib.pyplot as plt

class VanderPol:
    def __init__(self,mu):
        self.mu = mu

    def __call__(self,u,t):
        du1 = u[1]
        du2 = self.mu*(1-u[0]**2)*u[1]-u[0]
        return du1,du2


model = VanderPol(mu=5)

solver = ImplicitEuler(model)
solver.set_initial_condition([1,0])

time = np.linspace(0,20,5001)
u,t  = solver.solve(time)

plt.plot(t,u)
plt.show()

