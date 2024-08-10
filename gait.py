#Algorithm Description:
#This code loads gait data for parkinson and healthy controls,
#it converts the stride times into binary time series, applies Fourier 
#transform to these time series, and visualizes the power spectrum to
#analyze the dominant walking frequencies nad variability in gait patters.

import numpy as np
import scipy.io as sio
import matplotlib.pyplot as plt
from scipy.fftpack import fft

#Load the data from the mat file
matdata = sio.loadmat('gait.mat')

#Extract the data
park = matdata['park']
cont = matdata['cont']

#Plotting stride time
plt.subplot2grid((3,1),(0,0))
plt.plot(park[:,0],park[:,1],label='Parkinson patient')
plt.plot(cont[:,0],cont[:,1],label='Control')
plt.xlabel("Time (sec)")
plt.ylabel("Stride time (s)")
plt.legend()

#Defining sample rate
srate=1000

#Creating Binary time series for Parkinson's patients
parkts=np.zeros(int(park[-1,0]*srate)) #create a zero vector with length based on the last time point
for i in range(0,len(park)):
	parkts[int(park[i,0]*srate-1)]=1 #populate this vector with 1s at time points corresponding to steps
parktx=np.arange(0,len(parkts))/srate 
parkn = len(parktx) #determine number of time points of parktx

#the same thing for healthy controls
contts= np.zeros(int(cont[-1,0]*srate))
for i in range(0, len(cont)):
	contts[int(cont[i,0]*srate-1)]=1
conttx= np.arange(0,len(contts))/srate
contn= len(conttx)

#Plotting Time series of steps
plt.subplot2grid((3,1),(1,0))
plt.plot(parktx,parkts)
plt.xlabel('Time')
plt.ylabel('Step Indicator (binary)')
plt.xlim([0,50])

#Computing Power spectrum
parkPow= 2*np.abs(fft(parkts)/parkn)
contPow= 2*np.abs(fft(contts)/contn)

#Computing Frequency vectors 
parkHz= np.linspace(0,srate/2,int(np.floor(parkn/2)+1))
contHz= np.linspace(0,srate/2,int(np.floor(contn/2)+1))

#plotting power spectrum
plt.subplot2grid((3,1),(2,0))
plt.plot(parkHz[1:],parkPow[1:len(parkHz)])
plt.plot(contHz[1:],contPow[1:len(contHz)])
plt.xlabel('Frequency')
plt.ylabel('Power')
plt.xlim([0,7])
plt.show()
