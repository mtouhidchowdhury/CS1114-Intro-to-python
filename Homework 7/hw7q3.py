
#importing module
import random
#generating a random number and assign to a variable
randomNumber = random.randint(1,100)
#set number of guesses to 0 and how many remain to 5 
numberGuesses= 0
guessRemain = 5
#first guess
userGuess = int(input("please enter a number between 1 and 100: "))
# minus from guess remain and adding to number of guesses 
guessRemain -= 1
numberGuesses += 1
# making bounds for the ranges 
lowerBound = 0
upperBound = 101
#if first guess correct then goes to if otherwise goes to else 
if userGuess == randomNumber:
    print("Your Correct!")
#loop till guesses remaining is 0 and user's guess is the number 
else:
    while guessRemain != 0 and userGuess != randomNumber :
        if userGuess < randomNumber:
            lowerBound = userGuess
            userGuessLine = "Guess again between "+ str(lowerBound + 1) + " and " + str(upperBound - 1) + ". You have " + str(guessRemain) + " guesses remaining: "
            userGuess = int(input (userGuessLine))
            guessRemain -= 1
            numberGuesses += 1
        elif userGuess > randomNumber:
            upperBound = userGuess
            userGuessLine = "Guess again between " + str(lowerBound + 1) + " and "+ str(upperBound - 1) + ". You have " + str(guessRemain) + " guesses remaining: "
            userGuess = int(input (userGuessLine))
            guessRemain -= 1
            numberGuesses += 1
#output if won tells how many guesses took if lost then tells user that he/she lost 
if userGuess == randomNumber:
    line= "Congrats! you guessed the answer in " + str(numberGuesses) + " guesses!"
    print(line)
else:
    print ("You ran out of guesses")
    
    

