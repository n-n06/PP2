def tree(n):
    for i in range(1, n + 1):
        print(" "*(n - i), end = "")
        for j in range(1 + (2 * (i - 1))):
            print("*", end = "")
        print(" "*(n - i))

n = int(input())
tree(n)
