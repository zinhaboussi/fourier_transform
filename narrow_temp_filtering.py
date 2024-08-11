#Algorithm Description:
#Narrow termporal filtering is a technique used to isolate specific
#frequency components from a tine-domain signal. To implement it,
#first we need transform our time-domain signal to frequency-domain 
#using FFT.
#Then apply filter to retain only the desired frequencies while zeroing
#out the others.
#at end we use IFFT to convert the filtered frequency-domain signal
#back to the time-domain.

import numpy as np
import scipy.io as sio
import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft

#Load Data
matdata= sio.loadmat('braindata.mat')
timevec= matdata['timevec'][0]
srate= matdata['srate'][0]
braindata= matdata['braindata'][0]
n= len(timevec)

#figure with 3 plots
fig,axs= plt.subplots(3,1,figsize=(10,15))

#Plot time-domain signal
axs[0].plot(timevec,braindata)
axs[0].set_xlim([-.5, 1.5])
axs[0].set_xlabel('Time (sec)')
axs[0].set_ylabel('Voltage (µV)')
axs[0].set_title('Time domain')

#Compute power spectrum
dataFreq= fft(braindata)/n
powsepct= 2* np.abs(dataFreq)**2
hz= np.linspace(0, srate, n)

#Plot power spectrum
axs[1].plot(hz, powsepct[:len(hz)])
axs[1].set_xlim([0, 100])
axs[1].set_ylim([0, 500])
axs[1].set_xlabel('Frequency (Hz)')
axs[1].set_ylabel('Voltage (µV)')
axs[1].set_title('Frequency domain')

#Specify which frequencies to filter
peakFiltFreqs= [2,47]
c= 'kr'

#Loop over frequencies
for fi in range(len(peakFiltFreqs)):
	#construct the filter
	x= hz-peakFiltFreqs[fi] #shifts the freq axis to the center the Guassian filter at the desired frequency
	fx= np.exp(-(x/4)**2) #creating a Guassian function (fx) centered at the shifted freq. The higher the exp value is the narrower the width of the Gaussian will be (to avoid shjarp edges)
	
	
	#Apply the filter to the data
	filtdata= 2*np.real(ifft(np.multiply(dataFreq,fx))) #performs element-wise multiplication to the original data spectrum with the Gaussian filter to effectively filters out the freqs outside the Gaussian bandwidth, after we compute the ifft of the multiplied spectra.
	
	#Show the results
	axs[2].plot(timevec,filtdata, c[fi], label='%g Hz' %peakFiltFreqs[fi])
	
axs[2].set_xlim([-.5, 1.5])
axs[2].set_xlabel('Time (sec)')
axs[2].set_ylabel('Voltage (µV)')
axs[2].set_title('Time domain')
axs[2].legend()

plt.tight_layout()
plt.show()

