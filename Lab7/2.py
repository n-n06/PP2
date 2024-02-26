import pygame
import os
pygame.init()


_image_library = {}
def get_image(path):
        global _image_library
        image = _image_library.get(path)
        if image == None:
                canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
                image = pygame.image.load(canonicalized_path)
                _image_library[path] = image
        return image



screen = pygame.display.set_mode((400,300))
image = pygame.image.load("ball.png")

clock = pygame.time.Clock()

loop = True


pygame.mixer.music.load('te.mp3')
pygame.mixer.music.play(0)


while loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False


    

    screen.fill((255,255,255))

    screen.blit(get_image('ball.png'), (20,20))
    
    pygame.display.flip()
    clock.tick(60)
