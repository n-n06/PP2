thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thisdict = {"watermelon" : 5, "melon" : 6}
thisset = {"pear", "strawberry", "blackberry", "blueberry"}
thislist.extend(thistuple)
thislist.extend(thisdict)
thislist.extend(thisset)
print(thislist)

