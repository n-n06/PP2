def gen_even(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

n = int(input())
print(*[x for x in gen_even(n)], sep=", ")