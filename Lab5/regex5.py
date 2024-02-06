import re

string = input("Input a string: ")

x = re.search(r"a.*b\Z", string)

if x == None:
    print("Not Accepted")
else:
    print(f"Accepted at {x.span()} as {x.group()}")