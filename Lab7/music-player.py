'''
Music player that plays all of the 
'''
import os
import pygame
import tkinter
import re

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


volume = 1

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
queue = []
index = 0
audio_channel = mixer.Channel(1)

def folder_selection():
    root = tkinter.Tk()
    root.withdraw()
    selection = filedialog.askdirectory(initialdir = "C:", title = "Select a folder")
    for dirpath, dirname, filename in os.walk(selection, "."):
        for f in filename:
            queue.append(os.path.join(dirpath,f))

    return list(filter(re.compile(r".*\.(mp3|ogg|wav)$").match, queue))

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
            if event.key == pygame.K_UP:
                volume += 0.05
                if volume <= 1.0:
                    audio_channel.set_volume(volume)
                else:
                    volume = audio_channel.get_volume()
            if event.key == pygame.K_DOWN:
                volume -= 0.05
                if volume >= 0.0:
                    audio_channel.set_volume(volume)
                else:
                    volume = audio_channel.get_volume()


        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            #mouse position
            pos = pygame.mouse.get_pos()

            #getting audio files
            if folder_button.collidepoint(pos):
                queue = folder_selection()
                            
            #play button
            if play_button.collidepoint(pos) and not started:
                print(queue)
                try:
                    audio_channel.play(mixer.Sound(queue[index]))
                    started = True
                    play = get_image("pause1.png")
                except:
                    print("Nothing to play yet")
            elif play_button.collidepoint(pos) and paused and started:
                paused = False
                audio_channel.unpause()
                play = get_image("pause1.png")
            elif play_button.collidepoint(pos) and not paused and started:
                paused = True
                audio_channel.pause()
                play = get_image("play1.png")
            
            #back button
            elif back_button.collidepoint(pos):
                if shift:
                    index -= 1
                if started and index >= 0:
                    play = get_image("pause1.png")
                    audio_channel.play(mixer.Sound(queue[index]))
                else: 
                    play = get_image("play1.png")
                    started = False
                    audio_channel.stop()
                    index = 0
                
            #forward button
            elif forward_button.collidepoint(pos):
                index += 1
                if started and index < len(queue):
                    play = get_image("pause1.png")
                    audio_channel.play(mixer.Sound(queue[index]))
                else:
                    play = get_image("play1.png")
                    started = False
                    audio_channel.stop()
                    index = 0
 
    screen.fill((50,50,60))
    #button images

    play_button = screen.blit(play, play_rect)
    forward_button = screen.blit(forward, forward_rect)
    back_button = screen.blit(back, back_rect)
    folder_button = screen.blit(folder, folder_rect)

    #

    pygame.display.flip()
    clock.tick(90)


