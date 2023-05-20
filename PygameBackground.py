import pygame
from pygame.locals import *
from HangmanGame import *
from PygamePole import *
import time

class Game:
    def __init__(self, backgroundWidth, backgroundHeight, poleWidth, poleHeight, headWidth, headHeight, lives):
     
        self.hangmanGame = Hangman()

        pygame.init()

        self.lives = lives
        self.startTIme = time.time()
       

        self.backgroundWidth = backgroundWidth
        self.backgroundHeight = backgroundHeight
        self.textX = 0
        self.textY = 0

        self.poleWidth = poleWidth
        self.poleHeight = poleHeight

        self.headWidth = headWidth
        self.headHeight = headHeight
          
        
        self.text_font = pygame.font.Font("C:\\Users\\adeba\\OneDrive\\Hangman\\Fonts\\EraserRegular-DO1D.ttf", 85)
        self.clock = pygame.time.Clock()


        self.window = pygame.display.set_mode((backgroundWidth, backgroundHeight))
      
        pygame.display.set_caption('Hangman Game')    
       
        pygame.display.flip()


    def drawText(self, text,textColor, x, y):
        welcome = self.text_font.render(text, True, textColor)
        self.window.blit(welcome, (x, y))
       

    def quitGame(self):
        pygame.quit()

    def draw(self):
        self.window.fill(0)
        self.drawBackground()
        self.drawPole()
        self.drawText("Welcome to the hangman game.",(255,255,255), self.textX, self.textY) 
        self.drawText("".join(wordToSolve),(255,255,255), 700, 920)
        self.drawText("Lives: " + str(self.lives) ,(255,255,255), 1420, 90)
        self.drawText("Time: " + str(self.getTimeElapsed()) ,(255,255,255), 750, 90)
        self.drawHangman()
        # hangmanHead = pygame.image.load('C:\\Users\\adeba\\OneDrive\\Images\\Pole.png')
        # hangmanHead = pygame.transform.scale(hangmanHead, (self.headWidth, self.headHeight))
        # self.window.blit(hangmanHead, (100,100))
        

        pygame.display.flip()
       
               

    def validInput(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                userInput = pygame.key.name(event.key)

                if userInput in missingCharacters.keys():
                    print("yes")
                    for i in (missingCharacters[userInput]):    
                        wordToSolve[i] = userInput
                        missingCharacters.pop(userInput)
                
        


    def drawBackground(self):
        backgroundImg = pygame.image.load('C:\\Users\\adeba\OneDrive\\Images\\chalkboard.jpg')
        backgroundImg = pygame.transform.scale(backgroundImg,(self.backgroundWidth, self.backgroundHeight))
        self.window.blit(backgroundImg, (0,0)) 

    def drawPole(self):
        poleImg = pygame.image.load('C:\\Users\\adeba\\OneDrive\\Images\\Pole.png')
        poleImg = pygame.transform.scale(poleImg, (self.poleWidth, self.poleHeight))
        self.window.blit(poleImg, (-75,-100))

    

    def drawHangman(self):
        if self.lives <= 6:
            hangmanHead = pygame.image.load('C:\\Users\\adeba\\OneDrive\\Images\\Hangman_Head.png')
            hangmanHead = pygame.transform.scale(hangmanHead, (self.headWidth, self.headHeight))
            self.window.blit(hangmanHead, (200,200))

    def drawList(self, li, textColor, x, y):
        "".join(li)
        self.drawText("".join(li), textColor, x, y)

    def getTimeElapsed(self):
        return int(time.time() - self.startTIme)


    # def resetTimer(self):
    #     self.startTIme = time.time()
        
        
        
        



        

    def update(self):
        self.deltaTime = 0.01 * self.clock.tick()
        self.textX  += 8 * self.deltaTime
        self.textY += 8 * self.deltaTime
        self.hangmanGame.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and pygame.key.name(event.key) not in missingCharacters.keys():
                self.lives -=1
                print(self.lives)
            elif event.type == pygame.KEYDOWN and pygame.key.name(event.key) in missingCharacters.keys():
                for i in (missingCharacters[pygame.key.name(event.key)]):    
                    wordToSolve[i] =  pygame.key.name(event.key)
                    missingCharacters.pop( pygame.key.name(event.key))
        # if self.lives == 0 or missingCharacters == {}:       
        #     pygame.quit()
        

        #self.drawHead(lives)
        

    def hasQuit(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
        return False
                
 

game = Game(1920, 1080, 1000, 1080, 1000, 1000, 7)

randNumber = 0
# lives = 7
secondsElasped = 0


wordToSolveAsList(wordToSolve, randNumList, randNumber)
replacingAndStoringLetters(numLettersToRemove)
displayWordToSolve(wordToSolve)

while not game.hasQuit():
    game.draw()
    game.update()
    
  