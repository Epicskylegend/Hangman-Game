import random
import math
import re

class Hangman:

    words = ["pizza", "flower", "cherry", "finished", "persuaded"] # Word to solve
    
    randWord = random.choice(words) # Random word selected from words list
    randNumber = 0
    endResult = ""
    missingCharacters = {}
    lives = 7

    wordToSolve = []
    randNumList = []

    # Helper functions below

    # Function that welcomes user to the game
    def welcomeToGame():
        print("\n")
        print("Welcome to the hangman game.")  
        print("\n") 

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
         print("You now have " + str(lives) + " lives remaining.\n")


    # Function that is called if the user solves the word
    def wordSolved(randWord):
        print("You solved the word " + '"' + randWord + '"'  + ", congratulations.\n")
        raise SystemExit
    

    # Function to display text if the user runs out of lives
    def outOfLives(randWord):
        print("You ran out of lives and the game ends.\n")
        print("The word you were trying to solve was " + '"' + randWord + '"' + ".\n")
        raise SystemExit 


         
    
    subtract = len(randWord)/2 
    math.floor(subtract)

    numLettersToRemove =  math.floor(subtract)
    #print(lettersToRemove)

   
    for i in range(len(randWord)):
        wordToSolve.append(randWord[i])
       
        randNumList.append(randNumber)
        randNumber +=1 
    #print(randNumList)

    

    for i in range(numLettersToRemove):

        letterToReplace = random.randrange(len(randNumList))
        indexReplaced = randNumList[letterToReplace]


        
        missingCharacters[wordToSolve[indexReplaced]] = missingCharacters.get(wordToSolve[indexReplaced], []) + [indexReplaced] # List of values inside dictionary
        #print(missingCharacters)

        randNumList.pop(letterToReplace)
   

        wordToSolve[indexReplaced] = "_"

    welcomeToGame()
    guessALetter(wordToSolve)
   
   
    while endResult != randWord:   
       
       
        validLetter = input("The letter you guess is: ")  
       
        if validLetter.isalpha and len(validLetter) == 1:
           print("\n")
     

        elif validLetter.isalpha() and len(validLetter) > 1:
            print("Invalid input. You can only enter in one letter at a time.\n")


        if validLetter in missingCharacters.keys() and len(missingCharacters[validLetter]) == 1:
            print("There is 1 " + '"' + validLetter + '"' + " missing from this word.\n")


            for i in (missingCharacters[validLetter]):    
                wordToSolve[i] = validLetter

            missingCharacters.pop(validLetter)
           


        elif validLetter in missingCharacters.keys() and len(missingCharacters[validLetter]) > 1:
            print("There are " + '"' + str(len(missingCharacters[validLetter])) + '" ' +  validLetter + "'s" + " missing from the word.")


            for i in (missingCharacters[validLetter]):
                wordToSolve[i] = validLetter   

            missingCharacters.pop(validLetter)
    

           
        elif not validLetter.isalpha():
            print( str(validLetter) + " is not a valid input. Please enter in a letter.""\n")
   


        elif validLetter.isalpha and len(validLetter) == 1 and validLetter not in missingCharacters.keys():
            noLettersMissing(validLetter)
            lives -=1

        displayWordToSolve(wordToSolve)
            
        if lives >= 1:
            remainingLives(lives)


        if missingCharacters == {}:
            wordSolved(randWord)
        
        if lives == 0:
            outOfLives(randWord)