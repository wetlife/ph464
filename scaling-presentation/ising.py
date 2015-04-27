from __future__ import division
import sys
import matplotlib.pyplot as plt
import numpy as np

latticeSize = int(np.sqrt(float(sys.argv[1]))) # number of sites in a row or column of the lattice
H = np.zeros((latticeSize,latticeSize)) # magnetic field
J = 1 # strength of neighbor-interactions
microstate = np.ones((latticeSize,latticeSize), int) # initial lattice state
T = 1111.25 # temperature, units depend on kb
kb = 1 # Boltzmann's constant
beta = 1/(kb*T) # 1/(kb T)
metropolizations = 100*latticeSize**2  # number of times to metropolize

def indexPicker(size):
    'randomly pick a single index'
    return np.floor((size)*np.random.random())

def val(i,j,array=microstate):
    'implements cyclic boundary conditions on lattice'
    return array[i%latticeSize,j%latticeSize]

def siteEnergy(i,j,siteValue=False):
    'calculate energy of site (i,j) when site has value siteValue'
    if not siteValue: siteValue = val(i,j)
    return (val(i,j,H) - J*(val(i+1,j) + val(i,j+1)))*siteValue

def localEnergyDifference(i,j):
    'calculate energy about site (i,j) when site has value siteValue'
    return -2*(val(i,j,H) - J*(val(i-1,j) + val(i,j-1) + val(i+1,j) + val(i,j+1)  ))*val(i,j)

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

### iterate metropolis algorithm
def metropolizer( ):
    'metropolize microstate number of times equivalent to metropolizations'
    for metropolisIterationIndex in range(metropolizations):
        metropolisIterationIndex += 1
        i = indexPicker(latticeSize)
        j = indexPicker(latticeSize)

        deltaEnergy = localEnergyDifference(i,j)
        if deltaEnergy <= 0:
            microstate[i%latticeSize,j%latticeSize] = -1*val(i,j)
        elif np.random.random()<np.exp(-deltaEnergy/(kb*T)):
            microstate[i%latticeSize,j%latticeSize] = -1*val(i,j)


print 'There are ', latticeSize**2, ' sites.'
print 'The lattice will be metropolized ', metropolizations,' times.'
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


#----TODO----       Plot metropolized microstate total energy vs. T
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
