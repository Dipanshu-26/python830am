#basic data types , operators,functions and its types

#python

print("dipanshu")
print(10)
print("dip@123")

a = 10
print(a)
print(type(a))

a="dip"
print(a)
print(type(a))

a=-10
print(a)
print(type(a))

a=10.5
print(a)
print(type(a))

a=-10.5
print(a)
print(type(a))

a=True
print(a)
print(type(a))

a=False
print(a)
print(type(a))

#true=200
# a=true 
# print(a)
# print(type(a))

#dynamically typed language

#arithmatic operators 

print(10+20)
print(10-20)
print(10*20)
print(10/20)
print(10%20)

# 200 2, 500 12

#functions : reusable block of code 

# function calc(){
#   ....
#   ....
#   ....
# }

#function without parameter and without return type
#function defination
def calculator():
  print(200+2)
  print(200-2)
  print(200*2)
  print(200/2)
  print(200%2)
  

#call 
calculator()
calculator()
calculator()  
  
#function with parameter and without return type  

def calc1(x,y):       #x , y parameters 
  print(x+y)
  print(x-y)
  print(x*y)
  print(x/y)
  print(x%y)

#call 
print("-------------")
calc1(500,5)        #500 5 arguments
print("-------------")
calc1(400,12)

print("-------------")
#function with parameter and with return type  
#average of 3 numbers

def average(a,b,c):
  avg = (a+b+c)/3 
  return avg

#call 
#              a  b  c
res = average(10,20,30)
print(res)

res = average(23,45,67)
print(res)
print("-------------")
#comparision operators ==,!=,<,<=,>,<=
#entuty ===>entity ====> True,False
print(3 == 3)
print(3!=3)

print(3 > 2)
print(3 >= 3)

print(3 < 2)
print(3 <= 3)
print("-------------")
#logical operators
# and , or , not 

# and ==> if any input is false output is false ... true only when all inputs are true

# i/p     i/p    ==>   o/p
# T       T            T 
# T       F            F
# F       T            F
# F       F            F 

print(3 == 3 and 3 != 4)
#       T     and   T ==>T
print( 3 == 3 and 3 >= 5)
print(3 >= 5 and 3 == 3)
print(3>5 and 4<2)

print("-------------")
# or==> if any input is true output is true ... false only when all inputs are false

# i/p     i/p    ==>   o/p
# T       T            T 
# T       F           T
# F       T            T
# F       F            T

print(3 == 3 or 3 != 4)
#       T     or  T ==>T
print( 3 == 3 or 3 >= 5)
print(3 >= 5 or 3 == 3)
print(3>5 and 4<2)
print("-------------")
#not 
# true ==>false
# false==>true
print(not(3==3))
#    not (t) ==> f
print(not(3> 7))

print(not(3==3 and 3>9))
print(not(3==3 or 3>9))

# conditional operators