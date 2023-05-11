import random
class  Hangman:
    words = ["pizza", "flower", "cherry"]
    randWord = random.choice(words)
    newWord = 1
    spacing = []

   
    randList = []
    for i in range(len(randWord)):
        randList.append(randWord[i])
    print(randList)

  
    
   
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

   