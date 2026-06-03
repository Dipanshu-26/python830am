# Abstraction
# abstraction in python 
# instance method , static method , class method , abstractmethod
# abstract method will not have body 
# to abstract method ---> you have to inherit ABC class
# ❌ No, we cannot create an object of an abstract class in Python.

#Simple Definition : Abstraction means hiding implementation details and showing only important functionality to the user. 


from abc import ABC, abstractmethod

class WorldBank(ABC):
    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def loan(self):
        pass

class SBI(WorldBank):
    def save(self):
        print("SBI save")

    def loan(self):
        print("SBI loan")   

    def country(self):
        print("India")


#ab = WorldBank()

class PNB(WorldBank):
    def save(self):
        print("PNB save")

    def loan(self):
        print("PNB loan")   

    def country(self):
        print("India")


s= SBI()
s.loan()
s.save()
s.country()

#---------------------------------------------------------------------

#can abstract class have non abstracted method? -- yes

class WorldBank1(ABC):
    def countryHQ():
        print("USA")

    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def loan(self):
        pass

class SBI1(WorldBank):
    def save(self):
        print("SBI save")

    def loan(self):
        print("SBI loan")   

    def country(self):
        print("India")

s1= SBI1()
s1.loan()
s1.save()
s1.country()

WorldBank1.countryHQ()

#---------------------------------------------------------------------

#Can abstract class have constructor? --yes

class Employee(ABC):
    def __init__(self,name):
        self.name = name

    #normal method using self
    def company(self):
        print(self.name,"wprks at TCS")

    def Country():
        print("country is India")

    @abstractmethod
    def salary(self):
        pass

class Developer(Employee):
    def salary(self):
        print(self.name ," salary in 50000")     


d= Developer("dipanshu")   
d.company()   
d.salary()    

Employee.Country()




