import re

string = input("Input a string: ")

print("_".join(re.findall(r"\A[a-z][a-z]*|[A-Z][a-z]*", string)).lower())