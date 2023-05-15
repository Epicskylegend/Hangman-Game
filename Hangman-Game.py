from InputOutput import *
from RandWordGenerator import *
from GameLogic import *

class Hangman():
   
    randNumber = 0
    endResult = "" 
    lives = 7


    wordToSolveAsList(wordToSolve, randNumList, randNumber)
    replacingAndStoringLetters(numLettersToRemove)
    

    welcomeToGame()
    guessALetter(wordToSolve)
   
   
    while endResult != randWord:   
       
       
        validLetter = input("The letter you guess is: ")  
       
        if validLetter.isalpha and len(validLetter) == 1:
           newLine()
     
        elif validLetter.isalpha() and len(validLetter) > 1:
            invalidMultipleLetters()



        if validLetter in missingCharacters.keys() and len(missingCharacters[validLetter]) == 1:
            oneLetterMissing(validLetter)


            replaceMissingCharacters(missingCharacters, validLetter)

            missingCharacters.pop(validLetter)

           
        elif validLetter in missingCharacters.keys() and len(missingCharacters[validLetter]) > 1:
            
            multipleLettersMissing(validLetter, missingCharacters)

            replaceMissingCharacters(missingCharacters, validLetter)

            missingCharacters.pop(validLetter)
    
           
        elif not validLetter.isalpha():
           invalidInputNotLetter(validLetter)
   

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