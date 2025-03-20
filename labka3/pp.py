def is_prime1(x):
    if x<2:
        return False
    i=2
    while i<x:
        if x%i==0:
            return False
        else:
            i+=1
    return True
def filter_prime1(num):
    return [x for x in num if is_prime1(x)]
print(filter_prime1([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]))
class Shape():  
    def __init__(self):
        pass
    def vol(self, volume):
        self.volume=volume
        print(self.volume**3)
class Qudrate(Shape):
    def __init__(self):
        pass
s=Shape()
s.vol(7)
q=Qudrate()
q.vol(3)