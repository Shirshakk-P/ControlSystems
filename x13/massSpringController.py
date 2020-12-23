import numpy as np
import massSpringParam1 as P

class massSpringController:
    def __init__(self):
        self.x_hat = np.array([
            [0.0], # z_hat_0
            [0.0], # zdot_hat_0
        ])
        self.tau_d1 = 0.0 #control force, delayed 1 sample
        self.integrator = 0.0 # integrator
        self.error_d1 = 0.0 # error signal, delyaed 1 sample
        self.K = P.K # state feedback gain
        self.ki = P.ki # Input gain
        self.L = P.L # observer gain
        self.A = P.A # system model
        self.B = P.B
        self.C = P.C
        self.limit = P.tau_max # maximum force
        self.Ts = P.Ts # sample rate of controller
        
    def update(self, z_r, y):
        #update the observer and extreact z_hat
        x_hat = self.update_observer(y)
        z_hat = x_hat.item(0)
        
        #integrate error
        error = z_r - z_hat
        self.integrateError(error)
        
        #feedback linearizing force tau_fl
        tau_fl = P.k*z_hat
        
        # Compute the state feedback controller
        tau_tilde = -self.K @ x_hat - self.ki * self.integrator
        
        #compute total force
        tau = self.saturate(tau_fl + tau_tilde.item(0))
        self.tau_d1 = tau
        return tau, x_hat
    
    def integrateError(self, error):
        self.integrator = self.integrator + (self.Ts/2.0)*(error + self.error_d1)
        self.error_d1 = error
        
    def update_observer(self, y_m):
        #update the observer using RK4 integration
        F1 = self.observer_f(self.x_hat, y_m)
        F2 = self.observer_f(self.x_hat + self.Ts / 2 * F1, y_m)
        F3 = self.observer_f(self.x_hat + self.Ts / 2 * F2, y_m)
        F4 = self.observer_f(self.x_hat + self.Ts * F3, y_m)
        self.x_hat += self.Ts / 6 * (F1 + 2 * F2 + 2 * F3 + F4)

        return self.x_hat
    
    def observer_f(self, x_hat, y_m):
        #compute feedback linearizing force tau_fl
        z_hat = x_hat.item(0)
        tau_fl = P.k*z_hat
        
        # xhatdot = A*xhat + B*(u-ue) + L(y-C*xhat)
        xhat_dot = self.A @ x_hat + self.B * (self.tau_d1 - tau_fl) + self.L * (y_m - self.C @ x_hat)

        return xhat_dot
    
    def saturate(self, u):
        if abs(u) > self.limit:
            u = self.limit*np.sign(u)
        return u