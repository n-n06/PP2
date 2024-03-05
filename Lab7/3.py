import pygame
from random import randint
pygame.init()

screen = pygame.display.set_mode((400,300))
clock = pygame.time.Clock()
loop = True

li = ["circle", "square", "polygon", "outline", "line"]

def choose_random():
    figure = li[randint(0,4)]
    if figure == "circle":
        pygame.draw.circle(screen, (0,0,0), (100, 100), 50)
    if figure == "square":
        x = 100
        pygame.draw.rect(screen, (0,0,0), pygame.Rect(100, 100, 100, x))
    if figure == "polygon":
        pygame.draw.polygon(screen, (0,0,0), [(10,50),(10,30),(10,10),(40,30),(40,40)])
    if figure == "outline":
        pygame.draw.rect(screen, (0,0,255), pygame.Rect(10, 10, 100, 100), 10)
    else:
        pygame.draw.line(screen, (0,0,0), (0,0), (400,300), 10)


while loop:
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
    screen.fill((255,255,255))
    choose_random()

    
    pygame.display.flip()
    clock.tick(5)