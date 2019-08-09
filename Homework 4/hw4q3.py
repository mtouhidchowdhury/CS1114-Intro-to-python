#getting users desired expression
userExpression = input("Please input a mathematical expression: ")

#position of the blank
positionOfBlank = userExpression.find(' ')

#getting first number by indexing to the blank 
firstNumber = userExpression[0:positionOfBlank]

#taking the remainder of the statement 
remaining = userExpression[positionOfBlank+1:]

#getting the operator by taking the next first index
operand = remaining[0]

#getting second number by taking the remainder after the position
secondNumber = remaining[positionOfBlank:]

#checking what the operator is and doing the calculation
#printing the result 
if operand == '+':
    total = int(firstNumber) + int(secondNumber)
    print(firstNumber," + ",secondNumber," = ", total)
if operand == '-':
    total = int(firstNumber) - int(secondNumber)
    print(firstNumber," - ",secondNumber," = ", total)
if operand == '/':
    total = int(firstNumber) / int(secondNumber)
    print(firstNumber," / ",secondNumber," = ", total)
if operand == '*':
    total = int(firstNumber) * int(secondNumber)
    print(firstNumber," * ",secondNumber," = ", total)
