import f1,f2,f3,f4,f5
from f6 import rev
from f7 import has_33
from f8 import spy_game
from f9 import volume
from f10 import unique
from f11 import is_palindrome
from f12 import histogram
from f13 import guess_game

print("100 grams in ounces: ",f1.to_ounces(100))
print(f2.to_celciuim(270))
print(f3.solve(30,24))

print(f4.filter_prime([11,9,19,5,7,8,10]))
print(f5.all_perm("Eve"))
print(rev("history"))
print(has_33([3,4,3,5,6,8]))
print(spy_game([4,0,9,4,0,7]))
print(volume(5))
print(unique([1,1,2,3]))
print(is_palindrome("tenet"))
histogram([3,6,8,2,4,7])
guess_game()