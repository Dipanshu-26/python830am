#packing , unpacking , rest spread

#1. packing
numbers = 100,200,300

print(numbers)
print(type(numbers))

#2. unpacking

#a, b, c = 100,200,300
a,b,c = numbers
print(a)
print(b)
print(c)

numbers = 11, 22, 33, 44, 55,66,77
a, b , *c=numbers
print(a)
print(b)
print(c)

list1 = [10,20,30,40,50,60]
x,*y = list1
print(x)
print(y)


# 3. *args
def add_numbers(*numbers):
    print(f"numbers received = {numbers}" )

add_numbers(10,20,30,40,50)    

# 4. **kwargs

def student_details(**details):
    print(f"student details = {details}")

student_details(name = "rahul", course = "python", batch = "morning")  

# 4. spread 

list1 = [10,20,30]
list2 = [*list1, 40, 30]

print(list2)