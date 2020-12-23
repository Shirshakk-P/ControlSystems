import matplotlib.pylab as pylab
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation
from scipy.integrate import odeint
from pylab import plot,xlabel,ylabel,title,legend,figure,subplots
from pylab import cos, pi, arange, sqrt, pi, array, array



def MassSpringDamper(state,t):
    
    k=2.714;            # spring constant (N/m)
    c=0.437;           #damping coefficient (Ns/m)
    m=4.871;             # mass (kg)
    # unpack the state vector
    x,xd = state # displacement,x and velocity x'
    # compute acceleration xdd = x''
    # Force F is a sinusoidal with below parameters
    
    A = 5.0 # amplitude
    xdd = -k*x/m -c*xd + A*cos(2*pi*t)
    return [xd, xdd]



z = input("input initial Displacement Z")
z = float(z)
print(z)
state0 = [z, 0]  
ti = 0.0  
tf = 4.0  # final time
step = 0.001  # step
t = arange(ti, tf, step)
state = odeint(MassSpringDamper, state0, t)
x = array(state[:,[0]])
xd = array(state[:,[1]])

# Plotting displacement and velocity
pylab.rcParams['figure.figsize'] = (15, 12)
pylab.rcParams['font.size'] = 18

fig, ax1 = pylab.subplots()
ax2 = ax1.twinx()
ax1.plot(t,x*1e3,'b',label = r'$x (mm)$', linewidth=2.0)
ax2.plot(t,xd,'g--',label = r'$\dot{x} (m/sec)$', linewidth=2.0)
ax2.legend(loc='lower right')
ax1.legend()
ax1.set_xlabel('time , sec')
ax1.set_ylabel('disp (m)',color='b')
ax2.set_ylabel('velocity (m/s)',color='g')
pylab.title('Mass-Spring System')
pylab.grid()    
pylab.show()


fig = plt.figure()
fig.set_dpi(50)
fig.set_size_inches(7, 6.5)
a=np.arange(1,10,0.1)
animati=[]
ax = plt.axes(xlim=(-3, 3), ylim=(0, 1))
patch = plt.Rectangle((1, 0),0.8, 0.2, fc='g')
animati.append(patch)
l1,=ax.plot([],[],lw=2,color='k')
animati.append(l1)
l2,=ax.plot([],[],lw=2,color='b')
animati.append(l2)

def init():
    animati[0].set_xy([state0[0],0])
    ax.add_patch(animati[0])
    animati[1].set_data([],[])
    animati[2].set_data([],[])
    return animati

def animate(i):
    animati[0].set_xy([x[i],0])
    animati[1].set_data([-5,x[i]],[0.05,0.05])
    animati[2].set_data([-5,x[i]],[0.15,0.15])
    return animati

anim = animation.FuncAnimation(fig, animate, 
                               init_func=init, 
                               frames=10000, 
                               interval=0.00001,
                               blit="True")

plt.show()
