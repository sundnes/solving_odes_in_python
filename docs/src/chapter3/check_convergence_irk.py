from ImplicitRK import BackwardEuler,Radau2, Radau3
import numpy as np

def rhs(t, u):
    return u

def exact(t):
    return np.exp(t)

solver_classes = [(BackwardEuler, 1),
                  (Radau2, 3), (Radau3, 5)]

for solver_class, order in solver_classes: 
    solver = solver_class(rhs)
    solver.set_initial_condition(1.0)

    T = 3.0
    t_span = (0, T)
    N = 30
    print(f'{solver_class.__name__}, order = {order}')
    print(f'Time step (dt)   Error (e)     e/dt**{order}')
    for _ in range(10):
        t, u = solver.solve(t_span, N)
        dt = T / N
        e = abs(u[-1] - exact(T))
        if e < 1e-13:  # break if error is close to machine precision
            break
        print(f'{dt:<14.7f}   {e:<12.7f}  {e/dt**order:5.4f}')
        N = N * 2
