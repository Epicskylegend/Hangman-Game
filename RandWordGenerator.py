import random
import math

words = ["pizza", "flower", "cherry", "finished", "persuaded"] # Word to solve
    
randWord = random.choice(words) # Random word selected from words list

subtract = len(randWord)/2 
math.floor(subtract)

numLettersToRemove =  math.floor(subtract)


def wordToSolveAsList(wordToSolve, randNumList, randNumber):
 for i in range(len(randWord)):
    wordToSolve.append(randWord[i])
       
    randNumList.append(randNumber)
    randNumber +=1 