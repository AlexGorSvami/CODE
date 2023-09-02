import pygame
import sys

pygame.init()

#Создаю экран
screen = pygame.display.set_mode((800,600))
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#Шрифт
font = pygame.font.Font(None, 32)

while True:
    screen.fill(WHITE) #Заливка экрана

    #Проверка событий выхода
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    #Создание текстовой поверхности
    text = font.render('Hello world!', True, BLACK)

    #Помещаю текст в центр экрана
    screen.blit(text, ((screen.get_width() - text.get_width()) / 2, (screen.get_height() - text.get_height()) / 2))

    #Обновление экрана
    pygame.display.flip()