thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")#if not in set - raises an error

print(thisset)

thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")#does NOt raise an error if an element is not in the set

print(thisset)


thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)

thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)

thisset = {"apple", "banana", "cherry"}

del thisset

try:
    print(thisset)
except:
    print("there is no set here")