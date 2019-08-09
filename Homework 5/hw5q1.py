
#getting user input 
userInput = int(input("Please enter a positive integer: "))
#setting counter for total to 0 
total = 0
#starting odd number from 1
oddNumbers = 1
#while total is less than the userInput, print odd number and add 2
#add to total so loop doesnt run infinitely 
while total < userInput:
    print (oddNumbers)
    oddNumbers += 2
    total += 1 
    
