####### Converting text files from imperial to SI units ####

import numpy as np 
import csv

### converting knots, lbs, g, ft, ft/min, deg C, lbs/hr, psi
### knots = 0.5144444444444444 m/s
### lbs = 0.45359237 kgs
### g = 9.80665 m/s^2
### ft = 0.3048 m
### ft/min = 0.00508 m/s
### deg C = + 273.15 K
### lbs/hr = 0.0001259979 kg/s
### psi = 6894.75729 pas

def conversion(filename):

    
    
    f = open(filename, "r")
    n = open(filename[:-4]+"SI.txt", "w")
    lines = f.readlines()
    unit = lines[1]
    n.write(lines[0])
    if unit == 'g\n':
        n.write('m/s^2\n')
        for i in range(len(lines)-2):
            n.write(str(float(lines[i+2].strip())*9.80665)+"\n")
       


    n.close()


    

conversion('Data\Ahrs1_bLatAcc.txt')
