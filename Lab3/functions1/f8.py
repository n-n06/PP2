def spy_game(nums):
    a = False
    b = False
    for i in nums:
        if i == 0 and not a:
            a = True
            c = False
            continue
        if i == 0:
            b = True
        if i == 7 and a and b:
            c = True
    return a and b and c
