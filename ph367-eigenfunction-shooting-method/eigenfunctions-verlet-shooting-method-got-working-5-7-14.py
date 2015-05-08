from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

psi_old = 0						# value needed for solving the differential equation with the shooting method
psi = 1							# value needed for solving the differential equation with the shooting method
m = 1							# parametrized mass
hbar = 1						# parametrized value named for the area  in phase-space of uncertainty due to a single degree of freedom
L = 4.							# parametrized width of the infinite square-well
desiredPrecision = .1 			# precision for right boundary condition
energyDiff = 50 				# energy increment
En = 0							# current energy
dx = 0.01						# width of discretized of x-coordinates
xValues = np.arange(0,L,dx)		# actual values of x-coordinates
nodes = np.arange(1.,12.)		# list of energy-eigenstate-numbers
energies = np.zeros_like(nodes)	# initialize array for energy-values
rampy = True					# rampy potential in square well?
siney = False					# siney potential in square well?
potentialAdditionSize = 20		# play with me!
littleGuy = 5					# play with me!

def V(x):
	'add a potential to in the square-well'
	if rampy:
		if x<.25*L:
			returnVal = x/(.25*L)
		elif .25*L<x<L/2.:
			returnVal = 2-x/(.25*L)
		elif .5*L<x<.75*L:
			returnVal = 2-x/(.25*L)
		elif 3*L/4.<x:
			returnVal = -4+x/(.25*L)
		else:
			returnVal = (2-x)*littleGuy
	if siney:
		returnVal = np.sin(littleGuy*np.pi*x/L)
	return returnVal*potentialAdditionSize

def nodeCounter(values):
	'counts the nodes(roots not at ends) from a list of values'
	nodes = 0
	for n in range(len(values)-1):
		if np.sign(values[n]) != np.sign(values[n+1]):
			nodes += 1
	return nodes

def shoot(En):
	'shooting method finds another value based on previous two(two b.c. second order)'
	xValues   = np.arange(0,L,dx)
	psiValues = np.zeros(len(xValues))
	psiValues[1] = psi
	for i in range(2,len(xValues)):
		psiValues[i] = 2*(1+m*dx**2/hbar**2*(V(xValues[i-1])-En))*psiValues[i-1]-psiValues[i-2]
	return psiValues

def boundFinder(numNodes, En=En):
	'finds upper and lower bounds of energy-eigenvalue'
	while True:
		if nodeCounter(shoot(En)) <= numNodes:
			lowEnergyBound = En
			En += energyDiff
			if nodeCounter(shoot(En)) >= numNodes:
				highEnergyBound = En
				return [lowEnergyBound,highEnergyBound]
		if nodeCounter(shoot(En)) > numNodes:
			highEnergyBound = En
			En -= energyDiff
			if nodeCounter(shoot(En)) < numNodes:
				lowEnergyBound = En
				return [lowEnergyBound,highEnergyBound]

def bisection(lowEnergyBound,highEnergyBound,numNodes):
	'halves interval about energy-eigenvalue to the desired precision'
	while highEnergyBound-lowEnergyBound > desiredPrecision:
		if nodeCounter(shoot((highEnergyBound+lowEnergyBound)*.5)) <= numNodes:
			lowEnergyBound = (highEnergyBound+lowEnergyBound)*.5
		else:
			highEnergyBound = (highEnergyBound+lowEnergyBound)*.5
	return((highEnergyBound+lowEnergyBound)*.5)

# iterate through nodes, find energy-eigenvalues, plot eigenfunctions, and label plots with index-numbers
for i in range(len(nodes)):
	lowEnergyBound, highEnergyBound = boundFinder(nodes[i])
	energies[i] = bisection(lowEnergyBound,highEnergyBound,nodes[i])
	plottedPsiValues = shoot(energies[i])
	plt.plot(xValues,plottedPsiValues/(sum(abs(plottedPsiValues))/\
	len(plottedPsiValues))+(i+1)**2,label= str(i+1))

# plot potential, create legend, show plot 
potentialAddition = [V(x) for x in xValues]
plt.plot(xValues,potentialAddition,'k')
plt.legend(loc=0)
plt.show()
