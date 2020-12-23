#Mass Spring Damper system Parameter File
import numpy as np
import control as cnt
import sys
sys.path.append('..') #add parent directory
import massSpringParam as P

Ts = P.Ts
beta = P.beta
tau_max = P.tau_max
m = P.m
k = P.k
b = P.b

#tuning parameters
#tr=1.6    #previous homework was done on the basis of tr=1.6 and step input is taken from this homework onwards
tr = 1.5
zeta = 0.7

#State Space Equations
# xdot = A*x + B*u
# y = C*x
A = np.array([[0.0, 1.0],
              [-P.k/P.m, -P.b/P.m]])
B = np.array([[0.0],
              [1.0/P.m]])
C = np.array([[1.0, 0.0]])

#gain calculation
wn = 2.2/tr #natural frequency
des_char_poly = [1, 2*zeta*wn, wn**2]
des_poles = np.roots(des_char_poly)

#Compute the gains if the system is controllable
if np.linalg.matrix_rank(cnt.ctrb(A, B)) != 2:
    print("The system is not controllable")
else:
    #.A just turns K matrix into a numpy array
    K = (cnt.acker(A, B, des_poles)).A
    kr = -1.0/(C @ np.linalg.inv(A - B @ K) @ B)
    
print('K: ', K)
print('kr: ', kr)
