def down(n):
    x = n
    while x >= 0:
        yield x
        x -= 1

n = int(input())
for i in down(n):
    print(i)