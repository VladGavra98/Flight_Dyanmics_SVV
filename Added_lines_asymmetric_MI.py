# ---- Aperiodic Roll Added Lines ---- #

@Mat




# ---- Dutch Roll Added Lines ---- #

CYb = -0.75
Cnb = +0.1348
Cnr = -0.2061


CYblst = []
Cnblst = []
Cnrlst = []
lst = []
relerrorlst1 = []
relerrorlst2 = []

#within sign +/- 1
nn = 15
CYb_r = np.linspace(-1,0,nn)
Cnb_r = np.linspace(0,1,nn)
Cnr_r = np.linspace(-1,0,nn)

#unlimited -1 to 1
# nn = 20
# CYb_r = np.linspace(-1,1,nn)
# Cnb_r = np.linspace(-1,1,nn)
# Cnr_r = np.linspace(-1,1,nn)

#ADJUST percent of coeff
# rr = 50/100
# CYb_r = np.linspace(CYb*(1-rr),CYb*(1+rr),nn)
# Cnb_r = np.linspace(Cnb*(1-rr),Cnb*(1+rr),nn)
# Cnr_r = np.linspace(Cnr*(1-rr),Cnr*(1+rr),nn)


#specific (once alrady run through)
CYb_r = np.linspace(-0.7,-0.9,nn)
Cnb_r = np.linspace(-0.1,0.2,nn)
Cnr_r = np.linspace(-0.23,-0.12,nn)

#specific (once alrady run through)
# CYb_r = np.linspace(0.05,0.07,nn)
# Cnb_r = np.linspace(0.08,0.12,nn)
# Cnr_r = np.linspace(-0.1,+0.1,nn)


count = 0
for i in CYb_r:
    for j in Cnb_r:
        for k in Cnr_r:
            #j = 0.1095
            count += 1
            ar,bi,nmr,nmi,ftr,fti = eigerr(i,j,k)
            relerrorlst1.append(ar)
            relerrorlst2.append(bi)
            lst.append([i,j,k,ar,bi,nmr,nmi,ftr,fti])
            print(round(100*count/(nn**3),4),' %')


#print(relerror(CYb,Cnr,Cnb))

relerrorlst1 = np.array(relerrorlst1)
relerrorlst2 = np.array(relerrorlst2)

# minval = min(np.abs(relerrorlst2)) #min(np.abs((relerrorlst1**2+relerrorlst2**2)**0.5))
# for k in lst:
#     if np.abs(k[4]) == minval: #abs((k[3]**2+k[4]**2)**0.5) < minval*1.04:
#         print(k)


# minval = min(np.abs(relerrorlst1)) #min(np.abs((relerrorlst1**2+relerrorlst2**2)**0.5))
# for k in lst:
#     if np.abs(k[3]) == minval: #abs((k[3]**2+k[4]**2)**0.5) < minval*1.04:
#         print(k)

minval = min(np.abs((relerrorlst1**2+relerrorlst2**2)**0.5))
for k in lst:
    if np.abs((k[3]**2+k[4]**2)**0.5) < minval*1.01:
        print(k)




# ---- Aperiodic Spiral Added Lines ---- #
@Mat