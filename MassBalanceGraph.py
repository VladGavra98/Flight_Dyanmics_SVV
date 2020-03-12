import numpy as np
from massbalance import *


#FOR GRAPH
x = np.linspace(10,timelst[-1],10000)
y = []
for i in range(len(x)):
    if 52*60 < timelst[i] < 53*60:
        print('hit')
        y.append(cg(x[i], True))
    else:
        y.append(cg(x[i],False))
    #y.append(mass(x[i]))

plt.plot(x,y)
plt.grid(True)
plt.xlabel('Time [s]')
plt.ylabel('cg location/MAC [-]')
#plt.ylabel('Mass [kg')
plt.show()
