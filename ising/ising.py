from __future__ import division
from numpy import ones,zeros,exp
from numpy.random import random
import matplotlib.pyplot as plt

latticeSize     = 10 # number of sites in a row or column of the lattice
H               = zeros((latticeSize,latticeSize)) # magnetic field
J               = 1 # strength of neighbor-interactions
microstate      = ones((latticeSize,latticeSize), int) # initial lattice state
T               = 1 # temperature, units depend on kb
kb              = 1 # Boltzmann's constant
beta            = 1/(kb*T) # 1/(kb T)

def indexPicker(size):
    'randomly pick a single index'
    return round((size)*random())

def val(i,j,array=microstate):
    'implements cyclic boundary conditions on lattice'
    return array[i%latticeSize,j%latticeSize]

def siteEnergy(i,j,siteValue=False):
    'calculate energy of site (i,j) when site has value siteValue'
    if not siteValue: siteValue = val(i,j)
    return (val(i,j,H) + J*(val(i+1,j) + val(i,j+1)))*siteValue

def totalEnergy(flipValue=False,i=False,j=False): # calc. latt. NRG w/a flipped val.
    'return total energy of lattice'
    returnEnergy = 0;
    for i in range(latticeSize):
        for j in range(latticeSize):
            returnEnergy = returnEnergy + siteEnergy(i,j)
    if flipValue:
        returnEnergy = returnEnergy - siteEnergy(i,j) + siteEnergy(i,j,-1*val(i,j))
    return returnEnergy

def totalEnergyDifference(i,j):
    return totalEnergy()-totalEnergy(True,i,j)

#def siteEnergyDifference(i,j):
#    returnEnergyDifference = 0
#    for i in [i-1,i]:
#        for j in [j-1,j]:
#            returnEnergyDifference += siteEnergy(i,j)-siteEnergy(i,j,-1*val(i,j))
#    return returnEnergyDifference

### iterate metropolis algorithm
metropolizations = latticeSize**2 # number of times to metropolize
for metropolisIterationIndex in range(metropolizations):
    metropolisIterationIndex += 1
    i = indexPicker(latticeSize)
    j = indexPicker(latticeSize)
   
    if metropolisIterationIndex%10==0:
        print 'Metropolization ', metropolisIterationIndex, ': (', i, ',', j, ')', val(i,j)
        print "Current energy of microstate is ", totalEnergy()
    if siteEnergy(i,j,-1*val(i,j)) <= siteEnergy(i,j):
        microstate[i%latticeSize,j%latticeSize] = -1*val(i,j)
        continue
    elif random()<exp(-1*abs(siteEnergy(i,j,-1*val(i,j)) - siteEnergy(i,j))/(kb*T)):
        microstate[i%latticeSize,j%latticeSize] = -1*val(i,j)
        continue
    else:
        continue

#for i in range(latticeSize):
#    for f in range(latticeSize):
#        if totalEnergyDifference(i,j) != siteEnergyDifference(i,j):
#            print "ENERGY DIFFERENCES NOT EQUIVALENT!!!!!!"
#            print (i,j)
#        else: print "xxxxxxSUCCESSxxxxxx"

plt.imshow(microstate,interpolation='none')
plt.show()

        ### TODO:   
#xxxxxxxxxxxxxxxxxxxFinish metropolis algorithm
#    FAIL           Does site energy difference == total energy difference?
#xxxxxxxxxxxxxxxxxxxTest metropolis algorithm
#                   Plot metropolized microstate total energy vs. T
