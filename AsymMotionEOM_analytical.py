import numpy as np


S      = 30.00	          # wing area [m^2]
Sh     = 0.2 * S         # stabiliser area [m^2]
Sh_S   = Sh / S	          # [ ]
lh     = 0.71 * 5.968    # tail length [m]
c      = 2.0569	          # mean aerodynamic cord [m]
lh_c   = lh / c	          # [ ]
b      = 15.911	          # wing span [m]
bh     = 5.791	          # stabilser span [m]
A      = b ** 2 / S      # wing aspect ratio [ ]
Ah     = bh ** 2 / Sh    # stabilser aspect ratio [ ]
Vh_V   = 1	          # [ ]
ih     = -2 * np.pi / 180   # stabiliser angle of incidence [rad]

oew = 4157.174              #Operational Empty Weight [kg]

# aerodynamic properties
e      = 0.8             # Oswald factor [ ]
CD0    = 0.04            # Zero lift drag coefficient [ ]
CLa    = 5.084            # Slope of CL-alpha curve [ ]

# Constant values concerning atmosphere and gravity
rho0   = 1.2250          # air density at sea level [kg/m^3]
lam = -0.0065         # temperature gradient in ISA [K/m]
Temp0  = 288.15       # temperature at sea level in ISA [K]
R      = 287.05          # specific gas constant [m^2/sec^2K]
g      = 9.81            # [m/sec^2] (gravity constant)

#+++++++++++++++++++++++++++++++++ MAIN ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#C.G location
xcg = 0.25 * c

# Stationary flight condition
m_fuel    = 1197.484           #Total fuel mass [kg]
m_payload = 765             #Payload mass [kg]
gamma  = 0                   #flight path angle -
hp0    = 1527.048      	    # pressure altitude in the stationary flight condition [m]
V0     = 127.067            # true airspeed in the stationary flight condition [m/sec]
alpha0 = np.radians(1.4)        # angle of attack in the stationary flight condition [rad]
th0    = alpha0 + gamma    # pitch angle in the stationary flight condition [rad]

# Aircraft mass
m      =  4989.516 + m_payload         # mass [kg]  --changes

# Longitudinal stability
Cma    = -0.1          # longitudinal stabilty [ ]
Cmde   = -0.01            # elevator effectiveness [ ]

# air density [kg/m^3]
rho    = rho0 * pow( ((1+(lam * hp0 / Temp0))), (-((g / (lam*R)) + 1)))
W      = m * g


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


# ----------- TESTER ----------- #
#Aperiodic Roll
lambda_AR = Clp/(4*mub*KX2)
Db = lambda_AR


Aar = Clp - 4*mub*KX2*Db



#Dutch Roll
A = 8*mub**2*KZ2
B = -2*mub*(Cnr+2*KZ2*CYb)
C = 4*mub*Cnb + CYb * Cnr

lambda_DR1 = (-B + (B**2 - 4*A*C)**0.5)/(2*A)
lambda_DR2 = (-B - (B**2 - 4*A*C)**0.5)/(2*A)
Db = lambda_DR1  #switch, DR1 or DR2

row1 = [CYb - 2*mub*Db, -4*(mub)]
row2 = [Cnb,Cnr-4*mub*KZ2*Db]

Adr = np.zeros((2,2))
Adr[0:,] = row1
Adr[1:,] = row2








#Aperiodic Spiral
lambda_as = 2*CL*(Clb*Cnr-Cnb*Clr)/(Clp*(CYb*Cnr+4*mub*Cnb)-Cnp*(CYb*Clr+4*mub*Clb))
Db = lambda_as

row1 = [CYb,CL,0,-4*mub]
row2 = [0,-Db/2,1,0]
row3 = [Clb,0,Clp,Clr]
row4 = [Cnb,0,Cnp,Cnr]

Aas = np.zeros((4,4))
Aas[0:,] = row1
Aas[1:,] = row2
Aas[2:,] = row3
Aas[3:,] = row4

