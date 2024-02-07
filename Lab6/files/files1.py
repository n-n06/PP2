import os
from colorama import Fore, init

init(autoreset=True)
path = input("Input a path: ")
for dirpath, dirnames, filenames in os.walk(path, '.'):
    print(Fore.BLUE + str(dirpath))
    for f in filenames:
        print(os.path.join(dirpath, f))
    print("\n")
