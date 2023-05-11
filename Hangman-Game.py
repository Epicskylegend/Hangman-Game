import random
import math

class  Hangman:

    words = ["pizza", "flower", "cherry"]
    randWord = random.choice(words)
    spacing = []
    storedLetters = []
    randNumber = 0


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
        letterReplaced = randNumList[letterToReplace]

        storedLetters.append(randList[letterReplaced]) # Stores the characters the user needs to guess
        print(storedLetters)

        randNumList.pop(letterToReplace)
   

        #print(replaceLetter)
        randList[letterReplaced] = "_"
        newWord = ''.join(randList)
    print("\n\n\n") 
    print(newWord)



  
    
   
    print("Guess a letter for the word below\n")
    while newWord != randWord:   

        
        for i in range(len(randWord)):
           if i < len(randWord):
                #spacing += "_"
              
                newSpacing = ''.join(spacing)
        #print(newSpacing) 
    
    
        validInput = input("Guess a letter: ")
        if validInput.isalpha == True and len(validInput) == 1:
            print("The letter you guess is: " + validInput + ".")
        else:
            print("Invalid input.")
      
        

  
    #print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

   