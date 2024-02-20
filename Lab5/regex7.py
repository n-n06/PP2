import re

string = input("Input a string: ")

restring = re.split("_+", string)
print(restring)
restring = restring[0].lower() + "".join(map(lambda x: x.title(), restring[1:]))
print(restring)

#to convert everythin to CamelCase:
# restring = re.split("_+", string)
# restring =  "".join(map(lambda x: x.title(), restring))