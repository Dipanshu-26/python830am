#basic datatypes, operators ,conditional statements,loops 

#list 
x=10
print(x)
y=20
z=30
#          0  1  2   3  4
numbers = [10,20,30,40,50]                  #length=5
#          0     1        2          3
city = ["pune","delhi","banglore","kolkota"]    #length = 4
#           0        1       2  3   5         5
info = ["dipanshu","chawde",23,42,9922447802,True]   #length=6

print(numbers)
print(city)
print(info)

print(type(numbers))
print(type(info))

print(info[0])
print(city[2])
print(numbers[3])

print(len(numbers))
print(len(city))
print(len(info))


#          0  1  2 3  4   5 6  7
numbers = [99,67,4,10,20,33,47,5]    

print(len(numbers))
print(max(numbers))
print(min(numbers))

fruits = ["mango","grapes","banana","papaya"]
print(fruits[1])

#find perticular element present in list

print("banana" in fruits)
print("bananas" in fruits)
print("Banana" in fruits)

#loops
#          0     1        2          3        4      5
city = ["pune","delhi","banglore","kolkota","goa","nagpur"]    #length = 6 

for x in range(6):
  #print(x)            #x=0, x=1,x=2.........5,6(end)
  print(city[x])     #city[0],city[1].......city[5]

print("-----------------------")
#                   6   ==> 5 end
for x in range(len(city)):
  print(city[x])

print("-----------------------")
for x in range(len(fruits)):
  print(fruits[x])

print(len(fruits))