#list slicing

# List Slicing -  allows you to extract parts of a list using : list[start : end : step]
# start → index where slice begins
# end   → index where slice stops (not included)
# step  → how many items to skip

# Basic slicing

#      0   1  2  3  4  5  6
num = [10,20,30,40,50,60,70]

print(num[:5])

#skip first element

print(num[1::])

#whole list
print(num[::])

#skip last and first
print(num[1:6:])

#      0   1  2  3  4  5  6
num = [10,20,30,40,50,60,70]

print(num[::2])    #[10, 30, 50, 70]


print(num[1::2])   #[20, 40, 60]

#reverse

print(num[::-1])

print(num[::-2])

#list comprihensition

# List Comprehensions - List Comprehension provides a short, fast, clean way to create lists.
# Syntax: [new_item  for item in iterable  if condition]
#[expression for item in iterable]
# Basic Example

nums = [1,2,3,4,5,6]

sq=[]
for x in nums:
    sq.append(x*x)

print(sq)

#--------------------------------
#[new_item  for item in iterable  if condition]
nums = [1,2,3,4,5,6]

sq_new = [x*x for x in nums]
print(sq_new)

#cube

cube =[x*x*x for x in nums]   #1,2,3....
print(cube)                   #1,8,27...

nums2 = [4,6,9,10,44,77,52,90,97]
#even

even=[]
for x in nums2:
    if x%2==0:
        even.append(x)

print(even)

#LC
#[new_item  for item in iterable  if condition]
even_new = [x for x in nums2 if x%2 == 0]
print(even_new)

#odd

odd = [x for x in nums2 if x%2 != 0]
print(odd)

#create list 1 to 10

numbers = [x for x in range(1,11)]
print(numbers)

#table of 2
tableTwo = [x for x in range(2,21,2)]
print(tableTwo)

names = ['dipanshu','tanish','neel','nitin']

upper_names = [x.upper() for x in names ]
print(upper_names)

#nested list

list1=[1,2,3]
list2=['a','b','c']

#[(1,a),(1,b),(1,c),(2,a)....]

pairs = [(x,y) for x in list1 for y in list2]

print(pairs)
