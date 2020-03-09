import numpy as np

# Citation 550 - Linear simulation

# xcg = 0.25 * c

# Stationary flight condition

gamma = 0              #flight path angle -
hp0    =       	      # pressure altitude in the stationary flight condition [m]
V0     =             # true airspeed in the stationary flight condition [m/sec]
alpha0 =             # angle of attack in the stationary flight condition [rad]
th0    =  alpha0 + gamma    # pitch angle in the stationary flight condition [rad]

# Aircraft mass
m      =             # mass [kg]

# aerodynamic properties
e      = 0.8             # Oswald factor [ ]
CD0    = 0.04            # Zero lift drag coefficient [ ]
CLa    = 5.084            # Slope of CL-alpha curve [ ]

# Longitudinal stability
Cma    =             # longitudinal stabilty [ ]
Cmde   =             # elevator effectiveness [ ]

# Aircraft geometry

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
ih     = -2 * pi / 180   # stabiliser angle of incidence [rad]

# Constant values concerning atmosphere and gravity

rho0   = 1.2250          # air density at sea level [kg/m^3] 
lambda = -0.0065         # temperature gradient in ISA [K/m]
Temp0  = 288.15          # temperature at sea level in ISA [K]
R      = 287.05          # specific gas constant [m^2/sec^2K]
g      = 9.81            # [m/sec^2] (gravity constant)

# air density [kg/m^3]  
rho    = rho0 * power( ((1+(lambda * hp0 / Temp0))), (-((g / (lambda*R)) + 1)))   
W      = m * g            # [N]       (aircraft weight)

# Constant values concerning aircraft inertia

muc    = m / (rho * S * c)
mub    = m / (rho * S * b)
KX2    = 0.019
KZ2    = 0.042
KXZ    = 0.002
KY2    = 1.25 * 1.114

# Aerodynamic constants

Cmac   = 0                      # Moment coefficient about the aerodynamic centre [ ]
CNwa   = CLa                    # Wing normal force slope [ ]
CNha   = 2 * pi * Ah / (Ah + 2) # Stabiliser normal force slope [ ]
depsda = 4 / (A + 2)            # Downwash gradient [ ]

# Lift and drag coefficient

CL = 2 * W / (rho * V0 ** 2 * S)              # Lift coefficient [ ]
CD = CD0 + (CLa * alpha0) ** 2 / (pi * A * e) # Drag coefficient [ ]

# Stabiblity derivatives

CX0    = W * sin(th0) / (0.5 * rho * V0 ** 2 * S)
CXu    = -0.02792
CXa    = +0.47966		# Positive! (has been erroneously negative since 1993) 
CXadot = +0.08330
CXq    = -0.28170
CXde   = -0.03728

CZ0    = -W * cos(th0) / (0.5 * rho * V0 ** 2 * S)
CZu    = -0.37616
CZa    = -5.74340
CZadot = -0.00350
CZq    = -5.66290
CZde   = -0.69612

Cmu    = +0.06990
Cmadot = +0.17800
Cmq    = -8.79415

CYb    = -0.7500
CYbdot =  0     
CYp    = -0.0304
CYr    = +0.8495
CYda   = -0.0400
CYdr   = +0.2300

Clb    = -0.10260
Clp    = -0.71085
Clr    = +0.23760
Clda   = -0.23088
Cldr   = +0.03440

Cnb    =  +0.1348
Cnbdot =   0     
Cnp    =  -0.0602
Cnr    =  -0.2061
Cnda   =  -0.0120
Cndr   =  -0.0939

#c-matrix dimensions
s1 = (4,4)
s2 = (4,1)
s3 = (4,2)

#Creating the different c-matrices (c1, c2 &c3) for symmetrical flight
#c1 matrix
c1 = np.zeros(s1)
c1[0,0] = -2*muc*(c/V0)
c1[1,1] = (CZadot - 2*muc)*(c/V0)
c1[2,2] = -(c/V0)
c1[3,1] = Cmadot*(c/V0)
c1[3,3] = -2*muc*KY2*((c/V0)**2)

#c2 matrix
c2 = np.zeros(s1)
c2[0,0] = -CXu
c2[0,1] = -CXa
c2[0,2] = -CZ0
c2[0,3] = -CXq
c2[1,0] = -CZu
c2[1,1] = -CZa
c2[1,2] = -CX0
c2[1,3] = -(CZq + 2*muc)*(c/V0)
c2[2,3] = -(c/V0)
c2[3,0] = -Cmu
c2[3,1] = -Cma
c2[3,3] = -Cmq*(c/V0)

#c3 matrix
c3 = np.zeros(s2)
c3[0,0] = -CXde
c3[1,0] = -CZde
c3[3,0] = -Cmde

#Creating the different c-matrices (c4, c5 &c6) for asymmetrical flight
#c4 matrix
c4 = np.zeros(s1)
c4[0,0] = (CYbdot - 2*mub)*(b/V0)
c4[1,1] = (-0.5)*(b/V0)
c4[2,2] = -4*mub*KX2*(b/V0)*(b/(2*V0))
c4[2,3] = 4*mub*KXZ*(b/V0)*(b/(2*V0))
c4[3,0] = Cnb*(b/V0)
c4[3,2] = 4*mub*KXZ*(b/V0)*(b/(2*V0))
c4[3,3] = -4*mub*KZ2*(b/V0)*(b/(2*V0))

#c5 matrix
c5 = np.zeros(s1)
c5[0,0] = CYb
c5[0,1] = CL
c5[0,2] = CYp*(b/(2*V0))
c5[0,3] = (CYr - 4*mub)*(b/(2*V0))
c5[1,2] = (b/(2*V0))
c5[2,0] = Clb
c5[2,2] = Clp*(b/(2*V0))
c5[2,3] = Clr*(b/(2*V0))
c5[3,0] = Cnb
c5[3,2] = Cnp*(b/(2*V0))
c5[3,3] = Cnr*(b/(2*V0))

#c5 matrix
c5 = np.zeros(s3)
c5[0,0] = -CYda
c5[0,1] = -CYdr
c5[2,0] = -Clda
c5[2,1] = -Cldr
c5[3,0] = -Cnda
c5[3,1] = -Cndr
