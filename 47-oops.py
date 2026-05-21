#oops 

a=[1,2,3,4]
print(a)
print(type(a))

a="dipanshu"
print(a)
print(type(a))

# class ---->
# methods and properties 

# type 
# inrovert                   extrovert
# clam                       loud
# less outing                more outing
# less social                more social

#human 
# proerties  ==> name , age , weight, height 
# method ==> walk() ,talk()
# actions ==> returns 
# walk()==> health
# talk()==> communiaction

#vehicle 
#proerties ==> color, , type, logo,company
#method ==> start(),move(),stop()


#list   ===> class
# len, order, elemnts, size, mutable
# push(),pop(),shift(),unshift()

listA =[1,2,3,4,5]    # ===> object create with listA
print(len(listA))
listA.pop()
print(listA[0])

listB =[11,22,33,44]
listB.pop()
print(listB[0])

name = "dipanshu"   #===> object of class string 

#user defined datatype 
# class ==> properties and methods 
# creating object
# object ===> instance of class 

#program 1
class Person:
    # prperties 
    fname = None
    lname = None

    # method 
    def displayName(self):
        print(f"name = {self.fname} and surname = {self.lname}")

# self == adi
adi = Person()
print(adi.fname)
print(adi.lname)

adi.fname="Aditya"
adi.lname = "masalkar"

adi.displayName()
print(adi.fname)
print(adi.lname)

#-----------------------------------------------------------------
# self = dip
dip = Person()

dip.fname="dipanshu"
dip.lname="chawde"
dip.displayName()

print(dip.fname)
print(dip.lname)

#----------------------------------------------------------------
t = Person()
