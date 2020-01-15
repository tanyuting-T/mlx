'''
Wu
'''
import numpy as np


np.set_printoptions(precision=5,suppress=True)

#hterm use for different choices
#0 for not determined
#1 for 1D vector
#2 for 2D matrix
#3 for 4D tensor
#4 for 8D tensor
class hterm:
    def __init__(self, htype, hterm):
        self.htype = htype
        self.hterm = hterm
        
    def printf(self):
        print('htype is\n{}'.format(self.htype))
        print('hterm is\n{}'.format(self.hterm))