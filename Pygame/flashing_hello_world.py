import sys
import pygame

screen = pygame.display.set_mode((800,600))
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('/home/alex/CODE/Pygame/resources/shortbeep.mp3')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
HelloWorldColors = [BLACK, RED]
font = pygame.font.Font(None,32)
gamewindow = pygame.display.set_mode((800,600))

count = 0
while True:
    count = count + 1
    screen.fill(WHITE) # заполяем фон

    # Проверка событий выхода
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # Создаю текстовую поверхность
    text = font.render('Hello world!', True, HelloWorldColors[count % 2])

    pygame.time.delay(1000)

    # Создаю объёмный текст с чёрной прямоугольной рамкой
    pygame.draw.rect(screen, BLACK, 
    ((screen.get_width() - text.get_width()) / 2 - 10,
    (screen.get_height() - text.get_height()) / 2 - 10,
    text.get_width + 20,
    text.get_height + 20), 1)

    # Рисую смайлик над рамкой 32х32

    screen.blit(pygame.image.load('/home/alex/CODE/Pygame/resources/smiley.png'),
    ((screen.get_width()/2 -16,
      (screen.get_height() - text.get_height()) / 2 - 60)))

    # Перенос текстовой поверхности на экран
    screen.blit(text, ((screen.get_width() - text.get_width()) / 2,
     (screen.get_height() - text.get_height()) / 2))

     # подавать звуковой сигнал
    pygame.mixer_music.play()

    # Обновление экрана
    pygame.display.flip()


    
            