import pygame
import datetime
import os


pygame.init()
loop = True
clock = pygame.time.Clock()
print(datetime.datetime.now().second)



screen = pygame.display.set_mode((700,525))
pygame.display.set_caption("Mickey Clock")


_image_library = {}
def get_image(path):
    global _image_library
    image = _image_library.get(path)
    if image == None:
        canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
        image = pygame.image.load(canonicalized_path)
        _image_library[path] = image
    return image
clock_image = get_image("mickeyclock.jpg")
clock_rect = clock_image.get_rect(center = (screen.get_rect().center))

minute_image = get_image("minutes.png")
minute_rect = minute_image.get_rect(center = (screen.get_rect().center[0] - 65, screen.get_rect().center[1] - 64))

seconds_image = get_image("seconds.png")
seconds_rect = seconds_image.get_rect(center = (screen.get_rect().center[0] + 65, screen.get_rect().center[1] - 64))

surf = screen.blit(clock_image, clock_rect)
# screen.blit(minute_image, minute_rect)
screen.blit(seconds_image, seconds_rect)


def rotate(surf, image, origin, pivot, angle):
    image_rect = image.get_rect(topleft = (origin[0] - pivot[0], origin[1]-pivot[1]))
    offset_center_to_pivot = pygame.math.Vector2(origin) - image_rect.center
    rotated_offset = offset_center_to_pivot.rotate(-angle)
    rotated_image_center = (origin[0] - rotated_offset.x, origin[1] - rotated_offset.y)
    rotated_image = pygame.transform.rotate(image, angle)
    rotated_image_rect = rotated_image.get_rect(center = rotated_image_center)
    surf.blit(rotated_image, rotated_image_rect)


ang = 6
while loop:
    ang += 6
    clock.tick(20)
    
    pressed = pygame.key.get_pressed()


    alt = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
    ctrl = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            loop = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and ctrl:
                loop = False
            if event.key == pygame.K_F4 and alt:
                loop = False
            if event.key == pygame.K_ESCAPE:
                loop = False
    pygame.display.flip()
    rotate(screen, seconds_image, pivot=(700/2,525/2), origin=(seconds_rect.center), angle=ang)
    screen.blit(seconds_image, seconds_rect)
    
    