#!/usr/bin/python
import numpy as np
from scipy.fftpack import fft
import matplotlib.pyplot as plt


# # Read Results
data = np.loadtxt('./postProcessing/forceCoeffs/0/forceCoeffs.dat', skiprows=0)

L       = 2           # L = D - Diameter
V       = 1           # Velocity
time    = data[:,0]
Cd      = data[:,2]
Cl      = data[:,3]

del data


# # Compute FFT

N       = len(time)
dt      = time[2] - time[1]

freq    = np.fft.fftfreq(N, dt)
Cd_fft  = np.fft.fft(Cd) 
Cl_fft  = np.fft.fft(Cl)

# # Strouhal Number
# Find the index corresponding to max amplitude
Cl_max_fft_idx = np.argmax(abs(Cl_fft))  
freq_shed      = freq[Cl_max_fft_idx ]
St             = freq_shed * L / V

print "Vortex shedding freq: %.3f [Hz]" % (freq_shed)
print "Strouhal Number: %.3f" % (St)

# plt.plot(freq,Cd_fft)
# Figure 2.10
plt.plot(freq, Cl_fft)
plt.xlim(0, 0.3)
plt.show()

# # Explore Results
# # Figure 2.8
# # See if there atleast 10 cycles of oscillation
# # improves the accuracy; 
# plt.plot(time,Cl)
# plt.show()
# # Figure 2.9
# plt.plot(time,Cd)
# plt.show()
