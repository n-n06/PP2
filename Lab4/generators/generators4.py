def squares(a, b):
    x = a
    while x <= b:
        yield x**2
        x += 1

a,b = tuple(map(int, input().split()))
for i in squares(a,b):
    print(i)