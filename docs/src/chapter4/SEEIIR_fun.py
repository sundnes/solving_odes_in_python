import numpy as np
import matplotlib.pyplot as plt
from ODESolver import *

def SEEIIR_model(u,t):
    beta = 0.5; r_ia = 0.1; r_e2=1.25;
    lmbda_1=0.33; lmbda_2=0.5; p_a=0.4; mu=0.2;

    S, E1, E2, I, Ia, R = u
    N = sum(u)
    dS  = -beta*S*I/N - r_ia*beta*S*Ia/N - r_e2*beta*S*E2/N
    dE1 = beta*S*I/N + r_ia*beta*S*Ia/N + r_e2*beta*S*E2/N - lmbda_1*E1
    dE2 = lmbda_1*(1-p_a)*E1 - lmbda_2*E2
    dI  = lmbda_2*E2 - mu*I
    dIa = lmbda_1*p_a*E1 - mu*Ia
    dR  = mu*(I + Ia)
    return [dS, dE1, dE2, dI, dIa, dR]

S_0 = 5e6
E1_0 = 0
E2_0 = 100
I_0 = 0
Ia_0 = 0
R_0 = 0
U0 = [S_0, E1_0, E2_0, I_0, Ia_0, R_0]

solver = RungeKutta4(SEEIIR_model)
solver.set_initial_condition(U0)
time_points = np.linspace(0, 100, 101)
u, t = solver.solve(time_points)
S = u[:,0]; E1 = u[:,1]; E2 = u[:,2];
I = u[:,3]; Ia = u[:,4]; R = u[:,5]

plt.plot(t,S,label='S')
#plt.plot(t,E1,label='E1')
#plt.plot(t,E2,label='E2')
plt.plot(t,I,label='I')
plt.plot(t,Ia,label='Ia')
plt.plot(t,R,label='R')
plt.legend()
plt.savefig('seir_fig0.pdf')
plt.show()
