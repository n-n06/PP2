import os

#just some colorful text
#yello - for folders, white - files
from colorama import Fore, init
init(autoreset=True)

num = int(input("What do you want to print out:\n1 - only directories\n2 - files an directories\n3 - only files\n"))
path = input("Input a path: ")
if num == 1:
    for t in os.walk(path, "."):
        print(t[0])

elif num == 2:
    for dirpath, dirnames, filenames in os.walk(path, '.'):
        print(Fore.YELLOW + str(dirpath))
        for f in filenames:
            print(f)
            print(os.path.join(dirpath, f))
        else:
            print("")
else:
    for t in os.walk(path, "."):
        for f in t[2]:
            print(f)
