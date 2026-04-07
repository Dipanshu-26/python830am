#python 

print("hello")
print("dipanshu")
print(10)
print(10+10)
print("10+10")

a=10
print(a)
print(type(a))

a=-10
print(a)
print(type(a))


a=10.5
print(a)
print(type(a))

a=-10.6
print(a)
print(type(a))


a="dipanshu"
print(a)
print(type(a))

a='dip@123'
print(a)
print(type(a))


a='@#$'
print(a)
print(type(a))

a="1234"
print(a)
print(type(a))

a=True
print(a)
print(type(a))

a=False
print(a)
print(type(a))

true = 100
a=true
print(a)
print(type(a))

#python dynamically typed language

#arithmatic operator
print(10+5)
print(10-5)
print(10*5)
print(10/5)
print(10%5)

#10, 5    200 20  500 5 ===> 100(5*100)
print("-----------------------------")
#functions : reusable block of code

#function without parameter and without return type
#defination
def calculator():
    print(200+20)
    print(200-20)
    print(200*20)
    print(200/20)
    print(200%20)


#call
calculator()
calculator()
calculator()

print("-----------------------------")
#function with parameter and without return type
def calc1(x,y):           #x, y are parameters  
    print(x+y)
    print(x-y)
    print(x*y)
    print(x/y)
    print(x%y)

#call
calc1(500,5)              #500 , 5 arguments
calc1(123,3)

print("-----------------------------")
#function with parameter and with return type

#average of 3 numbers
def average(a,b,c):
    res = (a+b+c)/3
    return res 

avg = average(10,20,30)
print(avg)

print("-----------------------------")
#loops in python 
#for , while

#for 
#range(startIndex, endIndex, stepSize)
# startIndex : default 0 
# endIndex  : must (end index value in not included)
# stepSize : default +1 

#print 0 to 10

for x in range(11):     #x=0,1 ,2 ,3....10  ,11       (x <endIndex(11))
    print(x)










