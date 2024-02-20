import re

string = input("Input a string: ")
print(" ".join(re.findall(r"\A[a-z][a-z]*|[A-Z][a-z]*", string)))k