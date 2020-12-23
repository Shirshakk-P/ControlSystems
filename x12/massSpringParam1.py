#Mass Spring Damper System Parameter File
import numpy as np
import control as cnt
import sys
sys.path.append('..') #add parent directory
import massSpringParam as P

Ts = P.Ts #sample rate of the controller
beta = P.beta #dirty derivative gain
tau_max = P.tau_max #limit on control signal
m = P.m
k = P.k
b = P.b

#tuning parameters
tr = 1.6
zeta = 0.7
integrator_pole = np.array([-0.4])

#state space equations
#xdot = A*x + B*u
#y = C*x
A = np.array([[0.0, 1.0],
              [-P.k/P.m, -P.b/P.m]])
B = np.array([[0.0],
              [1/P.m]])
C = np.array([[1.0, 0.0]])

#form augumented system
A1 = np.array([[0.0, 1.0, 0.0],
               [-P.k/P.m, -P.b/P.m, 0.0],
               [-1.0, 0.0, 0.0]])
B1 = np.array([[0.0],
              [1/P.m],
              [0.0]])

#gain calculation
wn = 2.2/tr #natural frequency
des_char_poly = np.convolve(
    [1, 2*zeta*wn, wn**2],
    np.poly(integrator_pole))
des_poles = np.roots(des_char_poly)

#Compute the gains if the system is controllable
if np.linalg.matrix_rank(cnt.ctrb(A1, B1)) != 3:
    print("The system is not controllable")
else:
    K1 = cnt.acker(A1, B1, des_poles)
    K = np.array([[K1.item(0), K1.item(1)]])
    ki = K1.item(2)
    
print('K: ', K)
print('ki: ', ki)
