import pygame
pygame.init()

loop = True
screen = pygame.display.set_mode((500,500))
screen.fill((255,255,255))
pygame.display.set_caption("test")

clock = pygame.time.Clock()

while True:
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEMOTION and event.buttons[0]:
            pygame.draw.circle(screen, (0,0,0), event.pos, 15)

    pygame.display.update()
    clock.tick(360)
