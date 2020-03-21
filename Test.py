import numpy as np


def getInput(tab,timetab,t0,deltat): #to be exported; will be used for output as well
    """Returns the sliced array from tab when
    the time values (in seconds!) are contained in the interval (t0,t0+deltat)
    Output: tab[slices],time[slices]"""

    return tab[np.where((t0+deltat>timetab) & (t0<timetab))], timetab[np.where((t0+deltat>timetab) & (t0<timetab))]

print(getInput(np.array([3,4,2,1,2]),np.array([1,2,3,4,5]),2.3,3))