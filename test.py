'''
Wu
'''
import numpy as np
import hterm

array = np.linspace(0,1,10)
test_hterm = hterm.hterm(1,array)
test_hterm.printf()

array = np.diag([0,0.3,0.1,0.9])
test_hterm = hterm.hterm(2,array)
test_hterm.printf()

array = np.empty((2,3), dtype=object)
for j in range(array.shape[1]):
    array[0][j] = hterm.hterm(1,np.linspace(0,1,10))
    print(0,j)
    array[0][j].printf()
    
for j in range(array.shape[1]):
    array[1][j] = hterm.hterm(1,np.diag([0,0.3,0.1,0.9]))
    print(1,j)
    array[1][j].printf()