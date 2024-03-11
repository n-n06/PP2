import pygame
pygame.init()

screen = pygame.display.set_mode((600,400))

loop = True

while loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
    screen.fill((0,0,0))
    pygame.display.update()
