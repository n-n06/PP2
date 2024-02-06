import os
from colorama import Fore, Back, Style, init

init(autoreset=True)
path = input()
for dirpath, dirnames, filenames in os.walk(path, '.'):
    print(dirpath)
    for f in filenames:
        print(Fore.BLUE + f"{os.path.join(dirpath, f)}")
    print("\n")
