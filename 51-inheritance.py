#inheritance 

#incorrect way to write a code 
# class Student:
#     def __init__(self, fn, ln):
#         self.fname = fn
#         self.lname = ln

#     def displayName(self):
#         print(self.fname + self.lname)    


# class Teacher:
#     salary = 10000
#     def __init__(self, fn, ln):
#         self.fname = fn
#         self.lname = ln

#     def displayName(self):
#         print(self.fname + self.lname)  

    #   def displaySalary(self):
    #       print(self.salary)
#-------------------------------------------------------------------
#inheritance 
#parent class , child class 
#clild class can access properties and method of parent class 

#student --> parent
#Teacher --> child class

#parent having constructor and child having no constructor
# class Student:
#     def __init__(self, fn, ln):
#         self.fname = fn
#         self.lname = ln

#     def displayName(self):
#         print(self.fname + self.lname)   


# class Teacher(Student):
#     salary =10000

#     def displaySalary(self):
#         print(self.salary)

# s1 = Student("tanish","chawde")
# s1.displayName()
# print(s1.fname)

# t1 = Teacher("dipanshu","chawde")
# t1.displayName()
# t1.displaySalary()
# print(t1.fname)
# print(t1.salary)

#--------------------------------------------------------------------------

#parent and child class both having constructor

class Student:
    def __init__(self, fn, ln):
        self.fname = fn
        self.lname = ln

    def displayName(self):
        print(self.fname + self.lname)  

class Teacher(Student):
    def __init__(self,fn,ln,sal):
        super().__init__(fn,ln)
        self.salary = sal

    def displaySalary(self):
        print(self.salary)


s2 = Student("ms","dhoni")
s2.displayName()
print(s2.fname)

t2 = Teacher("rahul","dravid",200000)
t2.displayName()
t2.displaySalary()
print(t2.salary)
print(t2.fname)


