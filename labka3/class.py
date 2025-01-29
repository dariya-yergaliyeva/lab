import math
class baseString():
    def __init__(self):
        self.string=""
    def getString(self):
        self.string=input("Input something: ")
    def printString(self):
        print(self.string.upper())
s=baseString()
s.getString()
s.printString()
#2
class Shape():
    def __init__(self, a=0, b=0):
        self.lenght=a
        self.weight=b
    def area(self):
        print(self.lenght*self.weight)
class Square():
    def __init__(self, a):
        self.length=a
    def area(self):
        print(self.length**2)
shape=Shape()
shape.area()

sq=Square(4)
sq.area()
#3
class Rectangle():
    def __init__(self, length, width):
        self.length=length
        self.width=width
    def area(self):
        print(self.length*self.width)
rec=Rectangle(4, 6)
rec.area()
#4
class Points():
    def __init__(self, x, y):
        self.x=x
        self.y=y
    def show(self):
        print(self.x, self.y)
    def move(self, movex, movey):
        self.x=movex
        self.y=movey
    def dist(self, other):
        print(math.sqrt((other.x-self.x)**2+(other.y-self.y)**2))
p1=Points(4, 6)
p2=Points(7, 9)
p1.show()
p1.move(5, 9)
p1.show()
p1.dist(p2)
#5
class Account():
    def __init__(self, owner, balance):
        self.owner=owner
        self.balance=balance
    def deposit(self, cash):
        self.balance+=cash
        print("Your balance is: ", self.balance)
    def withdraw(self, consuption):
        if self.balance>=consuption:
            self.balance-=consuption
            print("Your balance is: ", self.balance)
        else:
            print("Not enough funds")
acc=Account("Anel Yeraliyeva", 1000)
acc.deposit(300)
acc.withdraw(800)
acc.withdraw(600)
#6
def is_prime(n):
    if n<2:
        return False
    for i in range(2, n):
        if n%i==0:
            return False
    return True
num=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
new=list(filter(lambda m: is_prime(m), num))
print(new)

