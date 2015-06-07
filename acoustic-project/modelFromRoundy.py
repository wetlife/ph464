from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import time
from random import random
#import pylab

plt.ion()
plt.figure()

c = 300 # m/s
size = 200 # m
latestTime = 90000 # max t-value in seconds
dt = 0.005 # step in seconds
dx = dy = .01 # dPosition = dx = dy; positions are in a squared-lattice
pArray = np.zeros((3,size,size)) # p(T,N,M); matrices of room's pressure at times t-dt, t, and t+dt stored in a 3D array s.t. p[0]=pOldMatrix, p[1]=pMatrix, and p[2]=pNewMatrix
percentageChanceOfImpulse = 10
cyclesPerFrame = 3
impulseFrequency = 

def p(timeStep,n,m):
    '''accesses matrices and enforces boundary conditions on them'''
    if n<=0 or m<=0 or n>=size or m>=size:
        return 0
    # diffracting boundary conditions below
    elif n < notchDepth and m in 
    else:
        return pArray[timeStep][n][m]

X,Y = np.meshgrid(np.linspace(0, size*dx, size), np.linspace(0, size*dx, size))

pArray[2][size/2][size/2] = 1 # supply an impulse at the initial instant
pArray[1][size/2][size/2] = 1 # supply an impulse at the initial instant

pArray[2] = np.exp(-((X-size*dx/2)**2 + (Y-size*dx/2)**2)/0.1**2)
pArray[1] = np.exp(-((X-size*dx/2)**2 + (Y-size*dx/2)**2)/0.1**2)

i = 0
for timeStep in range(0,latestTime):
    # set the current- and old-matrix values to increment time
    pArray[0] = pArray[1]
    pArray[1] = pArray[2]
    for m in range(size):
	    for n in range(size):
                # calculate the p-value at each position 
	        # use 2d version of centered verlet's
                pArray[2][n][m] = 2*p(1,n,m) -p(0,n,m,) +(dt/dx)**2\
                        *( p(1,n+1,m) +p(1,n-1,m) +p(1,n,m+1) +p(1,n,m-1) \
                        -4*p(1,n,m) )
    if random() > 1-percentageChanceOfImpulse/100:
        pArray[2][int(random()*size)][int(random()*size)] = 1
    i = i + 1
    if i % cyclesPerFrame == 0:
        plt.clf()
        plt.imshow( pArray[2], interpolation='none')
        plt.colorbar()
        plt.draw()
    #plt.show()
    #input('paused for debugging')
    #time.sleep(1)
