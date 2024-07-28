import numpy as np
import matplotlib.pyplot as plt

nReps = 50
srate = 1000 
t = np.arange(0,3-1/srate,1/srate) 
n = len(t)
# amplitude modulators for signal and noise
noiseAmp = 50 # or try 500 
signalAmp = 1 # or try 10
# signal parameters 
a= [2, 3, 4, 2] # amplitudes 
f = [1, 3, 6, 12] # frequencies
# initialize data matrix 
data = np.zeros((nReps,n))
# create signal 
signal = np.zeros(n) 
for i in range(len(a)): 
    signal = signal + a[i] * np.sin(2*np.pi*f [i] *t)

# modulate amplitude 
Signal = signal*signalAmp
# create trials with noise f
for repi in range(nReps): 
    data[repi,:] = signal + noiseAmp*np.random.randn(len(signal) )

# spectrum 1: time-domain averaging 
spect1 = 2*np.abs(np.fft.fft( np.mean(data,axis=0) )/n)**2
# spectrum 2: Fourier coefficient averaging 
spect2 = 2*np.abs( np.mean(np.fft.fft(data,axis=1)/n ,axis=0))**2
# spectrum 3: power averaging 
spect3 = np.mean( 2*np.abs( np.fft.fft(data,axis=1)/n )**2,axis=0)
# frequencies 
hz = np.linspace(0,srate/2,int(np.floor(n/2)+1))

# plot

plt.plot(hz,spect1[:len(hz)],'bs-' ,markersize=10) 
plt.plot(hz,spect2[:len(hz)],'ro-' ,markersize=10) 
plt.plot(hz,spect3[:len(hz)],'kp-' ,markersize=10)
plt.legend(['time ave','coef ave','power ave']) 
plt.xlim([0,20])    
plt.xlabel('Frequency (Hz)')
plt.ylabel('Power')
plt.show()