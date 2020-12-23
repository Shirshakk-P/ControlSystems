#Mass Spring Damper Parameter File
import numpy as np
import control as cnt
import sys
sys.path.append('..') # add parent directory
#import import_ipynb
import massSpringParam as P

#tuning parameters
tr = 1.6
zeta = 0.7
#integrator_pole=np.array([-2])
integrator_pole = 14
wn_obs = 10 # natural frequency for observer
zeta_obs = 0.707 #damping ratio for observer

Ts = P.Ts #sample rate of the controller
tau_max = P.tau_max #limit on control signal
m = P.m
k = P.k
b = P.b

#State Space Equations
A = np.array([[0.0, 1.0],
              [-(P.k/P.m), -(P.b/P.m)]])
n = A.shape[0]

B = np.array([[0.0],
              [(1/P.m)]])
C = np.array([[1.0, 0.0]])

#control design
#form augumented system
A1 = np.array([[0.0, 1.0, 0.0],[-P.k/P.m, -P.b/P.m, 0.0],[-1.0, 0.0, 0.0]])
B1 = np.array([[0.0],
              [1/P.m],
              [0.0]])

#gain calculation
wn = 2.2/tr #natural frequency
#des_char_poly = np.convolve([1, 2*zeta*wn, wn**2],np.poly(integrator_pole))
des_char_poly = np.convolve([1, 2*zeta*wn, wn**2],[1,integrator_pole])
des_poles = np.roots(des_char_poly)

#Compute the gains if the system is controllable
if np.linalg.matrix_rank(cnt.ctrb(A1, B1)) != 3:
    print("The system is not controllable")
else:
    K1 = cnt.acker(A1, B1, des_poles)
    K = np.array([[K1.item(0), K1.item(1)]])
    ki = K1.item(2)
    
#observer design
#des_obsv_char_poly = [1, 2*zeta_obs*wn_obs, wn_obs**2]
des_obsv_poles = des_poles[0:n]*2. #np.roots(des_obsv_char_poly)

#Compute the gains if the system is controllable
if np.linalg.matrix_rank(cnt.ctrb(A.T, C.T)) != 2:
    print("System not Observable")
else:
    L = cnt.acker(A.T, C.T, des_obsv_poles).T
    
print('K: ', K)
print('ki: ', ki)
print('L^T: ', L.T)
