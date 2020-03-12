import numpy as np

lhfusi = np.genfromtxt("lh_engine_FUSI.txt",skip_header=2)
rhfusi = np.genfromtxt("rh_engine_FUSI.txt",skip_header=2)
time = np.genfromtxt("timeSI.txt",skip_header=2)

totfusi = lhfusi+rhfusi