from __future__ import division
import numpy as np
import matplotlib as plt

latticeDimension = 3 # number of sites in a row or column of the lattice
H = np.zeros((latticeDimension,latticeDimension)) # magnetic field
J = 1 # strength of neighbor-interactions
microstate = np.ones((latticeDimension,latticeDimension), int) # initial lattice state

def indexPicker(dimension):
	'randomly pick a single index'
	return round((dimension-1)*np.random.rand())

def val(i,j):
    'implements cyclic boundary conditions on lattice'
    return microstate[i%latticeDimension,j%latticeDimension]

def siteEnergy(i,j,siteValue):
    'calculate energy of site (i,j) when site has value siteValue'
    return H[i%latticeDimension,j%latticeDimension]*val(i,j)\
            + J*siteValue*(val(i-1,j) +\
            val(i+1,j) +\
            val(i,j-1) +\
            val(i,j+1))

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
    for i in range(latticeDimension):
        for j in range(latticeDimension):
            returnEnergy = returnEnergy + siteEnergy(i,j,val(i,j))
    return returnEnergy

## implement metropolis algorithm
for metropolisIteration in range(2*latticeDimension**2):
	
    i = indexPicker(latticeDimension));
    j = indexPicker(latticeDimension));
    siteValue = val(i,j)
    print 'element ', n, ':', '(', i, ',', j, ')', val(i,j) 
    if localEnergy(i,j,-1*siteValue) < siteEnergy(i,j,siteValue):
        microstate[i,j] = -1*val(i,j)
        continue
    elif localEnergy(i,j,-1*siteValue) >= localEnergy(i,j,siteValue):
        microstate[i,j] = -1*val(i,j)
        continue

