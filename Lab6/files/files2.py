import os
import sys

path1 = r"C:\Users\nursu\OneDrive\Desktop\pp2\Lab5\regex1.py"
path2 = r"C:\Users\nursu\OneDrive\Desktop\pp2\Lab5\regex12.py"
print(f"{path1} exists: {os.access(path1, os.F_OK)}")
print(f"{path2} exists: {os.access(path2, os.F_OK)}")

