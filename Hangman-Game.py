import re
from InputOutput import *
from RandWordGenerator import *

class Hangman():
   
    randNumber = 0
    endResult = ""
    missingCharacters = {}
    lives = 7

    wordToSolve = []
    randNumList = []


    for i in range(len(randWord)):
        wordToSolve.append(randWord[i])
       
        randNumList.append(randNumber)
        randNumber +=1 
    #print(randNumList)



    for i in range(numLettersToRemove):

        letterToReplace = random.randrange(len(randNumList))
        indexReplaced = randNumList[letterToReplace]

   
        missingCharacters[wordToSolve[indexReplaced]] = missingCharacters.get(wordToSolve[indexReplaced], []) + [indexReplaced] # List of values inside dictionary

        randNumList.pop(letterToReplace)
   

        wordToSolve[indexReplaced] = "_"

    welcomeToGame()
    guessALetter(wordToSolve)
   
   
    while endResult != randWord:   
       
       
        validLetter = input("The letter you guess is: ")  
       
        if validLetter.isalpha and len(validLetter) == 1:
           print("\n")
     

        elif validLetter.isalpha() and len(validLetter) > 1:
            invalidMultipleLetters()

        if validLetter in missingCharacters.keys() and len(missingCharacters[validLetter]) == 1:
            oneLetterMissing(validLetter)


            for i in (missingCharacters[validLetter]):    
                wordToSolve[i] = validLetter

            missingCharacters.pop(validLetter)
           


        elif validLetter in missingCharacters.keys() and len(missingCharacters[validLetter]) > 1:
            
            multipleLettersMissing(validLetter, missingCharacters)

            for i in (missingCharacters[validLetter]):
                wordToSolve[i] = validLetter   

            missingCharacters.pop(validLetter)
    

           
        elif not validLetter.isalpha():
            invalidNumber(validLetter)
   


        elif validLetter.isalpha and len(validLetter) == 1 and validLetter not in missingCharacters.keys():
            wrongLetter(validLetter)
            lives -=1

        displayWordToSolve(wordToSolve)
            
        if lives >= 1:
            remainingLives(lives)


        if missingCharacters == {}:
            wordSolved(randWord)
        
        if lives == 0:
            outOfLives(randWord)