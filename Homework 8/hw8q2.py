'''
M Touhid Chowdhury
mtc405
function that returns the first word in a phrase
function that removes first word and gives remaining
function that reverses the phrase
main() interacts with user
'''


def returnFirstWord(phrase):
    indexOfFirstWord = phrase.find(' ')
    if indexOfFirstWord == -1:
        firstWord = phrase
    else:
        firstWord = phrase[:indexOfFirstWord]
    return firstWord


def removeFirstWord(phrase):
    indexOfFirstWord = phrase.find(' ')
    newPhrase = phrase[indexOfFirstWord+1:]
    return newPhrase


def reversePhrase(phrase):
    wordsInPhrase= phrase.count(' ')+1
    reversed1= ""
    count = 1
    while count <= wordsInPhrase:
        reversed1 =returnFirstWord(phrase) + ' '+  reversed1
        phrase = removeFirstWord(phrase)
        count += 1
    return reversed1


def driverMain():
    userPhrase = input("Please enter a phrase to reverse")
    newLine = reversePhrase(userPhrase)
    print(newLine)
    return newLine
    
driverMain()
