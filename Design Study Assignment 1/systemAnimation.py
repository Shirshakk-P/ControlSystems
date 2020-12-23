import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import import_ipynb
import massSpringParam as P

class massSpringAnimation:
    def __init__(self):
        self.flag_init = True #Used to indicate initialization
        #Initialize a figure and axes object
        self.fig, self.ax = plt.subplots()
        #Initialize a list of objects (patches and lines)
        self.handle = []
        #Specify the x,y axis limits
        plt.axis([0, 5*P.ell, -0.1, 5*P.ell])
        #Draw line for the ground
        plt.plot([0, 10*P.ell], [0,0], 'b--')
        #label axes
        plt.xlabel('z')
        
    def update(self, state):
        z = state.item(0)
        theta = state.item(0)
        self.draw_wall(z)
        self.draw_box(z)
        self.draw_spring(z)
        self.draw_damper(z)
        self.ax.axis('equal')
        if self.flag_init == True:
            self.flag_init = False
            
    def draw_wall(self, z):
        x = 0.0
        y = P.gap
        corner = (x,y)
        if self.flag_init == True:
            self.handle.append(mpatches.Rectangle(corner, P.w, P.h, fc = 'blue', ec = 'black'))
            self.ax.add_patch(self.handle[0])
        else:
            self.handle[0].set_xy(corner)
    
    def draw_box(self, z):
        x = z-P.ww/2.0
        y = P.gap
        corner = (x,y)
        if self.flag_init == True:
            self.handle.append(
            mpatches.Rectangle(corner, P.ww, P.hh, fc = 'limegreen', ec = 'black'))
            self.ax.add_patch(self.handle[1])
        else:
            self.handle[1].set_xy(corner)
    
    def draw_spring(self, z):
        x = P.w
        y = P.hh/2.0
        corner = (x,y)
        if self.flag_init == True:
            self.handle.append(
            mpatches.Rectangle(corner, 1.0-P.w-P.ww/2.0, 0.001, fc = 'black', ec = 'black'))
            self.ax.add_patch(self.handle[2])
        else:
            self.handle[2].set_xy(corner)
    def draw_damper(self, z):
        x = P.w
        y = P.hh/4.0
        corner = (x,y)
        if self.flag_init == True:
            self.handle.append(
            mpatches.Rectangle(corner, 1.0-P.w-P.ww/2.0, 0.01, fc = 'red', ec = 'black'))
            self.ax.add_patch(self.handle[3])
        else:
            self.handle[3].set_xy(corner)