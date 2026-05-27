# instance method
# class method method
# static methods -  no interaction with object , writing function inside the class
# Static method - does not use self, does not use cls, behaves like normal utility function
# Static methods - can be called using both class and object because they do not depend on instance (self) or class (cls) data.

#program 1

import random
class StringUtils:
    @staticmethod
    def make_upper(str):
        return str.upper()
    
    @staticmethod
    def email_validater(email):
        return "@" in email and "minskole.in" in email

    @staticmethod
    def number_generator():
        return random.randint(1000,1999)
    
print(StringUtils.make_upper("dipanshu"))
print(StringUtils.email_validater("dipanshu@minskole.in"))
print(StringUtils.email_validater("dipanshu_minskole.in"))   
print(StringUtils.number_generator())

#----------------------------------------------------------------------------------

#program 2

class Employee:
    #class level
    country = "India"

    #constructor
    def __init__(self, name, eid, sal):
        self.name=name
        self.empId = eid
        self.salary = sal

    #instance method
    def displayName(self):
        return self.name

    @classmethod
    def changeCountry(cls,nv):
        cls.country = nv  

    @staticmethod
    def calculateBonus(sal):
        return sal * 0.10

    #instance method
    def displayFinalSalary(self):
        return Employee.calculateBonus(self.salary) + self.salary

print("-------------------------------------")

e1 = Employee("dipanshu chawde",1,10000)
e2 = Employee("aditya masalkar",2,30000)
e3 = Employee("rucha gaware",3,40000) 

print(e1.displayFinalSalary())
print(e2.displayFinalSalary())
print(e3.displayFinalSalary())

print(e1.country)
print(e2.country)
print(e3.country)

Employee.changeCountry("UK")
print(e1.country)
print(e2.country)
print(e3.country)

e1.country = "USA"

print(e1.country)
print(e2.country)
print(e3.country)

print(Employee.calculateBonus(12000))
print(e1.calculateBonus(12000))

print(Employee.calculateBonus(e1.salary))        #10000