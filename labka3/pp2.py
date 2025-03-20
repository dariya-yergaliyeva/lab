def qua(x):
    for i in range(0, x+1):
        yield i**2
x= int(input())
print(list(qua(x)))
def tw(a,b):
    for i in range(a,b+1):
        if i%2==0:
            yield i
a=int(input())
b=int(input())
print(list(tw(a,b)))