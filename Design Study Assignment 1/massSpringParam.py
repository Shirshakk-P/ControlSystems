##Mass Spring Damper System Parameter File

#Physical parameters of the arm known to the controller
k=2.714;            # spring constant (N/m)
b=0.437;           #damping coefficient (Ns/m)
m=4.871;             # mass (kg)
g= 9.8
ell= 0.1
h = 0.3
w = 0.015
gap=0.005
ww=0.3
hh=.3

#Initial Conditions
z=0.0
zdot=0.0
theta= 0.0
thetadot= 0.0
#Simulation Parameters
t_start = 0.0 #Start time of simulation
t_end = 20.0 #End time of simulation
Ts= 0.01 #sample time for simulation
t_plot = 0.1 #the plotting and animaiton is updated at this rate

#Dirty derivatives parameters
sigma = 0.05 #cutoff freq for dirty derivative
beta = (2.0*sigma-Ts)/(2.0*sigma+Ts) #dirty derivative gain

#saturation limits
F_max = 2.0
