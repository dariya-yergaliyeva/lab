import math
#1
d=int(input("Input degree: "))
r=math.radians(d)
print("Output radian: ", r)

#2
height=int(input("Height: "))
base1=int(input("Base, first value: "))
base2=int(input("Base, second value: "))
t=0.5*height*(base1+base2)
print("Expected value: ", t)

#3
n=int(input("Input number of sides: "))
l=int(input("Input the length of a side: "))
s=(n*l**2)/(4*math.tan(math.pi/n))
print("The area of the polygon is: ", round(s))

#4
l=float(input("Length of base: "))
h=float(input("Height of base: "))
s1=h*l
print("Expected Output: ", s1)