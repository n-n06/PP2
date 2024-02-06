from collections import defaultdict
def unique(li):
    dict1 = defaultdict(int)
    for i in range(len(li)):
        dict1[li[i]] += 1
        if dict1[li[i]] > 1:
            li[i] = None
    return [x for x in li if x != None]
    

