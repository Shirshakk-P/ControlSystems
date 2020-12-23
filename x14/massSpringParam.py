# Mass Spring Damper System Parameter File
import numpy as np
# import control as cnt

# Physical parameters of the arm known to the controller
m = 4.871     # Mass of the cart, kg
ell = 10    # Length of the arm, m
#g = 9.8       # Gravity, m/s**2
b = 0.437      # Damping coefficient, Nms
k = 2.714     #Spring constant, N/m
gap = 0.0015

# parameters for animation
length = 3.0    # length of arm in animation
width = 3.0   # width of arm in animation
gap = 0.005
w = 0.3
# Initial Conditions
theta0 = 0.0       # ,rads
thetadot0 = 0.0         # ,rads/s
z0 = 0.0   # ,m
zdot0 = 0.0 # ,m/s

# Simulation Parameters
t_start = 0.0  # Start time of simulation
t_end = 50.0  # End time of simulation
Ts = 0.01  # sample time for simulation
t_plot = 0.05  # the plotting and animation is updated at this rate

# dirty derivative parameters
sigma = 0.05  # cutoff freq for dirty derivative
beta = (2.0*sigma-Ts)/(2.0*sigma+Ts)  # dirty derivative gain

# saturation limits
tau_max = 6.0                # Max force, N-m
