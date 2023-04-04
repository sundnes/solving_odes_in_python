import numpy as np
from ODESolver import *


class HodgkinHuxley:
    def __init__(
            self,
            Cm=1.0,
            gK=36,
            gNa=120.0,
            gL=0.3,
            EK=-77.0,
            ENa=50.0,
            EL=-54.4,
            I_stim=None):

        self.Cm = Cm    # Membrane capacitance, in uF/cm^2
        self.gK = gK    # Maximum conductance of potassium ion channels, in mS/cm^2
        self.gNa = gNa  # Maximum conductance of sodium ion channels, in mS/cm^2
        self.gL = gL    # Maximum conductance of leak channels, in mS/cm^2
        self.EK = EK    # Nernst potential of potassium ions, in mV
        self.ENa = ENa  # Nernst potential of sodium ions, in mV
        self.EL = EL    # Nernst potential of leak channels, in mV
        if I_stim is None:
            self.I_stim = lambda t: 0
        else:
            self.I_stim = I_stim

    def alpha_n(self, V):
        return 0.01 * (V + 55.0) / (1.0 - np.exp(-0.1 * (V + 55.0)))

    def beta_n(self, V):
        return 0.125 * np.exp(-0.0125 * (V + 65.0))

    def alpha_m(self, V):
        return 0.1 * (V + 40.0) / (1.0 - np.exp(-0.1 * (V + 40.0)))

    def beta_m(self, V):
        return 4.0 * np.exp(-0.0556 * (V + 65.0))

    def alpha_h(self, V):
        return 0.07 * np.exp(-0.05 * (V + 65.0))

    def beta_h(self, V):
        return 1.0 / (1.0 + np.exp(-0.1 * (V + 35.0)))

    def IK(self, V, n):
        return self.gK * n**4 * (V - self.EK)

    def INa(self, V, m, h):
        return self.gNa * m**3 * h * (V - self.ENa)

    def IL(self, V):
        return self.gL * (V - self.EL)

    def __call__(self, t, u):
        V, n, m, h = u
        dVdt = -(self.INa(V, m, h) + self.IK(V, n) +
                 self.IL(V) - self.I_stim(t)) / self.Cm
        dndt = self.alpha_n(V) * (1.0 - n) - self.beta_n(V) * n
        dmdt = self.alpha_m(V) * (1.0 - m) - self.beta_m(V) * m
        dhdt = self.alpha_h(V) * (1.0 - h) - self.beta_h(V) * h
        return [dVdt, dndt, dmdt, dhdt]
