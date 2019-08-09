
#getting user bound
userInput = int(input("Please enter a positive integer: "))
#begin with 2 
number = 2

while number < userInput or (number == userInput):
    even = 0
    odd = 0
    for x in str(number):
        if int(x) % 2 == 0:
            even += 1
        else:
            odd += 1
    if even > odd:
        print(number)
    number += 2 
