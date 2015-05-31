from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import pylab

c = 300 # m/s
size = 20 # m
latestTime = 10 # max t-value in seconds
dt = 0.1 # step in seconds
dPosition = .01 
boundaries = [0,size]
pNewMatrix = np.zeros((size,size)) # matrix of positions
pMatrix = np.zeros_like(room)
pOldMatrix = np.zeros_like(room)
room[0][0] = 1 # apply an impulse to the system

def pOld(n,m,matrix):
    if n<=0 or m<=0 or n>=size or m>=size:
        return 0
    else:
        return matrix[n,m]

for timeStep in range(0,latestTime,dt):
    for m in range(size):
	    for n in range(size):
                # calculate the p-value at each position 
	        # use 2d version of centered verlet's
                p[n][m] = get(n,m+1,
    plt.imshow( room, interpolation='none')
    plt.show()
