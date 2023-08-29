import random
import math

with open('C:\\Users\\adeba\\OneDrive\\Hangman\\words.txt'.strip('\n')) as f:
  lines = f.readlines()

randWord = str(random.choice(lines).strip())

# print(randWord)

subtract = len(randWord)/2 
math.ceil(subtract)

numLettersToRemove =  math.ceil(subtract)

# Function that turns the word that needs to be solved into a list
def wordToSolveAsList(wordToSolve, randNumList, randNumber):
 for i in range(len(randWord)):
 
    wordToSolve.append(randWord[i])
    randNumList.append(randNumber)
    randNumber +=1