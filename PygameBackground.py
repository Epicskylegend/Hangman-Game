import pygame
from pygame.locals import *

pygame.init()

backgroundWidth = 1920
backgroundHeight = 1080


window = pygame.display.set_mode((backgroundWidth, backgroundHeight))

backgroundImg = pygame.image.load('C:\\Users\\adeba\OneDrive\\Images\\Nature.jpg').convert()
pygame.display.set_caption('Hangman Game')
backgroundImg = pygame.transform.scale(backgroundImg,(backgroundWidth, backgroundHeight))


window.blit(backgroundImg, (0,0))   

pygame.display.flip()
status = True


def displayBackground():  
    window.blit(backgroundImg, (0,0))   

   
