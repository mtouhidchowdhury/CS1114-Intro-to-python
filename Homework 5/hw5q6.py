#obtaining user string
userString = input("Please enter line of text: ")
#obtaining letter to remove 
character = input("Please enter a character you want to remove: ")
#new string initialized
string =""
for letter in userString:
    if letter != character:
        string += letter
#print new string
print(string)
    
