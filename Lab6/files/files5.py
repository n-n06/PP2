#uses text5
f = open("text5.txt", "w")
li = input("Input a list of values separated by commas: ").split(", ")
f.write(str(li))
f.close()