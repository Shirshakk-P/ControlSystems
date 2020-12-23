import numpy as np
import massSpringParam1 as P

class massSpringController:
    #dirty derivatives to estimate zdot
    def __init__(self):
        self.K = P.K #State feedback gain
        self.kr = P.kr #Input gain
        self.limit = P.tau_max #Maximum force
        self.Ts = P.Ts #sample rate of controller
        
    def update(self, z_r, x):
        z = x.item(0)
        zdot = x.item(1)
        
        #Compute feedback linearizing force tau_fl
        tau_fl = P.k*z
        
        #Compute the state feedback controller
        tau_tilde = -self.K @ x + self.kr * z_r
        
        #Compute total force
        tau = self.saturate(tau_fl + tau_tilde)
        return tau
    
    def saturate(self, u):
        if abs(u) > self.limit:
            u = self.limit*np.sign(u)
            
        return u
