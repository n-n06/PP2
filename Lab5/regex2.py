import re

string = input("Input a string: ")

x = re.search(r"ab{2,3}[^b]+", string)
if x == None:
    print("Not Found")
else:
    print(f"Found at {x.span()} as {x.group()}")