#operator Overloading

print(10+10)
print("dipa" + "nshu")

class BookOne:
    def __init__(self,pgs):
        self.pages = pgs

    def __add__(self,other):
        return self.pages + other.pages
    
class BookTwo:
    def __init__(self,pgs):
        self.pages = pgs    

a=BookOne(500)
b=BookTwo(1000)

print(a+b)
print(a.pages+b.pages)

#---------------------------------------------------------

class BookA:
    def __init__(self,pgs):
        self.pages = pgs

    def __gt__(self,other):
        return self.pages > other.pages
    
class BookB:
    def __init__(self,pgs):
        self.pages = pgs    

a=BookA(5000)
b=BookB(1000)

print(a>b)
#print(b>a) #error