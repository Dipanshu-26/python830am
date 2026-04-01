#list 
a=10
b=20
c=30

#           0  1  2  3  4
numbers = [10,20,30,40,50,444]     #length = 5  last index = 4
print(numbers)
print(numbers[0])
print(numbers[2])
print(numbers[4])

print(type(numbers))

#len, min, max

print(len(numbers))
print(min(numbers))
print(max(numbers))

cities = ["pune","banglore","kolkota","delhi"]

print(len(cities))

# #to find element present or not
print("banglore" in cities)

print("nagpur" in cities)

print("Banglore" in cities)

listA = [11,22,33,44,55,66,77,88]

#loops
#for, while
# for 
# range(starIndex, endIndex, stepSize)
# starIndex ==> 0 
# endIndex ==> must  not included
# stepSize ==> +1

#        0  1   2  3  4 5   6  7
listA = [11,22,33,44,55,66,77,88]

for x in range(8):          # range(0,8(x<8),1) ==> x=0,1,2.......7,8
  #print(x)                 #x=0,1,2.......7
  print(listA[x])           #listA[0],listA[1],listA[2]......listA[7]

listA = [11,22,33,44,55,66,77,88,3,7,9,11,44,34]
print(len(listA))
for x in range(len(listA)):
  print(listA[x])

#----------------------------------------------------
cities = ["pune","banglore","kolkota","delhi"]
for x in range(len(cities)):
  print(cities[x])
#----------------------------------------------------

for cy in cities:      #cy="pune","banglore","kolkota","delhi"
  print(cy)

listA = [11,22,33,44,55,66,77,88,3,7,9,11,44,34]
for nm in listA:
  print(nm)
print("--------------------------------")
#----------------------------------------------------
listA = [11,22,33,44,55,66,77,88,3,7,9,11,44,34]

#find even 
for x in listA:
  if x%2==0:
    print(x)
print("--------------------------------")
#find  odd
for x in listA:
  if x%2!=0:
    print(x)

print("--------------------------------")
for x in range(len(listA)):
  if listA[x]%2==0:
    print(listA[x])
print("--------------------------------")
#find  odd
for x in range(len(listA)):
  if listA[x]%2!=0:
    print(listA[x])

#  list ==array
#         0  1  2  3
listA = [10,20,30,40]    #4
print(listA)

print(listA[0])
print(listA[1])
print(listA[2])
print(listA[3])

#while ==>list
# inilization
# while(condition )
# inc/dec

print("----------------------------")
#         0  1  2  3  4  5  6  7
listA = [10,20,30,40,50,60,70,80]  #length=8
i=0     # inilization
while i<8 :      #condition  #i=0,1,2.....7
  #print(i)        #0 ,1
  print(listA[i])   #listA[0],listA[1]........listA[7]
  i=i+1           #1,2.......7,8

print(len(listA))


print("----------------------------")


x=0
while x < len(listA):     #while x<8  
  print(listA[x])
  x=x+1 

















