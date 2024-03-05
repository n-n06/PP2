import pygame
pygame.init()

screen = pygame.display.set_mode((700,400))
pygame.display.set_caption("Balling")
loop = True
x = 350
y = 200
clock = pygame.time.Clock()

while loop:
    pressed = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
    if pressed[pygame.K_UP] and y > 25: y-= 10
    if pressed[pygame.K_DOWN] and y < 375: y += 10
    if pressed[pygame.K_LEFT] and x > 25: x -= 10
    if pressed[pygame.K_RIGHT] and x < 675: x+= 10

    screen.fill((0,0,0))
    pygame.draw.circle(screen, (0,255,0), (x,y), 25)

    pygame.display.flip()
    clock.tick(144)
