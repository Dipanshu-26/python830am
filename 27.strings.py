#strings in python
a="dipanshu"
print(a)
print(type(a))

c = """
hello ... 
I an learning python .
Python is very easy to go language
"""

print(c)
print(type(c))

c = '''
hello ... 
I an learning python .
Python is very easy to go language
'''

print(c)
print(type(c))

# f string in python

fn = "dipanshu"
ln = "chawde"

print(f"My name is {fn} and my surname is {ln}")

print("My name is "+fn+" and my surname is "+ln+"....")

print(f"My name is {fn} and \nMy surname is {ln}")

print("My name is "+fn+" and \nMy surname is "+ln+"....")

#----------------------------------------------------------------

#          0           1       2        3
names = ["dipanshu","nitin","tanish","neel"]
print(names[0])
names[0]="chawde"
print(names)


#str is immutable

name="dipanshu"
print(name[0])
print(name[2])

#name[0]="a"    #TypeError: 'str' object does not support item assignment

#          0         1         2
#          0123   012345   01234567
cities = ["pune","mumbai","banglore"]

print(cities[0])
print(cities[0][0])

print(cities[2][7])

print("banglore" in cities)

name="dipanshu"
print("a" in name)
print(len(cities))

#loops
name="dipanshu"
print(len(name))

for ch in range(8):
    print(name[ch])

name="dipanshu nitin chawde"  
for ch in range(len(name)): 
    print(name[ch]) 

print("----------------------------")

for ch in name:
    print(ch)

print("----------------------------")

i=0
while(i<len(name)):
    print(name[i])
    i=i+1

# does substring present in string    
c = '''
hello ... 
I am learning python .
Python is very easy to go language
'''

print("python" in c)
print("Python" in c)

print("hello" in c)
print("Hello" in c)

print("am le" in c)


#string methods 
#upper, lower,capitalize
x="niRanJan"

print(x.upper())
print(x.lower())
print(x.capitalize())

print(name.capitalize())
