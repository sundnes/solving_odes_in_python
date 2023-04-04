from ImplicitRK_v2 import *
import numpy as np
import matplotlib.pyplot as plt

class VanderPol:
    def __init__(self,mu):
        self.mu = mu

    def __call__(self,t,u):
        du0 = u[1]
        du1 = self.mu*(1-u[0]**2)*u[1]-u[0]
        return du0,du1
    
    def jac(self,t,u):
        jac = np.zeros((2,2))
        jac[0,1] = 1
        jac[1,0] = -2*self.mu*u[0]*u[1]-1
        jac[1,1] = self.mu*(1-u[0])**2
        return jac

if __name__ == '__main__':
    model = VanderPol(mu=1)

    
    solver = Radau3(model)

    solver.set_initial_condition([1,0])

    t_span = (0,20)
    t,u  = solver.solve(t_span=(0,20),N=1000)

    plt.plot(t,u)
    plt.show()
