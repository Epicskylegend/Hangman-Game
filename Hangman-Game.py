import random
import math
import re

class Hangman:

    words = ["pizza", "flower", "cherry", "finished", "persuaded"] # Word to solve
    alphabet = {"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o",
                "p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I",
                "J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"}
    
    randWord = random.choice(words) # Random word selected from words list
    randNumber = 0
    endResult = ""
    missingCharacters = {}
    lives = 7
   
    

    subtract = len(randWord) /2 
    math.floor(subtract)
    numLettersToRemove =  math.floor(subtract)
    #print(lettersToRemove)

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


        
        missingCharacters[wordToSolve[indexReplaced]] = missingCharacters.get(wordToSolve[indexReplaced], []) + [indexReplaced] 
        #print(missingCharacters)

        randNumList.pop(letterToReplace)
   

        wordToSolve[indexReplaced] = "_"
      
    print("\n\n\n") 
    print(wordToSolve)


    
    print("Guess a letter for the word above\n")
    while endResult != randWord:   
    
    
        validLetter = input("Guess a letter: ")
        
       
        if validLetter.isalpha and len(validLetter) == 1:
            print("The letter you guess is: " + validLetter + ".")

        elif validLetter.isalpha() and len(validLetter) > 1:
            print("Invalid input. You can only enter in one letter at a time.\n")



        if validLetter in missingCharacters.keys():
            print("There is at least 1 " + validLetter + " missing inside of this word.\n")

            for i in (missingCharacters[validLetter]):
                wordToSolve[i] = validLetter
            

            missingCharacters.pop(validLetter)
    
            
          
            print("The word now looks like:")
            print(wordToSolve)
            print("\n")
           
        elif not validLetter.isalpha():
            print( str(validLetter) + " is not a valid input. Please enter in a letter.""\n")
            print("The word currently looks like: ")
            print(wordToSolve)
            print("\n")

        elif validLetter in alphabet and validLetter not in missingCharacters.keys():
            print("There are NOT any " + validLetter + "'s missing inside of this word. You lose a life.\n")
            print("The word currently looks like: ")
            print(wordToSolve)
            print("\n")
            lives -= 1 
           
            
            if lives >= 1:
                print("You now have " + str(lives) + " lives remaining.\n")


        if missingCharacters == {}:
            print("You solved the word " + randWord + " congratulations.\n")
            raise SystemExit
        
        if lives == 0:
            print("You ran out of lives and the game ends.\n")
            print("The word you were trying to solve was " + randWord + ".\n")
            raise SystemExit 