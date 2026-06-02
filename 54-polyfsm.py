#polymorphism

#  same class same method different signature - overlading 
#  different class same method same signature - overriding

#overrriding

# class Animal:
#     def sound(self):
#         print("Basic generic Sound..")

# class Dog(Animal):
#     #overriding
#     def sound(self):
#         print("Bow Bow")     

# class Cat(Animal):
#     #overriding
#     def sound(self):
#         print("mew mew")        

# class Rabbit(Animal):
#     pass         

# a=Animal()
# b=Dog()
# c=Cat()
# d=Rabbit()

# # a.sound()
# # b.sound()
# # c.sound()
# # d.sound()

# for obj in(a,b,c,d):
#     obj.sound()

#  same class same method different signature - overlading 
#  different class same method same signature - overriding

# program 3
# Duck typing  - polmorphism

# Duck typing means: “If it looks like a duck and behaves like a duck, then treat it like a duck.”

# In Python, it means:
#  - Python does not care about the object’s class
#  - It only cares whether the object has the required method

class Duck:
    def speak(self):
        return"Quack Quck"

class Human:
    def speak(self):
        return "Hi, Hello!!"      

class Cat:
    def speak(self):
        return "Mew Mwe"

def call_speak(obj):
    print(obj.speak())           

dk = Duck()
hm = Human()
ct = Cat()    

call_speak(dk)
call_speak(hm)
call_speak(ct)

#--------------------------------------------

class PDFFile:
    def Open(self):
        print("Opening PDF")

class WordFile:
    def Open(self):
        print("Opening Word File ")

class ImageFile:
    def Open(self):
        print("Opening Image File")        

def open_file(file):
    file.Open()

pdf = PDFFile()
wf = WordFile()
imgf = ImageFile()

open_file(pdf)
open_file(wf)
open_file(imgf)
#--------------------------------------------
print("--------------------------")
# operator overloading (built in operator)

print(10+10)                    #addition
print("dipa" + "nshu")         #concat

class BookA:
    def __init__(self,pgs):
        self.pages = pgs

class BookB:
    def __init__(self,pgs):
        self.pages = pgs    

b1 = BookA(200)
b2= BookB(300)     

print(b1.pages+b2.pages)

#print(b1+b2)
#how to add object===>tm