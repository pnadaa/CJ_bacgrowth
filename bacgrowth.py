#A barebones program to estimate bacterial exponential growth times to harvest (primarily for Tree Lab comp cell preps)

import math

#Using formula A=P0*e^(rt)

#Obtaining original optical density at time = 0:

originalDensity = float(input("What is your original starting optical density? "))

#Obtaining optical density at intermediate time:
intermediateTime = float(input("At what timepoint was the measurement taken? Enter in minutes (eg 75) "))
intermediateDensity = float(input("What is the optical density at this timepoint? "))

#Obtaining endpoint optical density:

try:
    endpointDensityLower = float(input("What is your LOWER limit of the optical density? (Default: 0.35) " ))
except ValueError:
    endpointDensityLower = 0.35
    print("!!!Using default LOWER limit of 0.35!!!")

try:
    endpointDensityUpper = float(input("What is your UPPER limit of the optical density? (Default: 0.40) " ))
except ValueError:
    endpointDensityUpper = 0.40
    print("!!!Using default UPPER limit of 0.40!!!")


#Calculating the r constant:
rConstant = math.log(intermediateDensity/originalDensity)/intermediateTime

endpointTimeLower = round(math.log(endpointDensityLower/originalDensity)/rConstant)
endpointTimeUpper = round(math.log(endpointDensityUpper/originalDensity)/rConstant)
hourMinuteLower = '{:02d}:{:02d}'.format(*divmod(endpointTimeLower, 60))
hourMinuteUpper = '{:02d}:{:02d}'.format(*divmod(endpointTimeUpper, 60))
print(f"Expected time for OD of {endpointDensityLower}: {endpointTimeLower} minutes, or {hourMinuteLower} ")
print(f"Expected time for OD of {endpointDensityUpper}: {endpointTimeUpper} minutes, or {hourMinuteUpper} ")
