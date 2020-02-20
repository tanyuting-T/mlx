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
import mathtools as maths
from psi_new import PSI

N      = par.N
m      = par.m
mx     = par.mx
my     = par.my
nx     = par.nx
ny     = par.ny
Qx_dvr = par.Qx_dvr
Qy_dvr = par.Qy_dvr

# tree:                         
#                        (+)
#                        ||| N      
#                         O -m     
#                       /   \
#                      /     \
#                     O -mx   O -my
#                     |       |
#                     O -nx   O -ny

tape = (-10,
         N, 1, m, 
        -1, 1,
         2, 0, mx, my,
        -1, 1,
         1, 0, nx,
         0,-1, 2,   
         1, 0, ny,  
        -2)

# initial spf
# subparticle layer
spfx1 = np.exp(-0.5*(Qx_dvr.x)**2)
spfx1 = spfx1/np.sqrt(sum(spfx1*spfx1))
spfx2 = np.exp(-0.5*(Qx_dvr.x)**2)*Qx_dvr.x
spfx2 = spfx2/np.sqrt(sum(spfx2*spfx2))
spfx3 = spfx2.copy()

spfy1 = Qy_dvr.x/np.sqrt(sum(Qy_dvr.x**2))
spfy2 = spfy1.copy()
spfy3 = spfy1.copy()
spfy4 = spfy1.copy()

spfx  = np.stack((spfx1,spfx2,spfx3),axis=0)
spfy  = np.stack((spfy1,spfy2,spfy3,spfy4),axis=0)

# particle layer
np.random.seed(12)
spf_particle_x1 = np.random.rand(mx)
spf_particle_y1 = np.random.rand(my)

np.random.seed(123)
spf_particle_x2 = np.random.rand(mx)
spf_particle_y2 = np.random.rand(my)

spf_particle1   = np.outer(spf_particle_x1,spf_particle_y1)
spf_particle1   = spf_particle1/np.sqrt((spf_particle1**2).sum())
spf_particle2   = np.outer(spf_particle_x2,spf_particle_y2)
spf_particle2   = spf_particle2/np.sqrt((spf_particle2**2).sum())

spf_particle    = np.stack((spf_particle1,spf_particle2),axis=0)
#print(spf_particle)

# top layer
ns_num = maths.num_numberstate(N,m)
np.random.seed(1234)
spf_ns = np.random.rand(ns_num)
spf_ns = spf_ns/np.sqrt((spf_ns**2).sum())

# test
Psi = PSI(tape=tape)
print(Psi.psi_topnode)
Psi.PSI_ini(spf_ns,spf_particle,spfx,spfy)
print(Psi.psi_topnode)
