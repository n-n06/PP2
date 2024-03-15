'''
Music player that plays all of the 
'''
import os
import pygame
import tkinter
import re
import json

from tkinter import filedialog
from pygame import mixer

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
os.chdir("sprites")
play = get_image("play1.png")
forward = get_image("forward1.png")
back = get_image("back1.png")
folder = get_image("folder.png")
clear = get_image("clear.png")

play_rect = play.get_rect(center = (screen.get_rect().center[0], 350))
forward_rect = forward.get_rect(center = (screen.get_rect().center[0]*3/2, 350))
back_rect = back.get_rect(center = (screen.get_rect().center[0]/2, 350))
folder_rect = folder.get_rect(center = (40,40))
clear_rect = clear.get_rect(center = (40,100))
info_rect1 = pygame.Rect(200,50,400,40)
info_rect2 = pygame.Rect(200,150,400,40)


'''
File handling
'''
index = 0
queue = []
if os.access("songlist.json", os.F_OK):
    with open("songlist.json", "r") as sl:
        queue = json.load(sl)



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
                if started:
                    started = False
                    play = get_image("play1.png")
                    audio_channel.stop()
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
            #pause and unpause logic
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
            #clear button
            elif clear_button.collidepoint(pos):
                started = False
                audio_channel.stop()
                play = get_image("play1.png")
                if shift:
                    queue = []
                    os.remove("songlist.json")
                else:
                    with open("songlist.json", "r") as sl:
                        queue = json.load(sl)

 
    screen.fill((50,50,60))
    #button images

    play_button = screen.blit(play, play_rect)
    forward_button = screen.blit(forward, forward_rect)
    back_button = screen.blit(back, back_rect)
    folder_button = screen.blit(folder, folder_rect)
    clear_button = screen.blit(clear, clear_rect)

    font = pygame.font.Font(None, 36)
    text1 = font.render("Now Playing:", True, (255,255,255))
    text_rect1 = text1.get_rect(center=info_rect1.center)
    pygame.draw.rect(screen, (40,40,50), info_rect1)

    if started:
        screen.blit(text1, text_rect1)

        text2 = font.render(os.path.basename(queue[index]), True, (255,255,255))
        text_rect2 = text2.get_rect(center = info_rect2.center)
        pygame.draw.rect(screen, (40,40,50), info_rect2)
        screen.blit(text2, text_rect2)

    pygame.display.flip()
    clock.tick(90)

#upon closing the main window, the queue is written in a json file
with open("songlist.json", "w") as sl:
    json.dump(queue, sl)

