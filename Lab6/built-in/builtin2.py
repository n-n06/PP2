string = input()
print("Lower Case Letters: ", len([char for char in string if char.islower()]))
print("Upper Case Letters: ", len([char for char in string if char.isupper()]))