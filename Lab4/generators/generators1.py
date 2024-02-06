def square_gen(n):
    x = 1
    while x**2 < n:
        yield x**2
        x += 1

for i in square_gen(20):
    print(i)