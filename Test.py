import matplotlib.pyplot as plt
import numpy as np

timelst = np.genfromtxt("Data_SI_correct/timeSI.txt",skip_header=2)
rud = np.genfromtxt("Data_SI_correct/delta_rSI.txt",skip_header=2)
plt.grid()
plt.plot(timelst,rud,'r')
plt.axvline(60.1*60+1.5)
plt.show()