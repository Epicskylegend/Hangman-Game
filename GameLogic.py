import random
#from RandWordGenerator import numLettersToRemove

missingCharacters = {}
wordToSolve = []
randNumList = []


def replacingLetters(randNumList, indexReplaced):
    letterToReplace = random.randrange(len(randNumList))
    indexReplaced = randNumList[letterToReplace]


#def removeLetterFromDict(randNumList, letterToReplace):
   


def replacingAndStoringLetters(numLettersToRemove):
    for i in range(numLettersToRemove):

        letterToReplace = random.randrange(len(randNumList))
        indexReplaced = randNumList[letterToReplace]

        missingCharacters[wordToSolve[indexReplaced]] = missingCharacters.get(wordToSolve[indexReplaced], []) + [indexReplaced] # List of values inside dictionary

        randNumList.pop(letterToReplace)

        wordToSolve[indexReplaced] = "_"

        