from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import pylab

c = 300 # m/s
room = np.zeros((size,size)) # room is represented by a matrix of positions
size = 20 # m
room[0][0] = 1 # an impulse applied to the system
latestTime = 10 # max t-value in seconds
dt = 0.1 # step in seconds
positionSpacing = .01 

for timeStep in range(0,latestTime,dt)
    for m in range(size):
	    for n in range(size):
                # calculate the p-value for each node
		# use 2d version of centered verlet's 
		p[n][m] = 



    plt.imshow( room, interpolation='none')
    plt.show()
