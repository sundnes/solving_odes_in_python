import sys
from numpy import zeros

try:
    N = int(sys.argv[1])
except:
    print('Provide a command line argument; a number between 1 and 90.')
    exit()

x = zeros(N+1, int)
x[0] = 1
x[1] = 1
for n in range(2, N+1):
    x[n] = x[n-1] + x[n-2]
    print(n, x[n])
