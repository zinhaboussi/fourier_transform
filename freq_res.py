import numpy as np

srate= 1000
pnts=3000
signal= np.random.randn(pnts)
hz= np.linspace(0,srate/2,int(np.floor(pnts/2)+1))
freqres= np.mean(np.diff(hz))
print("Frequency resolution is: ",freqres,"Hz")

