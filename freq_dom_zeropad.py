#this code showcases how zero-padding in the frequency domain leads to a reconstructed time-domain signal that is essentially a sinc-interpolated version of the original signal.
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft,ifft

#create signal
signal= [4,6,-1,0,5,-4]

#original fft
signalX= fft(signal)

#zero-padding
n2pad= [0,10,100]

for i in range (len(n2pad)):
	#calculate the total length of the spectrum after adding the zeros
	zeropadN= len(signal)+n2pad[i]
	
	#reconstruction via iFFT
	reconSig= ifft(signalX, zeropadN)*zeropadN # this reconstructs time-domain signal based on the modified frequency information, the multiplication by zeropadN is common normalization step to compensate for the length increase during zero-padding.
	
	#time normalization and plotting
	normtime= np.linspace(0,1,len(reconSig)) #creates a normalized time axis based on the length of the reconstructed signal
	plt.plot(normtime,np.real(reconSig),"s-",label="%g-point FFT" %zeropadN)
plt.legend()
plt.xlabel("Time(norm.)")
plt.show()





