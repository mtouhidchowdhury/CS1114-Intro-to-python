#getting string from user
string = input("Please enter a string: ")
#beginning with empty string to further assign each character in 
emptyString = " "
#initiate detection as true 
detection = True 
for character in string:
    if character < emptyString:
        detection = False 
    emptyString = character
if detection == True:
    print(string, "is increasing")
if detection == False:
    print(string, "is not increasing")
    
