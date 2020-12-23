import warnings
warnings.filterwarnings("ignore")
import numpy as np
import matplotlib.pyplot as plt
import time
t0 = time.clock()

k=2.714;            # spring constant (N/m)
b=0.437;           #damping coefficient (Ns/m)
m=4.871;             # mass (kg)
x0=1
v0=0

simTime=10
tStep=0.001
iterations=int(simTime/tStep)
t=np.arange(0, iterations)

x=np.zeros((iterations,1))
x[0,:]=x0
v=np.zeros((iterations,1))
v[0,:]=v0
a=np.zeros((iterations,1))
a[0,:]=-((b*v0)+(k*x0))/m

for n in range(1,iterations):
    x[n,:]=x[n-1,:]+v[n-1,:]*tStep
    v[n,:]=v[n-1,:]+a[n-1,:]*tStep
    a[n,:]=-((b*v[n,:])+(k*x[n,:]))/m
    
    
plt.rcParams["figure.figsize"] = (20,10)
plt.figure()
plt.subplot(3,1,1)
plt.plot(t,x,'r',label='cart')
plt.ylabel('Position (m)')
plt.legend()
plt.subplot(3,1,2)
plt.plot(t,v,'b',label='cart')
plt.ylabel('velocity')
plt.legend()
plt.subplot(3,1,3)
plt.plot(t,a,'g',label='cart')
plt.ylabel('acceleration')
plt.legend()
