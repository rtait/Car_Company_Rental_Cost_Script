import sys
'''
Section 1: Collect customer input
'''
##Collect Customer Data - Part 1

##1)	Request Rental code:
#Prompt --> "(B)udget, (D)aily, or (W)eekly rental?"
rentalCode = input ("(B)udget, (D)aily, or (W)eekly rental?\n")

#2)	Request time period the car was rented.
#Prompt --> "Number of Days Rented:"
#Prompt --> "Number of Weeks Rented:"
#rentalPeriod = ?
#first branch - if/elif to determine the rentalcode
if  rentalCode == 'D':
   rentalPeriod = input ("Number of Days Rented:\n")
elif  rentalCode == 'B':
   rentalPeriod = input ("Number of Days Rented:\n")
elif rentalCode == 'W':
   rentalPeriod = input ("Number of Weeks Rented:\n")

#Calculation Part 1

##Set the base charge for the rental type as the variable baseCharge. 
#The base charge is the rental period * the appropriate rate:

budget_charge = 40.00
daily_charge = 60.00
weekly_charge = 190.00

#additional decision tree for rentalcode including basecharge
if rentalCode =='B':
   baseCharge = int(rentalPeriod) * int(budget_charge)
elif  rentalCode == 'D':
   baseCharge = int(rentalPeriod) * int(daily_charge)
elif rentalCode == 'W':
   baseCharge = int(rentalPeriod) * int(weekly_charge)
  
#Collect Customer Data - Part 2

#4)Collect Mileage information:
#a)	Prompt the user to input the starting odometer reading and store it as the variable odoStart

#Prompt -->"Starting Odometer Reading:\n"
# odoStart = ?
odoStart = input ("Starting Odometer Reading: \n")

#b)	Prompt the user to input the ending odometer reading and store it as the variable odoEnd

#Prompt -->"Ending Odometer Reading:"
# odoEnd = ?
odoEnd = input ("Ending Odometer Reading: \n")

#c) Calculate total miles

totalMiles = int(odoEnd) - int(odoStart)

# Calculate Charges 2

##	Calculate the mileage charge and store it as 
#   the variable mileCharge:
# rentalCode input
# Charges include a 3rd branching system to determine any additional charges

#a)	Code 'B' (budget) mileage charge: $0.25 for each mile driven
if rentalCode == 'B':
  mileCharge = int(totalMiles * 0.25)
  total = mileCharge + baseCharge

#b)	Code 'D' (daily) mileage charge: no charge if the average
#   number of miles driven per day is 100 miles or less;
#   i)	Calculate the averageDayMiles (totalMiles/rentalPeriod)

elif rentalCode == 'D':
  averageDayMiles = int(totalMiles) / int(rentalPeriod)
  if averageDayMiles <=100:
    extraMiles = 0
    total = baseCharge
    
#   ii)	If averageDayMiles is above the 100 mile per day
#       limit:
#     (1)	calculate extraMiles (averageDayMiles  - 100)
#     (2)	mileCharge is the charge for extraMiles, 
#         $0.25 for each mile
  elif averageDayMiles >100:
    extraMiles = averageDayMiles - 100
    mileCharge = baseCharge + (extraMiles * 0.25)
    total = mileCharge
    
#c)	Code 'W' (weekly) mileage charge: no charge if the 
#   average number of miles driven per week is 
#   900 miles or less;
 
#   i)	Calculate the averageWeekMiles (totalMiles/ rentalPeriod)

#   ii)	mileCharge is $100.00 per week if the average number of miles driven per week exceeds 900 miles
elif rentalCode == 'W':
  averageWeekMiles = int(totalMiles) / int(rentalPeriod)
  if averageWeekMiles < 900: 
    total = baseCharge
  else:
    total = baseCharge + int(rentalPeriod * 100)
  
#Printing the rental summary
print ("Rental Code:", rentalCode)
print ("Rental Period:", rentalPeriod)
print ("Starting Odometer:", odoStart)
print ("Ending Odometer:", odoEnd)
print ("Miles Driven:", totalMiles)
print ("Amount Due: $" , "%.2f" % total)

#   END