#class variables and instance variables 

class Students:
    #class variable
    country = "India"      #"UK"   #"japan"

    #instance variables
    def __init__(self,fn,ln,age):
        self.fname = fn
        self.lname = ln
        self.age = age

    @classmethod 
    def changeCountry(cls,nc):
        cls.country = nc

    #instance method 
    def displayName(self):
        print(self.fname + self.lname)

    #instance method to update age
    def updateAge(self,na):
        self.age = self.age+na 

n= Students("neel","chawde",8)     
n.displayName()
print(n.country)
n.updateAge(2)
print(n.age)  

n.changeCountry("UK")
print(n.country)


print("--------------")
n2= Students("rajasi","gaware",11) 
n2.displayName()
print(n2.country)
n2.updateAge(2)
print(n2.age)  

Students.changeCountry("japan")
print(n.country)
print(n2.country)

n.country = "Bharat"

n2.country = "USA"

print(n.country)
print(n2.country)

n3= Students("abc","xyz",11) 
print(n3.country)

#-----------------------------------------

# country == class variable 
# to change class variable ==>cls 

# Students.changeCountry("japan")
# n.changeCountry("UK")
# -- both works same -- class lavel variable value change for all objects

# #-----------------------------------------

# n.country = "Bharat"
# n2.country = "USA" 

# now neel and rajasi having their on value for country
# {
#     "fname" : "neel",
#     "lname" : "chawde",
#     "age" : 10
#     "country" : "bharat"
# }