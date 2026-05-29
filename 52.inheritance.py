#single inheritance

# class Student:
#     def __init__(self, fn, ln):
#         self.fname = fn
#         self.lname = ln

#     def displayName(self):
#         print(self.fname + self.lname)  

# class Teacher(Student):
#     def __init__(self,fn,ln,sal):
#         super().__init__(fn,ln)
#         self.salary = sal

#     def displaySalary(self):
#         print(self.salary)


# s2 = Student("ms","dhoni")
# s2.displayName()
# print(s2.fname)

# t2 = Teacher("rahul","dravid",200000)
# t2.displayName()
# t2.displaySalary()
# print(t2.salary)
# print(t2.fname)

#-------------------------------------------------------------------------------

#multilevel inheritance 
#grandFather ==> father ==> daughter

# class GrandFather:
#     def __init__(self, fn,ln):
#         self.fname = fn
#         self.lname=ln

#     def displayGName(self):
#         print(f"Grandfather name = {self.fname} {self.lname}")    

# class Father(GrandFather):
#     def __init__(self,fn,ln,ffn):
#         super().__init__(fn,ln)
#         self.ffname = ffn

#     def displayFName(self):
#         print(f"Father name = {self.ffname} {self.lname}")    

# class Daughter(Father):
#     def __init__(self, fn,ln,ffn,dfn):
#         super().__init__(fn,ln,ffn)
#         self.dfname=dfn

#     def displayDName(self):
#         print(f"Daughter name = {self.dfname} {self.lname}")           

# d = Daughter("gapalrao","masalkar","niranjan","dipanshu")

# d.displayDName()
# d.displayFName()
# d.displayGName()

# f=Father("gopalrao","masalkar","niranjan")
# f.displayGName()
# f.displayFName()
# print(f.ffname)
# print(f.fname)
# g=GrandFather("gopalrao","masalkar") 

#--------------------------------------------------------

#herarchical inheritance 
# mother => Daughter
# mother=> son

# class Mother:
#     def __init__(self, fn,ln):
#         self.fname = fn
#         self.lname = ln

#     def displayMName(self):
#         print(f"Mother name = {self.fname} {self.lname}")           

# class Daughter(Mother):
#     def __init__(self, fn,ln,dfn):
#         super().__init__(fn,ln)
#         self.dfname = dfn
        
#     def displayDName(self):
#         print(f"Daughter name = {self.dfname} {self.lname}")  


# class Son(Mother):
#     def __init__(self, fn,ln,sfn):
#         super().__init__(fn,ln)
#         self.sfname = sfn
        
#     def displaySName(self):
#         print(f"Son name = {self.sfname} {self.lname}")  

# s= Son("dipti","masaksar","aditya")
# s.displayMName()
# s.displaySName()
# print(s.fname)
# print(s.sfname)

# d= Daughter("dipti","masaksar","rucha")
# d.displayMName()
# d.displayDName()
# print(d.fname)
# print(d.dfname)

#----------------------------------------------------------------------------------
# multiple inheritance
#son ==> mother, father


# class Mother:
#     def __init__(self, fn,ln):
#         self.mfname = fn
#         self.lname = ln

#     def displayMName(self):
#         print(f"Mother name = {self.mfname} {self.lname}")     

# class Father:
#     def __init__(self,fn,ln):
#         self.ffname = fn
#         self.lname = ln

#     def displayFName(self):
#         print(f"Father name = {self.ffname} {self.lname}")   

# class Son(Father,Mother):
#     def __init__(self, fn,ln,mfn,sfn):
#         Father.__init__(fn,ln)
#         Mother.__init__(mfn,ln)
#         self.sfname = sfn
        
#     def displaySName(self):
#         print(f"Son name = {self.sfname} {self.lname}")  


# s=Son("niranjan","masalkar","dipti","aditya")
# s.displaySName()
# s.displayFName()
# #s.displayMName()



# #solution is change side or function name of mother

# Why Mother method is not called?
# Because Python follows MRO (Method Resolution Order) and checks parent classes from left to right.
# Since Father is written first







