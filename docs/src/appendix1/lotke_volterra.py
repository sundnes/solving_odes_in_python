import numpy as np
import matplotlib.pyplot as plt


x0 = 100                # initial prey population
y0 = 8                  # initial predator pop.
a = 0.0015
b = 0.0003
c = 0.006
d = 0.5
N = 10000               # number of time units (days)
index_set = range(N + 1)
x = np.zeros(len(index_set))
y = np.zeros_like(x)

x[0] = x0
y[0] = y0

for n in index_set[1:]:
    x[n] = x[n - 1] + a * x[n - 1] - b * x[n - 1] * y[n - 1]
    y[n] = y[n - 1] + d * b * x[n - 1] * y[n - 1] - c * y[n - 1]

plt.plot(index_set, x, label='Prey')
plt.plot(index_set, y, label='Predator')
plt.xlabel('Time')
plt.ylabel('Population')
plt.legend()
plt.show()
