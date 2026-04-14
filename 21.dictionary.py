info = ["dipanshu","chawde",32,42]

# descriptive data type 
# dictionary stores in key value pair

info = {
    "fname" : "dipanshu",
    "lname" : "chawde",
    "rno" : 32,
    "age" : 42
}

print(info)
print(type(info))

#CRUD

vechile = {
    "color" : "red",
    "type" : "sedan"
}

print(vechile)

# dict  does not stores the value by index.
# print(vechicle[0]) # error

print(vechile["color"])
print(info["fname"])

#len 

print(len(info))
print(len(vechile))

# find key is persent
print("fname" in info)

print("color" in vechile)

print("fnamee" in info)

print("dipanshu" in info)

#print(info.fname)

#print(vechile.color)

#get 

print(info.get("fname"))

print(vechile.get("color"))

print("--------------------------------------")
#retrive keys and values

student = {
    "name" : "tanish",
    "surname"  : "chawde",
    "age" :16,
    "class" : 12
}

print(student)
print(student["name"])
print(student.get("surname"))
print("age" in student)
print(len(student))
print("--------------------------------------")
print(student.keys())
print(student.values())
print(student.items())

skey = student.keys()
print(skey)
print(type(skey))

print(student.keys() , student.values())

print("--------------------------------------")
#add/update

student = {
    "name" : "tanish",
    "surname"  : "chawde",
    "age" :16,
    "class" : 12
}

student["rno"] = 23
print(student)

student["rno"] = 40
print(student)

student.update({"location" : "pune"})
print(student)

student.update({"location" : "mumbai"})
print(student)

print("--------------------------------------")

#del  : delet key from dictionary

del student["location"]
print(student)

#pop("keyname") - deletes given key from dictionary and returnd the value of deleted key

retval = student.pop("age")
print(student)
print(retval)

#popitem () - removes the last key from dictionary
student = {
    "name" : "tanish",
    "surname"  : "chawde",
    "age" :16,
    "class" : 12
}

print(student)
retval2 = student.popitem()
print(student)
print(retval2)

#clear  : removes all the keys
student = {
    "name" : "tanish",
    "surname"  : "chawde",
    "age" :16,
    "class" : 12
} 

print(student)
student.clear()
print(student)

#pop(k:v) : delets if exists(safe delets)

student = {
    "name" : "tanish",
    "surname"  : "chawde",
    "age" :16,
    "class" : 12
} 

student.pop("age")
print(student)

student.pop("age",None)
print(student)

#popitem()- remove last inserted key-value pair
student = {
    "name" : "tanish",
    "surname"  : "chawde",
    "age" :16,
    "class" : 12
}
print(student)
student.popitem()
print(student)

student.popitem()
print(student)