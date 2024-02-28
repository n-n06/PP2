import os
import sys
import colorama
colorama.init()
li = os.listdir(r"C:/Users/nursu/OneDrive/Desktop/songs")
for song in li:
    song = song.split(os.extsep)[0]
    print(colorama.Fore.CYAN, song)