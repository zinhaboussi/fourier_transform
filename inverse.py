import numpy as np
import math
import matplotlib.pyplot as plt

#define parameters and generate signal
srate = 1000
time = np.arange(0, 2.0, 1/srate)
pnts=  len(time)
signal= 2.5*np.sin(2*np.pi*4*time) + 1.5 *np.sin(2*np.pi*6.5*time)

#prepare fourier transform
fourTime= np.array(np.arange(0, pnts))/pnts
fCoefs= np.zeros(len(signal),dtype=complex) # Array to store fourier coefs

#computer fourier coefs
for fi in range(0,pnts):
    csw=np.exp(-1j*2*np.pi*fi*fourTime)
    fCoefs[fi]=np.sum(np.multiply(signal, csw))

#extract amplitudes
ampls= np.abs(fCoefs)/pnts
ampls[range(1,len(ampls))]= 2*ampls[range(1,len(ampls))] #Double the amplitude except for the DC component

#compute frequency vector
hz= np.linspace(0,srate/2, num=math.floor(pnts/2)+1)

#inverse fourier transform

#initialize time-domain reconstruction
reconSignal= np.zeros(len(signal))

for fi in range(0,pnts):
    csw= fCoefs[fi]*np.exp(1j*2*np.pi*fi*fourTime)
    reconSignal= reconSignal+csw

#divide by numbers of points to normalize
reconSignal= reconSignal/pnts

#plot the original and reconstructed signal
plt.plot(time,signal,"b--",label="origianl")
plt.plot(time,np.real(reconSignal),"ro",label="reconstructed")
plt.legend()
plt.show()


