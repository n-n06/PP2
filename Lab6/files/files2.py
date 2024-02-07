import os
import sys

path1 = input("Input a path: ")

print(f"{path1} exists: {os.access(path1, os.F_OK)}")
print(f"{path1} is readable: {os.access(path1, os.R_OK)}")
print(f"{path1} is writeable: {os.access(path1, os.W_OK)}")
print(f"{path1} is executable: {os.access(path1, os.X_OK)}")


