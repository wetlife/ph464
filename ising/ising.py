from __future__ import division
import sys
import matplotlib.pyplot as plt
import numpy as np

try: latticeSize = int(sys.argv[1]) # number of sites in a row 
except: latticeSize = 10            # or column of the lattice
H = np.zeros((latticeSize,latticeSize)) # magnetic field
J = 1 # strength of neighbor-interactions
microstate = np.ones((latticeSize,latticeSize), int) # initial lattice state
T = .25 # temperature, units depend on kb
kb = 1 # Boltzmann's constant
metropolizationsFactor = 100
metropolizations = metropolizationsFactor*(latticeSize)**2  # metropolizations to equilibrate 
temperatures = np.logspace(0,2,num=32)
energies = np.zeros(len(temperatures))
magnetizations = np.zeros(len(temperatures))

def indexPicker(size):
    'randomly pick a single index'
    return np.floor((size)*np.random.random())

def val(i,j,array=microstate):
    'implements cyclic boundary conditions on lattice'
    return array[i%latticeSize, j%latticeSize]

def siteEnergy(i,j,siteValue=False):
    'calculate energy of site (i,j) when site has value siteValue'
    if not siteValue: siteValue = val(i,j)
    return (val(i,j,H) - J*(val(i+1,j) + val(i,j+1)))*siteValue

def localEnergyDifference(i,j):
    'calculate energy about site (i,j) when site has value siteValue'
    return -2*(-val(i,j,H)-J*(val(i-1,j)+val(i,j-1)+val(i+1,j)+val(i,j+1)))*val(i,j)

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
    return flippedEnergy - totalEnergy()

def metropolizer(metropolizations):
    'metropolize microstate a number of times equivalent to metropolizations'
    energy = totalEnergy()
    Ei = energy
    for metropolisIterationIndex in range(metropolizations):
        i = indexPicker(latticeSize)
        j = indexPicker(latticeSize)
        deltaEnergy = localEnergyDifference(i,j)
        Ei = Ei + deltaEnergy
        if deltaEnergy <= 0:
            microstate[i%latticeSize,j%latticeSize] = -1*val(i,j)
        elif np.random.random()<np.exp(-deltaEnergy/(kb*T)):
            microstate[i%latticeSize,j%latticeSize] = -1*val(i,j)
        energy = energy + Ei
    return energy

def U(T):
    metropolizer(metropolizations);
    allEnergies = np.zeros(metropolizations)
    meanEnergy = totalEnergy()
    for k in range(metropolizations):
        allEnergies[k] = metropolizer(1)
    meanEnergy = np.sum(allEnergies)/metropolizations
    return meanEnergy

def M(T):
    magnetization = 0
    for i in range(latticeSize):
        for j in range(latticeSize):
            magnetization += val(i,j)
    return abs(magnetization)/latticeSize**2 

print 'There are ', latticeSize**2, ' sites.'
print 'The lattice is metropolized', metropolizations,\
'times to bring the system to "thermal equilibrium" prior',\
'to making each measurement.'

for k in range(len(temperatures)):
    T = temperatures[k]
    energy = U(T)
    magnetization = M(T)
    print 'U( T=',T, ') is',energy
    print 'M( T=',T, ') is',magnetization
    energies[k] = energy
    magnetizations[k] = magnetization

#plt.figure(1)  
#plt.imshow(microstate, interpolation='none') 

plt.figure(2)
plt.subplot(2,1,1)
plt.semilogx( temperatures, energies, 'gx' )
plt.grid(True,which="both",ls="-")
plt.title('Energy Vs. Temperature')

plt.subplot(2,1,2)
plt.semilogx( temperatures, magnetizations, 'r.' )
plt.grid(True,which="both",ls="-")
plt.title('Expected Magnetization of a Lattice Node Vs. Temperature')
plt.show()
