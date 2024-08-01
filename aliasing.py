#this code simulates aliasing, a phenomenon that occurs when a signal is sampled at a rate insuffiecent to capture all its frequency components.
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.fftpack import fft

#Simulation parameters
srate=1000 #sampling rate
time= np.arange(0,1,1/srate) #this creates an array of time points from 0 to just below 1 with a step of 1/1000
npnts=len(time) #calculate the number of data points 
signal=	np.sin(2*np.pi*5*time) #sinusoidal signal

#Measurement Parameters
msrate= 6 # defines the sampling rate of the measured signal
mtime=np.arange(0,1,1/msrate) # creates an array containing timestamps for the measured signal
midx= np.zeros(len(mtime),dtype=int) #initializes an empty array of integers with the same length as mtime, to store indices of the closest points in the analog signal for each measured sample.
for i in range(0,len(midx)):
	midx[i]=np.argmin(np.abs(time-mtime[i])) #finds the index in the time array correspong to the point closest in time to the current measured sample time "mtime[i]"

#plotting the time domain
plt.subplot2grid((2,2),(0,0))
plt.plot(time,signal,label="analog")
plt.plot(time[midx],signal[midx], "mo",label="sampled") # plots the measured signal (sample from the analog signal)
plt.title("Time domain")
plt.legend()

#plotting the power spectrum of the analog signal
plt.subplot2grid((2,2),(0,1))
sigX=2*np.abs(fft(signal,npnts)/npnts) #2*np.abs() and /npnts for better visualization
hz=np.linspace(0,srate/2,int(np.floor(npnts/2)+1)) #the fft result only captures freqs up to the Nyquist frequency (half the srate)
plt.stem(hz,sigX[0:len(hz)])
plt.xlim([0,20])
plt.title("Anplitude spectrum")

# now plot only the measured signal
plt.subplot2grid((2,2),(1,0))
plt.plot(time[midx],signal[midx])
plt.title('Measured signal')

# and its amplitude spectrum
plt.subplot2grid((2,2),(1,1))
sigX = 2*np.abs(fft(signal[midx],npnts)/len(midx))
hz   = np.linspace(0,msrate/2,int(np.floor(npnts/2)+1))

plt.plot(hz,sigX[0:len(hz)])
plt.xlim([0,20])
plt.title('Frequency domain of "analog" signal')
plt.show()

#the results will show the our analog signal is operating at freq of 5 and our measured signal is operating at half the nyquist freq witch means 3hz, so here there will be aliasing 
