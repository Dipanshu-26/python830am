# functions in python

def calaculator(x,y):
    print(x+y)
    print(x-y)
    print(x*y)
    print(x/y)
    print(x%y)

calaculator(100,200)    

# =====================================================
# Function with Different Data Types as Parameters
# =====================================================

print("--------------------------------------------")
# 1. Integer as parameter and Integer as return type
def average(a,b,c):
    avg = (a+b+c)/3
    return avg

res1 = average(10,20,30)
print(res1)
print("--------------------------------------------")

# -----------------------------------------------------
# 2. Float as parameter and Float as return type
def sub(x,y):
    return x-y

res2 = sub(20.5,15.7)
print(res2)
print("--------------------------------------------")

# -----------------------------------------------------
# 3. Boolean return type example

def canDrive(age,haveVechile):
    if age >=18 and haveVechile:
        return True
    else:
        return False

res3 =canDrive(34,False)
print(res3)
print("--------------------------------------------")

# -----------------------------------------------------
# 4. String as parameter and String as return type

def greet(name):
    return "Hello "+ name +" ..."

res4 = greet("dipanshu")
print(res4)
print("--------------------------------------------")

# -----------------------------------------------------
# 5. List as parameter and List as return type

city = ["pune","mumbai","nagpur"]

def addCity(cty,ctyname):
    cty.append(ctyname)
    return cty 

res4 = addCity(city,"nashik")
print(res4)
print("--------------------------------------------")

# -----------------------------------------------------
# 6. Dictionary as parameter and Dictionary as return type

info = {
    "name" : "dipanshu",
    "lname" : "chawde"
}

def addLocation(dict1):
    dict1["location"] ="pune"
    return dict1

res6=addLocation(info)
print(res6)
print("--------------------------------------------")

# -----------------------------------------------------
# 7. Tuple as parameter and Tuple as return type

numbers=(10,20,30,40)

def addToTuple(tupA):
    listA=list(tupA)
    listA.append(50)
    tupA=tuple(listA)
    return tupA

res7 = addToTuple(numbers)
print(res7)
print("--------------------------------------------")

# -----------------------------------------------------
# 8. Set as parameter and Set as return type

setA = {11,22,33,44}

def addToSet(setB):
    setB.add(55)
    return setB

res8=addToSet(setA)
print(res8)
print("--------------------------------------------")

# -----------------------------------------------------
# 9. Remove Duplicates from List using Function

numbers = [29,11,34,11,67,89,34,89,67,90,63,56,52]

def removeDuplicates(lst):
    uniqueList = list(set(lst))
    return uniqueList

res9=removeDuplicates(numbers)
print(res9)

# write a function to remove duplicates from list without using set


