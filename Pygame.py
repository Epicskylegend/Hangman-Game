import pygame
from pygame.locals import *

pygame.init()

width = 1920
height = 1080

window = pygame.display.set_mode((width, height))

backgroundImg = pygame.image.load('C:\\Users\\adeba\OneDrive\\Images\\Nature.jpg').convert()
pygame.display.set_caption('Hangman Game')
backgroundImg = pygame.transform.scale(backgroundImg,(width, height))

window.blit(backgroundImg, (0,0))   


pygame.display.flip()
status = True



def displayBackground():
   
    window.blit(backgroundImg, (0,0))   

    #for i in pygame.event.get():
        #if i.type == pygame.QUIT:
    
