#addition 
def addn(x,y):
    return x+y

print(addn(10,20))

#lambda 

addA = lambda x,y : x+y
print(addA(11,22))

sq = lambda x : x*x
q1 = sq(6)
print(q1)

cube = lambda a : a*a*a
print(cube(3))

#---------------------------------------------------
#function as parameter 

addA = lambda x,y : x+y
print(addA(11,22))

def addition(fn, x,y):
    r1 = fn(x,y)
    return r1

q2 = addition(addA, 33,44)
print(q2)   


add = lambda x,y : x+y 
sub = lambda x,y : x-y 
mul = lambda x,y : x*y 
div= lambda x, y : x/y 
mod =lambda x,y : x%y

def calculator(fn, x,y):
    res = fn(x,y)
    return res

print(f"addition = {calculator(add, 20,5)}")
print(f"substraction = {calculator(sub, 20,5)}")
print(f"multiplication = {calculator(mul, 20,5)}")
print(f"division = {calculator(div, 20,5)}")
print(f"modulus = {calculator(mod, 20,5)}")

print("-------------------------------")
#function as return type 

def multiplication():
    return lambda x,y : x*y

def division():
    return lambda x,y : x/y

def modulus():
    return lambda x,y : x%y

def addition():
    return lambda x,y : x+y

def substraction():
    return lambda x,y : x-y

# r1 = multiplication()
# print(r1(2,3))

add = addition()
mul = multiplication()
div=division()
mod = modulus()
sun = substraction()

print(f"addition = {add(50,5)}")
print(f"substraction = {sub(50,5)}")
print(f"multiplication = {mul(50,5)}")
print(f"division = {div(50,5)}")
print(f"modulus = {mod(50,5)}")