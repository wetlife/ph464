from __future__ import division
import sys
from numpy import ones,zeros,exp,arange,floor
from numpy.random import random
import matplotlib.pyplot as plt

latticeSize         = int(sys.argv[1]) # number of sites in a row or column of the lattice
H                   = zeros((latticeSize,latticeSize)) # magnetic field
J                   = 1 # strength of neighbor-interactions
microstate          = ones((latticeSize,latticeSize), int) # initial lattice state
T                   = 1111.25 # temperature, units depend on kb
kb                  = 1 # Boltzmann's constant
beta                = 1/(kb*T) # 1/(kb T)
metropolizations    = 1000  # number of times to metropolize

def indexPicker(size):
    'randomly pick a single index'
    return floor((size)*random())

def val(i,j,array=microstate):
    'implements cyclic boundary conditions on lattice'
    return array[i%latticeSize,j%latticeSize]

def siteEnergy(i,j,siteValue=False):
    'calculate energy of site (i,j) when site has value siteValue'
    if not siteValue: siteValue = val(i,j)
    return (val(i,j,H) + J*(val(i+1,j) + val(i,j+1)))*siteValue

def totalEnergy(): # calc. latt. NRG w/a flipped val.
    'return total energy of lattice'
    returnEnergy = 0
    for i in range(latticeSize):
        for j in range(latticeSize):
            returnEnergy = returnEnergy + siteEnergy(i,j)
    return returnEnergy

def totalEnergyDifference(i,j):
    microstate[i,j] *= -1
    flippedEnergy = totalEnergy()
    microstate[i,j] *= -1
    return totalEnergy() - flippedEnergy

#def siteEnergyDifference(i,j):
#    returnEnergyDifference = 0
#    for i in [i-1,i]:
#        for j in [j-1,j]:
#            returnEnergyDifference += siteEnergy(i,j)-siteEnergy(i,j,-1*val(i,j))
#    return returnEnergyDifference

### iterate metropolis algorithm
def metropolizer(metropolizations=metropolizations):
    'metropolize microstate number of times equivalent to metropolizations'
    for metropolisIterationIndex in range(metropolizations):
        metropolisIterationIndex += 1
        i = indexPicker(latticeSize)
        j = indexPicker(latticeSize)

#        if metropolisIterationIndex%10==0:
#            print 'Metropolization ', metropolisIterationIndex, ': (', i, ',', j, ')', val(i,j)
#            print "Current energy of microstate is ", totalEnergy()
        deltaEnergy = totalEnergyDifference(i,j)
        if deltaEnergy <= 0:
            microstate[i%latticeSize,j%latticeSize] = -1*val(i,j)
        elif random()<exp(-deltaEnergy/(kb*T)):
            microstate[i%latticeSize,j%latticeSize] = -1*val(i,j)


metropolizer()
print 'total energy is ', totalEnergy()
#plt.imshow(microstate,interpolation='none')
#plt.show()
#
#energyOfTemperatureIterations = 10
#energyAndTemperatureTuples = [(0,0)]*energyOfTemperatureIterations
#print '######################################'
#print 'lattice size is ',latticeSize
#print '######################################'
#print 'T-values should be integer steps from -15 to 15'
#for k in range(energyOfTemperatureIterations):
#    T = 30*(k-5)
#    metropolizer()
#    print '######################################'
#    print 'iteration = ', k
#    print 'T         = ', T
#    print 'Energy    = ', totalEnergy()
#    energyAndTemperatureTuples[k] = (T,totalEnergy())
#    print 'stored value ', energyAndTemperatureTuples[k]
#

    

        ### TODO ###   
#xxxxxxxxxxxxxxxxxxxFinish metropolis algorithm
#----FAIL----       Does site energy difference == total energy difference?
#xxxxxxxxxxxxxxxxxxxTest metropolis algorithm
#----TODO----       Plot metropolized microstate total energy vs. T

#TODO:
#-implement some way to find totalEnergy(temperature), call this E(T) below
#-function iterates over E(T) for several T-values
#   -index with parametrized range of integers
#   -converts those integers via parametrized algorithm to a range of temp-values
#   -(T,E) = (T, totalEnergy(T)
#   -(T,E) to an array for later plotting
#-function plots array of (T,E) as E versus T

#for i in range(latticeSize):
#    for f in range(latticeSize):
#        if totalEnergyDifference(i,j) != siteEnergyDifference(i,j):
#            print "ENERGY DIFFERENCES NOT EQUIVALENT!!!!!!"
#            print (i,j)
#        else: print "xxxxxxSUCCESSxxxxxx"
#   -convert indices to temperatures
#   -
#   -convert indices to temperatures
#   -
#   -convert indices to temperatures
#   -
