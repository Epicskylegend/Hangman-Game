import pygame
from pygame.locals import *

poleWidth = 500
poleHeight = 500



pole =  pygame.display.set_mode((poleWidth, poleHeight))

poleImg = pygame.image.load('C:\\Users\\adeba\OneDrive\\Pictures\\Pole.png')
poleImg = pygame.transform.scale(poleImg, (poleWidth, poleHeight))

pole.blit(poleImg, (0,0))
pygame.display.flip()

def displayPole():
    pole.blit(poleImg, (0,0))

