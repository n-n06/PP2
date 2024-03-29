import pygame
import datetime
import os

pygame.init()
loop = True
clock = pygame.time.Clock()

screen = pygame.display.set_mode((700,525))
pygame.display.set_caption("Mickey Clock")

'''
Image Handling
'''
_image_library = {}
def get_image(path):
    global _image_library
    image = _image_library.get(path)
    if image == None:
        canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
        image = pygame.image.load(canonicalized_path)
        _image_library[path] = image
    return image


clock_image = get_image("mickeyclock.png")
clock_rect = clock_image.get_rect(center = (screen.get_rect().center))

minute_image = get_image("rightarm.png")
minute_rect = minute_image.get_rect(center = (screen.get_rect().center[0], screen.get_rect().center[1]))

seconds_image = get_image("leftarm.png")
seconds_rect = seconds_image.get_rect(center = (screen.get_rect().center[0], screen.get_rect().center[1]))


button_rect = pygame.Rect(30,20,200,50)
string = "View time!"
not_pressed = True

seconds_calibration = 5
minutes_calibration = 45

'''
Rotation function
'''

def blitRotate(surface, image, image_rect, pos, angle):

    # offset from pivot to center
    offset_center_to_pivot = pygame.math.Vector2(pos) - image_rect.center
    
    # roatated offset from pivot to center
    rotated_offset = offset_center_to_pivot.rotate(-angle)

    # roatetd image center
    rotated_image_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)

    # get a rotated image
    rotated_image = pygame.transform.rotate(image, angle)
    rotated_image_rect = rotated_image.get_rect(center = rotated_image_center)

    # rotate and blit the image
    surface.blit(rotated_image, rotated_image_rect)


'''
Main Loop
'''

while loop:
    #setting the time in seconds and minutes
    seconds = datetime.datetime.now().second
    minutes = datetime.datetime.now().minute

    seconds_angle = -(seconds*6+seconds_calibration)
    minutes_angle = -(minutes*6+minutes_calibration)+seconds_angle/60
    
    
    #checking if alt and ctrl were pressed to avoid boilerplacte code
    pressed = pygame.key.get_pressed()
    alt = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
    ctrl = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]

    for event in pygame.event.get():
        #quit logic
        if event.type == pygame.QUIT:
            loop = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and ctrl:
                loop = False
            if event.key == pygame.K_F4 and alt:
                loop = False
            if event.key == pygame.K_ESCAPE:
                loop = False
        #checking if the mouse was pressed
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            #checking if the view time button was pressed
            if button_rect.collidepoint(mouse_pos) and not_pressed:
                not_pressed = False
            elif button_rect.collidepoint(mouse_pos) and not not_pressed:
                string = "View time!"
                not_pressed = True
        

    if not not_pressed:
        string = f"{datetime.datetime.now().minute}:{datetime.datetime.now().second}"

    #placing the clock and its hands on the main surface
    screen.blit(clock_image, clock_rect)
    blitRotate(screen, seconds_image, seconds_rect, (700/2,525/2),seconds_angle)
    blitRotate(screen, minute_image, minute_rect, (700/2,525/2),minutes_angle)
    
    #the text time
    font = pygame.font.Font(None, 36)
    text = font.render(string, True, (0,20,30))
    text_rect = text.get_rect(center=button_rect.center)
    pygame.draw.rect(screen, (245,245,220), button_rect)
    screen.blit(text, text_rect)

    pygame.display.update()
    clock.tick(60)

    
    
