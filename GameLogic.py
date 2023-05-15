import random

missingCharacters = {}
wordToSolve = []
randNumList = []


# Function for replacing missing letters when user guess correct letter(s)
def replaceMissingCharacters(missingCharacters, validLetter):
    for i in (missingCharacters[validLetter]):    
        wordToSolve[i] = validLetter
   

# Function that replacing random indices from the word to solve with underscores and adds them to a dictionary of lists
def replacingAndStoringLetters(numLettersToRemove):
    for i in range(numLettersToRemove):

        letterToReplace = random.randrange(len(randNumList))
        indexReplaced = randNumList[letterToReplace]

        missingCharacters[wordToSolve[indexReplaced]] = missingCharacters.get(wordToSolve[indexReplaced], []) + [indexReplaced] # List of values inside dictionary

        randNumList.pop(letterToReplace)

        wordToSolve[indexReplaced] = "_"     

        
# Function that removes letters from dictionary once they've been guessed
def removeLetterFromDict(validLetter):
    missingCharacters.pop(validLetter)
    