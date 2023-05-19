import random
import math

words = ["pizza", "flower", "cherry", "finished", "persuaded"] # Word to solve
    
randWord = random.choice(words) # Random word selected from words list

subtract = len(randWord)/2 
math.floor(subtract)

numLettersToRemove =  math.floor(subtract)

# Function that turns the word that needs to be solved into a list
def wordToSolveAsList(wordToSolve, randNumList, randNumber):
 for i in range(len(randWord)):
    wordToSolve.append(randWord[i])
       
    randNumList.append(randNumber)
    randNumber +=1 