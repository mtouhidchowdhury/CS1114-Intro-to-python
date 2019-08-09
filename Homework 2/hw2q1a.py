#calculate the BMI of person by taking their weight and height

weight = float(input("please enter weight in kilograms:")) #user weight input
height = float(input("please enter height in meters:"))# user height input

BMI = weight / (height**2) #using the BMI formula 

print ("BMI is", round(BMI,7))#printing the results 
