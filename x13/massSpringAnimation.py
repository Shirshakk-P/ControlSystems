import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import massSpringParam as P


class massSpringAnimation:
    '''
        Create arm animation
    '''
    def __init__(self):
        # Used to indicate initialization
        self.flagInit = True

        # Initializes a figure and axes object
        self.fig, self.ax = plt.subplots()

        # Initializes a list object that will be used to
        # contain handles to the patches and line objects.
        self.handle = []

        self.length=P.length
        self.width=P.width

        # Change the x,y axis limits
        plt.axis([-0.5*P.ell, 0.5*P.ell, -2.0*P.ell,
                  2.0*P.ell])

        # Draw a base line
        plt.plot([-0.5*P.ell, 0.5*P.ell], [0, 0],'k--')    
        
        #Draw a line representing wall
        plt.plot([-0.5*P.ell, -0.5*P.ell], [0, P.width + 1.0], 'k')

        # Draw pendulum is the main function that will call the
        # functions:
        # drawCart, drawCircle, and drawRod to create the animation.

    def update(self, u):
        # Process inputs to function
        z = u[0]   # position of mass, m
        self.draw_cart(z)
        self.draw_spring(z)
        self.ax.axis('equal')
        # Set initialization flag to False after first call
        if self.flagInit == True:
            self.flagInit = False
            
    def draw_cart(self, z):
        # specify bottom left corner of rectangle
        x = z - P.length/2.0
        y = P.gap
        corner = (x,y)
        # create rectangle on first call, update on subsequent calls
        if self.flagInit == True:
            # Create the Rectangle patch and append its handle
            # to the handle list
            self.handle.append(
                mpatches.Rectangle(corner, P.length, P.width,
                                   fc = 'green', ec = 'black'))
            # Add the patch to the axes
            self.ax.add_patch(self.handle[0])
        else:
            self.handle[0].set_xy(corner)
            
    def draw_spring(self, z):
        # specify x-y points of the spring
        X = [-0.5*P.ell, z - P.length/2.0] # X data points
        Y = [P.gap + P.width/2.0, P.gap + P.width/2.0]  # Y data points

        # When the class is initialized, a line object will be
        # created and added to the axes. After initialization, the
        # line object will only be updated.
        if self.flagInit == True:
            # Create the line object and append its handle
            # to the handle list.
            line, =self.ax.plot(X, Y, lw=2, c='blue')
            self.handle.append(line)
            self.flagInit=False
        else:
            self.handle[1].set_xdata(X)   # Update the line
            self.handle[1].set_ydata(Y)