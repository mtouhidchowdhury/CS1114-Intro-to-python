#this program takes years in integers and prints out estimated population

import math

#constants 
currentPopulation = 307357870
daysInYear = 365
HourInDay = 24
secondsInHour = 3600
#getting user input of number of years 
userInputYear = int(input("please enter the number of years: "))

#telling the user to wait while the program calculates
print("Please wait while we calculate....")

#converting user input to seconds 
seconds = userInputYear * daysInYear * HourInDay * secondsInHour

#getting the change of rate of each difference 
birthRate = seconds * (1/7)
deathRate = seconds * (1/13)
immigrantRate = seconds * (1/35)

#adding the changes to current population to get the new population 
population = currentPopulation + birthRate + immigrantRate - deathRate

#print new population 
print(" The estimated population growth is", int(population))
