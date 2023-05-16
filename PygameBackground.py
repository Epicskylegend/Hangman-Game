import pygame
from pygame.locals import *

pygame.init()


backgroundWidth = 1920
backgroundHeight = 1080

text_font = pygame.font.SysFont(None, 100, bold = True)



window = pygame.display.set_mode((backgroundWidth, backgroundHeight))

backgroundImg = pygame.image.load('C:\\Users\\adeba\OneDrive\\Images\\chalkboard.jpg')
pygame.display.set_caption('Hangman Game')
backgroundImg = pygame.transform.scale(backgroundImg,(backgroundWidth, backgroundHeight))


window.blit(backgroundImg, (0,0))   

pygame.display.flip()


def drawText(text, font, textColor, x, y):
    welcome = font.render(text, True, textColor)
    window.blit(welcome, (x, y))