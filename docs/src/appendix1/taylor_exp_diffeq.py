import numpy as np

x = 0.5 #approximate exp(x) for x = 0.5

N = 5
index_set = range(N+1)
a = np.zeros(len(index_set))
e = np.zeros(len(index_set))
a[0] = 1

print(f'Exact: exp({x}) = {np.exp(x)}')
for n in index_set[1:]:
    e[n] = e[n-1] + a[n-1]
    a[n] = x/n*a[n-1]
    print(f'n = {n}, approx. {e[n]}, error = {np.abs(e[n]-np.exp(x)):4.5f}')
