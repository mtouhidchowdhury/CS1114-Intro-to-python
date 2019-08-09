#takes 3 digit positive integer and prints the sum


user = int(input("please input a three digit positive number"))
#getting user input

firstDigit = user // 100
#first digit attained by dividing by 100 without remainder

secondDigit = (user // 10) % 10
#second digit attained by dividing by 10 without remainder, then taking remainder of that


thirdDigit = user % 10
# dividing by 10 and taking the remainder only(ones place)

sumOfDigits = firstDigit + secondDigit + thirdDigit
#sum of the digits

print(" The sum of its digits is", sumOfDigits)
#printing outcome 
