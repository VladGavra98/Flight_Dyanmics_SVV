import numpy as np
from massbalance import *


#FOR GRAPH
x = np.linspace(10,timelst[-1],1000)
y = []


for i in range(len(x)):
    if 52*60 < x[i] < 53*60:
        print('hit')
        y.append(cg(x[i], True))
    else:
        y.append(cg(x[i],False))
plt.plot(x,y)
plt.grid(True)
plt.xlabel('Time [s]')
plt.ylabel('cg location [-]')
plt.show()


# for i in range(len(x)):
#     y.append(mass(x[i]))
# plt.plot(x,y)
# plt.grid(True)
# plt.xlabel('Time [s]')
# plt.ylabel('Mass [kg]')
# plt.show()

# for i in range(len(x)):
#     y.append(fuelmomentall(x[i]))
# plt.plot(x,y)
# plt.grid(True)
# plt.xlabel('Time [s]')
# plt.ylabel('Fuel Moment Arm ')
# plt.show()
#
# for i in range(len(x)):
#     y.append(fuelonboard(x[i]))
# plt.plot(x,y)
# plt.grid(True)
# plt.xlabel('Time [s]')
# plt.ylabel('Fuel [lb]')
# plt.show()
