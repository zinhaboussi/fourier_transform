import numpy as np
import math
import matplotlib.pyplot as plt
import timeit
import random
import scipy.fftpack

#create the signal
pnts=1000
signal= np.random.randn(pnts)

#start the timer for the slow FT
tic= timeit.default_timer()

#prepare the FT
fourTime= np.array(range(0,pnts))/pnts
fCoefs= np.zeros(len(signal),dtype=complex)

for fi in range(pnts):
    csw=np.exp(-1j*2*np.pi*fi*fourTime)
    fCoefs[fi]= np.sum(np.multiply(signal,csw))

#end timer for slow FT
toc=timeit.default_timer()
t1=toc-tic

#time the fast FT
tic=timeit.default_timer()
fCoefsF= scipy.fftpack.fft(signal)
toc=timeit.default_timer()
t2=toc-tic

#plot
plt.bar([1,2],[t1,t2])
plt.title("Computation times")
plt.ylabel("Time (sec)")
plt.xticks([1,2],["loop","fft"])
plt.show()