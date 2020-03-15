# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 14:25:48 2020

@author: vladg
"""

import numpy as np
import pandas as pd
import os
import scipy.io as sp
import matplotlib.pyplot as plt

root = r"C:\Users\vladg\OneDrive\Documents\GitHub\Flight_Dyanmics_SVV"
mydir = r"C:\Users\vladg\OneDrive\Documents\GitHub\Flight_Dyanmics_SVV\Data_SI_correct"


def calcT(h): #ISA tmeperature
    return 15.0 - 0.0065*h

def getData(mydir):
    os.chdir(mydir)

    lst = []
    for root, dirs, files in os.walk(mydir):
        for file in files:
            # print(file)
            fullData = pd.read_csv(file,"\n")
            data = fullData[2:]
            name = fullData.columns[0]
            # units = str(fullData[0])
            local = {"name":name,"data":data}
            lst.append(local)

    return lst

def genThrust(fid,h,M,deltaT,FMFr,FMFl):
    """Generates the tthrust.txt file for the thrust calculations
 Input: altitude                      h [m]
         mach number                  M [-]
         delta real-ISA               T [C]
         Fuel Mass Flow right engine  [kg/s]
         Fuel Mass flow left engine   [kg/s]

         All from Reader/pg32
 Output: matlab.dat file for thrust.exe app"""



    # Open the file

    #Create the command file
    fid.write( str(h) + " ")
    fid.write(str(M) + " ")
    fid.write(str(deltaT) + " ")
    fid.write(str(FMFr)+ " ")
    fid.write(str(FMFl)+ " ")

    #For next data point
    fid.write("\n")


    return 1

def plotting(x,y,name,variable,unit,mins=False):
    """Use this for plotting."""
    ax = plt.figure(str(name))
    # ax.legend("best")

    if mins:
        x/=60  #change time to mins from secs
    plt.plot(x,y,label=name)
    plt.xlabel("t [s]")

    lab = str(str(variable)+" "+"["+unit+"]")
    plt.ylabel(lab)
    plt.grid(True)
    plt.show()



lst = getData(mydir)

# for item in lst:
#     if "Angle of attack" in item["name"]:
#         alphatab = np.array(item["data"])
#         print("Alpha:",alphatab)
#         lst.remove(item)

    # if "Time" in item["name"]:
    #     timetab = np.array(item["data"])
    #     print("Time:",timetab)




#Data aquisition & Unit conversion (when needed)
timetab = np.genfromtxt("timeSI.txt",dtype=float,skip_header=2,delimiter='\n')  #s DONT CHANGE!


Htab = np.genfromtxt("Dadc1_altSI.txt",dtype=float,skip_header=2,delimiter='\n')  #m
Ttab = np.genfromtxt("Dadc1_tatSI.txt",dtype=float,skip_header=2,delimiter='\n')    #C
Mtab = np.genfromtxt("Dadc1_machSI.txt",dtype=float,skip_header=2,delimiter='\n')  #-
Tisa = calcT(Htab)   #C
FMFr_tab = np.genfromtxt("rh_engine_FMFSI.txt",dtype=float,skip_header=2,delimiter='\n')  #kg/s
FMFl_tab = np.genfromtxt("lh_engine_FMFSI.txt",dtype=float,skip_header=2,delimiter='\n') #kg/s

alphatab = np.genfromtxt("vane_AOASI.txt",dtype=float,skip_header=2,delimiter='\n')  #deg
gtab = np.genfromtxt("Ahrs1_VertAccSI.txt",dtype=float,skip_header=2,delimiter='\n')
elevtab =  np.genfromtxt("delta_eSI.txt",dtype=float,skip_header=2,delimiter='\n')
os.chdir(root)
file = str("matlab.dat")

try:
    fid = open(file,"w")
except:
    print("Fail cannot be found/opne!\n")

for i in range(10):
    genThrust(fid,Htab[i],Mtab[i],abs(Ttab[i]-Tisa[i]),FMFl_tab[i],FMFr_tab[i])

fid.close()

#++++++++++++++++++++++++++++++++++++++Plotting++++++++++++++++++++++++++++++++++++++++++++++++++++
plotting(timetab,elevtab,name="Elevator deflection",variable="${\delta}_e$",unit="rad",mins=True)
# Run the Thrust calling command
os.system("thurst(1).exe")