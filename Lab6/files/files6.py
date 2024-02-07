#creates alphabet with 26 txt files named from A to Z
from string import ascii_uppercase
import os

#creating a new folder alphabet where we will store all of the files
new_path = "C:\\Users\\nursu\\OneDrive\\Desktop\\pp2\\Labs\\Lab6\\files\\alphabet"
os.makedirs(new_path)

#iterating over the uppercase alphabet
for letter in ascii_uppercase:
    f = open(f"{new_path}\\{letter}.txt", "w")
    f.write(f"This is {letter}'s txt file")
    f.close()
