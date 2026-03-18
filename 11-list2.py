#CRUD ==> create retrive update delete

#append , insert, extend

#append add element at last

listA=["dipanshu","nitin","tanish","neel"]
print(listA)

listA.append("aditya")
print(listA)

listA.append("akay")
print(listA)


a=[1,2]
b=[3,4]
print(a)
print(b)
a.append(b)

print(a)
print(b)

c="dipanshu"
a.append(c)
print(a)


#insert add element at given index
#        0          1        2      3
listB=["grapes","papaya","mango","banana"]    #last index =3 total length= 4
listB.insert(0,"watermelon")
print(listB)

listB.insert(2,"cherry")
print(listB)

listB.insert(len(listB),"muskmelon")
print(listB)


#extend 
# extend - one list to another list
# extend() in Python is a list method used to add multiple items from another iterable (list, tuple, set, string, etc.) 
# to the end of the list.


a=['d','i','p']
a.extend("anshu")
print(a)

a=[1,2]
b=[3,4]
a.extend("dip")
print(a)

a.extend("123")
print(a)

a.extend(b)
print(a)


a=[1,2]
b=[3,4]
a.extend(b)
print(a)

#deleting elements

#del listname[i], pop(i),pop,remove(el),clear

#del
#        0       1        2       3       4
listC=["pune","nagpur","delhi","mumbai","jaipur"]

del listC[2]
print(listC)

#pop : delets last element and teturn deleted value

#        0       1        2       3       4
listC=["pune","nagpur","delhi","mumbai","jaipur"]
ret =listC.pop()
print(listC)
print(ret)



#        0       1        2       3       4
listC=["pune","nagpur","delhi","mumbai","jaipur"]
listC.pop(2)
print(listC)

#remove(ele/value)==> delets first matching value
listC=["pune","jaipur","delhi","nagpur","delhi","mumbai","pune","jaipur"]

listC.remove("pune")
print(listC)

listC.remove("delhi")
print(listC)

#clear--> delets all elements
listC=["pune","jaipur","delhi","nagpur","delhi","mumbai","pune","jaipur"]
listC.clear()
print(listC)

# | Method              | What it does                 | Works by |
# | ------------------- | ---------------------------- | -------- |
# | `del listname[i]`   | Deletes element              | index    |
# | `pop(i)`            | Deletes + returns element    | index    |
# | `pop()`             | Deletes last element         | —        |
# | `remove(value)`     | Deletes first matching value | value    |
# | `clear()`           | Deletes all elements         | —        |










