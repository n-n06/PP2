import os

path = input()

if os.access(path, os.F_OK):
    print(f"File is readeable: {os.access(path, os.R_OK)}\nFile is writeable: {os.access(path, os.W_OK)}")
    os.remove(path)
    print("The file is Deleted")