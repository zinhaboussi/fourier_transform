import numpy as np
import math
import matplotlib.pyplot as plt
import scipy.fftpack
import random
from mpl_toolkits.mplot3d import Axes3D

# create the signal
samrate= 1000 #sampling rate
time= np.arange(0. ,2., 1/samrate) # Time vector from 0 to 2 seconds with intervals of 1/samrate

pnts = len(time) # Number of time points
signal= 2.5*np.sin(2*np.pi*4*time)+1.5*np.sin(2*np.pi*6.5*time)

fourTime= np.array(range(pnts)) / pnts #normalized frequency vector used to generate the complex sine waves
fourCoefs= np.zeros((len(signal)), dtype=complex) #array initialized to store the fourier coefficients, which will be complex numbers

for freq in range(pnts):
    #create complex sine wave
    csw= np.exp(-1j*2*np.pi*freq*fourTime) # this line generate complex sine wave with a frequency proportional to freq
    
    #compute dot product between sine wave and signal
    fourCoefs[freq]= np.sum(np.multiply(signal, csw)) / pnts #it gives the fourier coefficient for the current freq, the result is divided by the number of points to normalize the coefficient

ampls= 2*np.abs(fourCoefs) #calculate the amplitude

#compute frequencies vector
hz= np.linspace(0, samrate/2, int(math.floor(pnts/2.)+1)) # creates a linearly spaced array from 0 to the Nyquist frequency (half the sampling rate).

plt.stem(hz, ampls[range(len(hz))])
plt.xlabel("Frequency (Hz)"), plt.ylabel("Amplitude (a.u.)")
plt.xlim(0,10)
plt.show()