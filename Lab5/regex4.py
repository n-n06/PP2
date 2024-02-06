import re

string = input("Input a string: ")

#an uppercase characte at the beginning followed by 0 or more lowercases
x = re.search(r"\A[A-Z][a-z]*", string)

if x == None:
    print("Not accepted")
else:
    print(f"Accepted at {x.span()} as {x.group()}")