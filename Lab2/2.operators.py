
'''Python divides the operators in the following groups:

Arithmetic operators
Assignment operators
Comparison operators
Logical operators
Identity operators
Membership operators
Bitwise operators'''




print(10 + 5)
print(10 - 5)
print(10 * 5)
print(10 / 5)
print(10 ** 5)
print(14 % 5)
print(14 // 5)

x = 5
x += 3
x -= 4
x *= 20
x /= 4
x %= 100
x //= 5
print(x, "\n")

y = 2049
print(y)
y &= 3
print(y)
y |= 4
print(y)
y ^= 17
print(y)
y >>=2
print(y)
y <<=3
print(y, end = "\n")

print(10 == 10)
print(10 > 9)
print(10 < 9)
print(10 >= 10)
print(8 <= 9)
print(0 != 1)
print(True and False)
print(True or False)
print(not(True or False), "\n")




li = [2,3,4]
li2 = [4,2,3]

print(li is li2)
print(5 not in li, "\n")


print((6 + 3) - (6 + 3))

print(100 + 5 * 3)

print(5 + 4 - 7 + 3, "\n")

'''Exercises'''

print(10 * 5)
print(10 / 2)

fruits = ["apple", "banana"]
if "apple" in fruits:
    print("Yes, apple is a fruit!")

if 5 != 10:
    print("5 and 10 is not equal")

if 5 == 10 or 4 == 4:
    print("At least one of the statements is true")