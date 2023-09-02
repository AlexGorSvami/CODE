import pygame
import sys

#Инициализировать  игру
pygame.init()

#Create  the screen
gamewindow = pygame.display.set_mode((800,600))

White =  (255, 255, 255)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        gamewindow.fill(White)
        pygame.display.flip()