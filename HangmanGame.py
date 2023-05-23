import pygame
from pygame.locals import *
from HangmanLogic import *
import time
from Clock import Clock
from gameSounds import Sounds
from gameSounds import *

class Game:
    def __init__(self, backgroundWidth, backgroundHeight, poleWidth, poleHeight, headWidth, headHeight, bodyWidth, bodyHeight, legWidth, legHeight, armWidth, armHeight, lives):
     
        self.hangmanGame = Hangman()
        self.gameTimer = Clock()
        self.exitTimer = Clock()
        self.isGameOver = False
        
        self.playGameSounds = Sounds()

    

        pygame.init()
        pygame.mixer.init()

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

        self.bodyWidth = bodyWidth
        self.bodyHeight = bodyHeight

        self.legWidth = legWidth
        self.legHeight = legHeight

        self.armWidth = armWidth
        self.armHeight = armHeight
          
        
        self.text_font = pygame.font.Font("C:\\Users\\adeba\\OneDrive\\Hangman\\Fonts\\EraserRegular-DO1D.ttf", 70)
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
        #self.drawText("Welcome to the hangman game.",(255,255,255), self.textX, self.textY) 
        if missingCharacters != {} and self.lives != 0:
            self.drawText("".join(wordToSolve),(255,255,255), 700, 750)

        elif missingCharacters == {}:
            self.drawText("You solved the word ", (255,255,255), 550, 800)
            self.drawText('"' + ("".join(wordToSolve) + '"'), (255,255,255), 800, 900)

        self.drawText("Lives: " + str(self.lives) ,(255,255,255), 1420, 90)

        if self.lives == 0:
            self.drawText("The word you tried to solve was: " , (255,255,255), 300, 800)
            self.drawText('"' + ("".join(randWord) + '"'), (255,255,255), 800, 900)

        self.drawText("Time: " + str(self.getTimeElapsed()) ,(255,255,255), 800, 90)

        if self.lives > 0 and missingCharacters != {}:
            self.drawText("".join(alphabet), (255,255,255), 330, 900)


        self.drawHangman()
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
        poleImg = pygame.image.load('C:\\Users\\adeba\\OneDrive\\Images\\Hangman_Pole.png')
        poleImg = pygame.transform.scale(poleImg, (self.poleWidth, self.poleHeight))
        self.window.blit(poleImg, (-75,-100))

    

    def drawHangman(self):
        if self.lives <= 5:
            hangmanHead = pygame.image.load('C:\\Users\\adeba\\OneDrive\\Images\\Hangman_Head.png')
            hangmanHead = pygame.transform.scale(hangmanHead, (self.headWidth, self.headHeight))
            self.window.blit(hangmanHead, (270,-15))


        if self.lives <= 4:
            hangmanBody = pygame.image.load('C:\\Users\\adeba\\OneDrive\\Images\\Hangman_Body.png')
            hangmanBody = pygame.transform.scale(hangmanBody, (self.bodyWidth, self.bodyHeight))
            self.window.blit(hangmanBody, (115,250))

        if self.lives <= 3:
            hangmanArm1 = pygame.image.load('C:\\Users\\adeba\\OneDrive\\Images\\Hangman_Arm.png')
            hangmanArm1 = pygame.transform.scale(hangmanArm1, (self.armWidth, self.armHeight))
            self.window.blit(hangmanArm1, (270,-30))

        if self.lives <= 2:
            hangmanArm2 = pygame.image.load('C:\\Users\\adeba\\OneDrive\\Images\\Hangman_Arm2.png')
            hangmanArm2 = pygame.transform.scale(hangmanArm2, (self.armWidth, self.armHeight))
            self.window.blit(hangmanArm2, (70,-30))

        if self.lives <= 1:
            hangmanLeg1 = pygame.image.load('C:\\Users\\adeba\\OneDrive\\Images\\Hangman_Leg.png')
            hangmanLeg1 = pygame.transform.scale(hangmanLeg1, (self.legWidth, self.legHeight))
            self.window.blit(hangmanLeg1, (195,365))


        if self.lives <= 0:
            hangmanLeg2 = pygame.image.load('C:\\Users\\adeba\\OneDrive\\Images\\Hangman_Leg2.png')
            hangmanLeg2 = pygame.transform.scale(hangmanLeg2, (self.legWidth, self.legHeight))
            self.window.blit(hangmanLeg2, (150,365))


    def drawList(self, li, textColor, x, y):
        "".join(li)
        self.drawText("".join(li), textColor, x, y)

    def getTimeElapsed(self):
        if self.lives > 0 and missingCharacters != {}:
            return self.gameTimer.getTimeElasped()
        else:
            return 0

    # def resetTimer(self):
    #     self.startTIme = time.time()
        
        

    def update(self):
        self.deltaTime = 0.01 * self.clock.tick()
        self.textX  += 8 * self.deltaTime
        self.textY += 8 * self.deltaTime
        self.hangmanGame.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and pygame.key.name(event.key) not in missingCharacters.keys() and pygame.key.name(event.key) in alphabet and missingCharacters != {} and self.lives > 0:
                self.playGameSounds.lostLifeSound()
                self.lives -=1
                alphabet.remove(pygame.key.name(event.key))
                print(self.lives)
      


                

            elif event.type == pygame.KEYDOWN and pygame.key.name(event.key) in missingCharacters.keys() and pygame.key.name(event.key) in alphabet and missingCharacters != {} and self.lives > 0:
                
                for i in (missingCharacters[pygame.key.name(event.key)]):
                    self.playGameSounds.chalkDrawingSound()
                    wordToSolve[i] =  pygame.key.name(event.key)
                missingCharacters.pop( pygame.key.name(event.key))
              
                alphabet.remove(pygame.key.name(event.key))

        if self.lives == 0 or missingCharacters == {}:
            self.gameOver()
          
       


    def removeGuessedLetters(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and pygame.key.name(event.key) and pygame.key.name(event.key) in alphabet:
                alphabet[pygame.key.name(event.key)] 
                #alphabet.remove(pygame.key.name(event.key))
                print(alphabet)

    def gameOver(self):
        if not self.isGameOver:
            self.exitTimer.reset()
            self.isGameOver = True
            return
        if self.exitTimer.getTimeElasped() >= 2:
            pygame.quit()


        


    def hasQuit(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
        return False
                
 

game = Game(1920, 1080, 940, 1080, 800, 800, 1100, 500, 1000, 500, 1000, 1000, 6)
randNumber = 0
# lives = 7
secondsElasped = 0


wordToSolveAsList(wordToSolve, randNumList, randNumber)
replacingAndStoringLetters(numLettersToRemove)
displayWordToSolve(wordToSolve)

while not game.hasQuit():
    game.draw()
    game.update()