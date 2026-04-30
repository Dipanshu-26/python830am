# lambda function

#addition 
def add(x,y):
    return x+y

e= add(3,5)
print(e)

#lambda --keyword 

addB = lambda x,y : x+y
e2 = addB(10,20)
print(e2)

#---------------------------
sqr = lambda x:x*x
print(sqr(4))

#--------------------------
cube = lambda x :x*x*x
print(cube(3))

#----------------------------------------------

# function a parameter and function as return 
addA = lambda x,y : x+y
print(addA)
print(addA(4,5))

# function a parameter
addA = lambda x,y : x+y

def addition(fn,x,y):
    e=fn(x,y)
    return e

q1 = addition(addA,11,22)    
print(q1)

addA = lambda x,y : x+y
subA = lambda x,y:x-y
mul = lambda x,y:x*y
div = lambda x,y:x/y
mod = lambda x,y:x%y

def calculator(fn,x,y):
    res = fn(x,y)
    return res

c1 = calculator(addA,20,5)
print(c1)

c2 = calculator(subA,20,5)
print(c2)

c3 = calculator(mul,20,5)
print(c3)

c4 = calculator(div,20,5)
print(c4)

c5 = calculator(mod,20,5)
print(c4)

#function as return type
def multiplication():
    return lambda x,y:x*y

q2 =multiplication()
print(q2)

res2 = q2(10,5)
print(res2)