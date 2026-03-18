#conditional statements
#one input multiple outcome

#if , if-elif

#num 0 to 5 ==>5%,   6 to 10 ==>10%,    above 10 ===>20%

num=70
if(num>0 and num <=5):
  print("5% discount")

if(num > 6 and num <=10):
  print("10% discount")
  
if(num>10):
  print("20% discount")

#---------------------------------
print("---------------------")
num=-3
if(num>0 and num <=5):       #if(true)
  print("5% discount")

elif(num > 6 and num <=10):
  print("10% discount")
  
elif(num>10):
  print("20% discount")
else:
  print("enter valid number..")
  
#---------------------------------
print("---------------------")  

#marks >=90 A,   >=75   B,     >=65  C
marks =98

if marks >=90:
  print("A")
if marks>=75:
  print("B")
if marks >=65:
  print("C")
  
#---------------------------------
print("---------------------")  

#marks >=90 A,   >=75   B,     >=65  C
marks =60

if marks >=90:
  print("A")
elif marks>=75:
  print("B")
elif marks >=65:
  print("C")  
else:
  print("please try again...")
  
#---------------------------------
print("---------------------")    
  
#find greater number of 2
x=100
y=100

if x>y:
  print("x is greater")
if y>x:  
  print("y is greater")
else:
  print("both are equal")
print("---------------------")   
#find greater number of 3

a=200 
b=200 
c=100

if a>b and a>c:
  print("a is greater")
elif b>a and b>c:
  print("b is greater")
elif c>a and c>b:
  print("c is greater")
else:
  print("all or bigger 2 are equal")

#loops