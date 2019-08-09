
#setting total to 1 
total = 1
#setting userNumber to 1 
userNumber = 1
#counting number of digits 
numberOfDigits = 0
while userNumber != "Done":
    userNumber = input("Please enter a positive integer or 'Done': ")
    if userNumber == "Done":
        total = total 
    else:
        total = int(userNumber) * total
        numberOfDigits+= 1
#calculating geometric mean 
geometricMean = total**(1/numberOfDigits)
#printing output
print(round(geometricMean,3))
