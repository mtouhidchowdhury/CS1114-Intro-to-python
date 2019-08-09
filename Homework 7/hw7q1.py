

#getting string and number to shift 
string = input("Please enter a text")
shift = int(input("please enter a shift:"))
#empty string to put the ciphered message in
cipher =""
#loop through string 
for currentLetter in string:
    if currentLetter.isupper():
        curciph = ord(currentLetter)+shift
        if curciph >= 91:
            curciph = curciph - 26
        cipher = cipher + chr(curciph)
    elif currentLetter.islower():
        curciph = ord(currentLetter)+ shift
        if curciph >= 123:
            curciph = curciph -26
        cipher = cipher + chr(curciph)
    else:
        cipher = cipher + currentLetter
#print outcome        
print("Encrypted string is:", cipher)      
