import re

string = input("Input a string: ")

restring = re.split("[A-Z]",string)
print(restring)