import numpy as np
import matplotlib.pyplot as plt

#Step 1: Generate a clean signal
#Define parameters
frequencies=[5,20,50]
amplitudes=[1,0.5,0.2]
sampling_rate=1000
duration=1
time= np.linspace(0,duration, int(sampling_rate*duration),endpoint=False)

#Generate sine waves
signal= amplitudes[0]*np.sin(2*np.pi*frequencies[0]*time) +\
        amplitudes[1]*np.sin(2*np.pi*frequencies[1]*time) +\
        amplitudes[2]*np.sin(2*np.pi*frequencies[2]*time) 

#Step 2: Generate noisy repetitions
num_repetitions= 50
noise_amplitude= 0.5
noisy_signals= np.zeros((num_repetitions, len(time)))

for i in range(num_repetitions):
    noise= noise_amplitude*np.random.normal(size=len(time))
    noisy_signals[i, :]= signal+noise

#plot the clean signal and one example of the noisy signal
plt.figure(figsize=(12,6))
plt.subplot(2,1,1)
plt.plot(time,signal)
plt.title("Clean Signal")
plt.subplot(2,1,2)
plt.plot(time,noisy_signals[0])
plt.title("Noisy Signal Example")
plt.tight_layout()
plt.show()