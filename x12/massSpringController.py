import numpy as np
import massSpringParam1 as P

class massSpringController:
    def __init__(self):
        self.integrator = 0.0 # Integrator
        self.error_d1 = 0.0 # Error signal delayed by 1 sample
        self.K = P.K # State feedback gain
        self.ki = P.ki # Input gain
        self.limit = P.tau_max # Maximum force
        self.Ts = P.Ts # sample rate of controller
        
    def update(self, z_r, x):
        z = x.item(0)
        
        #integrate error
        error = z_r - z
        self.integrateError(error)
        
        #compute feedback linearizing force tau_fl
        tau_fl = P.k * z
        
        # Compute the state feedback controller
        tau_tilde = -self.K @ x - self.ki*self.integrator
        
        # Compute total force
        tau = self.saturate(tau_fl + tau_tilde)
        return tau
    
    def integrateError(self, error):
        self.integrator = self.integrator + (self.Ts/2.0)*(error + self.error_d1)
        self.error_d1 = error
        
    def saturate(self, u):
        if abs(u) > self.limit:
            u = self.limit*np.sign(u)
        return u
