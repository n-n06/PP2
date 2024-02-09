from random import getrandbits, randint
bool_tuple = tuple(bool(getrandbits(1)) for i in range(randint(1,10)))
print(bool_tuple)
print(all(bool_tuple))