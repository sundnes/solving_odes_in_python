def Newton(f, dfdx, x, epsilon=1.0E-7, max_n=100):
    n = 0
    while abs(f(x)) > epsilon and n <= max_n:
        x = x - f(x)/dfdx(x)
        n += 1
    return x, n, f(x)


#Demo: solve x**3-4x+3=0
def f(x):
    return x**3-4*x-3

def df(x):
    return 3*x**2-4

x0 = 1.0
sol, its, f_val = Newton(f,df,x0)
print(f'Solver converged in {its} iterations, x={sol:g}, f(x)={f_val:g}')
