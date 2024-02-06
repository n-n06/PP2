thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

thislist = ["apple", "banana", "cherry"]
popped = thislist.pop()
print(thislist)
print(popped)

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist[1:]
print(thislist)



thislist = ["apple", "banana", "cherry"]
del thislist
try:
    print(thislist)
except:
    print("the list was deleted, it is no longer defined")

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)