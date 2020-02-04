import numpy as np
import math
import mathtools as maths
np.set_printoptions(precision=5,suppress=True)

class PSI:
    def __init__(self,**opts): #通过赋值的方式以字典的形式传入参数
        self.num_orbital=None  # m
        self.num_particle=None  # N
        
        self.num_numberstate=opts.get("n",None)  # n
        
        self.num_subparticle_x=None  # mx
        self.num_subparticle_y=None  # my
        self.num_primitive_x=None  # nx
        self.num_primitive_y=None  # ny
        
        self.psi_topnode=np.zeros(self.num_numberstate,dtype=complex)
        self.psi_numberstate=np.zeros((self.num_numberstate,self.num_orbital),dtype=int)
        self.psi_particle=np.zeros((self.num_orbital,self.num_subparticle_x,self.num_subparticle_y),dtype=complex)
        self.psi_subparticle_x=np.zeros((self.num_subparticle_x,self.num_primitive_x),dtype=complex)
        self.psi_subparticle_y=np.zeros((self.num_subparticle_y,self.num_primitive_y),dtype=complex)
        
        # start from tape
        tape = opts.get("tape",None)
        if tape is not None:
            self._init_from_tape(tape)
        
        
    def _init_from_tape(self,tape):
        self._tape = tape
      
        i = 1
        pnode = []
        subnode = []
        subnode_s = []
        while tape[i] != -2:
            if tape[i] > 1:
                if tape[i+3] == -1:
                    pnode.append(tape[i])
                    pnode.append(tape[i+2])
                    i = i +3
                else:
                    a = tape[i] + i + 3
                    b = tape[i+2:a]
                    subnode.extend(b)
                    i = i + tape[i] + 2
            if tape[i] == 1:
                subnode_s.append(tape[i+2])
                i += 3
            if tape[i] <= 0:
                if tape[i] == -1:  # go down
                    i += 2
                if tape[i] == 0:  # jump up
                    i += 3
                if tape[i] == -2:  # exit
                    break
                                          
        self.num_particle = pnode[0]
        self.num_orbital = pnode[1]
        self.num_subparticle_x = subnode[0]
        self.num_subparticle_y = subnode[1]
        
    def PSI_ini(self,ns,startSPF,spfx,spfy):
        """
        initializes coefficients of initial wave function of a bosonic layer.
        """
        #无截断的情况
        self.num_numberstate = maths.num_numberstate(self.num_particle,self.num_orbital)
        
        #psi赋值（未完成）
        self.psi_topnode=np.zeros(self.num_numberstate,dtype=complex)
        self.psi_numberstate=np.zeros((self.num_numberstate,self.num_orbital),dtype=int)
        
        self.psi_particle=startSPF
        self.psi_subparticle_x=spfx
        self.psi_subparticle_y=spfy
        
        
        
        return psi_ini
    
