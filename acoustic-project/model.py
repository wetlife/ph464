from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import time

a = 300 # m/s
size = 20 # m
latestTime = 90 # max t-value in seconds
dt = 0.1 # step in seconds
dx = dy = .01 # dPosition = dx = dy; positions are in a squared-lattice
pArray = np.zeros((3,size,size)) # p(T,N,M); matrices of room's pressure at times t-dt, t, and t+dt stored in a 3D array s.t. p[0]=pOldMatrix, p[1]=pMatrix, and p[2]=pNewMatrix

def p(timeStep,n,m):
    '''accesses matrices and enforces boundary conditions on them'''
    if n<=0 or m<=0 or n>=size or m>=size:
        return 0
    else:
        return pArray[timeStep][n][m]

pArray[2][3][4] = 1 # supply an impulse at the initial instant

for timeStep in range(0,latestTime):
    # set the current- and old-matrix values to increment time
    pArray[0] = pArray[1]
    pArray[1] = pArray[2]
    for m in range(size):
	    for n in range(size):
                # calculate the p-value at each position 
	        # use 2d version of centered verlet's
                pArray[2][n][m] = 2*p(1,n,m) +p(0,n,m,) +(dt/dx)**2\
                        *( p(1,n+1,m) +p(1,n-1,m) +p(1,n,m+1) +p(1,n,m-1) \
                        -4*p(1,n,m) )
    plt.imshow( pArray[2], interpolation='none')
    plt.legend()
    plt.show()
