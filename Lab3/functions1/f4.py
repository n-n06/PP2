def filter_prime(li):
    for i in range(len(li)):
        for j in range(2, li[i]):
            if li[i] % j == 0 and li[i] > j:
                li[i] = 0
    return [x for x in li if x != 0]

