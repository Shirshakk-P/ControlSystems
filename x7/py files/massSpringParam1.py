#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
#import control as cnt
import sys
sys.path.append('..') #add parent directory
#import import_ipynb
import massSpringParam as P

Ts = P.Ts #sample rate of the controller
beta = P.beta #dirty derivative gain
tau_max = P.tau_max #limit on control signal

#PD gains
kp = 4.5928
kd = 11.7403

print('kp: ', kp)
print('kd: ', kd)


# In[ ]:




