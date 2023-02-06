import numpy as np
import matplotlib.pyplot as plt
x0 = 100                      # initial population
rho = 5                       # growth rate in %
R = 500                       # max population (carrying capacity)
N = 200                       # number of years

index_set = range(N+1)
x = np.zeros(len(index_set))

x[0] = x0
for n in index_set[1:]:
    x[n] = x[n-1] + (rho/100) *x[n-1]*(1 - x[n-1]/R)

plt.plot(index_set, x)
plt.xlabel('years')
plt.ylabel('amount')
plt.show()
