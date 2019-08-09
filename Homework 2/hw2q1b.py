#takes user weight and height converts and then uses BMI formula

oneKilogram = 0.453592 # one kilogram in a pound
oneMeter = 0.0254 #one meter in an inch 

userPound = float(input("please enter weight in pounds:")) #takes users weight in pound

kilograms = userPound * oneKilogram #converts to kilogram 

userInches = float(input("please enter height in inches:"))#takes users height inches

inches = userInches * oneMeter #converts to meters 

BMI = kilograms / (inches**2) #bmi formula 

print("BMI is:", round(BMI,7))#printing outcome


