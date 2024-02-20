def squares(a, b):
    x = a
    while x <= b:
        yield x**2
        x += 1

a,b = tuple(map(int, input("Input two numbers: ").split()))
for i in squares(a,b):
    print(i)