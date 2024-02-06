import re

string = input("Input a string: ")

string2 = re.sub(r"[\s,\.]", string=string, repl=":")

print(string2)

