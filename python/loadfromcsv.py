# Autogenerated with SMOP 
from smop.core import *
# 

    
@function
def loadfromcsv(inpfilename=None,folder=None,*args,**kwargs):
    varargin = loadfromcsv.varargin
    nargin = loadfromcsv.nargin

    ##
#        Project: Fluid - structure interaction on deformable surfaces
#         Author: Luca Di Stasio
#    Institution: ETH Zrich
#                 Institute for Building Materials
# Research group: Computational Physics for Engineering Materials
#        Version: 0.1
#  Creation date: July 2nd, 2014
#    Last update: July 9th, 2014
    
    #    Description: 
#          Input: 
#         Output:
    
    #                 Ordering of flags:
#                 flags(1)  --> save fixed lattice (computational domain)
#                 flags(2)  --> save moving mesh (physical domain)
#                 flags(3)  --> save velocities (LSM)
#                 flags(4)  --> save masses (LSM)
#                 flags(5)  --> save elastic forces (LSM)
#                 flags(6)  --> save damping forces (LSM)
#                 flags(7)  --> save external forces (LSM)
#                 flags(8)  --> save total forces (LSM)
#                 flags(9)  --> save particle kinetic energy per dof (LSM)
#                 flags(10) --> save particle kinetic energy (LSM)
#                 flags(11) --> save total kinetic energy (LSM)
#                 flags(12) --> save particle potential energy (LSM)
#                 flags(13) --> save total potential energy (LSM)
#                 flags(14) --> save particle dissipation function (LSM)
#                 flags(15) --> save total dissipation function (LSM)
#                 flags(16) --> save covariant base vectors
#                 flags(17) --> save contravariant base vectors
#                 flags(18) --> save metric tensor
#                 flags(19) --> save metric tensor determinant
#                 flags(20) --> save g
#                 flags(21) --> save reciprocal metric coefficients
#                 flags(22) --> save first Christoffel symbols
#                 flags(23) --> save second Christoffel symbols
#                 flags(24) --> save Riemann tensor
#                 flags(25) --> save Ricci tensor
#                 flags(26) --> save Ricci curvature
#                 flags(27) --> save density (LBM)
#                 flags(28) --> save velocity in cartesian components (LBM)
#                 flags(29) --> save pressure (LBM)
#                 flags(30) --> save strain rate tensor (LBM)
#                 flags(31) --> save strain rate (LBM)
#                 flags(32) --> save stress tensor (LBM)
#                 flags(33) --> save viscosity (LBM)
#                 flags(34) --> save relaxation time (LBM)
#                 flags(35) --> save sound velocity (LBM)
#                 flags(36) --> save particle equilibrium populations (LBM)
#                 flags(37) --> save particle populations (LBM)
    
    ##
    
    filename=strcat(folder,'/',inpfilename,'.csv')
    R1=0
    C1=0
    R2=0
    C2=9 - 1
    RNG=matlabarray(cat(R1,C1,R2,C2))
    basicdata=csvread(filename,R1,C1,RNG)
    data.N = copy(basicdata[1,1])
    data.Nx = copy(basicdata[1,2])
    data.Ny = copy(basicdata[1,3])
    data.Nz = copy(basicdata[1,4])
    data.dt = copy(basicdata[1,5])
    data.tmax = copy(basicdata[1,6])
    data.t = copy(basicdata[1,7])
    data.i = copy(basicdata[1,8])
    data.nvars = copy(basicdata[1,9])
    R1=1
    C1=0
    R2=1
    C2=nvars - 1
    RNG=matlabarray(cat(R1,C1,R2,C2))
    dataindex=csvread(filename,R1,C1,RNG)
    for i in arange(1,nvars).reshape(-1):
        if 1 == dataindex[1,i]:
            R1=dataindex[2,i]
            C1=dataindex[3,i]
            R2=dataindex[4,i]
            C2=dataindex[5,i]
            RNG=matlabarray(cat(R1,C1,R2,C2))
            data.lattice = copy(csvread(filename,R1,C1,RNG))
        else:
            if 2 == dataindex[1,i]:
                R1=dataindex[2,i]
                C1=dataindex[3,i]
                R2=dataindex[4,i]
                C2=dataindex[5,i]
                RNG=matlabarray(cat(R1,C1,R2,C2))
                data.mesh = copy(csvread(filename,R1,C1,RNG))
            else:
                if 3 == dataindex[1,i]:
                    R1=dataindex[2,i]
                    C1=dataindex[3,i]
                    R2=dataindex[4,i]
                    C2=dataindex[5,i]
                    RNG=matlabarray(cat(R1,C1,R2,C2))
                    data.vel = copy(csvread(filename,R1,C1,RNG))
                else:
                    if 4 == dataindex[1,i]:
                        R1=dataindex[2,i]
                        C1=dataindex[3,i]
                        R2=dataindex[4,i]
                        C2=dataindex[5,i]
                        RNG=matlabarray(cat(R1,C1,R2,C2))
                        data.m = copy(csvread(filename,R1,C1,RNG))
                    else:
                        if 5 == dataindex[1,i]:
                            R1=dataindex[2,i]
                            C1=dataindex[3,i]
                            R2=dataindex[4,i]
                            C2=dataindex[5,i]
                            RNG=matlabarray(cat(R1,C1,R2,C2))
                            data.Fel = copy(csvread(filename,R1,C1,RNG))
                        else:
                            if 6 == dataindex[1,i]:
                                R1=dataindex[2,i]
                                C1=dataindex[3,i]
                                R2=dataindex[4,i]
                                C2=dataindex[5,i]
                                RNG=matlabarray(cat(R1,C1,R2,C2))
                                data.Fdamp = copy(csvread(filename,R1,C1,RNG))
                            else:
                                if 7 == dataindex[1,i]:
                                    R1=dataindex[2,i]
                                    C1=dataindex[3,i]
                                    R2=dataindex[4,i]
                                    C2=dataindex[5,i]
                                    RNG=matlabarray(cat(R1,C1,R2,C2))
                                    data.Fext = copy(csvread(filename,R1,C1,RNG))
                                else:
                                    if 8 == dataindex[1,i]:
                                        R1=dataindex[2,i]
                                        C1=dataindex[3,i]
                                        R2=dataindex[4,i]
                                        C2=dataindex[5,i]
                                        RNG=matlabarray(cat(R1,C1,R2,C2))
                                        data.Ftot = copy(csvread(filename,R1,C1,RNG))
                                    else:
                                        if 9 == dataindex[1,i]:
                                            R1=dataindex[2,i]
                                            C1=dataindex[3,i]
                                            R2=dataindex[4,i]
                                            C2=dataindex[5,i]
                                            RNG=matlabarray(cat(R1,C1,R2,C2))
                                            data.Ekinpdof = copy(csvread(filename,R1,C1,RNG))
                                        else:
                                            if 10 == dataindex[1,i]:
                                                R1=dataindex[2,i]
                                                C1=dataindex[3,i]
                                                R2=dataindex[4,i]
                                                C2=dataindex[5,i]
                                                RNG=matlabarray(cat(R1,C1,R2,C2))
                                                data.Ekinp = copy(csvread(filename,R1,C1,RNG))
                                            else:
                                                if 11 == dataindex[1,i]:
                                                    R1=dataindex[2,i]
                                                    C1=dataindex[3,i]
                                                    R2=dataindex[4,i]
                                                    C2=dataindex[5,i]
                                                    RNG=matlabarray(cat(R1,C1,R2,C2))
                                                    Ekin=csvread(filename,R1,C1,RNG)
                                                    data.Ekin = copy(Ekin[1])
                                                else:
                                                    if 12 == dataindex[1,i]:
                                                        R1=dataindex[2,i]
                                                        C1=dataindex[3,i]
                                                        R2=dataindex[4,i]
                                                        C2=dataindex[5,i]
                                                        RNG=matlabarray(cat(R1,C1,R2,C2))
                                                        data.Epotp = copy(csvread(filename,R1,C1,RNG))
                                                    else:
                                                        if 13 == dataindex[1,i]:
                                                            R1=dataindex[2,i]
                                                            C1=dataindex[3,i]
                                                            R2=dataindex[4,i]
                                                            C2=dataindex[5,i]
                                                            RNG=matlabarray(cat(R1,C1,R2,C2))
                                                            Epot=csvread(filename,R1,C1,RNG)
                                                            data.Epot = copy(Epot[1])
                                                        else:
                                                            if 14 == dataindex[1,i]:
                                                                R1=dataindex[2,i]
                                                                C1=dataindex[3,i]
                                                                R2=dataindex[4,i]
                                                                C2=dataindex[5,i]
                                                                RNG=matlabarray(cat(R1,C1,R2,C2))
                                                                data.Dfuncp = copy(csvread(filename,R1,C1,RNG))
                                                            else:
                                                                if 15 == dataindex[1,i]:
                                                                    R1=dataindex[2,i]
                                                                    C1=dataindex[3,i]
                                                                    R2=dataindex[4,i]
                                                                    C2=dataindex[5,i]
                                                                    RNG=matlabarray(cat(R1,C1,R2,C2))
                                                                    Dfunc=csvread(filename,R1,C1,RNG)
                                                                    data.Dfunc = copy(Dfunc[1])
                                                                else:
                                                                    if 16 == dataindex[1,i]:
                                                                        R1=dataindex[2,i]
                                                                        C1=dataindex[3,i]
                                                                        R2=dataindex[4,i]
                                                                        C2=dataindex[5,i]
                                                                        RNG=matlabarray(cat(R1,C1,R2,C2))
                                                                        data.covariantbase = copy(csvread(filename,R1,C1,RNG))
                                                                    else:
                                                                        if 17 == dataindex[1,i]:
                                                                            R1=dataindex[2,i]
                                                                            C1=dataindex[3,i]
                                                                            R2=dataindex[4,i]
                                                                            C2=dataindex[5,i]
                                                                            RNG=matlabarray(cat(R1,C1,R2,C2))
                                                                            data.contravariantbase = copy(csvread(filename,R1,C1,RNG))
                                                                        else:
                                                                            if 18 == dataindex[1,i]:
                                                                                R1=dataindex[2,i]
                                                                                C1=dataindex[3,i]
                                                                                R2=dataindex[4,i]
                                                                                C2=dataindex[5,i]
                                                                                RNG=matlabarray(cat(R1,C1,R2,C2))
                                                                                data.metriccoefficients = copy(csvread(filename,R1,C1,RNG))
                                                                            else:
                                                                                if 19 == dataindex[1,i]:
                                                                                    R1=dataindex[2,i]
                                                                                    C1=dataindex[3,i]
                                                                                    R2=dataindex[4,i]
                                                                                    C2=dataindex[5,i]
                                                                                    RNG=matlabarray(cat(R1,C1,R2,C2))
                                                                                    data.J = copy(csvread(filename,R1,C1,RNG))
                                                                                else:
                                                                                    if 20 == dataindex[1,i]:
                                                                                        R1=dataindex[2,i]
                                                                                        C1=dataindex[3,i]
                                                                                        R2=dataindex[4,i]
                                                                                        C2=dataindex[5,i]
                                                                                        RNG=matlabarray(cat(R1,C1,R2,C2))
                                                                                        data.g = copy(csvread(filename,R1,C1,RNG))
                                                                                    else:
                                                                                        if 21 == dataindex[1,i]:
                                                                                            R1=dataindex[2,i]
                                                                                            C1=dataindex[3,i]
                                                                                            R2=dataindex[4,i]
                                                                                            C2=dataindex[5,i]
                                                                                            RNG=matlabarray(cat(R1,C1,R2,C2))
                                                                                            data.reciprocalmetriccoefficients = copy(csvread(filename,R1,C1,RNG))
                                                                                        else:
                                                                                            if 22 == dataindex[1,i]:
                                                                                                R1=dataindex[2,i]
                                                                                                C1=dataindex[3,i]
                                                                                                R2=dataindex[4,i]
                                                                                                C2=dataindex[5,i]
                                                                                                RNG=matlabarray(cat(R1,C1,R2,C2))
                                                                                                data.firstChristoffelsymbol = copy(csvread(filename,R1,C1,RNG))
                                                                                            else:
                                                                                                if 23 == dataindex[1,i]:
                                                                                                    R1=dataindex[2,i]
                                                                                                    C1=dataindex[3,i]
                                                                                                    R2=dataindex[4,i]
                                                                                                    C2=dataindex[5,i]
                                                                                                    RNG=matlabarray(cat(R1,C1,R2,C2))
                                                                                                    data.secondChristoffelsymbol = copy(csvread(filename,R1,C1,RNG))
                                                                                                else:
                                                                                                    if 24 == dataindex[1,i]:
                                                                                                        R1=dataindex[2,i]
                                                                                                        C1=dataindex[3,i]
                                                                                                        R2=dataindex[4,i]
                                                                                                        C2=dataindex[5,i]
                                                                                                        RNG=matlabarray(cat(R1,C1,R2,C2))
                                                                                                        data.Riemanntensor = copy(csvread(filename,R1,C1,RNG))
                                                                                                    else:
                                                                                                        if 25 == dataindex[1,i]:
                                                                                                            R1=dataindex[2,i]
                                                                                                            C1=dataindex[3,i]
                                                                                                            R2=dataindex[4,i]
                                                                                                            C2=dataindex[5,i]
                                                                                                            RNG=matlabarray(cat(R1,C1,R2,C2))
                                                                                                            data.Riccitensor = copy(csvread(filename,R1,C1,RNG))
                                                                                                        else:
                                                                                                            if 26 == dataindex[1,i]:
                                                                                                                R1=dataindex[2,i]
                                                                                                                C1=dataindex[3,i]
                                                                                                                R2=dataindex[4,i]
                                                                                                                C2=dataindex[5,i]
                                                                                                                RNG=matlabarray(cat(R1,C1,R2,C2))
                                                                                                                data.R = copy(csvread(filename,R1,C1,RNG))
                                                                                                            else:
                                                                                                                if 27 == dataindex[1,i]:
                                                                                                                    R1=dataindex[2,i]
                                                                                                                    C1=dataindex[3,i]
                                                                                                                    R2=dataindex[4,i]
                                                                                                                    C2=dataindex[5,i]
                                                                                                                    RNG=matlabarray(cat(R1,C1,R2,C2))
                                                                                                                    data.rho = copy(csvread(filename,R1,C1,RNG))
                                                                                                                else:
                                                                                                                    if 28 == dataindex[1,i]:
                                                                                                                        R1=dataindex[2,i]
                                                                                                                        C1=dataindex[3,i]
                                                                                                                        R2=dataindex[4,i]
                                                                                                                        C2=dataindex[5,i]
                                                                                                                        RNG=matlabarray(cat(R1,C1,R2,C2))
                                                                                                                        data.u = copy(csvread(filename,R1,C1,RNG))
                                                                                                                    else:
                                                                                                                        if 29 == dataindex[1,i]:
                                                                                                                            R1=dataindex[2,i]
                                                                                                                            C1=dataindex[3,i]
                                                                                                                            R2=dataindex[4,i]
                                                                                                                            C2=dataindex[5,i]
                                                                                                                            RNG=matlabarray(cat(R1,C1,R2,C2))
                                                                                                                            data.p = copy(csvread(filename,R1,C1,RNG))
                                                                                                                        else:
                                                                                                                            if 30 == dataindex[1,i]:
                                                                                                                                R1=dataindex[2,i]
                                                                                                                                C1=dataindex[3,i]
                                                                                                                                R2=dataindex[4,i]
                                                                                                                                C2=dataindex[5,i]
                                                                                                                                RNG=matlabarray(cat(R1,C1,R2,C2))
                                                                                                                                data.S = copy(csvread(filename,R1,C1,RNG))
                                                                                                                            else:
                                                                                                                                if 31 == dataindex[1,i]:
                                                                                                                                    R1=dataindex[2,i]
                                                                                                                                    C1=dataindex[3,i]
                                                                                                                                    R2=dataindex[4,i]
                                                                                                                                    C2=dataindex[5,i]
                                                                                                                                    RNG=matlabarray(cat(R1,C1,R2,C2))
                                                                                                                                    data.gammadot = copy(csvread(filename,R1,C1,RNG))
                                                                                                                                else:
                                                                                                                                    if 32 == dataindex[1,i]:
                                                                                                                                        R1=dataindex[2,i]
                                                                                                                                        C1=dataindex[3,i]
                                                                                                                                        R2=dataindex[4,i]
                                                                                                                                        C2=dataindex[5,i]
                                                                                                                                        RNG=matlabarray(cat(R1,C1,R2,C2))
                                                                                                                                        data.sigma = copy(csvread(filename,R1,C1,RNG))
                                                                                                                                    else:
                                                                                                                                        if 33 == dataindex[1,i]:
                                                                                                                                            R1=dataindex[2,i]
                                                                                                                                            C1=dataindex[3,i]
                                                                                                                                            R2=dataindex[4,i]
                                                                                                                                            C2=dataindex[5,i]
                                                                                                                                            RNG=matlabarray(cat(R1,C1,R2,C2))
                                                                                                                                            data.mu = copy(csvread(filename,R1,C1,RNG))
                                                                                                                                        else:
                                                                                                                                            if 34 == dataindex[1,i]:
                                                                                                                                                R1=dataindex[2,i]
                                                                                                                                                C1=dataindex[3,i]
                                                                                                                                                R2=dataindex[4,i]
                                                                                                                                                C2=dataindex[5,i]
                                                                                                                                                RNG=matlabarray(cat(R1,C1,R2,C2))
                                                                                                                                                data.tau = copy(csvread(filename,R1,C1,RNG))
                                                                                                                                            else:
                                                                                                                                                if 35 == dataindex[1,i]:
                                                                                                                                                    R1=dataindex[2,i]
                                                                                                                                                    C1=dataindex[3,i]
                                                                                                                                                    R2=dataindex[4,i]
                                                                                                                                                    C2=dataindex[5,i]
                                                                                                                                                    RNG=matlabarray(cat(R1,C1,R2,C2))
                                                                                                                                                    data.cs = copy(csvread(filename,R1,C1,RNG))
                                                                                                                                                else:
                                                                                                                                                    if 36 == dataindex[1,i]:
                                                                                                                                                        R1=dataindex[2,i]
                                                                                                                                                        C1=dataindex[3,i]
                                                                                                                                                        R2=dataindex[4,i]
                                                                                                                                                        C2=dataindex[5,i]
                                                                                                                                                        RNG=matlabarray(cat(R1,C1,R2,C2))
                                                                                                                                                        data.feq = copy(csvread(filename,R1,C1,RNG))
                                                                                                                                                    else:
                                                                                                                                                        if 37 == dataindex[1,i]:
                                                                                                                                                            R1=dataindex[2,i]
                                                                                                                                                            C1=dataindex[3,i]
                                                                                                                                                            R2=dataindex[4,i]
                                                                                                                                                            C2=dataindex[5,i]
                                                                                                                                                            RNG=matlabarray(cat(R1,C1,R2,C2))
                                                                                                                                                            data.f = copy(csvread(filename,R1,C1,RNG))
    
    return data