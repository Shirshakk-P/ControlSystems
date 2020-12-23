import numpy as np

class signalGenerator:
    
    def __init__(self, amplitude=10.0, frequency=0.01, z_offset=0):
        self.amplitude = amplitude
        self.frequency = frequency
        self.z_offset = z_offset
        
    def square(self, t):
        if t % (1.0/self.frequency) <= 0.5/self.frequency:
            out = self.amplitude + self.z_offset
        else:
            out = - self.amplitude + self.z_offset
        return out 
    
    def sawtooth(self, t):
        tmp= t % (0.5/self.frequency)
        out = 4 * self.amplitude * self.frequency*tmp - self.amplitude + self.z_offset
        return out
    
    def step(self, t):
        if t>= 0.0:
            out = self.amplitude + self.z_offset
        else:
            out = self.z_offset
        return out
    
    def random(self, t):
        out = np.random.normal(self.z_offset, self.amplitude)
        return out 
    
    def sin(self, t):
        out = self.amplitude* np.sin(2*np.pi*self,frequency*t) \
        + self.z_offset
        return out