import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np

plt.ion() 

class dataPlotter:
    def __init__(self):
        #Number of subplots = num_of_rows*num_of_cols
        self.num_rows = 3 #Number of subplot rows
        self.num_cols = 1 #Number of subplot columns
        
        #Create figure and axes handles
        self.fig, self.ax = plt.subplots(self.num_rows,
                                         self.num_cols,
                                         sharex=True)
        
        #Instantiate lists to hold the time and data hsitories
        self.time_history = [] #time
        self.r_history = [] #reference r
        self.y_history = [] #output y
        self.ydot_history = [] #velocity ydot
        self.u_history = [] #input u
        
        #create a handle for every subplot
        self.handle = []
        self.handle.append(subplotWindow(self.ax[0], ylabel='y', title='Simple System'))
        self.handle.append(subplotWindow(self.ax[1], ylabel='ydot'))
        self.handle.append(subplotWindow(self.ax[2], xlabel='t(s)', ylabel='u'))
        
    def update(self, time, reference, state, control):
        #update the time history of all plot variables
        self.time_history.append(time) #time
        self.r_history.append(reference) #reference initial position
        self.y_history.append(state.item(0)) 
        self.ydot_history.append(state.item(1))
        self.u_history.append(control)
        
        #update plot with associated histories
        self.handle[1].update(self.time_history, [self.r_history, self.y_history])
        self.handle[1].update(self.time_history, [self.ydot_history]) 
        self.handle[1].update(self.time_history, [self.u_history])

class subplotWindow:
    #Create individual subplot.
    def __init__(self, ax,
                 xlabel='',
                 ylabel='',
                 title='',
                 legend=None):
        
        self.legend = legend
        self.ax = ax
        self.colors = ['b', 'g', 'r', 'c', 'm', 'y', 'b']
        self.line_styles= ['-','-','--','-.',':']
        
        self.line = []
        #Configure the axes
        self.ax.set_ylabel(ylabel)
        self.ax.set_xlabel(xlabel)
        self.ax.set_title(title)
        self.ax.grid(True)
        #Keeps track of  intialization
        self.init = True
        
    def update(self, time, data):
        #Adds data to the plot
        #Initialize the plot the first time routine is called
        if self.init == True:
            for i in range(len(data)):
                #Instantiate the plot the first time routine is called
                self.line.append(Line2D(time,
                                        data[i],
                                        color=self.colors[np.mod(i, len(self.colors) - 1)],
                                        ls=self.line_styles
                                                [np.mod(i, len(self.line_styles) - 1)],
                                        label=self.legend 
                                            if self.legend != None else None))
                self.ax.add_line(self.line[i])
            self.init = False
            #add legend if one is specified
            if self.legend != None:
                plt.legend(handles=self.line)
        else:#Add new data to the plot
            #Updates the x and y data of each line
            for i in range(len(self.line)):
                self.line[i].set_xdata(time)
                self.line[i].set_ydata(data[i])
         #Adjust the axis to fit all the data   
        self.ax.relim()
        self.ax.autoscale()