import random

def replacingLetters(randNumList, indexReplaced):
    letterToReplace = random.randrange(len(randNumList))
    indexReplaced = randNumList[letterToReplace]

"""wordToSolve = []
randNumList = []
missingCharacters = {}

letterToReplace = random.randrange(len(randNumList))
indexReplaced = randNumList[letterToReplace]


missingCharacters[wordToSolve[indexReplaced]] = missingCharacters.get(wordToSolve[indexReplaced], []) + [indexReplaced] # List of values inside dictionary

randNumList.pop(letterToReplace)"""