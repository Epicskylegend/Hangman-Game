import pygame
from pygame.locals import *
from HangmanGame import *
from PygamePole import *

class Game:
    def __init__(self, backgroundWidth, backgroundHeight, poleWidth, poleHeight, headWidth, headHeight, lives):
     
        self.hangmanGame = Hangman()

        pygame.init()

        self.lives = lives
        self.backgroundWidth = backgroundWidth
        self.backgroundHeight = backgroundHeight
        self.textX = 0
        self.textY = 0

        self.poleWidth = poleWidth
        self.poleHeight = poleHeight

        self.headWidth = headWidth
        self.headHeight = headHeight
          
        
        self.text_font = pygame.font.SysFont(None, 100)
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
        self.drawText(str(wordToSolve),(255,255,255), 700, 920)
        self.drawText("Lives: " + str(self.lives) ,(255,255,255), 1550, 90)
        self.drawText("Time: " + str(secondsElasped) ,(255,255,255), 750, 90)
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
        if self.lives == 6:
            hangmanHead = pygame.image.load('C:\\Users\\adeba\\OneDrive\\Images\\Hangman_Head.png')
            hangmanHead = pygame.transform.scale(hangmanHead, (self.headWidth, self.headHeight))
            self.window.blit(hangmanHead, (-15,-100))
        



        

    def update(self):
        self.deltaTime = 0.01 * self.clock.tick()
        self.textX  += 8 * self.deltaTime
        self.textY += 8 * self.deltaTime
        self.hangmanGame.update()
        self.drawHangman()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and pygame.key.name(event.key) not in missingCharacters.keys():
                self.lives -=1
                print(self.lives)
            elif event.type == pygame.KEYDOWN and pygame.key.name(event.key) in missingCharacters.keys():
                for i in (missingCharacters[pygame.key.name(event.key)]):    
                    wordToSolve[i] =  pygame.key.name(event.key)
                    missingCharacters.pop( pygame.key.name(event.key))
        if self.lives == 0 or missingCharacters == {}:       
            pygame.quit()
        

        #self.drawHead(lives)
        

    def hasQuit(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
        return False
                
 

game = Game(1920, 1080, 1000, 1080, 10, 10, 7)

randNumber = 0
# lives = 7
secondsElasped = 0


wordToSolveAsList(wordToSolve, randNumList, randNumber)
replacingAndStoringLetters(numLettersToRemove)
displayWordToSolve(wordToSolve)

while not game.hasQuit():
    game.draw()
    game.update()
  