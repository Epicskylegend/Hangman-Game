import random
import math
import re

class  Hangman:

    words = ["pizza", "flower", "cherry", "finished", "persuaded"]
    alphabet = {"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o",
                "p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I",
                "J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"}
    randWord = random.choice(words)
    spacing = []
    randNumber = 0
    endResult = ""
    missingCharacters = {}
    lives = 7
   
    



    subtract = len(randWord) /2 
    math.floor(subtract)
    lettersToRemove =  math.floor(subtract)
    #print(lettersToRemove)

    randList = []
    randNumList = []
    for i in range(len(randWord)):
        randList.append(randWord[i])
        #print(randList)
        randNumList.append(randNumber)
        randNumber +=1 
    #print(randNumList)

    

    for i in range(lettersToRemove):

        letterToReplace = random.randrange(len(randNumList))
        indexReplaced = randNumList[letterToReplace]


        
        #missingCharacters[randList[indexReplaced]] = [indexReplaced] # dictionary that stores values user needs to guess 
        
        missingCharacters[randList[indexReplaced]] = missingCharacters.get(randList[indexReplaced], []) + [indexReplaced] 
        print(missingCharacters)

        randNumList.pop(letterToReplace)
   

        #print(replaceLetter)
        randList[indexReplaced] = "_"
        #newWord = ''.join(randList)
    print("\n\n\n") 
    print(randList)


 
    print(randWord)
    print("Guess a letter for the word above\n")
    while endResult != randWord:   

        
        for i in range(len(randWord)):
           if i < len(randWord):
                #spacing += "_"
              
                newSpacing = ''.join(spacing)
        #print(newSpacing) 
    
    
        validLetter = input("Guess a letter: ")
        
       
        if validLetter in alphabet and len(validLetter) == 1:
            print("The letter you guess is: " + validLetter + ".")
        else:
            print("Invalid input. Enter in a single letter.")



        if validLetter in missingCharacters.keys():
            print("There is at least 1 " + validLetter + " missing inside of this word.")

            for i in (missingCharacters[validLetter]):
                randList[i] = validLetter
                #print(randList)

            missingCharacters.pop(validLetter)
            print(missingCharacters)
            endResult == ''.join(randList)
            print(endResult)


           
          
            print("The word now looks like:")
            print(randList)
            print("\n")
           
        else:
            print("There are NOT any " + validLetter + "'s missing inside of this word. That's a strike.")
            lives -= 1
            print("You now have " + str(lives) + " lives remaining.\n")


        if missingCharacters == {}:
            print("You solved the word " + randWord + " congratulations.\n")
            raise SystemExit
        
        if lives == 0:
            print("You ran out of lives and the game ends.")
            raise SystemExit

    
        
      
        

  
    #print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

   