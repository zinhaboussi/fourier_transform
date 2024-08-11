#Algorithm:
#1. Load the image
#2. Compute the 2D FFT of the image as use fftshift to center the low frequencies
#3. Create a guassion filter to attenuate specific freqs
#4. Apply the Guassian filter
#5. Reconstruct the image

import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft2, fftshift, ifft2
from PIL import Image
import scipy.stats as stats

#load the image
houria= np.asarray(Image.open('houria.png'))
imgL= np.mean(houria, axis=2)

#Plot original image
plt.subplot2grid((2,2),(0,0))
plt.imshow(imgL, cmap=plt.cm.gray)
plt.axis('off')
plt.title('Original image')

#Compute the 2D FFT and shift zero frequency component to the center
imgX= fftshift(fft2(imgL))
powr2= np.log(np.abs(imgX))

#Plot the amplitude spectrum
plt.subplot2grid((2,3),(1,0))
plt.imshow(powr2, cmap=plt.cm.gray)
plt.clim([0,15])
plt.axis('off')
plt.title('Amplitude spectrum')

#Gaussian filter parameters
width= .1 #width of Gaussian(control the amounts of high-freq filtering)
lims= np.shape(imgL) #get the image dimenstions 
xr= stats.zscore(np.arange(lims[0])) #creates normalized cordinator array
[x,y]= np.meshgrid(xr,xr) #creates a 2d meshgrid (x,y) from the normalized coordinates

gaus2d= 1-np.exp(-(x**2+y**2)/(2*width**2)) #calc 2d Gaussian filter based on width parameter. This filter attenuates high freqs in the iamge spectrum. Briefly the line add 1- at beggining of the next line to invert the filter

#Plotting the Guassian filter
plt.subplot2grid((2,3),(1,1))
plt.imshow(gaus2d, cmap=plt.cm.gray)
plt.axis('off')
plt.title('Gain function')

#show modulated spectrum
plt.subplot2grid((2,3),(1,2))
plt.imshow(np.log(np.abs(np.multiply(imgX, gaus2d))), cmap=plt.cm.gray) #element-wise multiplies the images spectrum with gaussian filter. This effectively filters out high freqs based on the Gaussian shape
plt.axis('off')
plt.clim([0,15])
plt.title('Modulated spectrum')

#Reconstrcut the Filtered image
imgrecon = np.real(ifft2( fftshift(np.multiply(imgX,gaus2d) )))

plt.subplot2grid((2,2),(0,1))
plt.imshow( imgrecon ,cmap=plt.cm.gray)
plt.axis('off')
plt.title('Filtered image')

plt.show()


