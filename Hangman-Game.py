import random
import math

class  Hangman:

    words = ["pizza", "flower", "cherry"]
    alphabet = {"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o",
                "p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I",
                "J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"}
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



  
    
   
    print("Guess a letter for the word above\n")
    while newWord != randWord:   

        
        for i in range(len(randWord)):
           if i < len(randWord):
                #spacing += "_"
              
                newSpacing = ''.join(spacing)
        #print(newSpacing) 
    
    
        validInput = input("Guess a letter: ")
        if validInput in alphabet and len(validInput) == 1:
            print("The letter you guess is: " + validInput + ".")
        else:
            print("Invalid input. Enter in a single letter.")
        if validInput in randWord:
            print("There is at least 1 " + validInput + " inside of this word.")
            print("The word now looks like " )
        else:
            print("There are NOT any " + validInput + "'s inside of this word. That's a strike.")
      
        

  
    #print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

   