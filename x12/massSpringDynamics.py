import numpy as np 
import random
import massSpringParam as P


class massSpringDynamics:
    def __init__(self, alpha=0.0):
        # Initial state conditions
        self.state = np.array([
            [P.z0],      # initial position
            [P.zdot0]
        ])  # initial positional rate

        alpha = 0.2
        # Mass of the arm, kg
        self.m = P.m * (1.+alpha*(2.*np.random.rand()-1.))

        # Damping coefficient, Ns
        self.b = P.b * (1.+alpha*(2.*np.random.rand()-1.))  

        #Spring constant,
        self.k = P.k * (1.+alpha*(2.*np.random.rand()-1.))
        
        # sample rate at which the dynamics are propagated
        self.Ts = P.Ts  
        self.force_limit = P.tau_max

    def update(self, u):
        # This is the external method that takes the input u at time
        # t and returns the output y at time t.
        # saturate the input force
        u = self.saturate(u, self.force_limit)
        
        self.rk4_step(u)  # propagate the state by one time sample
        y = self.h()  # return the corresponding output

        return y

    def f(self, state, u):
        # Return xdot = f(x,u), the system state update equations
        # re-label states for readability
        z = state.item(0)
        zdot = state.item(1)
        zddot = -(self.b/self.m) * zdot - (self.k/self.m) * z + (1/self.m) * u;
        xdot = np.array([[zdot],
                         [zddot]])
        
        return xdot

    def h(self):
        # return the output equations
        # could also use input u if needed
        z = self.state.item(0)
        y = np.array([[z]])

        return y

    def rk4_step(self, u):
        # Integrate ODE using Runge-Kutta RK4 algorithm
        F1 = self.f(self.state, u)
        F2 = self.f(self.state + self.Ts / 2 * F1, u)
        F3 = self.f(self.state + self.Ts / 2 * F2, u)
        F4 = self.f(self.state + self.Ts * F3, u)
        self.state += self.Ts / 6 * (F1 + 2 * F2 + 2 * F3 + F4)

    def saturate(self, u, limit):
        if abs(u) > limit:
            u = limit*np.sign(u)

        return u
