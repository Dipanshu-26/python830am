a=20
print(a)

b='dipanshu'
print(b)

c=10+10
print(c)

c="10+10"
print(c)

# +,-,*,/,%

print(300+3)
print(300-3)
print(300*3)
print(300/3)
print(300%3)

print("---------------------")
#500,5

#functions : reusable block of code

#function without parameter and without return type

# function calculator(){         #fuction in js
#   ....
#   ....
#   ...
# }

#function defination
def calculator():
  print(300+3)
  print(300-3)
  print(300*3)
  print(300/3)
  print(300%3)
  
print("---------------------")
#function call
calculator()
calculator()
calculator()

print("---------------------")
#function with parameter and with out return type

def calc2(x,y):        # x, y parameter
  print(x+y)
  print(x-y)
  print(x*y)
  print(x/y)
  print(x%y)
  
#call 
#      x  y
calc2(500,5)        #500,5 arguments
calc2(200,12)
print("---------------------")
#function with parameter and with return type

#average of 3 numbers

def average(a,b,c):
  avg = (a+b+c)/3 
  return avg
  print("i m after return")   #this will never ge executed
  
#call 
res = average(100,200,300)
print(res)


res2 = average(55,66,77)
print(res2)

print("---------------------")
#deposit withdraw, balance

balance = 10000

def deposit(amt):
  return balance + amt

def withdraw(amt):
  return balance - amt

print(balance)           #10000
balance = withdraw(5000)  
print(balance)           #5000

balance = deposit(7000)
print(balance)          #12000


balance = deposit(10000)
print(balance) 

balance = withdraw(2000)  
print(balance)           #5000

 
# function without parameter without return type
# function with parameter without return type
# function with parameter with return type

# comparision operators