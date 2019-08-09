userInput = int(input("please enter number"))

n = 0
m = "1"
num = 1
space = ' '
while n != userInput:
    line = space* (userInput-n) + m
    nextNumber = num + 1
    num += 1 
    m += str(nextNumber)
    n += 1
    print(line)
    

