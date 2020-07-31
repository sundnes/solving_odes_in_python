import numpy as np
import matplotlib.pyplot as plt
F = 1e7                      # initial amount
p = 5                         # interest rate
I = 3
q = 75
N = 40                         # number of years
index_set = range(N+1)
x = np.zeros(len(index_set))
c = np.zeros_like(x)

x[0] = F
c[0] = q*p*F*1e-4

for n in index_set[1:]:
    x[n] = x[n-1] + (p/100.0)*x[n-1] - c[n-1]
    c[n] = c[n-1] + (I/100.0)*c[n-1]

plt.plot(index_set, x, 'ro',label = 'Fortune')
plt.plot(index_set, c, 'go', label = 'Yearly consume')
plt.xlabel('years')
plt.ylabel('amounts')
plt.legend()
plt.show()
