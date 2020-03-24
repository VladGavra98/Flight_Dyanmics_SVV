import numpy as np



mub = 16.17367
KZ2 = 0.042
Cnr = -0.2061
CYb = -0.75
Cnb = 0.1348


#Dutch Roll
A = 8*mub**2*KZ2
B = -2*mub*(Cnr+2*KZ2*CYb)
C = 4*mub*Cnb + CYb * Cnr

lambda_DR1 = (-B + (B**2 - 4*A*C)**0.5)/(2*A)
lambda_DR2 = (-B - (B**2 - 4*A*C)**0.5)/(2*A)
dm = 110.7544/15.911

print(A,B,C)
print(lambda_DR1*dm)
print(lambda_DR2*dm)



#
# row1 = [CYb - 2*mub*Db, -4*(mub)]
# row2 = [Cnb,Cnr-4*mub*KZ2*Db]
#
# Adr = np.zeros((2,2))
# Adr[0:,] = row1
# Adr[1:,] = row2