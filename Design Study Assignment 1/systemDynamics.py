import numpy as np
class systemDynamics:
    def __init__(self, sample_rate):
        #Initial state conditions
        z0 = 0.0;
        zdot0 = 0.0
        self.state = np.array([
            [z0],
            [zdot0],
        ])
        self.Ts = sample_rate
        self.limit = 1.0
        self.a0 = 0.608
        self.a1 = 0.109
        self.b0 = 0.195
        alpha = 0.2 #Uncertainity parameter
        self.a1 = self.a1 * (1.+alpha*(2.*np.random.rand()-1.))
        self.a0 = self.a0 * (1.+alpha*(2.*np.random.rand()-1.))
        self.b0 = self.b0 * (1.+alpha*(2.*np.random.rand()-1.))
        
    def f(self, state, u):
        #for system xdot = f(x, u), return f(x,u)
        z = state.item(0)
        zdot = state.item(1)
        #The equation of motion.
        zddot = -self.a1 * zdot - self.a0 * z + self.b0 * u
        zdot = np.array([[zdot], [yddot]])
        return zdot
    def h(self):
        #Returns the measured output y = h(x)
        z = self.state.item(0)
        return z
    
    def update(self, u):
        u = self.saturate(u, self.limit)
        self.rk4_step(u)
        z = self.h()
        return z
    
    def rk4_step(self, u):
        F1 = self.f(self.state, u)
        F2 = self.f(self.state + self.Ts / 2 * F1, u)
        F3 = self.f(self.state + self.Ts / 2 * F2, u)
        F4 = self.f(self.state + self.Ts * F3, u)
        self.state += self.Ts / 6 * (F1 + 2 * F2 + 2 * F3 + F4)
        
    def saturate(self, u, limit):
        if abs(u) > limit:
            u = limit*np.sign(u)
        return u