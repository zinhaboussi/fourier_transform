#This code demonstrates the relationship between sampling rate, signal length, and the number of time points used for calculating Fourier frequencies.
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft

#temporal parameters
srates=[100,100,1000]
timedur=[1,10,1]
freq=5 

#setup plotting
fig,ax= plt.subplots(2,1,figsize=(10,9))
colors="kmb"
symbols="op."
legendText= [0]*len(srates)

for parami in range(len(srates)):
	
	#define sampling rate in this round
	srate= srates[parami]
	
	#define time
	time=np.arange(-1,timedur[parami],1/srate)
	
	#crate signal (Morlet wavelet)
	signal = np.multiply( np.cos(2*np.pi*freq*time) , np.exp( (-time**2) / .05 ) )
	
	#compute FFT and normalize 
	signalX = fft(signal)
	
	signalX = signalX/np.max(signalX) #Normalizes the magnitude of the FFT results by dividing by the maximum value in `signalX`. This helps in better visualizing the relative amplitudes of different frequency components.
    
	#define vector of freqs in Hz
	hz= np.linspace(0,srate/2,int(np.floor(len(signal)/2)+1)) #Creates a vector of frequencies in Hz ranging from 0 to half the sampling rate using `np.linspace`. This is because the FFT result has information only up to the Nyquist frequency (half the sampling rate).


	
	#plot  time-domain signal
	ax[0].plot(time,signal,color=colors[parami],marker=symbols[parami])
	
	#plot frequency-domain signal
	ax[1].plot(hz,np.abs(signalX[0:len(hz)]),color=colors[parami],marker=symbols[parami]) #Plots the magnitude spectrum (absolute value of the FFT) in the second subplot, which represents the frequency content of the signal. Only the frequencies corresponding to the created `hz` vector are plotted.


	
	#legend text
	legendText[parami]=f'srate={srates[parami]}, N={timedur[parami]+1} s'#Updates the legend text with information about the current sampling rate and signal duration.
	
ax[0].set_xlim([-1,1])
ax[0].set_xlabel('Time (s)')
ax[0].set_ylabel('Amplitude')
ax[0].set_title('Time domain')
ax[0].legend(legendText)

ax[1].set_xlabel('Frequency (Hz)')
ax[1].set_ylabel('Amplitude')
ax[1].set_title('Frequency domain')
ax[1].legend(legendText)

plt.show()
