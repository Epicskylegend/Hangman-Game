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
        #print(randList)
        randNumList.append(randNumber)
        randNumber +=1 
    #print(randNumList)

    

    for i in range(numLettersToRemove):

        letterToReplace = random.randrange(len(randNumList))
        indexReplaced = randNumList[letterToReplace]


        
        #missingCharacters[randList[indexReplaced]] = [indexReplaced] # dictionary that stores values user needs to guess 
        
        missingCharacters[wordToSolve[indexReplaced]] = missingCharacters.get(wordToSolve[indexReplaced], []) + [indexReplaced] 
        #print(missingCharacters)

        randNumList.pop(letterToReplace)
   

        #print(replaceLetter)
        wordToSolve[indexReplaced] = "_"
        #newWord = ''.join(randList)
    print("\n\n\n") 
    print(wordToSolve)


 
    
    print("Guess a letter for the word above\n")
    while endResult != randWord:   
    
    
        validLetter = input("Guess a letter: ")
        
       
        if validLetter in alphabet and len(validLetter) == 1:
            print("The letter you guess is: " + validLetter + ".")
        else:
            print("Invalid input. Enter in a single letter.\n")



        if validLetter in missingCharacters.keys():
            print("There is at least 1 " + validLetter + " missing inside of this word.\n")

            for i in (missingCharacters[validLetter]):
                wordToSolve[i] = validLetter
                #print(randList)

            missingCharacters.pop(validLetter)
    
            
          
            print("The word now looks like:")
            print(wordToSolve)
            print("\n")
           
        else:
            print("There are NOT any " + validLetter + "'s missing inside of this word. That's a strike.\n")
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
            raise SystemExit 