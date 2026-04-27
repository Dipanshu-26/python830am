a=10
print(a)
print(type(a))

a=10.5
print(a)
print(type(a))

a="dipanshu"
print(a)
print(type(a))

a=[10.20,30,40]
print(a)
print(type(a))

a={"name" : "dipanshu"}
print(a)
print(type(a))

a=True
print(a)
print(type(a))

a=(11,22,33)
print(a)
print(type(a))

#set
a={100,200,300}
print(a)
print(type(a))


a={100,200,300,100,200,300}
print(a)
print(type(a))

#set does not store duplicates
#set is unordered collection 

#can set element can be acced with index-- no
setA={11,22,33,44}
#print(setA[0])   #TypeError: 'set' object is not subscriptable

print(len(setA))   #4 

#loops
for items in setA:
    print(items)


arr=[11,22,33,44,55]
for el in range(len(arr)):
    print(arr[el])    

#can we use range --no
#while -- no 
# for items in range(len(setA)):
#     print(setA[items])       #TypeError: 'set' object is not subscriptable

print("--------------------")
print(min(setA))
print(max(setA))

#methods 

#add
setB={'a','b','c','d'}
setB.add("gg")
print(setB)

setB.add("a")
print(setB)

#pop

setB.pop()
print(setB)

#remove
setB.remove("gg")
print(setB)

# Sets in Python are unordered collections.
# That means the elements inside a set do not maintain any specific order 
# — not by insertion order, not sorted order.

setC={33,44,55,66}
setC.update("77")
print(setC)

setC.update([1,2,3,4])
print(setC)

setC.update(["77"])
print(setC)

setC.update("dipanshuu")
print(setC)

setC.update(["dipanshu"])
print(setC)

setC.update({'aa','bb'})
print(setC)

setD=setC    #copy reference 

print(setD)

setD.remove("dipanshu")
print(setC)
print(setD)

print("-----------------")
#copy

setE=setC.copy()
print(setE)
print(setC)

setE.remove("aa")

print(setE)
print(setC)

#clear
setE.clear()
print(setE)