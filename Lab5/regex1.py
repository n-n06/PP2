import re

string = input("Input a string: ")
x = re.search(r"ab*", string)
y = re.findall(r"ab*", string)


if x == None:
    print("Not found!")
else:
    print(f"Found at {x.span()} as {x.group()}")


