#getting user length of sequence 
length = int(input("please enter the length of the sequence: "))
#set a variable to 0 to compare to length 
start = 0
#total of all numbers set to 1 for now 
total = 1
#loops while start isnt equal to length 
while start != length:
    userNumber = int(input("Please enter a positive integer: "))
    total = userNumber * total
    start += 1
#calculating geometric mean 
geometricMean = total**(1/length)
#printing output
print(round(geometricMean,3))
