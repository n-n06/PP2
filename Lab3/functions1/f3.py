def solve(num_heads, num_legs):
    num_rabbits = (num_legs - (num_heads * (2)))/2
    num_chickens = num_heads - num_rabbits
    return int(num_rabbits), int(num_chickens)

