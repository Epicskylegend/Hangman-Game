
def welcomeToGame():
    print("\n")
    print("Welcome to the hangman game.")  
    print("\n") 


#def numbLettersToRemove(subtract, randWord):
    #  subtract = len(randWord)/2 
    #  math.floor(subtract)
    #  numLettersToRemove =  math.floor(subtract)


    # Function to print the word the user needs to solve
def displayWordToSolve(wordToSolve):
    print("The word currently looks like:")
    print(wordToSolve)
    print("\n")


    # Function that prompts user to guess a word
def guessALetter(wordToSolve):
    print("Guess a letter for the word below.\n")
    print(wordToSolve)
    print("\n") 


# Function that tells user when they guess a letter that isn't missing
def noLettersMissing(validLetter):
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
