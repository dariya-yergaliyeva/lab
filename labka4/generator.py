#1
N=int(input("Input number: "))
for i in range(1, N+1):
    print(i**2)

#2
n=int(input("Input number: "))
evennum=[]
for i in range(0, n+1):
    if i%2==0:
        evennum.append(str(i))
print(", ".join(evennum))

#3
def func_gen(x):
    for i in range(0, x+1):
        if i%3==0 and i%4==0:
            yield i
x=int(input("Enter: "))
print(list(func_gen(x)))

#4
a=int(input("start: "))
b=int(input("stop: "))
for i in range(a,b+1):
    print( i**2)
#5
m=int(input("enteeeerr: "))
dec=[]
for i in range(m, 0, -1):
    dec.append(str(i))
print(", ".join(dec))