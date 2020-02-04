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
    
'''
Tan
'''
import parameter as par
import wavefunction as wfn
from psi_new import PSI

Qx_dvr = par.Qx_dvr
Qy_dvr = par.Qy_dvr

tape   = par.tape

N      = par.N
m      = par.m

# initial number states of the species:
ns = np.zeros(m,int)
ns[0] = N-1
ns[m-1] = 1

# initial spf
spfx1 = np.exp(-0.5*(Qx_dvr.x)**2)
spfx1 = spfx1/np.sqrt(sum(spfx1*spfx1))
spfx2 = np.exp(-0.5*(Qx_dvr.x)**2)*Qx_dvr.x
spfx2 = spfx2/np.sqrt(sum(spfx2*spfx2))
spfy1 = Qy_dvr.x/np.sqrt(sum(Qy_dvr.x**2))
spfy2 = spfy1

# spf补足


#将两个自由度分别打包在一个列表,得到第2层的spf
spfx = [spfx1,spfx2]
spfy = [spfy1,spfy2]

startSPF   = [spfx,spfy]

# test
Psi = PSI(tape=tape)
psi.ini = Psi.init_coef_sing_spec_B(ns,startSPF,spfx,spfy)
