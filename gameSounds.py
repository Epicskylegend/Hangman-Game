import pygame

class Sounds:

    def __init__(self):
        pygame.mixer.init()
        self.correctLetter = pygame.mixer.Sound('C:\\Users\\adeba\\OneDrive\\Hangman\\Sounds\\ChalkDrawing.mp3')
        self.incorrectLetter = pygame.mixer.Sound('C:\\Users\\adeba\\OneDrive\\Hangman\\Sounds\\ChalkFalling.mp3')
   

    def chalkDrawingSound(self):
        return pygame.mixer.Sound.play(self.correctLetter)
    

    def lostLifeSound(self):
        return pygame.mixer.Sound.play(self.incorrectLetter)
