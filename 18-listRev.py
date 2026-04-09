#CRUD ==>create , retrive, upadate, delete

#append extend insert

listA=["dipanshu","tanish","nitin","neel"]
print(listA)

#append
listA.append("aditya")
print(listA)

listA.append("akay")
print(listA)

a=[1,2]
b=[3,4]
a.append(b)
print(a)      #[1, 2, [3, 4]]
print(b)

#a= [1, 2, [3, 4]]
#     0  1    2

print(a[2])

c="dipanshu"
a.append(c)
print(a)

#--------------------------------------------------------------
#insert will add element at given index

listB = ['a','b','c','d','e']   # length = 5   , last index =4  new index =5
#         0   1   2   3    4

listB.insert(2,111)
print(listB)

listB.insert(5, "dip")
print(listB)

#using insert method add element at last 

listB.insert(len(listB),"lastel")
print(listB)

#extend 
#add one list to another list
nm = ["d","p","n"]
nm.extend("anshu")
print(nm)

a=[1,2]
b=[3,4]
a.extend(b)
print(a)

#----------------------------------------------------------------------------------
#deleting element from list

#del listname[i], pop(i), pop, remove(element), clear

#del listname[i]

#         0        1       2        3       4        5
listA = ["pune","delhi","mumbai","nagpur","nashik","jaipur"]

print(listA)
del listA[3]
print(listA)

#pop()
#         0        1       2        3       4        5
listA = ["pune","delhi","mumbai","nagpur","nashik","jaipur"]

print(listA)
listA.pop()
listA.pop()
print(listA)

#pop(i)
#         0        1       2        3       4        5
listA = ["pune","delhi","mumbai","nagpur","nashik","jaipur"]
print(listA)
listA.pop(1)
print(listA)
listA.pop(1)
print(listA)

#remove(element)
#         0        1       2        3       4        5
listA = ["pune","delhi","mumbai","nagpur","nashik","jaipur"]
print(listA)
listA.remove("nashik")
print(listA)

#clear - delets all elements from list
#         0        1       2        3       4        5
listA = ["pune","delhi","mumbai","nagpur","nashik","jaipur"]
print(listA)
listA.clear()
print(listA)

# | Method              | What it does                 | Works by |
# | ------------------- | ---------------------------- | -------- |
# | `del listname[i]`   | Deletes element              | index    |
# | `pop(i)`            | Deletes + returns element    | index    |
# | `pop()`             | Deletes last element         | —        |
# | `remove(value)`     | Deletes first matching value | value    |
# | `clear()`           | Deletes all elements         | —        |












