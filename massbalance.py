import numpy as np


#VARIABLE parameters
blockfuel = 2000 #Fuel at t=0      check consistent with others

fuelusedlst = [1, 2, 3, 4, 5, 6]  # Wf (Fuel Used)                USE OUR DATA
fueltimelst = [1, 2, 3, 4, 5, 6]  # t values for Wf (Fuel Used)   USE OUR DATA

#Pax weights
Arun = 95
Hans = 102
Paul = 89
Vlad = 82
Max = 66
Mat = 81
Flori = 69
Phil = 85
Jack = 96



#NON-VARIABLE parameters
BEW = 9165 #Basic Empty Weight    lbs
BEWarm = 291.65 #Basic Empty Weight Moment Arm   inches from datum
seatsarm = np.array([131,131,214,214,251,251,288,288,170,170]) #Seat Moment Arms   inches from datum

#Fuel Moment Arm Initial Parameters
fuelmass = np.linspace(100,2100,21)
fuelmomentall = np.array([298.16,591.18,879.08,1165.42,1448.4,1732.53,2014.8,2298.84,2581.92,2866.3,3150.18,3434.52,3718.52,4003.23,4287.76,4572.24,4856.56,5141.16,5425.64,5709.9,5994.04])






def interpolate(x1,x2,y1,y2,x):
    return (y2-y1)*(x-x1)/(x2-x1) + y1



def fuelonboard(t):
    for i in range(len(fueltimelst)-1):
        if fueltimelst[i] <= t <= fueltimelst[i+1]:
            f_used = interpolate(fueltimelst[i],fueltimelst[i+1],fuelusedlst[i],fuelusedlst[i+1],t)
            return blockfuel - f_used
    if t <= fueltimelst[0]:
        print("t less than first recorded value. No fuel used yet")
        return blockfuel
    if t >= fueltimelst[-1]:
        print("t specified greater than last recorded t-value (constant extrapolation)")
        return blockfuel - fuelusedlst[-1]

def fuelmoment(t):
    for l in range(len(fuelmomentall)-1):
        if fuelmass[l] <= fuelonboard(t) <= fuelmass[l+1]:
            return interpolate(fuelmomentall[l],fuelmomentall[l+1],fuelmass[l],fuelmass[l+1],fuelonboard(t))
    if fuelonboard(t) < fuelmass[0]:
        print("Fuel too low - Moment arm inaccurate")
    if fuelonboard(t) > fuelmass[-1]:
        print("Fuel beyond moment arm data")


def cg(t,cgmove): #cgmove = False if Jack is in seat 8, set cgmove = True if Jack has moved for cg shift
    seat1 = Arun
    seat2 = Hans
    seat3 = Vlad
    seat4 = Max
    seat5 = Mat
    seat6 = Flori
    seat7 = Phil
    seat8 = Jack
    seat9 = 0
    seat10 = Paul

    if cgmove == True:
        seat8 = 0
        seat9 = Jack


    seats = [seat1,seat2,seat3,seat4,seat5,seat6,seat7,seat8,seat9,seat10]

    seatmoment = 0
    seatmass = 0
    for s in range(len(seats)):
        seatmoment += seats[s]*seatsarm[s]
        seatmass += seats[s]

    momentsum = seatmoment + BEW*BEWarm + fuelmoment(t)
    totalmass = seatmass + BEW + fuelonboard(t)
    x_cg_inch = momentsum/totalmass
    x_cg = (x_cg_inch - 261.56)*2.54/100  #x_cg from LEMAC   in [m] !!
    return x_cg


print(cg(4,False))

