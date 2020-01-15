'''
Wu
'''
import numpy as np

#parameter for tree


N = 2                                                    #number for particles
n = 3                                                    #number for numberstate
m = 2                                                    #number for orbitals

mx = 3                                                   #number for spf_subparticle_x
xmin = -5.0                                              #left boundary for x
xmax = 5.0                                               #right boundary for x
nx = 100                                                 #number for grid_x

my = 4                                                   #number for spf_subparticle_y
ymin = -5.0                                              #left boundary for y
ymax = 5.0                                               #right boundary for y
ny = 100                                                 #number for grid_y


#parameter for hamiltion

#parameter for kinetic
kinetic_x = 1.0                                          #strength for kinetic power in direction x
kinetic_y = 1.0                                          #strength for kinetic power in direction y

#potential in direction x.several choices
#1.static harmonic potentials: omega_x^2*x^2
#2.periodic harmonic potentials (a*sin(b*t+c)+d)*x^2
type_potential_x = 1                                     #1 for static and 2 for periodic
omega_x = 1.0                                            #parameter for 1. omega_x^2*x^2
periodic_a_x = 1.0                                       #parameter for 2.
periodic_b_x = 1.0                                       #parameter for 2.
periodic_c_x = 1.0                                       #parameter for 2.
periodic_d_x = 1.0                                       #parameter for 2.


#potential in direction y.several choices
#1.static harmonic potentials: omega_y^2*y^2
#2.periodic harmonic potentials (a*sin(b*t+c)+d)*y^2
type_potential_y = 1                                     #1 for static and 2 for periodic
omega_y = 1.0                                            #parameter for 1. omega_y^2*y^2
periodic_a_y = 1.0                                       #parameter for 2.
periodic_b_y = 1.0                                       #parameter for 2.
periodic_c_y = 1.0                                       #parameter for 2.
periodic_d_y = 1.0                                       #parameter for 2.


#parameter for delta interaction
strength_delta = 1.0                                     #parameter for delta interaction