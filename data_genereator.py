# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 14:25:48 2020

@author: vladg
"""

import numpy as np
import pandas as pd
import os
import scipy.io as sp

root = r"C:\Users\vladg\OneDrive\Documents\GitHub\Flight_Dyanmics_SVV"
mydir = r"C:\Users\vladg\OneDrive\Documents\GitHub\Flight_Dyanmics_SVV\Data"


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




lst = getData(mydir)

for item in lst:
    if "Angle of attack" in item["name"]:
        alphatab = np.array(item["data"])
        print("Alpha:",alphatab)
        lst.remove(item)

    # if "Time" in item["name"]:
    #     timetab = np.array(item["data"])
    #     print("Time:",timetab)




#Data aquisition & Unit conversion (when needed)
Htab = np.genfromtxt("Dadc1_alt.txt",dtype=float,skip_header=2,delimiter='\n') * 0.3048  #m
Ttab = np.genfromtxt("Dadc1_tat.txt",dtype=float,skip_header=2,delimiter='\n')    #C
Mtab = np.genfromtxt("Dadc1_mach.txt",dtype=float,skip_header=2,delimiter='\n')  #-
Tisa = calcT(Htab)   #C
FMFr_tab = np.genfromtxt("rh_engine_FMF.txt",dtype=float,skip_header=2,delimiter='\n') * 0.000126 #kg/s
FMFl_tab = np.genfromtxt("lh_engine_FMF.txt",dtype=float,skip_header=2,delimiter='\n') * 0.000126 #kg/s


os.chdir(root)
file = str("matlab.dat")

try:
    fid = open(file,"w")
except:
    print("Fail cannot be found/opne!\n")

for i in range(10):
    genThrust(fid,Htab[i],Mtab[i],abs(Ttab[i]-Tisa[i]),FMFl_tab[i],FMFr_tab[i])

fid.close()

# Run the Thrust calling command
os.system("thurst(1).exe")