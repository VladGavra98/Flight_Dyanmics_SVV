# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 14:25:48 2020

@author: vladg
"""

import numpy as np
import pandas as pd
import os
import scipy.io as sp


mydir = r"C:\Users\vladg\OneDrive\Documents\GitHub\Flight_Dyanmics_SVV\Data"
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


for item in lst:
    if "Angle of attack" in item["name"]:
        alphatab = np.array(item["data"])
        print("Alpha:",alphatab)
        lst.remove(item)

    if "Time" in item["name"]:
        timetab = np.array(item["data"])
        print("Time:",timetab)



