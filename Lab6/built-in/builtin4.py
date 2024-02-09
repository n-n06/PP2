import math, time
num = int(input())
sleept = int(input())
time.sleep(sleept/1000)
print(f"Square root of {num} after {sleept} miliseconds is {math.sqrt(num)}")