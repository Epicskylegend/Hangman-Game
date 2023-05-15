# Function that welcomes the user to the game
def welcomeToGame():
    print("\n")
    print("Welcome to the hangman game.")  
    print("\n") 


# Function to print the word the user needs to solve
def displayWordToSolve(wordToSolve):
    print("The word currently looks like:")
    print(wordToSolve)
    print("\n")

def newLine():
    print("\n")


# Function that prompts user to guess a word
def guessALetter(wordToSolve):
    print("Guess a letter for the word below.\n")
    print(wordToSolve)
    print("\n") 


# Function that gives the user an error when they enter in more than 1 letter
def invalidMultipleLetters():
    print("Invalid input. You can only enter in one letter at a time.\n")

# Functions that tells the user they entered in an integer which isn't allowed
def invalidNumber(validLetter):
     print( str(validLetter) + " is not a valid input. Please enter in a letter.""\n")


# Function that tells user that there is one of the letter they guessed missing
def oneLetterMissing(validLetter):
      print("There is 1 " + '"' + validLetter + '"' + " missing from this word.\n")


# Function that tells user that there are multiple of the letter they guessed missing
def multipleLettersMissing(validLetter, missingCharacters):
    print("There are " + '"' + str(len(missingCharacters[validLetter])) + '" ' +  validLetter + "'s" + " missing from the word.")


# Function that tells user when they guess a letter that isn't missing
def wrongLetter(validLetter):
    print("There are no " + validLetter + "'s missing inside of this word. You lose a life.\n")


# Function called to display the leftover lives of the user
def remainingLives(lives):
        print("You currently have " + str(lives) + " lives remaining.\n")


# Function that is called if the user solves the word
def wordSolved(randWord):
    print("You solved the word " + '"' + randWord + '"'  + ", congratulations.\n")
    raise SystemExit


# Function to display text if the user runs out of lives
def outOfLives(randWord):
    print("You ran out of lives and the game ends.\n")
    print("The word you were trying to solve was " + '"' + randWord + '"' + ".\n")
    raise SystemExit 