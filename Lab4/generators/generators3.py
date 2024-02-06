def gen(n):
    x = 0
    while x <= n:
        if x % 12 == 0:
            yield x
        x += 1

n = int(input())
for i in gen(n):
    print(i)