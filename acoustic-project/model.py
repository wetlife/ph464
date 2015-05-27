from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import pylab

room = np.zeros((100,100))
room[0][0] = 1



image = plt.imshow( room, interpolation='none')
plt.show()
