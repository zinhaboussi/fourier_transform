#Algorithm Description:
#The brain waves algorithm analyzes EEG data to identify rhythmic 
#patterns, such as the alpha rhythm, by computing and visualizing the
#the time-domain signal and its frequency-domain amplitude spectrum.

import numpy as np
import scipy.io as sio
import matplotlib.pyplot as plt
from scipy.fftpack import fft

matdata = sio.loadmat('EEGrestingState.mat')

eegdata= matdata['eegdata']
eegdata= eegdata[0]
srate= matdata['srate']
srate= srate[0]

n=len(eegdata)
timevec= np.arange(n)/srate

dataX= fft(eegdata)/n
ampspect= 2*abs(dataX)
hz= np.linspace(0,srate/2,int(np.floor(n/2)+1))

plt.plot(timevec,eegdata)
plt.xlabel('Time (sec)')
plt.ylabel('Amplitude (µV)')
plt.title('Time-domain signal')

plt.plot(hz, ampspect[0:int(np.floor(n/2)+1)])
plt.xlim([0, 70])
plt.ylim([0, .6])
plt.title('Frequency-domain')
plt.show()	
