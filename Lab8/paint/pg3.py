import pygame



rect_select_img = pygame.image.load("rect_select.png")
circle_select_img = pygame.image.load("circle_select.png")
palette_select_img = pygame.image.load("palette.png")
eraser_select_img = pygame.image.load("eraser.png")

rect_select_button = rect_select_img.get_rect(center = (40,40))
circle_select_button = circle_select_img.get_rect(center = (120,40))
palette_select_button = palette_select_img.get_rect(center = (200,40))
eraser_select_button = eraser_select_img.get_rect(center = (280,40))


def main():
    pygame.init()
    screen = pygame.display.set_mode((640,480))
    clock = pygame.time.Clock()
    
    radius = 15
    x = 0
    y = 0
    points = []
    mode = "blue"

    while True:

        pressed = pygame.key.get_pressed()

        alt = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl:
                    return
                if event.key == pygame.K_F4 and alt:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
                
                if event.key == pygame.K_r:
                    mode = "red"
                elif event.key == pygame.K_g:
                    mode = "green"
                elif event.key == pygame.K_b:
                    mode = "blue"

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    radius = min(200, radius + 1)
                elif event.button == 3:
                    radius = max(1, radius - 1)
            
            if event.type == pygame.MOUSEMOTION:
                position = event.pos
                points = points + [position]
                points = points[-256:]

            

            screen.fill((0,0,0))

            #drawing
            i = 0
            while i < len(points) - 1:
                drawLine(screen, i, points[i], points[i + 1], radius, mode)
                i += 1
            
            pygame.draw.rect(screen, (112,128,144), (0,0,320,80))
            screen.blit(rect_select_img, rect_select_button)
            screen.blit(circle_select_img, circle_select_button)
            screen.blit(palette_select_img, palette_select_button)
            screen.blit(eraser_select_img, eraser_select_button)
            
            pygame.display.flip()
            clock.tick(144)
            
def drawLine(screen, index, start, end, width, color_mode):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))

    if color_mode == "blue":
        color = (c1, c1, c2)
    elif color_mode == "red":
        color = (c2, c1, c1)
    elif color_mode == "green":
        color = (c1, c2, c1)

    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))

    for i in range(iterations):            
        progress = 1.0 * i /iterations
        aprogress = 1 - progress

        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x,y), width)

main()



