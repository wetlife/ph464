import numpy as np
import matplotlib.pyplot as plt
import os

os.chdir('~/local-osu/ph464/scaling-presentation/data/')
# get totalDiff-times from file:
totTimes = np.loadtxt( 'wngr412-pc15-tot-1to100.txt')
# construct list of n-values (input sizes);
totNs = [(range(len(totTimes))[n]+1)**2 for n in range(len(totTimes))]
