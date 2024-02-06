import re

string = input("Input a string: ")

x = re.search("([a-z]_)*[a-z]", string)

if x == None:
    print("Not Found")
else:
    print(f"Found at {x.span()} as {x.group()}")