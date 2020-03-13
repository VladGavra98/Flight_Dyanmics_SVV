import numpy as np

# Constant values concerning aircraft inertia
muc = m / (rho * S * c)
mub = m / (rho * S * b)
KX2 = 0.019
KZ2 = 0.042
KXZ = 0.002
KY2 = 1.25 * 1.114

# Aerodynamic constants

Cmac = 0  # Moment coefficient about the aerodynamic centre [ ]
CNwa = CLa  # Wing normal force slope [ ]
CNha = 2 * np.pi * Ah / (Ah + 2)  # Stabiliser normal force slope [ ]
depsda = 4 / (A + 2)  # Downwash gradient [ ]

# Lift and drag coefficient

CL = 2 * W / (rho * V0 ** 2 * S)  # Lift coefficient [ ]
CD = CD0 + (CLa * alpha0) ** 2 / (np.pi * A * e)  # Drag coefficient [ ]

# Stabiblity derivatives

CX0 = W * np.sin(th0) / (0.5 * rho * V0 ** 2 * S)
CXu = -0.02792
CXa = +0.47966  # Positive! (has been erroneously negative since 1993)
CXadot = +0.08330
CXq = -0.28170
CXde = -0.03728

CZ0 = -W * np.cos(th0) / (0.5 * rho * V0 ** 2 * S)
CZu = -0.37616
CZa = -5.74340
CZadot = -0.00350
CZq = -5.66290
CZde = -0.69612

Cmu = +0.06990
Cmadot = +0.17800
Cmq = -8.79415

CYb = -0.7500
CYbdot = 0
CYp = -0.0304
CYr = +0.8495
CYda = -0.0400
CYdr = +0.2300

Clb = -0.10260
Clp = -0.71085
Clr = +0.23760
Clda = -0.23088
Cldr = +0.03440

Cnb = +0.1348
Cnbdot = 0
Cnp = -0.0602
Cnr = -0.2061
Cnda = -0.0120
Cndr = -0.0939

Db = 1 #TEMP

row1 = [CYb,CL,0,-4*mub]
row2 = [0,-Db/2,1,0]
row3 = [Clb,0,Clp,Clr]
row4 = [Cnb,0,Cnp,Cnr]

Aas = np.zeros((0,0))
Aas[0:,] = row1
Aas[1:,] = row2
Aas[2:,] = row3
Aas[3:,] = row4