#calculate the BMI of person by taking their weight and height then classifying them

weight = float(input("please enter weight in kilograms:")) #user weight input
height = float(input("please enter height in meters:"))# user height input

BMI = weight / (height**2) #using the BMI formula 

print ("BMI is", round(BMI,7))#printing the results 
#classifying the person based on bmi
if BMI < 18.5:
    print("Your considered underweight.")
elif 18.5 >= BMI <= 24.9:
    print("Your considered normal.")
elif 25>= BMI <= 29.9:
    print("Your condered overweight.")
elif BMI >= 30:
    print("Your Obese!")
