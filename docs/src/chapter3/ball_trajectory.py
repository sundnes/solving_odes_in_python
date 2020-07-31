from ODESolver import ForwardEuler
import numpy as np
import matplotlib.pyplot as plt


def f(u, t):
    x, vx, y, vy = u
    g = 9.81
    return [vx, 0, vy, -g]

# Initial condition, start at the origin:
x = 0; y = 0
# velocity magnitude and angle:
v0 = 5; theta = 80*np.pi/180
vx = v0*np.cos(theta); vy = v0*np.sin(theta)

U0 = [x, vx, y, vy]

solver= ForwardEuler(f)
solver.set_initial_condition(U0)
time_points = np.linspace(0, 1.0, 101)
u, t = solver.solve(time_points)
# u is an array of [x,vx,y,vy] arrays, plot y vs x:
x = u[:,0];  y = u[:,2]

plt.plot(x, y)
plt.title('The trajectory of the ball')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
