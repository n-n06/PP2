import pygame
import os
from random import choice
pygame.init()

'''
Image Section
'''
#a utility function to get an image from different path formats
_image_library = {}
def get_image(path):
    global _image_library
    image = _image_library.get(path)
    if image == None:
        canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
        image = pygame.image.load(canonicalized_path)
        _image_library[path] = image
    return image


'''
Screen Section
'''
#setting a display and an image
screen = pygame.display.set_mode((400,300))
# image = pygame.image.load("ball.png")
clock = pygame.time.Clock()
loop = True

'''
Sound Section
'''

_sound_library = {}
def play_sound(path):
  global _sound_library
  sound = _sound_library.get(path)
  if sound == None:
    canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
    sound = pygame.mixer.Sound(canonicalized_path)
    _sound_library[path] = sound
  sound.play()

_songs = ["inferno.mp3", "hype.mp3", "ano bando.ogg", "etea.mp3"]
_currently_playing = None
SONG_END = pygame.USEREVENT + 1
# pygame.mixer.music.set_endevent(SONG_END)
# pygame.mixer.music.load('inferno.mp3')
# pygame.mixer.music.queue("ano bando.ogg")
# pygame.mixer.music.play(0)  # use -1 to play inf many time

def play_different_songs():
    global _songs, _currently_playing
    next_song = choice(_songs)
    while next_song == _currently_playing:
        next_song = choice(_songs)
    _currently_playing = next_song
    pygame.mixer.music.load(next_song)
    pygame.mixer.music.play()


kick = "kick.wav"
snare = "snare.wav"
hat = "hat.wav"
crash = "crash.wav"
play_different_songs()


'''
Main Loop
'''

while loop:
    pause = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_x:
            play_sound(kick)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_z:
            play_sound(snare)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_n:
            play_sound(kick)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_m:
            play_sound(snare)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            play_sound(hat)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
            play_sound(crash)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_k:
            play_sound(hat)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_l:
            play_sound(crash)
        if event.type == SONG_END:
            print("the song ended!")

   
    # pressed = pygame.key.get_pressed()
    # if pressed[pygame.K_SPACE]:
    #     pause = True
    #     pygame.mixer.music.pause()
    # if pressed[pygame.K_SPACE] and pause:
    #     pygame.mixer.music.unpause() 

    

    screen.fill((255,255,255))

    screen.blit(get_image('ball.png'), (20,20))
    
    pygame.display.flip()
    clock.tick(144)
