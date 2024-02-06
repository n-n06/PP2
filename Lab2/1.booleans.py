print(10 > 9)
print(10 == 9)
print(10 < 9)

a = 200
b = 33

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

print(bool("Hello"))         #all true from here
print(bool(15))

x = "Hello"
y = 15

print(bool(x))                 
print(bool(y))

bool("abc")
bool(123)
bool(["apple", "cherry", "banana"]) #to here


bool(False)     #all false from here
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})        



class myclass():
    def __len__(self):
        return 0

myobj = myclass()
print(bool(myobj))      #to here


def myFunction() :
    return True

print(myFunction())


def myFunction() :
    return True

if myFunction():
    print("YES!")
else:
    print("NO!")


x = 200
print(isinstance(x, int), "\n")




'''Exercises'''

print(10>9)
print("Is correct?", (10>9) == True)

print(10 == 9)
print("Is correct?",(10 == 9) == False)

print(10 < 9)
print("Is correct?",(10 < 9) == False)

print(bool("abc"))
print("Is correct?",bool("abc") == True)

print(bool(0))
print("Is correct?", bool (0) == False)


