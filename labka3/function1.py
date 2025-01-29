#1
def ouns(grams):
    ones=grams*0.0354
    print(ones)
ouns(35)
#2
def centigrade(faringate):
    c=(5/9)*(faringate-32)
    print(c)
centigrade(273)
#3
def count(h, l):
    rabbits=(l-2*h)//2
    chickens=h-rabbits
    return rabbits, chickens
print(count(35, 94))
#4
def is_prime(x):
    if x<2:
        return False
    for i in range(2, int(x)):
        if x%i==0:
            return False
    return True
def filter_prime(num):
    return [x for x in num if is_prime(x)]
print(filter_prime([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]))    
#5
def new_strings(s):
    if len(s)==1:
        return [s]
    new=[]
    for i in range(len(s)):
        for x in new_strings(s[:i]+s[i+1:]):
            new.append(s[i]+x)
    return new
print(new_strings("hello"))
#6
def inverse(sentence):
    return " ".join(sentence.split()[::-1])  

print(inverse("I love cat"))
#7
def three(n):
    for i in range(len(n)-1):
        if n[i]==3 and n[i+1]==3:
            return True
print(three([1, 3, 3, 4, 5]))
#8
def agint(n):
    for i in range(len(n)-1):
        if n[i]==0 and n[i+1]==0 and n[i+2]==7:
            return True
print(agint([1, 2, 3, 0, 0, 7, 8]))
#9
import math
def volume(r):
    v=(4/3)*math.pi*r**3
    print(v)
volume(5)
#10
def unique(ls):
    res=[]
    for i in ls:
        if i not in res:
            res.append(i)
    return res
print(unique([1, 1, 2, 2, 3, 4, 4]))
#11
def polindrom(sts):
    rev=sts[::-1]
    if sts==rev:
        return True
print(polindrom("level"))
#12
def histograma(n):
    for i in n:
        print('*'*i)
histograma([8, 4,5, 6])
#13
import random
def guess_random_number():
    num=random.randint(1, 21)  
    print("Hello! What is your name?") 
    name=input()
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")    
    print("Take a guess")
    cout=0
    while True:
        n=int(input())
        if n<num:
            print("Your guess is too low.")
            print("Take a guess")
            cout+=1
        elif n>num:
            print("Your guess is too high.")
            print("Take a guess")
            cout+=1
        elif n==num:
            print(f"Good job, {name}! You guessed my number in {cout} guesses!")
            break
guess_random_number()