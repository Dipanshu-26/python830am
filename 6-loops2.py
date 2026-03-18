#conditional statements
#one input and multiple outputs

#if , if-elif 
#marks A,B,C

# marks  = 81
# if marks > 45:
#   print("C")
# if marks > 60 :
#   print("B")
# if marks > 75:
#   print("A")

# marks  = 46
# if marks > 75:
#   print("A")
# elif marks > 60 :
#   print("B")
# elif marks > 45:
#   print("C")
# else : 
#   print("enter valid marks..")
  
#---------------------------------------------
#numbers 0-5 %5, 6 to 10 10%, above 10 20%

num=-11

if num>=0 and num<=5:
  print("5% discount")
elif  num>=6 and num<=10:
  print("10% discount")
elif num>10:  
  print("20% discount")
else:
  print("enter valid number...")

#---------------------------------------------
a=100
b=100

if a>b:
  print("a is greater")
else:
  print("b is greater")

#---------------------------------------------
a=1000
b=10000

if a>b:
  print("a is greater")
elif b>a:  
  print("b is greater")
else:
  print("both are equal")

#---------------------------------------------
a=300
b=300
c=40

if a>b and a>c:
  print("a is greater")
elif b>a and b>c:
  print("b is greater")
elif c>a and c>b:
  print("c is greater")
else:
  print("either all or any 2 are equal...")

#-------------------------------------------------

#loops

print(1)
print(2)
print(3)
print(4)
print(5)

#print 0 to 10

#for, while

#for
#range(startIndex, endIndex, stepSize )
# startIndex by default 0 
# endIndex : compulsary last value nit included
# stepSize : by default 1 

#print 0 to 10

for x in range(11):       #x=0,1,,2,3,4,5,6,7,8,9,10,11(false)
  print(x)                #x=0,1,,2,3,4,5,6,7,8,9,10

print("---------------")
#print 1 to 10
for x in range(1,11):
  print(x)

print("---------------")  
#print table of 2 
#               x<21
for x in range(2,21,2):    # x= 2, 4,6,8,10,12,14,18,20,22(false come out of loop)
  print(x)                # x= 2, 4,6,8,10,12,14,18,20

print("---------------")  
#print table of 5

for x in range(5, 51, 5):
  print(x)
  
print("---------------") 

for x in range(1,11):
  print(x*5)

#print 0 to 10 in reverse
for a in range(10,-1,-1):    #a=10
  print(a)

#print table of 2 inreverse

for x in range(20,1,-2):
  print(x)


#print table of 5 in reverse
for x in range(50,4,-5):
  print(x)
  
#while loop