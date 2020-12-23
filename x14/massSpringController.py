import numpy as np
#import import_ipynb
import massSpringParam1 as P

class massSpringController:
    def __init__(self):
        self.observer_state = np.array([
            [0.0], # estimate of z
            [0.0], # estimate of z_hat
            [0.0], # estimate of disturbance
        ])
        self.tau_d1 = 0.0      #control force, delayed 1 sample
        self.integrator = 0.0  # integrator
        self.error_d1 = 0.0    # error signal, delyaed 1 sample
        self.K = P.K           # state feedback gain
        self.ki = P.ki         # Input gain
        self.L = P.L           # observer gain
        self.Ld = P.Ld
        self.L2 = P.L2
        self.A2 = P.A2         # system model
        self.B2 = P.B2
        self.C2 = P.C2
        self.limit = P.tau_max # maximum force
        self.Ts = P.Ts         # sample rate of controller
        
    def update(self, z_r, y_m):
        #update the observer and extract z_hat
        x_hat, d_hat = self.update_observer(y_m)
        z_hat = x_hat.item(0)
        
        #integrate error
        error = z_r - z_hat
        self.integrateError(error)
        
        #feedback linearizing force tau_fl
        tau_fl = P.k*z_hat
        
        # Compute the state feedback controller
        tau_tilde = -self.K @ x_hat - self.ki * self.integrator - d_hat
        
        #compute total force
        tau = self.saturate(tau_fl + tau_tilde.item(0))
        self.tau_d1 = tau
        
        return tau, x_hat, d_hat
    
    def integrateError(self, error):
        self.integrator = self.integrator + (self.Ts/2.0)*(error + self.error_d1)
        self.error_d1 = error
        
    def update_observer(self, y_m):
        #update the observer using RK4 integration
        F1 = self.observer_f(self.observer_state, y_m)
        F2 = self.observer_f(self.observer_state + self.Ts / 2 * F1, y_m)
        F3 = self.observer_f(self.observer_state + self.Ts / 2 * F2, y_m)
        F4 = self.observer_f(self.observer_state + self.Ts * F3, y_m)
        self.observer_state += self.Ts / 6 * (F1 + 2 * F2 + 2 * F3 + F4)
        x_hat = np.array([[self.observer_state.item(0)],
                          [self.observer_state.item(1)]])
        d_hat = self.observer_state.item(2)

        return x_hat, d_hat
    
    def observer_f(self, x_hat, y_m):
        #compute feedback linearizing force tau_fl
        z_hat = x_hat.item(0)
        tau_fl = P.k*z_hat
        
        # xhatdot = A*xhat + B*(u-ue) + L(y-C*xhat)
        xhat_dot = self.A2 @ x_hat + self.B2 * (self.tau_d1 - tau_fl) + self.L2 * (y_m - self.C2 @ x_hat)

        return xhat_dot
    
    def saturate(self, u):
        if abs(u) > self.limit:
            u = self.limit*np.sign(u)
        return u