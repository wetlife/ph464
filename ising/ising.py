from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

latticeSize = 3 # number of sites in a row or column of the lattice
H = np.zeros((latticeSize,latticeSize)) # magnetic field
J = 1 # strength of neighbor-interactions
microstate = np.ones((latticeSize,latticeSize), int) # initial lattice state

def indexPicker(dimension):
	'randomly pick a single index'
	return round((dimension-1)*np.random.rand())

def val(i,j):
    'implements cyclic boundary conditions on lattice'
    return microstate[i%latticeSize,j%latticeSize]

def siteEnergy(i,j,siteValue):
    'calculate energy of site (i,j) when site has value siteValue'
    return H[i%latticeSize,j%latticeSize]*val(i,j) + J*siteValue*(val(i-1,j) + val(i+1,j) + val(i,j-1) + val(i,j+1))

def localEnergy(i,j,siteValue):
    'calculate energy of (i,j) site and nearest neighbors'
    returnEnergy = 0
    for iAndNeighbors in range(i-1,i+2):
        for jAndNeighbors in range(j-1,j+2):
            returnEnergy = returnEnergy + siteEnergy(iAndNeighbors,jAndNeighbors,val(iAndNeighbors,jAndNeighbors))
    return returnEnergy

def totalEnergy():
    'return total energy of lattice'
    returnEnergy = 0;
    for i in range(latticeSize):
        for j in range(latticeSize):
            returnEnergy = returnEnergy + siteEnergy(i,j,val(i,j))
    return returnEnergy
    
print totalEnergy()

A = np.random.rand(50,50)
plt.imshow(A, interpolation='nearest')
plt.show()


## implement metropolis algorithm
#for metropolisIteration in range(2*latticeSize**2):
	
    #i = indexPicker(latticeSize));
    #j = indexPicker(latticeSize));
    #siteValue = val(i,j)
    #print 'element ', n, ':', '(', i, ',', j, ')', val(i,j) 
    #if localEnergy(i,j,-1*siteValue) < siteEnergy(i,j,siteValue):
        #microstate[i,j] = -1*val(i,j)
        #continue
    #elif siteEnergy(i,j,-1*siteValue) >= siteEnergy(i,j,siteValue):
        #microstate[i,j] = -1*val(i,j)
        #continue

