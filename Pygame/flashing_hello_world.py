import sys
import pygame

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('Pygame/resources/shortbeep.mp3')

# Create the screen
screen = pygame.display.set_mode((800, 600))
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

HelloWorldColors = [BLACK, RED]

# Шрифт
font = pygame.font.Font(None, 32)

count = 0
while  True:
    count += 1
    screen.fill(WHITE)

    # Проверка событий выхода
    if event.type == pygame.QUIT:
        sys.exit()

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()

    if mouse_pos != None:
        screen.blit(pygame.image.load(
            'Pygame/resources/smiley.png'),
            (mouse_pos[0] - 16, mouse_pos[1] - 16))
    else:
        screen.blit(pygame.image.load(
            'Pygame/resources/smiley.png'),
            (screen.get_width() / 2 - 16,
            (screen.get_height() - text.get_height()) / 2 - 60))

    # Создание текстовой поверхности и чередование цветов
    text = font.render('Hello world!', True, HelloWorldColors[count % 2])
    pygame.time.wait(1000)

    # Создание черной прямоугольной рамки
    pygame.draw.rect(screen, BLACK,
                ((screen.get_width() - text.get_width()) / 2 - 10,
                (screen.get_height() - text.get_height()) / 2 - 10,
                text.get_width() + 20, text.get_height() + 20),1)


                 # Ожидание в 1 сек
    pygame.time.wait(1000)

    screen.blit(pygame.image.load('Pygame/resources/smiley.png'),
                (screen.get_width()/2-16,
                (screen.get_height() - text.get_height()) / 2 - 60))

    screen.blit(text, ((screen.get_width() - text.get_width()) / 2, (screen.get_height() - text.get_height()) / 2))            

    pygame.mixer_music.play()

    pygame.display.flip()


    
            