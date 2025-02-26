import time
import math
#1
numbers = [2, 3, 4, 5]
q=list(map(lambda x: pow(x, 2), numbers))
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
outp=math.sqrt(inp)
print(f"squere root of {inp} after {inp2} miliseconds is {outp}")
#ex5
ex5=(1, 1, 1)
ex51=(1,0,0)
print(all(ex5))
print(all(ex51))
