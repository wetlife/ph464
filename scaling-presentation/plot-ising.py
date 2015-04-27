import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt( 'time-ising.txt' )
print 'Ns'
print data[:,0]
print 'times'
print data[:,1]

plt.loglog(data[:,0],data[:,1],'r*-')

Ns = 10**np.arange(0.0, 5, 0.5)
plt.loglog(Ns,0.7 + 0.002*Ns,'b-')
plt.show()

