import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft

m=50 #length of signal
n=11 #length of kernel

signal= np.zeros(m)
signal[range(int(m*.4),int(m*.6))]=1 #set the middle portion of the signal to 1, creating a rectungular pulse.

kernel = np.zeros(n)
kernel[range(int(n*.25),int(n*.8))]=np.linspace(1,0,int(n*.55)) #set a portion of the kernel to linearly decreasing set of values from 1 to 0.

#plot signal and kernel
plt.subplot2grid((3,1),(0,0))
plt.plot(signal)
plt.title('Signal')

plt.subplot2grid((3,1),(1,0))
plt.plot(kernel)
plt.title('Kernel')

#setup convolution parameters
nConv=	m+n-1 #total length for convolution
halfk= np.floor(n/2) #half the length of the kernel

#perform FFT on Signal and kernel
mx= fft(signal,nConv)
nx= fft(kernel,nConv)

#convolution via Poinr-Wise Multiplication in Frequency-domain
convres= np.real(ifft(np.multiply(mx,nx)))

#the following line will crops the wings of the convo result "convress", because the conv result is typically longer than the original due to zero-padding. This removes the extra parts at the beginning and the end caused by padding
convres= convres[range(int(halfk), int(len(convres) - halfk + 1))]

#plot the result of convolution
plt.subplot2grid((3,1),(2,0))
plt.plot(convres,'b')
plt.title('Result of Convolution')

#for comparing with the python convolution function
plt.plot(np.convolve(signal,kernel,mode='same'),'ro')
plt.show()


