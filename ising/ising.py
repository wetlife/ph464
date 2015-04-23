from __future__ import division
from numpy import ones zeros
from numpy.random import random
import matplotlib.pyplot as plt

latticeSize = 3 # number of sites in a row or column of the lattice
H = np.zeros((latticeSize,latticeSize)) # magnetic field
J = 1 # strength of neighbor-interactions
microstate = np.ones((latticeSize,latticeSize), int) # initial lattice state
beta = 1/T # 1/(K_B T)

def indexPicker(size):
    'randomly pick a single index'
    return round((size-1)*random())

def val(i,j,array=microstate):
    'implements cyclic boundary conditions on lattice'
    return array[i%latticeSize,j%latticeSize]

def siteEnergy(i,j,siteValue=val(i,j)):
    'calculate energy of site (i,j) when site has value siteValue'
    return val(i,j,H)*val(i,j) + J*siteValue*(val(i+1,j) + val(i,j+1))

#def localEnergy(i,j,siteValue):
#    'calculate energy of (i,j) site and nearest neighbors'
#    returnEnergy = 0
#    for iAndNeighbors in range(i-1,i+2):
#        for jAndNeighbors in range(j-1,j+2):
#            returnEnergy = returnEnergy + siteEnergy(iAndNeighbors,jAndNeighbors,val(iAndNeighbors,jAndNeighbors))
#    return returnEnergy

def totalEnergy(flipPosition=False): # takes argument of form [siteValue,i,j]
    'return total energy of lattice'
    returnEnergy = 0;
    for i in range(latticeSize):
        for j in range(latticeSize):
            returnEnergy = returnEnergy + siteEnergy(i,j)
    if flipPosition:
        returnEnergy = returnEnergy - siteEnergy(i,j) + siteEnergy(i,j,-1*val(i,j)
    return returnEnergy

def totalEnergyDifference():
totalEnergyDifference = 1
    
print totalEnergy()

#plt.imshow(microstate)
#plt.show()

## iterate metropolis algorithm
metropolizations = range(latticeSize**2) # number of times to do metropolis alg
for metropolisIterationIndex in metropolizations:
    i = indexPicker(latticeSize));
    j = indexPicker(latticeSize));
    siteValue = val(i,j)
    
    print 'Metropolization ', n, ': (', i, ',', j, ')', val(i,j)
    if siteEnergy(i,j,-1*val(i,j)) <= siteEnergy(i,j)
        microstate[i,j] = -1*val(i,j)
        continue
    elif siteEnergy(i,j,-1*siteValue) - siteEnergy(i,j,siteValue)) < -T*math.log(random.rand:
        microstate[i,j] = -1*val(i,j)
        continue

        ### TODO:   
#                   Finish metropolis algorithm
#                   Does site energy difference == total energy differwnce?
#                   Finish metropolis algorithm
#                   Test metropolis algorithm
#                   Plot metropolized microstate total energy vs. T
