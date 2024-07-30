import numpy as np
import math
import matplotlib.pyplot as plt
import scipy.fftpack

#zero-padding in the fft function

#create the signal
signal= [4,6,-1,0,5,-4]

#number of zeros to add after the signal
num_pad=[0,10,100]

#loop through zero-padding values
for i in range(0,len(num_pad)):
	#calculate the total length after zero-padding
	zeropadN= len(signal)+num_pad[i]
	
	#compute fft and amplitude
	signalamp= np.abs(scipy.fftpack.fft(signal,zeropadN))
	
	#normalization (this is optional)
	signalamp=signalamp/1
	
	#create frequency units for plotting
	frequnits=np.linspace(0,1,zeropadN+1)
	
	#plot
	plt.plot(frequnits[:-1],signalamp,"s-",label="%g-point FFT" %zeropadN)

plt.legend()
plt.xlabel("Frequency (.5=Nyquist)")
plt.ylabel("Amplitude (.a.u.)")
plt.show()
