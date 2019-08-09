#part a 

#asking user to input odd length string
userString = input("Please enter a string of odd length: ")

#getting the length of the string
userStringLength = len(userString)

#dividing the string by integer division
indexOfMiddleCharacter = (userStringLength // 2) 

#getting the index that number
middleCharacter = userString[indexOfMiddleCharacter]
#printing the output

print("middle character: ", middleCharacter)


#part b

#getting the first half of the string by splitting
firstHalf = userString[0:indexOfMiddleCharacter]

#printing the output
print("The first half of the string: ",firstHalf)

#c

#getting the second half of the string by splitting
secondHalf = userString[indexOfMiddleCharacter+1:]

#printing the second half 
print("The second half of the string: ",secondHalf)
