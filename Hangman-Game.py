import random
import math

class  Hangman:

    words = ["pizza", "flower", "cherry"]
    randWord = random.choice(words)
    spacing = []
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
        randNumList.pop(letterToReplace)
       
        #print(replaceLetter)
        randList[letterReplaced] = "_"
        newWord = ''.join(randList)
    
    print(newWord)



  
    
   
    print("Guess a letter for the word below")
    """while newWord != randWord:   

        print(randWord)
        for i in range(len(randWord)):
           if i < len(randWord):
                spacing += "_"
                i+=1
                newSpacing = ''.join(spacing)
        print(newSpacing) """
    
    
    validInput = input(randWord)
    if validInput.isalpha and len(validInput) == 1:
        print("The letter you guess is " + validInput + ".")
    else:
        print("Invalid input.")
      
        

  
    #print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

   