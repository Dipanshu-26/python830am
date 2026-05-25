#program 1
class Person:
    fname = None
    lname = None

    def diasplyName(self):
        print(f"name = {self.fname} and surname = {self.lname}")

adi = Person()
print(adi.fname)
print(adi.lname) 
adi.diasplyName() 

adi.fname = "Aditya"
adi.lname = "masalker"
adi.diasplyName()    

print(adi.fname)
print(adi.lname)

dip = Person()

dip.fname="dipanshu"
dip.lname="chawde"
dip.diasplyName()

#-----------------------------------------------------------------------------------

#program 2 
#consrructor 
# a constructor is a special method in a class that is automatically called when a new object is created.
# Its main purpose is to initialize the object’s attributes (set initial values) when the object is instantiated. 
# __init__


class Person2:
    #constructor
    def __init__(self,fn,ln):
        self.fname = fn
        self.lname = ln

    def displayName(self):
        print(f"name = {self.fname} and surname = {self.lname}")    

# object
#self = adi2
adi2 = Person2("aditya2", "masalkar2")      

adi2.displayName()
print(adi2.fname)


dip2 = Person2("dipanshu2","chawde2")

dip2.displayName()
print(dip2.fname)

#--------------------------------------------------------------------------------------
#program 3 
#class level variable 

class Bank:
    #class level variable
    country = "India"

    def __init__(self, fn, accno, bal):
        self.fullName = fn
        self.accNo = accno
        self.bal = bal

    def deposit(self, amount):
        self.bal = self.bal + amount     
        return self.bal
    
    def withdraw(self, amount):
        if amount < self.bal :
            self.bal = self.bal - amount
            return self.bal
        else :
            return "Insufficient balance"
        

n = Bank("neel",123,10000)
newBal = n.deposit(2000)
print(newBal)

res = n.withdraw(5000)
print(res)

res2 = n.withdraw(8000)
print(res2)

