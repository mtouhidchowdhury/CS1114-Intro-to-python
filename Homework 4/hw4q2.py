#a
#getting character from user
userCharacter = input("Please enter a character: ")

#checking whether it is upper, lower, numeric or else 
if userCharacter.isupper()== True:
    print(userCharacter," is upper case letter.")
elif userCharacter.islower()== True:
    print(userCharacter," is lower case letter.")
elif userCharacter.isdigit()== True:
    print(userCharacter," is a digit.")
else:
    print(userCharacter," is a non alphanumeric character.")


#b

#without using string methods 

#getting character from user
userSecondCharacter = input("Please enter another character: ")
AsciiValue = ord(userSecondCharacter)

#comparing ascii values of the character to its specific grouping

#printing the type 
if AsciiValue >= ord('a') and AsciiValue <= ord('z'):
    print("This is a lowercase letter.")
elif AsciiValue >= ord('A') and AsciiValue <= ord('Z'):
    print("This is a uppercase letter.")
elif AsciiValue >= ord('0') and AsciiValue <= ord('9'):
    print("This is a digit.")
else:
    print("This is a non alphanumeric character.")
