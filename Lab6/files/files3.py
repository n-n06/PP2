import os

path1 = input("Input a path: ")

if os.access(path1, os.F_OK):
    print(f"The path {path1} exists!")
    if os.path.isfile(path1):
        print(f"The directory portion of the path: {os.path.dirname(path1)}")
        print(f"The filename portion of the path: {os.path.basename(path1)}")
    else:
        print(f"The directory of the path: {path1}")
else:
    print(f"The path {path1} does not exist")
