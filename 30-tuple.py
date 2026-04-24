#list, dict, string

# Python has 4 main built-in collection types

# | Collection Type | Ordered?                 | Mutable?     | Allows Duplicates?            | Syntax         |
# | --------------- | -----------------------  | -----------  | ---------------------------   | -------------- |
# | List            | ✔ Ordered               | ✔ Mutable    | ✔ Yes                         | `[ ]`          |
# | Tuple           | ✔ Ordered               | ❌ Immutable | ✔ Yes                         | `( )`          |
# | Set             | ❌ Unordered            | ✔ Mutable    | ❌ No (unique elements only)  | `{ }`          |
# | Dictionary      | ✔ Ordered (Python 3.7+) | ✔ Mutable    | Keys: ❌ No, Values: ✔ Yes    | `{key: value}` |

l1=[1,2,2,3,4,5,5]
l1[0] = 111
print(l1)

d="dipanshu"
print(d)
#d[0]="a"
print(d[0])

#----tuple-------------------------------------------------
# A tuple is a collection of items, just like a list, but with one important difference:
# Tuples are immutable (cannot be changed after creation)

#define

tup = 11,
print(tup)
print(type(tup))

tup = 11
print(tup)
print(type(tup))

tup = 11,22,33,44
print(tup)
print(type(tup))

tup = (11,22,33,44)
print(tup)
print(type(tup))

#does tuple stores values by index?  - yes

print(tup[0])
print(tup[2])

names = ("dipanshu","aditya","rucha")

print(names[0])
print(names[1])
print(names[2])

#names[0]="akay"    #TypeError: 'tuple' object does not support item assignment

# names = ("aaa","bbb","ccc") 
# print(names)

# can we update 1 single value ? No , fixed length 
# tuples are fixed length 

# Why Use Tuple?
# When data should not change (e.g., coordinates, constants)
# Faster than lists
# Safe from accidental modification

# perticular value exists
names = ("dipanshu","aditya","rucha")
print("aditya" in names)

#length
print(len(names))

#min , max
tup = 88,99,77,11,22,33,44
print(min(tup))
print(max(tup))


#unpacking in tuple
tup1 = 11,22,33,44
# a=tup1[0]
# b=tup1[1]
# c=tup1[2]
# d=tup1[3]
# print(d)

a,b,c,d = tup1
print(c)
print(type(a))

names = ("dipanshu","aditya","rucha")
n1,n2,n3 = names
print(n1)
print(type(n1))

#loops
names = ("dipanshu","aditya","rucha","akay","rajasi")
for i in range(len(names)):            #for i in range(5):
    print(names[i])

print("----------------------")
for el in names:
    print(el)    


print("----------------------")
i=0
while i<len(names):
    print(names[i])
    i=i+1

#count

t1 = ('a','b','a','d','x','x','d','d')
print(t1.count('d'))
print(t1.count('x'))

#index
print(t1.index('d'))
print(t1.index('a'))

#single element assignment
t=11,
print(type(t))
t=(11,)
print(type(t))

x=11
print(type(x))
x=(11)
print(type(x))

# Key Characteristics
# - Ordered (items keep their position)
# - Immutable (cannot modify, add, or remove items)
# - Allows duplicate values
# - Can store different data types