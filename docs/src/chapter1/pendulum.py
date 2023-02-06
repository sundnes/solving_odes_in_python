from math import sin

class Pendulum:
    def __init__(self, L, g = 9.81):
        self.L = L 
        self.g = g 
    
    def __call__(self,t,u):
        theta, omega = u
        dtheta = omega
        domega = -self.g/self.L * sin(theta)
        return [dtheta, domega]


if __name__ == '__main__':
    from forward_euler_class_v1 import *
    problem = Pendulum(L=1)
    solver = ForwardEuler_v1(problem)
    solver.set_initial_condition([np.pi/4,0])
    T = 10
    N = 1000
    t, u = solver.solve(T=T,N=N)
    
    plt.plot(t,u[:,0],label=r'$\theta$')
    plt.plot(t,u[:,1],label=r'$\omega$')
    plt.title(f'Pendulum problem, Forward Euler, $\Delta t$ = {T/N}')
    plt.xlabel('t')
    plt.ylabel(r'Angle ($\theta$) and angular velocity ($\omega$)')
    plt.legend()
    plt.show()