'''
1. file browsing
2. play, stop, next, previous

'''
import os
import pygame
import tkinter
from tkinter import filedialog
from pygame import mixer
from time import time
pygame.init()
mixer.init()


'''
Main window
'''
screen = pygame.display.set_mode((800,450))
pygame.display.set_caption("Music Player")
clock = pygame.time.Clock()
loop = True
paused = False
started = False

#volume settings
volume = 100





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
play = get_image("play1.png")
forward = get_image("forward1.png")
back = get_image("back1.png")
folder = get_image("folder.png")

play_rect = play.get_rect(center = (screen.get_rect().center[0], 350))
forward_rect = forward.get_rect(center = (screen.get_rect().center[0]*3/2, 350))
back_rect = back.get_rect(center = (screen.get_rect().center[0]/2, 350))
folder_rect = folder.get_rect(center = (40,40))


'''
File handling
'''
queue = [mixer.Sound("audio.mp3"), mixer.Sound("android.mp3")]
index = 0
audio_channel = mixer.Channel(1)

'''
The Main Loop
'''
while loop:

    pressed = pygame.key.get_pressed()

    #frequent keys
    alt = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
    ctrl = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
    shift = pressed[pygame.K_LSHIFT] or pressed[pygame.K_RSHIFT]

    for event in pygame.event.get():
        #quitting logic
        if event.type == pygame.QUIT:
            loop = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and ctrl:
                loop = False
            if event.key == pygame.K_F4 and alt:
                loop = False
            if event.key == pygame.K_ESCAPE:
                loop = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            #play and pause buttons
            pos = pygame.mouse.get_pos()
            if play_button.collidepoint(pos) and not started:
                started = True
                audio_channel.play(queue[index])
                play = get_image("pause1.png")
            elif play_button.collidepoint(pos) and paused:
                paused = False
                audio_channel.unpause()
                play = get_image("pause1.png")
            elif play_button.collidepoint(pos) and not paused:
                paused = True
                audio_channel.pause()
                play = get_image("play1.png")
            
            #back button
            elif back_button.collidepoint(pos):
                if shift:
                    index -= 1
                if started and index >= 0:
                    play = get_image("pause1.png")
                    audio_channel.play(queue[index])
                else: 
                    play = get_image("play1.png")
                    started = False
                    audio_channel.stop()
                    index = 0
                
            #forward button
            elif forward_button.collidepoint(pos):
                index += 1
                if started:
                    try:
                        play = get_image("pause1.png")
                        audio_channel.play(queue[index])
                    except:
                        play = get_image("play1.png")
                        started = False
                        audio_channel.stop()
                        index = 0
            
            elif folder_button.collidepoint(pos):
                root = tkinter.Tk()
                root.withdraw()
                selection = filedialog.askdirectory(initialdir = "C:", title = "Select a folder")
                print(os.listdir(selection))
                
                
                
                
    screen.fill((50,50,60))
    #button images
    volume = pygame.draw.rect(screen, (0,))
    play_button = screen.blit(play, play_rect)
    forward_button = screen.blit(forward, forward_rect)
    back_button = screen.blit(back, back_rect)
    folder_button = screen.blit(folder, folder_rect)

    #

    pygame.display.flip()
    clock.tick(90)


# dirname = filedialog.askdirectory()
# print(dirname)
'''
1. folder browsing (tkinter, write files in a txt and read them)
2. file representation and append system
3. creating of playlists (maybe)
'''