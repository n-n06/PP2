from itertools import permutations

def all_perm(s):
    for x in permutations(s):
        print(''.join(x))
    
