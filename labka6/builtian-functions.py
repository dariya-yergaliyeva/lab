import time
import math
from functools import reduce
#1
numbers = [2, 3, 4, 5]
q=reduce(lambda x, y: x * y, numbers)
print(q)
#2
ex2="My Friends and I will create our oen Startup"
lc=sum(1 for i in ex2 if i.islower())
uc=len(list(filter(str.isupper, ex2)))
print(uc)
print(lc)
#3
ex3="level"
if ex3==ex3[::-1]:
    print("polindrom")
else:
    print("no")
#ex4
inp=int(input())
inp2=int(input())
time.sleep(inp2/1000)
outp=inp**0.5
print(f"squere root of {inp} after {inp2} miliseconds is {outp}")
#ex5
ex5=(1, 1, 1)
ex51=(1,0,0)
print(all(ex5))
print(all(ex51))
