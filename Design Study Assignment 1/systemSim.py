import simpy
import random
import statistics
import numpy as np
import matplotlib
matplotlib.use('TKAgg')
import matplotlib.pyplot as plt
import import_ipynb
import massSpringParam as P
#from systemDynamics import systemDynamics
from signalGenerator import signalGenerator
from systemAnimation import massSpringAnimation
#from dataPlotter import dataPlotter

#Simulation parameter
#t_start = 0.0
#t_end = 20.0
#t_plot = 0.1
#Ts = 0.01

#instantiate system, controller and refernce classes
#system = systemDynamics(sample_rate=P.Ts)
reference = signalGenerator(amplitude=1.0, frequency = 0.05)
disturbance = signalGenerator(amplitude=1.0, frequency = 0.5)
noise = signalGenerator(amplitude=0.01,frequency=0.1)

#instantiate the simulation plots and ainmation
#dataPlot = dataPlotter()
animation = massSpringAnimation()

t = P.t_start
#y = system.h()
while t < P.t_end:
    r = reference.square(t)
    d = disturbance.step(t)
    n = noise.random(t)
    u = reference.sawtooth(t)
    states = np.array([[d], [n]])
    animation.update(states)
    #dataPlot.update(t, r, states, u)
    
    t = t + P.t_plot
    plt.pause(0.05)

print('Press any Key to close')
plt.waitforbuttonpress()
plt.close
