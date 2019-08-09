#getting word from user 
userWord = input("Please enter a word: ")

#setting vowel and consonant count to 0 
vowels = 0
consonants = 0

#looping through the word and checking if it has vowels or consonant 
for letter in userWord:
    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u' or letter == 'A' or letter == 'E' or letter == 'I' or letter == 'O' or letter == 'U' :
        vowels += 1
    else:
        consonants += 1

#printing the outcome 
print(userWord, "has", vowels,"vowels and", consonants, "consonants.")
