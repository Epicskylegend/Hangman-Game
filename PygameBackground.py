import pygame
from pygame.locals import *
from PygamePole import *
from HangmanGame import *

class Game:
    def __init__(self, backgroundWidth, backgroundHeight):
       
        pygame.init()

        self.backgroundWidth = backgroundWidth
        self.backgroundHeight = backgroundHeight
        self.textX = 0
        self.textY = 0

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
        self.drawText("Welcome to the hangman game.",(255,255,255), self.textX, self.textY) 
        game.drawText("Lives" ,(255,255,255), 1700, 10)
        pygame.display.flip()


    def drawBackground(self):
        backgroundImg = pygame.image.load('C:\\Users\\adeba\OneDrive\\Images\\chalkboard.jpg')
        backgroundImg = pygame.transform.scale(backgroundImg,(self.backgroundWidth, self.backgroundHeight))
        self.window.blit(backgroundImg, (0,0)) 

        

    def update(self):
        self.deltaTime = 0.01 * self.clock.tick()
        self.textX  += 8 * self.deltaTime
        self.textY += 8 * self.deltaTime
        


    def hasQuit(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
        return False
                
 

game = Game(1920, 1080)



while not game.hasQuit():
    game.draw()
    game.drawText("Lives" ,(255,255,255), 500, 500)
    game.update()
    print("loop")
    #drawPole(poleWidth, poleHeight)

