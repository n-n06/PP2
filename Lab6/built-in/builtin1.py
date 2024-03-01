li = input().split()
print(eval("*".join(li)))

'''
alternative:
'''
# from functools import reduce
# li = list(map(int, input().split()))
# print(reduce(lambda x,y:x*y, li))
